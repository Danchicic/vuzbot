from bs4 import BeautifulSoup
from selenium import webdriver
import fake_useragent
import re

from selenium.webdriver.common.by import By


def get_page(url: str, headers: dict) -> list:
    """
    Get the web page content and extract relevant information about students.

    Args:
        url (str): The URL of the web page.
        headers (dict): Headers for the HTTP request.

    Returns:
        list: A list of tuples containing the priority and mark of each student.

    """
    # Fetch the web page content
    # page = requests.get(url=url, headers=headers).text
    # with open('index.html', 'w+') as f:
    #     f.write(page)

    # Read the saved HTML file
    with open('index.html') as f:
        src = f.read()

    # Parse the HTML using BeautifulSoup
    page = BeautifulSoup(src, 'lxml')
    table = page.find_all('tr')
    students = []
    for student in table:
        original_id = student.find(class_='fio').text.strip()
        priority = student.find(class_='accepted').text.strip()
        mark = student.find_all(class_='sum')[-1].text.strip()

        students.append((original_id, priority, mark))

    return students[1:]


def get_comp() -> list[str]:
    url = 'https://priem.mirea.ru/accepted-entrants-list/'
    user = fake_useragent.UserAgent().random
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user}")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    competitions = []
    try:
        driver.get(url=url)
        # time.sleep(6)
        competitions = []
        competitions_web = driver.find_elements(By.CLASS_NAME, 'compType')
        for comp in competitions_web:
            if re.match(r"\d{2}\.\d{2}\.\d{2}", comp.text.strip().split()[0]):
                competitions.append(comp.text)
    except Exception as ex:
        print(ex)
    return competitions


def main() -> None:
    get_comp()
    '''url: str = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205436693126454&prior=any&documentType=any&accepted=0&acceptedEntrant=any&onlyActive=1&onlyPaid=0'

    headers: dict = {
        "user-agent": fake_useragent.UserAgent().random,
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }

    """
    Main function to call and print the results of `get_page()`.

    """
    print(get_page(url=url, headers=headers))'''


if __name__ == '__main__':
    main()

import requests
from bs4 import BeautifulSoup

url: str = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205436693126454&prior=any&documentType=any&accepted=0&acceptedEntrant=any&onlyActive=1&onlyPaid=0'

headers: dict = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.3.764 Yowser/2.5 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}


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
        priority = student.find(class_='accepted').text.strip()
        mark = student.find_all(class_='sum')[-1].text.strip()
        students.append((priority, mark))

    return students[1:]


def main() -> None:
    """
    Main function to call and print the results of `get_page()`.

    """
    print(get_page(url=url, headers=headers))


if __name__ == '__main__':
    main()

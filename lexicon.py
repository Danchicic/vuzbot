from services import GetVuzTable

lexicon_ru: dict[str, str] = {
    'start': 'Привет,\n я бот для просмотра своего номера в списках вузов\nЧтобы приступить к работе отправь свой СНИЛС в формате 111-111-111-22',
    'snils_correct': 'Выберите один из предложенных вузов',
    'snils_uncorrect': "Вы ввели не корректный снилс, попробуйте еще раз",
    'change_snils': 'Введите новый снилс',
    'change_vuz': 'Выберите из предложенного списка',
    'change_comp': 'Выберите факультет',
    'stop': 'Чтобы вывести статистику по каждому из них, можно воспользоваться командой /check'
}
vuzes: list[str] = ['МИРЭА', 'МАИ', 'МЭИ']
competitions_mirea: dict[str, str] = GetVuzTable.get_comp()
competitions_mai: dict[str, str] = {
    'str': 'str',
}

from services.mirea import get_comp

lexicon_ru: dict[str, str] = {
    'start': 'Привет,\n я бот для просмотра своего номера в списках вузов\nЧтобы приступить к работе отправь свой СНИЛС в формате 111-111-111-22',
    'snils_correct': 'Выберите один из предложенных вузов',
    'snils_uncorrect': "Вы ввели не корректный снилс, попробуйте еще раз"
}
vuzes: list[str] = ['МИРЭА', 'МАИ', 'МЭИ']
competitions: dict[str, str] = get_comp()

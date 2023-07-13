from typing import Type

from services.mei import get_mei_comp
from services.mirea import get_mirea_comp

lexicon_ru: dict[str, str] = {
    'start': 'Привет,\n я бот для просмотра своего номера в списках вузов\nЧтобы приступить к работе отправь свой СНИЛС в формате 111-111-111-22',
    'snils_correct': 'Введите сумму ваших балов по экзаменам',
    'snils_uncorrect': "Вы ввели не корректный снилс, попробуйте еще раз",
    'uncorrect_data': 'Вы ввели некорректные данные',
    'change_snils': 'Введите новый снилс',
    'change_vuz': 'Выберите интересующий вас ВУЗ',
    'change_mark': 'Введите свои баллы',
    'stop': 'Чтобы вывести статистику по каждому из них, можно воспользоваться командой /check',
    'change_comp': 'Выберите факультет для просмотра\n<b>Если хотите выбрать сразу несколько и добавить их в избранное введите команду</b> /favourite',
    'change_vuz_for_favourites': 'Сейчас вы меняете вуз для сохранения факультетов',
}
vuzes: list[str] = ['МИРЭА', 'МЭИ']

competitions_mirea = get_mirea_comp()
competitions_mei = get_mei_comp()
if __name__ == '__main__':
    print(competitions_mirea)
    print(competitions_mei)

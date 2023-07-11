import lexicon
import re


def text_in_vuz(text) -> bool:
    return text.text in lexicon.vuzes


def is_comp(text):
    return re.match(r"\d{2}\.\d{2}\.\d{2}\n\([а-яА-Я]{3,5}\)", text.text)

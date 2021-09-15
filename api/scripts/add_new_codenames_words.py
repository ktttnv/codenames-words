import re
import os.path
from api.modules import errors
from api.helpers import helper

ocd = open(os.path.dirname(__file__) + '/../dictionaries/original_codenames_dictionary.txt', 'r', encoding='utf-8')
codenames_words = list(map(helper.remove_new_line_symbol, ocd.readlines()))

rnd = open(os.path.dirname(__file__) + '/../dictionaries/russian_nouns_dictionary.txt', 'r', encoding='utf-8')
russian_words = list(map(helper.remove_new_line_symbol, rnd.readlines()))


def is_word_in_codenames_dictionary(target_word):
    return helper.has_item_in_sorted_list(codenames_words, target_word)


def is_word_in_russian_dictionary(target_word):
    return helper.has_item_in_sorted_list(russian_words, target_word)


def run():
    reg_exp = '[а-я` -]+'
    max_word_length = 15

    print('Мы начинаем! Введите слова, которые Вы бы хотели добавить в новый словарь для игры Codenames. Чтобы '
          'закончить добавление слов, введите 0.')

    while True:
        try:
            test_str = input("Введите новое слово: ").lower().replace('ё', 'е')
            if test_str == "0":
                print("Bye!")
                break
            elif re.fullmatch(reg_exp, test_str) is None:
                raise errors.ValueDoesNotMatchRegExpError
            elif len(test_str) > max_word_length:
                raise errors.ValueTooLong
            elif is_word_in_codenames_dictionary(test_str):
                raise errors.ValueIsInCodenamesDictionary
            elif not is_word_in_russian_dictionary(test_str):
                answer_to_add = input('Данного слова нет в словаре русских слов (существительных). Вы уверены, '
                                      'что хотите добавить это слово? Введите "да", если согласны: ')
                if answer_to_add == "да":
                    print('Ok, we are adding this:', test_str)
                else:
                    print('Ok, we will not add this')
            else:
                print('Ok, we are adding this:', test_str)

        except errors.ValueDoesNotMatchRegExpError:
            print('Допустимые символы - буквы русского алфавита, дефис, пробел и апостроф. Пожалуйста, '
                  'используйте только их.')
        except errors.ValueTooLong:
            print('Длина слова не должна превышать', max_word_length, 'символов.')
        except errors.ValueIsInCodenamesDictionary:
            print('Данное слово уже есть в списке слов Codenames.')


run()

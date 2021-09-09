import re
import helper


# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueDoesNotMatchRegExpError(Error):
    """Raised when the input value does not match to regular expression"""
    pass


class ValueTooLong(Error):
    """Raised when the input value is too long"""
    pass


class ValueIsInCodenamesDictionary(Error):
    """Raised when the input value is already in codenames dictionary"""
    pass
#
#
# class ValueIsNotInRussianDictionary(Error):
#     """Raised when the input value is not in Russian dictionary"""
#     pass


ocd = open('dictionaries/original_codenames_dictionary.txt', 'r')
codenames_words = list(map(helper.remove_new_line_symbol, ocd.readlines()))

rnd = open('dictionaries/russian_nouns_dictionary.txt', 'r')
russian_words = list(map(helper.remove_new_line_symbol, rnd.readlines()))


def is_word_in_codenames_dictionary(target_word):
    return helper.bin_search(codenames_words, target_word)


def is_word_in_russian_dictionary(target_word):
    return helper.bin_search(russian_words, target_word)


def example():
    while True:
        reg_exp = '[а-яё` -]+'
        max_word_length = 15

        try:
            test_str = input("Введите новое слово: ").lower()

            if re.fullmatch(reg_exp, test_str) is None:
                raise ValueDoesNotMatchRegExpError
            elif len(test_str) > max_word_length:
                raise ValueTooLong
            elif is_word_in_codenames_dictionary(test_str):
                raise ValueIsInCodenamesDictionary
            elif not is_word_in_russian_dictionary(test_str):
                answer_to_add = input('Данного слова нет в словаре русских слов (существительных). Вы уверены, '
                                      'что хотите добавить это слово? Введите "да", если согласны: ')
                if answer_to_add == "да":
                    print('Ok, we are adding this')
                else:
                    print('Ok, we will not add this')
            else:
                print(test_str)

        except ValueDoesNotMatchRegExpError:
            print('Допустимые символы: буквы русского алфавита, дефис, пробел и апостроф. Пожалуйста, '
                  'используйте только их.')
        except ValueTooLong:
            print('Длина слова не должна превышать', max_word_length, 'символов.')
        except ValueIsInCodenamesDictionary:
            print('Данное слово уже есть в списке слов Codenames.')
        else:
            print("выходим из цикла!")
            break


example()

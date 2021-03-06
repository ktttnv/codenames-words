import os.path
from api.helpers import helper


def change_all_yo_letters_in_file(file_path):
    file_data = open(file_path, 'r+')
    all_lines = list(map(helper.remove_new_line_symbol, file_data.readlines()))

    all_lines_updated = list(map(lambda line: line.replace('ё', 'е'), all_lines))

    file_data.seek(0)
    file_data.write('\n'.join(all_lines_updated))


change_all_yo_letters_in_file(os.path.dirname(__file__) + '/../dictionaries/russian_nouns_dictionary.txt')

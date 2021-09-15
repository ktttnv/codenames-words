import os.path
from api.helpers import helper

f = open(os.path.dirname(__file__) + '/../dictionaries/original_codenames_dictionary.txt', 'r+')

all_words = list(map(helper.remove_new_line_symbol, f.readlines()))
all_words.sort()

f.seek(0)
f.write('\n'.join(all_words))

f.close()

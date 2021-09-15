import helper

f = open('dictionaries/original_codenames_dictionary.txt', 'r+')

all_words = list(map(helper.remove_new_line_symbol, f.readlines()))
all_words.sort()

f.seek(0)
f.write('\n'.join(all_words))

f.close()

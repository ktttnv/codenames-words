f = open('original_codenames_dictionary.txt', 'r+')


def remove_new_line_symbol(line):
    return line[:-1] if line[-1] == '\n' else line


all_words = list(map(remove_new_line_symbol, f.readlines()))
all_words.sort()

f.seek(0)
f.write('\n'.join(all_words))

f.close()

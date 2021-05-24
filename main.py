# Letter Capitalize
import re

def Capitalize(string):
    word_split = re.findall("\S+", string)

    new_word_ls = []

    for x in range(len(word_split)):
        new_word_ls.append(word_split[x].capitalize())

    new_sen = " ".join(new_word_ls)

    return new_sen


print(Capitalize("i am rahul tanna"))
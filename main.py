from pathlib import Path
import re
import string

punc = string.punctuation
punc = punc.replace("-", "")
punc = punc.replace("'", "")


def validateWord(word):
    lower = word.lower()
    if lower[-1] == "-" or lower[-1] == "'":
        lower = lower[:-1]

    if lower == "":
        return None
    return lower


def getWords(line):
    for l in punc:
        line = line.replace(l, " ")

    return list(validateWord(n) for n in line.split())


def collector(input, output):
    dictionary = dict()
    for content in open(input, encoding='utf-8'):
        result = getWords(content)
        for word in result:
            if word is None:
                continue

            if word not in dictionary:
                dictionary[word] = 0
            dictionary[word] += 1

    arr = []
    for content in open(input, encoding='utf-8'):
        for word in getWords(content):
            if word is None:
                continue

            if word in dictionary:
                arr.append(word + " " + str(dictionary[word]))
                dictionary.pop(word)

    file = open(output, "w", encoding="utf-8")
    file.write("\n".join(arr))
    if len(arr) > 0:
        file.write("\n")
    file.close()
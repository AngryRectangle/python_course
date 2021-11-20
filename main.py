from pathlib import Path
import re
import string


def collector(input, output):
    punc = string.punctuation
    punc = punc.replace("-", "")
    punc = punc.replace("'", "")
    dictionary = dict()
    for content in open(input, encoding='utf-8'):
        content = content.replace("\n", " ")
        for l in punc:
            content = content.replace(l, " ")

        result = content.split()
        for word in result:
            lower = word.lower()
            if lower[-1] == "-" or lower[-1] == "'":
                lower = lower[:-1]

            if lower == "":
                continue
            if lower not in dictionary:
                dictionary[lower] = 0
            dictionary[lower] += 1

    arr = []
    for content in open(input, encoding='utf-8'):
        content = content.replace("\n", " ")
        for l in punc:
            content = content.replace(l, " ")

        result = content.split()
        for word in result:
            lower = word.lower()
            if lower[-1] == "-" or lower[-1] == "'":
                lower = lower[:-1]

            if lower in dictionary:
                arr.append(lower + " " + str(dictionary[lower]))
                dictionary.pop(lower)

    file = open(output, "w", encoding="utf-8")
    file.write("\n".join(arr))
    if len(arr) > 0:
        file.write("\n")
    file.close()

# collector("input.txt", "output.txt")

from pathlib import Path
import re


def collector(input, output):
    content = ""
    for line in open(input, encoding='utf-8'):
        content += line

    re.UNICODE = True
    prog = re.compile("[a-zа-я]+")
    content = content.replace("\n", " ")
    #content = content.replace("", " ")
    #content = content.replace("", " ")
    result = content.split()
    dictionary = dict()
    for word in result:
        match = re.findall(prog, word.lower())
        if match is None:
            continue
        lower = ""
        for word in match:
            lower+=word

        if lower.isspace() or lower == "`" or lower == "" or lower == "-" or lower == "_":
            continue

        if lower not in dictionary:
            dictionary[lower] = 0
        dictionary[lower] += 1

    sum = 0
    for value in dictionary.values():
        sum += value

    arr = []
    for word in result:
        match = re.findall(prog, word.lower())
        if match is None:
            continue
        lower = ""
        for word in match:
            lower += word

        if lower.isspace() or lower == "`" or lower == "":
            continue

        if lower in dictionary:
            arr.append(lower + " " + str(dictionary[lower]))
            dictionary.pop(lower)

    file = open(output, "w", encoding="utf-8")
    file.write("\n".join(arr))
    file.close()

# collector("input.txt", "output.txt")

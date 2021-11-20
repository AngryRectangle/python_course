import string

punc = string.punctuation
punc = punc.replace("-", "")
punc = punc.replace("'", "")


def validateWord(word):
    lower = word.lower()
    while len(lower) > 0 and (lower[-1] == "-" or lower[-1] == "'"):
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
    count = 1
    for content in open(input, encoding='utf-8'):
        result = getWords(content)
        for word in result:
            if word is None:
                continue

            if word not in dictionary:
                dictionary[word] = (0, [])

            current = dictionary[word]
            current[1].append(count)
            dictionary[word] = (current[0] + 1, current[1])
            count += 1

    values = list((k, v[0], v[1]) for k, v in dictionary.items())
    values.sort(key=lambda x: x[2][0])
    arr = []
    for value in values:
        joined = " ".join(list(map(lambda x: str(x), value[2])))
        arr.append(value[0] + " " + str(value[1]) + " " + joined)

    file = open(output, "w", encoding="utf-8")
    file.write("\n".join(arr))
    if len(arr) > 0:
        file.write("\n")
    file.close()

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
                dictionary[word] = []

            current = dictionary[word]
            current.append(count)
            dictionary[word] = current
            count += 1

    arr = []
    for key, value in dictionary.items():
        joined = " ".join(list(map(lambda x: str(x), value)))
        arr.append(key + " " + str(len(value)) + " " + joined)

    file = open(output, "w", encoding="utf-8")
    file.write("\n".join(arr))
    if len(arr) > 0:
        file.write("\n")
    file.close()

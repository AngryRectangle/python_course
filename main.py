import sys

input = sys.argv[0]
output = sys.argv[1]

file = open(input)
data = file.readlines()
file.close()

dictionary = dict()
for line in data:
    words = line.split()
    for word in words:
        lower = word.lower()
        if word not in dictionary:
            dictionary[lower] = 0
        dictionary[lower] += 1

sum = 0
for value in dictionary.values():
    sum += value

arr = []
for line in data:
    words = line.split()
    for word in words:
        lower = word.lower()
        if word in dictionary:
            arr.append(word + " " + str(dictionary[lower]))
            dictionary.pop(lower)

file = open(output, "w")
file.close()
Numbers = [1, 2, 4, 5, 3, 4, 7, 3, 1]

uniques = []

for number in Numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
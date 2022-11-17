NUMBERS = [5,2,8,4,1,9,7,3,10,6]

for i in range(0, len(NUMBERS)):
    minimum = i

    for j in range(i + 1, len(NUMBERS)):
        if NUMBERS[j] < NUMBERS[minimum]:
            minimum = j

    if minimum != i:
        NUMBERS[minimum], NUMBERS[i] = NUMBERS[i], NUMBERS[minimum]

print(NUMBERS)
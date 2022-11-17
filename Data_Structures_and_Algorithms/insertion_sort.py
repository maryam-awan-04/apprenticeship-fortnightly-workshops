NUMBERS = [5,2,8,4,1,9,7,3,10,6]

for i in range(1, len(NUMBERS)):
    sort_value = NUMBERS[i]

    while NUMBERS[i - 1] > sort_value and i > 0:
        NUMBERS[i], NUMBERS[i - 1] = NUMBERS[i - 1], NUMBERS[i]
        i = i - 1

print(NUMBERS)
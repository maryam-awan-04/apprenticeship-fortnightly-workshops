import numpy as np

NUMBERS = np.array([5,2,8,4,1,9,7,3,10,6])
sorted_numbers = np.array_split(NUMBERS, len(NUMBERS))

for i in range(0, len(sorted_numbers)):
    minimum = i

    for j in range(i + 1, len(sorted_numbers)):
        if sorted_numbers[j] < sorted_numbers[minimum]:
            minimum = j

    if minimum != i:
        NUMBERS[minimum], NUMBERS[i] = NUMBERS[i], NUMBERS[minimum]

print(NUMBERS)
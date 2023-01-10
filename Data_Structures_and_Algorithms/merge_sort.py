import numpy as np
import unittest

def merge_sort(LIST):
    LIST = np.array(LIST)
    sorted_numbers = np.array_split(LIST, len(LIST))

    for i in range(0, len(sorted_numbers)):
        minimum = i

        for j in range(i + 1, len(sorted_numbers)):
            if sorted_numbers[j] < sorted_numbers[minimum]:
                minimum = j

        if minimum != i:
            LIST[minimum], LIST[i] = LIST[i], LIST[minimum]
    
    return LIST

print(merge_sort([5,2,8,4,1,9,7,3,10,6]))
print(merge_sort(['e','b','d','a','c']))

class TestSelectionSort(unittest.TestCase):
    def test_numbers_one_to_ten(self):
        actual = merge_sort([5,2,8,4,1,9,7,3,10,6])
        expected = merge_sort([1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(actual, expected)
    
    def test_numbers_one_to_ten_double(self):
        actual = merge_sort([5,2,8,4,1,9,7,3,10,6,5,2,8,4,1,9,7,3,10,6])
        expected = merge_sort([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10])
        self.assertEqual(actual, expected)
    
    def test_numbers_one_to_ten_quadruple(self):
        actual = merge_sort([5,2,8,4,1,9,7,3,10,6,5,2,8,4,1,9,7,3,10,6,5,2,8,4,1,9,7,3,10,6,5,2,8,4,1,9,7,3,10,6])
        expected = merge_sort([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10])
        self.assertEqual(actual, expected)
    
    def test_letters(self):
        actual = merge_sort(['e','b','d','a','c'])
        expected = merge_sort(['a','b','c','d','e'])
        self.assertEqual(actual, expected)
        
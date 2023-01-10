import unittest

def insertion_sort(LIST):
    for i in range(1, len(LIST)):
        sort_value = LIST[i]

        while LIST[i - 1] > sort_value and i > 0:
            LIST[i], LIST[i - 1] = LIST[i - 1], LIST[i]
            i = i - 1
    
    return LIST

print(insertion_sort([5,2,8,4,1,9,7,3,10,6]))
print(insertion_sort(['e','b','d','a','c']))

class TestSelectionSort(unittest.TestCase):
    def test_numbers_one_to_ten(self):
        actual = insertion_sort([5,2,8,4,1,9,7,3,10,6])
        expected = insertion_sort([1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(actual, expected)
    
    def test_numbers_one_to_ten_double(self):
        actual = insertion_sort([5,2,8,4,1,9,7,3,10,6,5,2,8,4,1,9,7,3,10,6])
        expected = insertion_sort([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10])
        self.assertEqual(actual, expected)
    
    def test_numbers_one_to_ten_quadruple(self):
        actual = insertion_sort([5,2,8,4,1,9,7,3,10,6,5,2,8,4,1,9,7,3,10,6,5,2,8,4,1,9,7,3,10,6,5,2,8,4,1,9,7,3,10,6])
        expected = insertion_sort([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10])
        self.assertEqual(actual, expected)
    
    def test_letters(self):
        actual = insertion_sort(['e','b','d','a','c'])
        expected = insertion_sort(['a','b','c','d','e'])
        self.assertEqual(actual, expected)
        
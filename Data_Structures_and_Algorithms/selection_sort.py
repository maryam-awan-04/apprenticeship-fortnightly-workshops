import unittest

def selection_sort(LIST):
    for i in range(0, len(LIST)):
        minimum = i

        for j in range(i + 1, len(LIST)):
            if LIST[j] < LIST[minimum]:
                minimum = j

        if minimum != i:
            LIST[minimum], LIST[i] = LIST[i], LIST[minimum]
    
    return LIST

print(selection_sort([5,2,8,4,1,9,7,3,10,6]))
print(selection_sort(['e','b','d','a','c']))

class TestSelectionSort(unittest.TestCase):
    def test_numbers_one_to_ten(self):
        actual = selection_sort([5,2,8,4,1,9,7,3,10,6])
        expected = selection_sort([1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(actual, expected)
    
    def test_numbers_one_to_ten_double(self):
        actual = selection_sort([5,2,8,4,1,9,7,3,10,6,5,2,8,4,1,9,7,3,10,6])
        expected = selection_sort([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10])
        self.assertEqual(actual, expected)
    
    def test_numbers_one_to_ten_quadruple(self):
        actual = selection_sort([5,2,8,4,1,9,7,3,10,6,5,2,8,4,1,9,7,3,10,6,5,2,8,4,1,9,7,3,10,6,5,2,8,4,1,9,7,3,10,6])
        expected = selection_sort([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10])
        self.assertEqual(actual, expected)
    
    def test_letters(self):
        actual = selection_sort(['e','b','d','a','c'])
        expected = selection_sort(['a','b','c','d','e'])
        self.assertEqual(actual, expected)
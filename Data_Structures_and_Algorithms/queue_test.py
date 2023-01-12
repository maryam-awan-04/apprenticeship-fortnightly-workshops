from names_queue import Names
import unittest

class TestQueue(unittest.TestCase):
    
    def test_add_name(self):
        queue = Names(['fred', 'wilma'])
        result = queue.add_name('betty')
        self.assertEqual(result, ['fred','wilma','betty'])

    def test_remove_name(self):
        queue = Names(['fred', 'wilma'])
        result = queue.remove_name(self)
        self.assertEqual(result, ['wilma'])

    def test_peek(self):
        queue = Names(['fred', 'wilma'])
        result = queue.peek(self)
        self.assertEqual(result, ['fred'])

if __name__ == '__main__':
    unittest.main()
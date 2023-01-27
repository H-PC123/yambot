import unittest

class TestBot(unittest.TestCase):

    def test_(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()
import unittest
import articles_handler as ah

class Test_test_author(unittest.TestCase):
    def test_correct_nicknames(self):
        authors = ['author', 'AUTHOR', 'aUTHOR', 'Author', 'AuThOr', 'author1', 'author_1', 'author__auth', 'Author_A1', '12345678', '123456AU', '1234_123']
        for author in authors:
            self.assertTrue(ah.check_author(author))
    
    def test_uncorrect_nicknames(self):
        authors=['pro designer', 'Pro Designer', 'Pro designer_1', 'Pro-designer', 'Auth.AUTHOR', '$$$$', '', ' ', 'Author$_$', '1234 5678']
        for author in authors:
            self.assertFalse(ah.check_author(author))

if __name__ == '__main__':
    unittest.main()

import unittest

from cleaner import Cleaner



def use_cleaner(html_snippet):
    cleaner = Cleaner(html_snippet)

    cleaner.clean()
    
    return str(cleaner)


class CleanerTest(unittest.TestCase):

    
    # TODO: SETUP THE TESTS
    def test(self):

        self.assertEqual(use_cleaner(), )

        self.assertEqual(use_cleaner(), )
        
        self.assertEqual(use_cleaner(), )
        
        self.assertEqual(use_cleaner(), )


def __name__ == "__main__":
    unittest.main()


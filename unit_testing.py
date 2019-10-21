
import unittest

from test_cases import *

from Cleaner.cleaner import Cleaner 



TEST_INDEX = 0
RESULT_INDEX = 1


def use_cleaner(html_snippet):
    cleaner = Cleaner(html_snippet)

    cleaner.clean()
    
    return str(cleaner)


def prepare_htmls():
    pass



class CleanerTest(unittest.TestCase):


    def test_script(self):
        '''
        Tests the removal of the <script> tag
        '''

        filtered_html = use_cleaner(script_test[TEST_INDEX])
        filtered_html.strip()
        result_html = script_test[RESULT_INDEX]
        result_html.strip()

        self.assertEqual(filtered_html, result_html)



    def test_empty_tags(self):
        '''
        Tests the removal of empty tags
        '''

        filtered_html = use_cleaner(empty_tags[TEST_INDEX])
        filtered_html.strip()
        print(filtered_html)
        result_html = empty_tags[RESULT_INDEX]
        result_html.strip()

        self.assertEqual(filtered_html, result_html)



if __name__ == "__main__":
    unittest.main()



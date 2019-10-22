
import unittest

from test_cases import *

from cleaner import Cleaner 



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

        [filtered_html, result_html] = processing_for_test(empty_tags)
        filtered_html = use_cleaner(empty_tags[TEST_INDEX])
        filtered_html.strip()
        print(filtered_html)
        result_html = empty_tags[RESULT_INDEX]
        result_html.strip()

        self.assertEqual(filtered_html, result_html)



    def test_arab(self):
        '''
        Tests the removal of comments and the encoding output of BeautifulSoup for arab
        '''

        [filtered_html, result_html] = processing_for_test(arab_and_comment)

        self.assertEqual(filtered_html, result_html)


def strip_white_space(text):
    return text.replace(" ", "").replace("\t", "").replace("\n", "")


def processing_for_test(test_case):
    filtered_html = use_cleaner(test_case[TEST_INDEX])
    filtered_html = strip_white_space(filtered_html)

    result_html = test_case[RESULT_INDEX]
    result_html = strip_white_space(result_html)

    return [filtered_html, result_html]


if __name__ == "__main__":
    unittest.main()



from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Edge('E:\\Ki 1 nam 3\\Tester\\Prak3\\edgedriver_win64\\msedgedriver.exe')
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Check out its homepage of to-do list app
        self.browser.get('http://localhost:8000')

        # Notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
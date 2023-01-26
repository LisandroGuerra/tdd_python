import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()


    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Lisandro was looking for a to-do app and decides to check-out the homepage
        self.browser.get('http://localhost:8000')

        # He realizes that page the title an the header mention to-do list
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test.')
        

        # He is invited to immediately insert a task item

        # He types "Buy a new pillow" in a text box

        # When he types "enter" the page is updated and now it lists
        # "1: Buy a new pillow" as an item in the to-do list

        # Still have a text box inviting him to add another item
        # He types "Buy a pillow cover to my pillow"

        # The page is updated and now shows two tasks in the to-do list

        # Lisandro asks to him self if the site will remember his list. 
        # Than he notices that the site generates a unique URL to him.
        # There is a short text explaning this

        # He accesses the URL and his to-do list still there

        # Satisfied he goes back to sleep


        # browser.close()

if __name__ == '__main__':
    unittest.main(warnings='ignore')

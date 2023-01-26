from selenium import webdriver


browser = webdriver.Firefox()

# Lisandro was looking for a to-do app and decides to check-out the homepage
browser.get('http://localhost:8000')

# He realizes that page the title an the header mention to-do list
assert 'To-Do' in browser.title

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

browser.quit()
# browser.close()

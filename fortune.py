## Automating a fortune_login##
def fortune_login():

driver.get ("https://fortune.com/")

driver.find_element_by_id("email").send_keys('sanjoyganguli@hotmail.com')
driver.find_element_by_id("pass").send_keys("fakepassword")
driver.find_element_by_id("loginbutton").click

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver.exe")
driver.get("https://jqueryui.com/datepicker/")

driver.implicitly_wait(30)
driver.find_element_by_id("datepicker").click()


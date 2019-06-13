
from selenium import webdriver


driver=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver.exe")
driver.get("file:///C:/Users/Admin/Desktop/Webtabledemo.html")

Col_count=driver.find_elements_by_xpath("//*[@id='123']/tbody/tr/td[1]")

for i in Col_count:
    v=print(i.text)
    if v==3:
        amma=driver.find_elements_by_xpath("//*[@id='123']/tbody/td[3]")
        print(amma.text)


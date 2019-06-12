# //*[@id="123"]/tbody/tr[1]/td[1]   #1
# //*[@id="123"]/tbody/tr[1]/td[2]   #A
# //*[@id="123"]/tbody/tr[1]/td[3]    #100


# //*[@id="123"]/tbody/tr[2]/td[1]
# //*[@id="123"]/tbody/tr[2]/td[2]
# //*[@id="123"]/tbody/tr[2]/td[3]

# //*[@id="123"]/tbody/tr[3]/td[1]
# //*[@id="123"]/tbody/tr[3]/td[2]
# //*[@id="123"]/tbody/tr[3]/td[3]


from selenium import webdriver


driver=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver.exe")
driver.get("file:///C:/Users/Admin/Desktop/Webtabledemo.html")

var=driver.find_elements_by_xpath("//*[@id='123']/tbody/tr[1]/td")
print(var)
print(len(var))

for i in var:
    print(i.text)

#
# col_var=driver.find_elements_by_xpath("//*[@id='123']/tbody/tr[1]/td")
# col_count=len(col_var)
# print("col count",col_count)
#
#
# row_var=driver.find_elements_by_xpath("//*[@id='123']/tbody/tr")
# row_count=len(row_var)
# print("row count",row_count)

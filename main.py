from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


user=input("UserName")
password=input("Password")
Active = input("Do you want Active user yes/no?")

driver=webdriver.Chrome(executable_path="C:\\Users\\liorsw\\Desktop\\chromedriver.exe")

## get access account ##
driver.get("http://localhost:8080/plugins/servlet/techtime-usermanagement/bulkchange/selectusers")
y=driver.find_element_by_xpath("/html/body/div/div/div/div/main/form/div[1]/div[2]/div/div[1]/input")
y.send_keys(user)
y=driver.find_element_by_xpath("/html/body/div/div/div/div/main/form/div[1]/div[2]/div/div[2]/input")
y.send_keys(password)
y.send_keys(Keys.ENTER)

##Scan Group##
driver.get("http://localhost:8080/secure/admin/user/GroupBrowser.jspa")
y=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/main/form/div[1]/fieldset/div[2]/input")
y.send_keys(password)
y=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/main/form/div[1]/fieldset/div[2]/input")
y.send_keys(Keys.ENTER)
x=driver.find_element_by_xpath("/html/body/div[1]/div/section/div[2]/div/main/table/tbody").text
z=list(map(lambda x:x.split(" ")[0].replace("\n",""),x.split("Delete")))
for i in range (len(z)-1):
    print (z[i])


##Group##
d=0
driver.get("http://localhost:8080/plugins/servlet/techtime-usermanagement/bulkchange/selectusers")
group= input("Choose Name Group")
for i in st:
    if i == group:
        print("Match")
        break
    else:
       print("not match")



y=driver.find_element_by_xpath("/html/body/div[1]/div/section/div[2]/div/main/div/div[2]/div[1]/div[1]/form[1]/div[1]/div/div/ul/li/input")
y.send_keys(group)
time.sleep(1)
y.send_keys(Keys.DOWN, Keys.RETURN)


##Active_User##
def Activeuser(Active):
   Active=str(Active)
   if Active == 'yes':
       y = driver.find_element_by_xpath(
           "/html/body/div[1]/div/section/div[2]/div/main/div/div[2]/div[1]/div[1]/form[1]/div[7]/div/select/option[2]").click()
   else:
       print("No active")
Activeuser(Active)


## SelectAll + Export ##
time.sleep(2)
y=driver.find_element_by_xpath("/html/body/div[1]/div/section/div[2]/div/main/div/div[2]/div[2]/div[1]/div[1]/div/div[1]/div/button[1]").click()
time.sleep(1)
y=driver.find_element_by_xpath("/html/body/div[1]/div/section/div[2]/div/main/div/div[2]/div[2]/div[1]/div[1]/div/div[1]/div/a").click()
time.sleep(1)
y=driver.find_element_by_xpath("/html/body/div[1]/div/section/div[2]/div/main/div/div[2]/div[2]/div[2]/ul/li[1]/a").click()

print("Excel downloading now...")

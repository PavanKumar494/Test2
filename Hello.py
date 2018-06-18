import csv
from selenium.webdriver import Firefox, Chrome, Ie
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

with open('C:/Users/Igs-DT01/Desktop/sample.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    email = []
    mobile = []
    password = []
    firstname = []
    lastname = []
    zipcode = []
    ssn = []
    for row in readCSV:
        emailVar = row[0]
        mobileVar = row[1]
        passwordVar = row[2]
        firstnameVar = row[3]
        lastnameVar = row[4]
        zipcodeVar = row[5]
        ssnVar = row[6]

        email.append(emailVar)
        mobile.append(mobileVar)
        password.append(passwordVar)
        firstname.append(firstnameVar)
        lastname.append(lastnameVar)
        zipcode.append(zipcodeVar)
        ssn.append(ssnVar)

    email.pop(0)
    mobile.pop(0)
    password.pop(0)
    firstname.pop(0)
    lastname.pop(0)
    zipcode.pop(0)
    ssn.pop(0)

for x, y in zip(email, mobile):
    browser = Firefox(executable_path='E:/Pavan/geckodriver-v0.20.1-win64/geckodriver.exe')
    browser.get("https://us.castlighthealth.com")
    wait = WebDriverWait(browser, 30)
    wait.until(expected_conditions.title_contains('Castlight - Sign In'))

    browser.find_element_by_xpath("(//a[contains(text(),'Register')])[1]").click()
    wait = WebDriverWait(browser, 30)
    wait.until(expected_conditions.title_contains('Castlight - Registration'))
    # browser.find_element_by_id("email").send_keys("Hat")
    browser.find_element_by_id("email").send_keys(x)
    browser.find_element_by_id("mobilePhoneNumber").send_keys(y)
    time.sleep(10)
    browser.quit()


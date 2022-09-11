from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')
cookies_link = browser.find_element("xpath","/html/body/div[4]/div/div/button[2]")
cookies_link.click()

sleep(5)

def login():
 
    username_input = browser.find_element("css selector","input[name='username']")
    password_input = browser.find_element("css selector","input[name='password']")

    username_input.send_keys("<Your Username>")
    password_input.send_keys("<Your Password>")

    login_button = browser.find_element("xpath","/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]")
    login_button.click()

    sleep(5)

    save_credentials_button = browser.find_element("css selector", "button.sqdOP:nth-child(1)")
    save_credentials_button.click()

    sleep(3)

    turn_on_notifications_button = browser.find_element("css selector", "button._a9--:nth-child(2)")
    turn_on_notifications_button.click()

    sleep(3)

def open_followers(account_instagram):
    browser.get("https://www.instagram.com/" + account_instagram + "/followers/")
    sleep(5)
    browser.find_element("xpath","/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()

login()

#for account in sources:
    #open_followers(account)
    #time.sleep(10)
    #scroll_followers(2)
    #follow_followers()

browser.close()

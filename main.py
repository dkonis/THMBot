import sys
import datetime
from login import *
from keepstreak import *
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def main():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.headless = True
    firefox_options.set_preference("dom.push.enabled", False)
    firefox_options.add_argument("--mute-audio")
    driver = webdriver.Firefox(service=Service(GeckoDriverManager(path=os.getcwd()).install(), log_path=os.devnull), options=firefox_options)
    driver.implicitly_wait(10)
    os.system("cls" if sys.platform == "win32" else "clear")

    with open("tryhackmebot.log", 'a') as f:
        print("[+] Starting...")
        date = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
        f.write(f"{date}\n")
        f.write("[+] Starting...\n")

    login_form(driver)
    keep_streak(driver)

    with open("tryhackmebot.log", 'a') as f:
        print("[+] Closing...")
        f.write("[+] Closing...\n\n")

    driver.quit()


if __name__ == "__main__":
    main()

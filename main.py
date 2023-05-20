import sys
import datetime
from login import *
from keepstreak import *
from browser import *


def main():
    driver = get_driver()
    driver.implicitly_wait(10)
    os.system("cls" if sys.platform == "win32" else "clear")

    with open("tryhackmebot.log", 'w') as f:
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

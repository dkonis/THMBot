import time
import random
from login import *
from selenium.webdriver.common.by import By


def keep_streak(driver):
    try:
        time.sleep(random.uniform(3,6))
        driver.get("https://tryhackme.com/room/polkit")
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/div/div[1]/div/div/div/div[3]/div/div/div/div[2]").click()
        time.sleep(random.uniform(1,2))
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/div/div[1]/div/div/div/div[3]/div/div/div/div[2]/div/a[3]").click()
        time.sleep(random.uniform(1,3))
        driver.find_element(By.XPATH, "/html/body/div[2]/div[12]/div/div/div[3]/button").click()

        with open("tryhackmebot.log", 'a') as f:
            print("[+] Room's Progress Reset")
            f.write("[+] Room's Progress Reset\n")

        time.sleep(random.uniform(3,6))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(random.uniform(2,3))
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div[5]/div[2]/div[1]/div[2]/div/div[4]/div[2]/button").click()

        time.sleep(random.uniform(1,3))
        driver.get("https://tryhackme.com/room/polkit")
        streak = driver.find_element(By.ID, "user-streak").get_attribute("data-streak")

        with open("tryhackmebot.log", 'a') as f:
            print(f"[+] Success! Your Streak is {streak}")
            f.write(f"[+] Success! Your Streak is {streak}\n")
    except KeyboardInterrupt:
        pass        
    except Exception:
        with open("tryhackmebot.log", 'a') as f:
            print("[+] Something Went Wrong, Trying Again...")
            f.write("[+] Something Went Wrong, Trying Again...\n")
        keep_streak(driver)

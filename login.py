import os
import time
import random
import configparser
from urllib import request
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
import pydub
import speech_recognition


def change_type():
    sound = pydub.AudioSegment.from_mp3(f"{os.getcwd()}/recapchasound/sample.wav")
    sound.export(f"{os.getcwd()}/recapchasound/sample.wav", format="wav")


def recapcha(driver):
    time.sleep(random.uniform(1,3))
    with open("tryhackmebot.log", 'a') as f:
        print("[+] Attempting to Solve Recaptcha")
        f.write("[+] Attempting to Solve Recaptcha\n")

    frames = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(frames)
    
    time.sleep(random.uniform(1,3))
    driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click()
    
    time.sleep(random.uniform(1,3))
    driver.switch_to.default_content()
    try:
        frames = driver.find_element(By.XPATH, "/html/body/div[4]/div[4]").find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(frames)
        driver.find_element(By.ID, "recaptcha-audio-button").click()

        time.sleep(random.uniform(1,3))
        driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/button").click()

        time.sleep(random.uniform(1,3))
        src = driver.find_element(By.XPATH, "/html/body/div/div/div[7]/a").get_attribute("href")
        os.makedirs("recapchasound", exist_ok=True)
        request.urlretrieve(src, f"{os.getcwd()}/recapchasound/sample.wav")
        change_type()

        sample_audio = speech_recognition.AudioFile(f"{os.getcwd()}/recapchasound/sample.wav")
        recognize = speech_recognition.Recognizer()
        with sample_audio as source:
            audio = recognize.record(source)
        
        key = recognize.recognize_google(audio)
        with open("tryhackmebot.log", 'a') as f:
            print(f"[+] Recaptcha Passcode: {key}")
            f.write(f"[+] Recaptcha Passcode: {key}\n")

        driver.find_element(By.ID, "audio-response").send_keys(key.lower())
        time.sleep(random.uniform(1,3))
        driver.find_element(By.ID, "recaptcha-verify-button").click()
    except ElementNotInteractableException:
        pass
    driver.switch_to.default_content()

def login_form(driver):
    if os.path.exists(r'account.conf'):
        config = configparser.ConfigParser()
        config.read("account.conf")
    else:
        with open("tryhackmebot.log", 'a') as f:
            print("[+] Cannot load config. Please run setup.")
            f.write("[+] Cannot load config. Please run setup\n")
            exit(1)
    try:
        driver.get("https://tryhackme.com/login")
        time.sleep(random.uniform(3,6))
        driver.find_element(By.CLASS_NAME, "form-control").send_keys(config["account"]["mail"])
        time.sleep(random.uniform(1,3))
        driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/form/div[2]/input").send_keys(config["account"]["pass"])
        recapcha(driver)
        
        time.sleep(random.uniform(1,3))
        driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/form/button").click()

        if driver.current_url == "https://tryhackme.com/dashboard":
            with open("tryhackmebot.log", 'a') as f:
                print("[+] You Are Logged In!")
                f.write("[+] You Are Logged In!\n")
        else:
            login_form(driver)
    except KeyboardInterrupt:
        pass
    except Exception:
        with open("tryhackmebot.log", 'a') as f:
            print("[+] Something Went Wrong, Trying Again...")
            f.write("[+] Something Went Wrong, Trying Again...\n")
        login_form(driver)

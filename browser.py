import subprocess, platform, time, os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as ffService
from selenium.webdriver.chrome.service import Service as chService
from webdriver_manager.firefox import GeckoDriverManager as gdm
from webdriver_manager.chrome import ChromeDriverManager as cdm

os_family = platform.uname().system
if os_family == "Linux":
    s = ["sh",f"{os.getcwd()}/id_browser.sh"]
elif os_family == "Windows":
    s = ["powershell", f"{os.getcwd()}\id_browser.ps1"]

def get_browser_bin(command):
    with open("f", 'w') as file:
        p = subprocess.Popen(command, stdout=file)
        time.sleep(2)
        file.close()
    with open("f", 'r') as file:    
        e = file.readline().strip()
        file.close()
        try:
            os.remove("f")
            return e
        except FileNotFoundError:
            pass
        except PermissionError:
            pass


browser_exec = get_browser_bin(s)
print(browser_exec)

def get_driver():
    if "chrome" in browser_exec:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--mute-audio")
        driver = webdriver.Chrome(browser_exec, service=chService(cdm(path=os.getcwd()).install()), options=chrome_options)        
    elif "firefox" in browser_exec:
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--headless')
        firefox_options.set_preference("media.volume_scale", "0.0")
        firefox_options.set_preference("dom.push.enabled", False)
        driver = webdriver.Firefox(firefox_binary=browser_exec, service=ffService(gdm(path=os.getcwd()).install()), options=firefox_options)
    else:
        print("Could not create webdriver for browser.")
    return driver
    
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
from random import randint, choice
import threading

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
def genera_video():
    slp=randint(60,300)
    #options = Options()
    #options.add_argument('--headless=new')
    driver = webdriver.Chrome()
    driver.get("https://www.croxyproxy.com/_fr/social")
    youtube = ["https://www.youtube.com/watch?v=5gzA2SR_9Mk", "https://www.youtube.com/watch?v=5gzA2SR_9Mk", 
               "https://www.youtube.com/watch?v=5gzA2SR_9Mk","https://www.youtube.com/watch?v=ntC2F4Vf2FI",
               "https://www.youtube.com/watch?v=ntC2F4Vf2FI","https://www.youtube.com/watch?v=DM0Zks4QoUw"]

    try:
        consent_button_proxy = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'fc-choice-dialog'))
        )

        consent_buttons_proxy = consent_button_proxy.find_element(By.CLASS_NAME, 'fc-cta-consent')
        if consent_buttons_proxy:
            consent_buttons_proxy.click()
        
            input_url = driver.find_element(By.ID,"url")
            submit   = driver.find_element(By.ID,"requestSubmit")
            input_url.send_keys(choice(youtube))
            #wait = WebDriverWait( driver, 50 )
            submit.click()
        
    except TimeoutException:
        print('Cookie modal missing')

    try:
        # wait up to 15 seconds for the consent dialog to show up
        consent_overlay = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, 'dialog'))
        )

        # select the consent option buttons
        consent_buttons = consent_overlay.find_elements(By.CSS_SELECTOR, '.eom-buttons button.yt-spec-button-shape-next')
        if len(consent_buttons) > 1:
            # retrieve and click the 'Accept all' button
            accept_all_button = consent_buttons[1]
            accept_all_button.click()
            sleep(slp)
    except TimeoutException:
        print('Cookie modal missing')
        
def auto_video():
    threads = list()
    for i in range(3):
        x=threading.Thread(target=genera_video)
        threads.append(x)
        x.start()
        sleep(randint(0,3))
        
    for th in threads:
        th.join()
        
if __name__ == "__main__":
    while True:
        auto_video()
        sleep(randint(2,15))
        
    

    
    


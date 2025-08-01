import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
import time, os

def gerar_audio(frase, voz):
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

    driver = uc.Chrome(options=options)
    driver.get("https://fakeyou.com/")

    time.sleep(4)
    driver.find_element(By.ID, "model-search").send_keys(voz)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "dropdown-item").click()
    time.sleep(1)

    driver.find_element(By.ID, "text-to-speak").send_keys(frase)
    driver.find_element(By.ID, "submit-button").click()

    time.sleep(12)
    audio = driver.find_element(By.TAG_NAME, "audio").get_attribute("src")
    os.system(f"curl {audio} -o vozdk.wav")

    driver.quit()
    return "vozdk.wav"

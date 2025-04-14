# loop.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_scraper(driver, wait, keyword_file):
    with open(keyword_file, "r", encoding="utf-8") as f:
        keywords = [kw.strip() for kw in f if kw.strip()]

    for idx, keyword in enumerate(keywords, 1):
        print(f"[{idx}/{len(keywords)}] Processing: {keyword}")
        driver.get("https://app.pinsearch.co/keyword-research")

        search_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter your seed keyword']")))
        search_input.clear()
        search_input.send_keys(keyword)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Search']"))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Select all']")))

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Select all']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Export')]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'All Keywords')]"))).click()

        print(f"✅ Exported: {keyword}")
        time.sleep(3)

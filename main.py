# main.py
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from login import login
from loop import run_scraper
from config import EMAIL, PASSWORD, KEYWORD_FILE  # <-- imported here

def main():
    options = Options()
    options.add_argument('--start-maximized')
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 25)

    try:
        login(driver, wait, EMAIL, PASSWORD)
        run_scraper(driver, wait, KEYWORD_FILE)
        print("🎉 All keywords exported.")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

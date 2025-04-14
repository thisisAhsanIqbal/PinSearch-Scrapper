# login.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, wait, email, password):
    driver.get("https://app.pinsearch.co/sign-in")

    wait.until(EC.presence_of_element_located((By.ID, "identifier-field"))).send_keys(email)
    wait.until(EC.presence_of_element_located((By.ID, "password-field"))).send_keys(password)

    continue_btn = driver.execute_script("""
        return document.querySelector("body > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > form:nth-child(3) > button:nth-child(3)");
    """)
    wait.until(lambda d: continue_btn.is_enabled())
    continue_btn.click()

    try:
        popup = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/button/*[name()='svg']")))
        popup.click()
        print("✅ Closed popup.")
    except:
        print("⚠️ No popup appeared.")

    wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Keyword Finder']")))
    print("✅ Logged in successfully.")

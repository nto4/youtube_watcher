import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--disable-useAutomationExtension")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument("--disable-application-cache")
options.add_argument("--incognito")
# options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--silent")



URL = "https://www.youtube.com/watch?v=VfOt_onJbYQ" # hangi videolinkini izleyecek
KAC_SN_IZLESIN = 10 # kac saniye reklamlar için 2 kez 10 ar sn beklıyoruz eger reklam yoksa 20 sn bekleyecek yanı bu surenın uzerıne kac sn ızlesın reklam var ise bu sureyı ızlemez bılgıne  

browser = webdriver.Chrome(options=options, executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browser.get(URL)

WebDriverWait(browser, 15).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[@aria-label='Play']"))).click()

for i in range(2): # 2 reklam cıkıyor gordugum max 5 er sn den her seferınde 10 sn ye kadar beklıyor 
    try:
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
            (By.ID, "ad-text:6"))).click()
    except:
        pass

time.sleep(KAC_SN_IZLESIN)

browser.quit()


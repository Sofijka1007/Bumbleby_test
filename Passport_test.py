from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as pug

s = Service('C:/Selenium/firefox/geckodriver.exe')
driver = webdriver.Firefox(service=s)
wait = WebDriverWait(driver, 5)
driver. implicitly_wait(10)

driver.get("https://qa.neapro.site/login/")
driver. maximize_window()

# авторизация в Личном кабинете

driver.find_element(By.XPATH, "./html/body/div/div/div/section/div[2]/div/div/div/form/div[1]/div[1]/div/input").send_keys("racoon@racoon.coon")
driver.find_element(By.XPATH, "./html/body/div/div/div/section/div[2]/div/div/div/form/div[1]/div[2]/div/input").send_keys("Rr123456")
driver.find_element(By.XPATH, "./html/body/div/div/div/section/div[2]/div/div/div/form/div[2]/button").click()

# Форма "Паспорт"

driver.find_element(By.XPATH, "./html/body/div/div/div/div[3]/div/div/div[3]/div/div/div[2]/div[2]/div[1]").click()

# Заполение полей формы

driver.find_element(By.ID, "surname").send_keys("Енотиков")
driver.find_element(By.ID, "name").send_keys("Котик")
driver.find_element(By.ID, "patronymic").send_keys("Енотович")
driver.find_element(By.XPATH, "./html/body/div[1]/div/div/div[3]/div/div/div[3]/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div/input").send_keys("12.04.2000")
driver.find_element(By.ID, "passportSeries").click()
driver.find_element(By.ID, "passportSeries").clear()
driver.find_element(By.ID, "passportSeries").send_keys("2222")
driver.find_element(By.ID, "passportNumber").click()
driver.find_element(By.ID, "passportNumber").clear()
driver.find_element(By.ID, "passportNumber").send_keys("555666")
driver.find_element(By.XPATH, "./html/body/div/div/div/div[3]/div/div/div[3]/div/div/div[2]/div[3]/div[3]/div/div[1]/div/div/input").send_keys("15.04.2014")
driver.find_element(By.ID, "code").click()
driver.find_element(By.ID, "code").clear()
driver.find_element(By.ID, "code").send_keys("203111")
driver.find_element(By.ID, "cardId").clear()
driver.find_element(By.ID, "cardId").send_keys("11122255588")
driver.find_element(By.ID, "issued").send_keys("ОУФМС лесных енотиков")
seladr = driver.find_element(By.XPATH, "./html/body/div/div/div/div[3]/div/div/div[3]/div/div/div[2]/div[3]/div[5]/div/div/div/div/div/input")
seladr.send_keys("г Москва, ул Московская, д 1, кв 1")
wait.until(EC.visibility_of_element_located((By.XPATH, "./html/body/div/div/div/div[3]/div/div/div[3]/div/div/div[2]/div[3]/div[5]/div/div/div/div/div[2]/span[1]")))
seladr.send_keys(Keys.DOWN)
seladr.send_keys(Keys.ENTER)
driver.find_element(By.ID, "phone").click()
driver.find_element(By.ID, "phone").clear()
driver.find_element(By.ID, "phone").send_keys("9874562233")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Прикрепление файла

driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div/div[3]/div/div/div[2]/div[3]/div[9]/button[1]").click()
pug.typewrite("Koala.jpg", 0.1)
pug.press('enter')

# Отправка формы

fill = driver.find_element(By.XPATH, "./html/body/div/div/div/div[3]/div/div/div[3]/div/div/div[2]/div[3]/div[9]/button[2]")
wait.until(EC.element_to_be_clickable(fill))
fill.click()
driver.close()

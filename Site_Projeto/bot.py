import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome(
    executable_path="/Users/Asus/Downloads/chromedriver"
)

driver.get("http://127.0.0.1:5500/Login/DashBoard.html")
f = open("results.txt", "a")
f.truncate(0)

driver.maximize_window()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div/ul/li[6]/a').click()
time.sleep(1)
driver.find_element(By.ID,"user").send_keys("Admin")
time.sleep(1)
driver.find_element(By.ID,"pass").send_keys("admin12345")
time.sleep(1)
f.write("Dei login como cliente!\n")

driver.find_element(By.XPATH,'/html/body/section/div[2]/div/div/div[1]/div[4]/a').click()
time.sleep(1)

f.write("Entrei na página dos meus animais!\n")

driver.find_element(By.XPATH,'/html/body/div/ul/li[3]/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/section/div[2]/div/div[2]/button').click()
time.sleep(1)
driver.find_element(By.ID,"nome").send_keys("Tobi")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='sexo']/option[2]").click()
time.sleep(1)
driver.find_element(By.ID,"age").send_keys("10")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='size']/option[3]").click()
time.sleep(2)
driver.find_element(By.ID,"submitInput").click()

f.write("Adicionei um novo animal!\n")

driver.execute_script("window.scrollBy(0,290)","")
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div/ul/li[5]/a").click()
time.sleep(2)
flag=driver.find_element(By.XPATH,"/html/body/section/div[2]/div/section[2]/div/div[2]/div/button")
driver.execute_script("arguments[0].scrollIntoView();",flag)
flag.click()

f.write("Adicionei um Colete de Arrefecimento ao carrinho!\n")
time.sleep(2)
flag=driver.find_element(By.XPATH,"/html/body/section/div[2]/div/section[2]/div/div[4]/div/button")
driver.execute_script("arguments[0].scrollIntoView();",flag)
flag.click()
f.write("Adicionei um Kong Osso ao carrinho!\n")
time.sleep(2)

flag=driver.find_element(By.XPATH,"/html/body/section/div[2]/div/section[2]/div/div[6]/div/button")
driver.execute_script("arguments[0].scrollIntoView();",flag)
flag.click()
f.write("Adicionei um Master Food Junior Premium ao carrinho!\n")
time.sleep(2)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/section/div[2]/div/section[3]/div[2]/div[1]/div[2]/button").click()
f.write("Removi o Colete de Arrefeciento do carrinho!\n")
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/section/div[2]/div/section[3]/div[4]/button").click()

driver.find_element(By.XPATH,"//*[@id='popup']/input[1]").send_keys("Teste")
driver.find_element(By.XPATH,"//*[@id='popup']/input[2]").send_keys("Teste")
driver.find_element(By.XPATH,"//*[@id='popup']/input[3]").send_keys("123456789")
driver.find_element(By.XPATH,"//*[@id='popup']/input[4]").send_keys("Rua Teste")
driver.find_element(By.XPATH,"//*[@id='popup']/input[5]").send_keys("1234-567")

time.sleep(1)

f.write("Comprei novos items para os meus animais!\n")

driver.find_element(By.XPATH,"/html/body/div/ul/li[5]/a").click()
time.sleep(2)

driver.execute_script("arguments[0].scrollIntoView();",driver.find_element(By.XPATH,"/html/body/section/div[2]/div/div[2]/section/div[2]/a/h3"))

time.sleep(2)

driver.find_element(By.XPATH,"/html/body/section/div[2]/div/div[2]/section/div[2]/a").click()
time.sleep(2)


driver.find_element(By.XPATH,"/html/body/section/div[2]/div/div/div/div/div[1]/div[2]/div/div[4]/span[2]").click()
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/section/div[2]/div/div/div/div/div[2]/div[2]/a[1]/button").click()
time.sleep(2)

f.write("Marquei uma consulta com um veterinário para os meus animais!\n")

driver.find_element(By.XPATH,"/html/body/div/ul/li[8]/a").click()
time.sleep(2)

driver.execute_script("arguments[0].scrollIntoView();",driver.find_element(By.XPATH,"/html/body/section/div[2]/div/div/div/div[3]/div[2]/a"))
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/section/div[2]/div/div/div/div[3]/div[2]/a").click()
time.sleep(2)


driver.find_element(By.ID,"cardName").send_keys("Teste")
driver.find_element(By.ID,"cardNum").send_keys("Teste")
driver.find_element(By.ID,"cVV").send_keys("123")
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/section/button").click()
time.sleep(1)

f.write("Aderi a um novo plano!\n")
f.close()

driver.quit()


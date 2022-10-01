from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# ---------- TODO ------------ 

#ENTER YOUR CHROMEDRIVER LOCATION 

chromedriver_location = "enter your chromedriver.exe location including chromedriver.exe in the end"
driver = webdriver.Chrome(chromedriver_location)
driver.get("https://www.duolingo.com")

account = '//*[@id="root"]/div/div/span[1]/div/div[1]/div[2]/div[2]/a'
username_input = '//*[@id="overlays"]/div[5]/div/div[2]/form/div[1]/div[1]/div[1]/label/div/input'
password_input = '//*[@id="overlays"]/div[5]/div/div[2]/form/div[1]/div[1]/div[2]/label/div[1]/input'
login_submit = '//*[@id="overlays"]/div[5]/div/div[2]/form/div[1]/button/span'

WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[data-test='have-account']"))).click()

# --------- TODO -------------

#ENTER YOUR DUOLINGO EMAIL AND PASSOWRD FOR LOGIN


driver.find_element_by_css_selector("input[data-test='email-input']").send_keys("enter your email")
driver.find_element_by_css_selector("input[data-test='password-input']").send_keys("enter password")
button = driver.find_element_by_css_selector("button[data-test='register-button']")
driver.execute_script("arguments[0].click();", button)


WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[4]/div/div/div/div[1]/div/div[2]/div[1]/div/div[5]/div/div/div/div[1]/div'))).click()


WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[4]/div/div/div/div[1]/div/div[2]/div[1]/div/div[5]/div/div[2]/div/div[1]/div[4]/a'))).click()


WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[data-test='player-toggle-keyboard']"))).click()

gWords = []
size = []

for i in range(10):	

	time.sleep(0.5)
	
	size.append(len(driver.find_elements_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/span/div')))
	
	nsize = size[i]  

	gWords = []

	for j in range(1,nsize+1):
		gWords.append(WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/span/div['+str(j)+']'))).text)

	s = " "

	s = s.join(gWords)
	 
	ele = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"textarea[data-test='challenge-translate-input']")))

	translations = {
		"Darf ich dich zum abendessen einladen": "May I invite you to dinner",
		"Ich finde dich nett": "I think you are nice",
		"Der Kaffee geht auf mich": "The coffee is on me",
		"Deine Augen sind wie Sterne.": "Your eyes are like stars",
		"Ich finde dich süß": "I think you're cute",
		"Willst du tanzen": "Do you want to dance",
		"Darf ich dich küssen": "May I kiss you",
		"Ich möchte dich besser kennen lernen": "I would like to get to know you better",
		"Du siehst aus wie meine nachste freundin": "You look like my next girlfriend",
		"Ich bin neu hier, und du?": "I am new here, and you",
		"Du bist schlau": "You are smart",
		"Du bist witzig": "You are funny",
		"Kann ich dir ein Getränk bestellen": "Can I order you a drink",
		"Ich hab mich in dich verliebt": "I have fallen in love with you",
		"Du kannst gut tanzen!": "You can dance well",
		"Ich liebe dich": "I love you",
		"Ich mag dich": "I like you",
		"Kann ich dich anrufen": "Can I call you",
		"Willst du mit mir ausgehen": "Do you want to go out with me"
	}

	if s in translations.keys():
		ele.send_keys(translations[s])

	WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[data-test='player-next']"))).click()

	WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[data-test='player-next']"))).click()

	time.sleep(0.5)
	if(i==4):

		WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[data-test='player-next']"))).click()

	i = i+1

time.sleep(4)
driver.find_element_by_css_selector("button[data-test='player-next']").click()
time.sleep(7)
driver.close()


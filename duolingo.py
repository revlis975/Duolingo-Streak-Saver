from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--output=/dev/null")
chrome_options.add_argument("--mute-audio")


driver = webdriver.Chrome(options=chrome_options)
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

time.sleep(5)

try:
	WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[5]/div/div/div[1]/div/div[2]/div[1]/div/div[5]/div/div/div/div[1]/div/div[1]/div[1]'))).click()
	time.sleep(3)
	WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[5]/div/div/div[1]/div/div[2]/div[1]/div/div[5]/div/div[2]/div/div[1]/div[4]/a'))).click()
except:
	try:
		WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="overlays"]/div[4]/div/div[2]/button/span'))).click()
		time.sleep(3)
		WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[5]/div/div/div/div[1]/div/div[2]/div[1]/div/div[5]/div/div[2]/div/div[1]/div[4]/a'))).click()
	except:
		WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="overlays"]/div[4]/div/div/div/div[2]/button'))).click()
		time.sleep(3)
		WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[5]/div/div/div/div[1]/div/div[2]/div[1]/div/div[5]/div/div[2]/div/div[1]/div[4]/a'))).click()
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

	if(s.startswith('Darf ich dich zum')):
		ele.send_keys("May I invite you to dinner")

	if(s.startswith('Ich finde dich nett')):
		ele.send_keys("I think you are nice")

	if(s.startswith('Der Kaffee')):
		ele.send_keys("The coffee is on me")

	if(s.startswith('Deine Augen sind')):
		ele.send_keys("Your eyes are like stars")

	if(s.startswith('Ich finde dich s????')):
		ele.send_keys("I think you're cute")

	if(s.startswith('Willst du tanzen')):
		ele.send_keys("Do you want to dance")

	if(s.startswith('Darf ich dich k??ssen')):
		ele.send_keys("May I kiss you")

	if(s.startswith('Ich m??chte dich besser')):
		ele.send_keys("I would like to get to know you better")

	if(s.startswith('Du siehst aus wie meine')):
		ele.send_keys("You look like my next girlfriend")

	if(s.startswith('Ich bin neu')):
		ele.send_keys("I am new here, and you")

	if(s.startswith('Du bist schlau')):
		ele.send_keys("You are smart")

	if(s.startswith('Du bist witzig')):
		ele.send_keys("You are funny")

	if(s.startswith('Kann ich dir ein')):
		ele.send_keys("Can I order you a drink")

	if(s.startswith('Ich hab mich in dich verliebt')):
		ele.send_keys("I have fallen in love with you")

	if(s.startswith('Du kannst gut tanzen')):
		ele.send_keys("You can dance well")

	if(s.startswith('Ich liebe dich')):
		ele.send_keys("I love you")

	if(s.startswith('Ich mag dich')):
		ele.send_keys("I like you")

	if(s.startswith('Kann ich dich anrufen')):
		ele.send_keys("Can I call you")

	if(s.startswith('Willst du mit mir ausgehen')):
		ele.send_keys("Do you want to go out with me")

	WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[data-test='player-next']"))).click()

	WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[data-test='player-next']"))).click()

	time.sleep(0.5)
	if(i==4):

		WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[data-test='player-next']"))).click()

	i = i+1

print("Congratulations on continuing your streak!!")
time.sleep(4)
driver.find_element_by_css_selector("button[data-test='player-next']").click()
time.sleep(7)
driver.close()


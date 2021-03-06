from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

driver = webdriver.Chrome("C:/Users/HP/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://www.duolingo.com")

account = '//*[@id="root"]/div/div/span[1]/div/div[1]/div[2]/div[2]/a'
username_input = '//*[@id="overlays"]/div[5]/div/div[2]/form/div[1]/div[1]/div[1]/label/div/input'
password_input = '//*[@id="overlays"]/div[5]/div/div[2]/form/div[1]/div[1]/div[2]/label/div[1]/input'
login_submit = '//*[@id="overlays"]/div[5]/div/div[2]/form/div[1]/button/span'

driver.find_element_by_xpath(account).click()

#TIP - Use xpath for clicks and css selector for sendkeys
# driver.implicitly_wait(20)
# time.sleep(5)
# driver.switch_to.frame("frame_id or frame_name")
# driver.find_element_by_xpath(username_input).send_keys("kleerhan@garagedoormaricopas.com")
# WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,username_input))).send_keys("kleerhan@garagedoormaricopas.com")

#------------------ ITS A DUMMY ACCOUNT WITH TEMPORARY EMAIL FOR NOW-----------------


driver.find_element_by_css_selector("input[data-test='email-input']").send_keys("guptaryan975@gmail.com")
driver.find_element_by_css_selector("input[data-test='password-input']").send_keys("aryan2001")
button = driver.find_element_by_css_selector("button[data-test='register-button']")
driver.execute_script("arguments[0].click();", button)
# driver.find_element_by_css_selector("div[data-test='skill-icon']").click()
# driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/div[2]').click()
# WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[5]/div/div/div/div[2]'))).click()
WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[5]/div/div/div/div[1]/div/div[2]/div[1]'))).click()
time.sleep(1)
# WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[5]/div/div[2]/div/div[1]/div[3]/button'))).click()
WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[5]/div/div[2]/div/div[1]/div[3]/button'))).click()
# driver.implicitly_wait(20)
# driver.find_element_by_css_selector("input[data-test='password-input']").send_keys("bruhbruh")<div class="yWRY8 _3yAjN">Use keyboard</div>
WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[data-test='player-toggle-keyboard']"))).click()

# html = urllib.request.urlopen(driver.current_url, context=ctx).read()
# print(driver.current_url)
# soup = BeautifulSoup(html, 'html.parser')

# for item in soup.select("div._34k_q _3Lg1h _13doy"):
#     print(item.get_text())
# url = driver.current_url
# page = requests.get(url)
# tree = html.fromstring(page.content)
# print(tree)
# #This will create a list of buyers:
# print(tree.xpath('//div[@class="_34k_q _3Lg1h _13doy"]/text()'))
# //*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/span/div[5]
# //*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/span/div[1]
gWords = []
size = []

# for j in range(10):
# print(WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/span/div[1]'))).text)
for j in range(10):	
	# driver.implicitly_wait(30)
	time.sleep(1)
	# WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"textarea[data-test='challenge-translate-input']"))).click()
	# time.sleep(1)
	size.append(len(driver.find_elements_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/span/div')))
	
	# nsize = 0

	# # -------------- SIZE AS IT TURNED OUT WAS CUMULATIVE WITH EVERY PAGE -------------
	# if(j>0):
	# 	nsize = size[j] - size[j-1]
	# else:
	nsize = size[j]  
	print(nsize)
	gWords = []
	print(gWords)
	for i in range(1,nsize+1):
		gWords.append(WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/span/div['+str(i)+']'))).text)
		# gWords.append(driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/span/div['+str(i)+']').text)

	s = " "
	print(s)
	s = s.join(gWords)
	print(s)

	# ele = driver.find_element_by_css_selector("textarea[data-test='challenge-translate-input']")
	 
	ele = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"textarea[data-test='challenge-translate-input']")))

	# type(ele)

	# def translate(ele):

	if(s.startswith('Darf ich dich zum')):
		ele.send_keys("May I invite you to dinner")

	if(s.startswith('Ich finde dich nett')):
		ele.send_keys("I think you are nice")

	if(s.startswith('Der Kaffee')):
		ele.send_keys("The coffee is on me")

	if(s.startswith('Deine Augen sind')):
		ele.send_keys("Your eyes are like stars")

	if(s.startswith('Ich finde dich süß')):
		ele.send_keys("I think you're cute")

	if(s.startswith('Willst du tanzen')):
		ele.send_keys("Do you want to dance")

	if(s.startswith('Darf ich dich küssen')):
		ele.send_keys("May I kiss you")

	if(s.startswith('Ich möchte dich besser')):
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
	time.sleep(2)
	if(j==4):
		WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[data-test='player-next']"))).click()
	j = j+1

time.sleep(7)
WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[data-test='player-next']"))).click()

# bWords = []
# size.append(len(driver.find_elements_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/span/div')))

# nsize = 0
# # if(j>0):
# # 	nsize = size - tot

# # else:
# nsize = size[1] - size[0]

# print(nsize)
# for i in range(1,nsize+1):
# 	print(driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/span/div['+str(i)+']').text)

# s = " "
# s = s.join(bWords)
# print(s)

# ele = driver.find_element_by_css_selector("textarea[data-test='challenge-translate-input']")

# if(s.startswith('Darf ich dich zum')):
# 	ele.send_keys("May I invite you to dinner")

# if(s.startswith('Ich finde dich nett')):
# 	ele.send_keys("I think you are nice")

# if(s.startswith('Der Kaffee')):
# 	ele.send_keys("The coffee is on me")

# if(s.startswith('Deine Augen sind')):
# 	ele.send_keys("Your eyes are like stars")

# if(s.startswith('Ich finde dich süß')):
# 	ele.send_keys("I think you're cute")

# if(s.startswith('Willst du tanzen?')):
# 	ele.send_keys("Do you want to dance")

# if(s.startswith('Darf ich dich küssen?')):
# 	ele.send_keys("May I kiss you")

# if(s.startswith('Ich möchte dich besser')):
# 	ele.send_keys("I would like to get to know you better")

# if(s.startswith('Du siehst aus wie meine')):
# 	ele.send_keys("You look like my next girlfriend")

# if(s.startswith('Ich bin neu')):
# 	ele.send_keys("I am new here, and you")

# if(s.startswith('Du bist schlau')):
# 	ele.send_keys("You are smart")

# if(s.startswith('Du bist witzig')):
# 	ele.send_keys("You are funny")

# if(s.startswith('Kann ich dir ein')):
# 	ele.send_keys("Can I order you a drink")

# if(s.startswith('Ich hab mich in dich verliebt')):
# 	ele.send_keys("I have fallen in love with you")

# if(s.startswith('Du kannst gut tanzen')):
# 	ele.send_keys("You can dance well")

# if(s.startswith('Ich liebe dich')):
# 	ele.send_keys("I love you")

# if(s.startswith('Ich mag dich')):
# 	ele.send_keys("I like you")

# if(s.startswith('Kann ich dich anrufen')):
# 	ele.send_keys("Can I call you")

# if(s.startswith('Willst du mit mir ausgehen')):
# 	ele.send_keys("Do you want to go out with me")

# WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[data-test='player-next']"))).click()
# WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[data-test='player-next']"))).click()
# # for i in range(1,4):
# 	paths.append('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/span/div['+str(i)+']')


# for path in paths:
# 	if(WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,path))).text):
# 		gWords.append(WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,path))).text)
# 	else: break

# print("bruh"+gWords)

# List<WebElement> allLinks = driver.findElements(By.xpath("//div[@class='datepicker']/div/table/tbody/tr/td/table/tbody[2]/tr/td[@class='' or @class='datepickerSaturday' or @class='datepickerSunday']/a/span"));
# List<WebElement> allLinks = driver.findElements(By.xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/span'));

# Iterator<WebElement> itr = allLinks.iterator();
# while(itr.hasNext()) :
#     System.out.println(itr.next().getText());
# }
# driver.implicitly_wait(20)
# # gWords = driver.findElements(By.xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/span'))
# # for item in gWords:
# # 	print(item.text)
# # print(WebDriverWait(driver,30).until(EC.presence_of_elements_located((By.XPATH,'//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/span'))).text)
# # //*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/span/div[1]
# # //*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/span/div[2]
# # //*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/span/div[3]

# gWords = driver.find_elements_by_class_name('_34k_q _3Lg1h _13doy')
# for item in gWords:
# 	print(item.text)
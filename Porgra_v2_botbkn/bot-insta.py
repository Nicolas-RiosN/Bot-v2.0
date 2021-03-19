from selenium import webdriver


def openInstagram():
	browser = webdriver.Chrome(executable_path='./chromedriver')
	browser.get("https://instagram.com/")
	time.sleep(3)
	
	cookie_button = browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
	cookie_button.click()
	time.sleep(3)

	login = browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
	login.send_keys("TU_USERNAME_AQUI")

	pwd = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
	pwd.send_keys("TUS_CLAVES_AQUI")

	login_button = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')

	login_button.click()
	time.sleep(5)

	browser.get('https://www.instagram.com/direct/t/340')
	time.sleep(5)
	
	notification = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
	notification.click()
	time.sleep(5)

	chat = browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[1]/a')
	chat.click()
	time.sleep(5)

	return browser;

def sendLove(browser, text):
	textBox = browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea') #Primero con tabindex = -1 , _2HE1Z _1hRBM
	textBox.send_keys(text)
	
	time.sleep(1)
	
	sendMessageButton = browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
	sendMessageButton.click()

	print(text)
	return;


def do_your_magic(driver):
	print "================= RoBot-Bakansito-profedemeun7 INICIALIZADO =================" 
	msg = ['Mensaje1' , 'Mensaje1', 'Mensaje1' , 'Mensaje1', 
	'Mensaje1', 'Mensaje1', 'Mensaje1', 'Mensaje1', 'Mensaje1' , 'Mensaje1', 'Mensaje1', 'Mensaje1'
	,'Mensaje1' 'Mensaje1']

	for i in msg:
		sendLove(driver, i)
		



mi_browser = openInstagram()


do_your_magic(driver=mi_browser)
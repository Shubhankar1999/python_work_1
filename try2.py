from selenium import webdriver
from PIL import ImageGrab,ImageOps
import numpy as np
import time
import pyautogui
from selenium.webdriver.common.keys import Keys
# dino nose = 363,523
# 450, 490        550,566

dinonose = [358,525]
replayBtn = [dinonose[0]+270,dinonose[1]+10]
def restartGame():
	pyautogui.click(replayBtn)

def getImageAt(x1,y1, x2,y2):
	
	img = ImageGrab.grab(bbox=(x1,y1,x2,y2)) #bbox specifies specific region (bbox= x,y,width,height *starts top-left)
	grayImg = ImageOps.grayscale(img)
	arrayImg = np.array(grayImg)
	#print(arrayImg.sum())
	return arrayImg.sum()

chromeDriverPath = 'C:\\Users\\shubh\\Downloads\\chromedriver_win32\\chromedriver.exe'
browser = webdriver.Chrome(chromeDriverPath)
#browser.maximize_window()
siteName = "https://chromedino.com/"
#browser.set_page_load_timeout(10)
browser.get(siteName)
# browser.find_element_by_name("q").send_keys("Amazon")
# browser.find_element_by_name("q").send_keys(Keys.ENTER)
# timesleep = 4

# try:
# 	link = browser.find_elements_by_class_name("LC20lb")
# 	# print(link)
# 	link[0].click()
timesleep=10
# 680, 490 ...............930,477,  ,,,970,512
print("Opened browser")
#browser.maximize_window()

Name = "offline main-page"
#dino = browser.find_elements_by_css_selector("offline.main-page")
dino = browser.find_elements_by_xpath("""//*[@id="t"]""")
print("Found dino",dino,"\n")
dino[0].send_keys(Keys.UP)
go = True

x1 = dinonose[0] +10
y1 = dinonose[1] -10
x2 = dinonose[0]+140
y2 = dinonose[1]+35
err = 3000
x11,y11,x22,y22 = dinonose[0]+250,dinonose[1]-13,dinonose[0]+290,dinonose[1]+22
op = getImageAt(x1,y1,x2,y2)
ct = 0
initt = time.time()
limit = 100
while go == True:
	
	sum1 = getImageAt(x1,y1,x2,y2)
	#print(op,"............",sum1)
	ct+=1
	if ct==limit:
		print("----------")
		ct=0
		# x2+=20
		if err>50:
			err = err * 0.30
	if sum1<op-err:
		dino[0].send_keys(Keys.UP)
			
	else:
		pass
		#dino[0].send_keys(Keys.DOWN)
		#time.sleep(0.05)
	rest = getImageAt(x11,y11,x22,y22)
	if  rest == 305992:
		time.sleep(3)
		#restartGame()
		go =False
	#print("rest",rest)
	
	
	time.sleep(0.01)

endt = time.time()
print(ct, endt-initt)
time.sleep(3)
browser.quit()
# print(link.get_attribute('href'))
#browser.find_element_by_name("search_query").send_keys("Latest tech")
# time.sleep(timesleep)
# browser.quit()


"""

<h2 data-attribute="Redmi 6 Pro (Black, 4GB RAM, 64GB Storage)" data-max-rows="0" class="a-size-medium s-inline  s-access-title  a-text-normal">Redmi 6 Pro (Black, 4GB RAM, 64GB Storage)</h2>

"""
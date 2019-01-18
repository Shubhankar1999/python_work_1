from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
chromeDriverPath = 'C:\\Users\\shubh\\Downloads\\chromedriver_win32\\chromedriver.exe'
browser = webdriver.Chrome(chromeDriverPath)

#browser.set_page_load_timeout(10)
browser.get("https://www.amazon.in/")
# browser.find_element_by_name("q").send_keys("Amazon")
# browser.find_element_by_name("q").send_keys(Keys.ENTER)
# timesleep = 4

# try:
# 	link = browser.find_elements_by_class_name("LC20lb")
# 	# print(link)
# 	link[0].click()
timesleep=1
try:
	print("Opened amazon")
	search_box = browser.find_element_by_name("field-keywords")
	search_box.send_keys("SmartPhone")
	search_box.send_keys(Keys.ENTER)
	print("Searched for smartphones")
	class_of_search  = "a-size-medium s-inline  s-access-title  a-text-normal"
	phones = browser.page_source
	ind = 0
	for i in range(20):
		x = phones.find(class_of_search,ind+1)
		print(">> ",x ,"\n", phones[x-50:x+200],"\n")
		ind = x

	ad = browser.find_elements_by_class_name(class_of_search)

except:
	print("No such element")
	timesleep = 1


# print(link.get_attribute('href'))
#browser.find_element_by_name("search_query").send_keys("Latest tech")
time.sleep(timesleep)
browser.quit()
"""

<h2 data-attribute="Redmi 6 Pro (Black, 4GB RAM, 64GB Storage)" data-max-rows="0" class="a-size-medium s-inline  s-access-title  a-text-normal">Redmi 6 Pro (Black, 4GB RAM, 64GB Storage)</h2>

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://text-compare.com/")
driver.maximize_window()
driver.implicitly_wait(10)
input1=driver.find_element_by_xpath("//textarea[@id='inputText1']")
input2=driver.find_element_by_xpath("//textarea[@id='inputText2']")
input1.send_keys("max man min man")
act=ActionChains(driver)

# input select All

# ctrl+A
# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# input copy all

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# press tab to navigate input2

act.send_keys(Keys.TAB).perform()

# input2---ctrl+V  Paste the text

# act.key_down(Keys.CONTROL)
# act.send_keys('v')
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
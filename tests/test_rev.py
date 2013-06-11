from selenium import webdriver
from selenium.webdriver.common.by import By  
from unittestzero import Assert
import time

def test_element_displayed():
    driver = webdriver.Firefox()
    driver.get('http://www.lusini.de/deals/aktuell/')

    driver.find_element(By.CSS_SELECTOR, '.smallerText.lighterText>a').click()
    driver.find_element(By.CSS_SELECTOR, '.tellAFriend .link').click()
    time.sleep(2)
    test_ele = driver.find_element(By.ID, 'fromName')

    Assert.true(test_ele.is_displayed())
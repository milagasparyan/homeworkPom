from project.Lib import LIB
from selenium.webdriver.common.by import By

class ChooseCountry:

    #---locators---
    checkbox       = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/input[1]")
    proceedButton  = (By.XPATH, "//button[contains(text(),'Proceed')]")

    #check terms and conditions
    def __init__(self, browser):
            self.browser = browser

   #click to Add mango to cart
    def clickCheckbox(self, browser ):
       LIB.wait_for_element(self,browser,self.checkbox)
       self.browser.find_element(*self.checkbox).click()

    def clickProccedButton(self, browser ):
        LIB.wait_for_element(self,browser,self.proceedButton)
        self.browser.find_element(*self.proceedButton).click()


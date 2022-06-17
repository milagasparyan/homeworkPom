from project.Lib import LIB
from selenium.webdriver.common.by import By

class Cart:

    #---locators---
    placeOrder          = (By.XPATH, "//button[contains(text(),'Place Order')]")

    def __init__(self, browser):
        self.browser = browser

           #click to Add mango to cart
    def clickplaceOrder(self, browser ):
       LIB.wait_for_element(self,browser,self.placeOrder)
       self.browser.find_element(*self.placeOrder).click()






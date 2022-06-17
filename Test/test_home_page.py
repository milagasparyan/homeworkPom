from project.Lib import LIB
from project.POM import Home
from selenium import webdriver

"""
Go to URL, click on mango add to card and ,
click on the cart icon, click proceed to checkout
"""

def test_1():
    #open browser
    obj_lib = LIB()
    browser = obj_lib.open_browser()

    #navigate to url
    obj_lib.page_load(browser)

    #assert page title
    actualTitle = obj_lib.getTitle(browser)
    expectedTitle = "GreenKart - veg and fruits kart", "https://rahulshettyacademy.com/seleniumPractise/#/" 
    assert actualTitle == expectedTitle
                   
    #add mango to cart
    obj_home = Home()
    obj_home.clickMango(browser)
    actualText = obj_home.getItemsText(browser)
    expectedText = "1"
    actualPrice = obj_home.getPriceText(browser)
    expectedPrice = "75"
    assert actualText == expectedText

    #Click on "Proceed to checkout" button

    obj_home.clickCartIcon(browser)
    obj_home.clickProceedCheckout(browser)

    actualURL = browser.current_url
    expectedURL = "https://rahulshettyacademy.com/seleniumPractise/#/cart"
    assert actualURL == expectedURL

    

    

    




    







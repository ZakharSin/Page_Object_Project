from selenium.webdriver.common.by import By
class ProductLocators():
    BASKET = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    MESSAGE_NAME = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    MESSAGE_PRICE = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
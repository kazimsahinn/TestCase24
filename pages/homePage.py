from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.PageBase import PageBase


class HomePage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    logo = (By.XPATH, "//*[@class='logo pull-left']")
    productsCard = (By.XPATH, "(//*[@class='productinfo text-center'])[2]")
    add_ProductsCard = (By.XPATH, "(//*[@class='btn btn-default add-to-cart'])[4]")
    added_cart = (By.XPATH,"//*[@class='modal-title w-100']")
    continueShopping = (By.XPATH, "//*[@class='btn btn-success close-modal btn-block']")
    clickCart = (By.XPATH, "(//*[@class='fa fa-shopping-cart'])[1]")
    logged = (By.CSS_SELECTOR, "li:nth-of-type(10) > a")
    deleteAccount = (By.XPATH, "//*[@class='fa fa-trash-o']")
    accountDeleted = (By.XPATH, "//*[@class='title text-center']")




    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 200);") # scroll

    def visible_logo(self):

        visibleLogo = self.wait_element_visibility(HomePage.logo)
        return visibleLogo.is_displayed()



    def hover_productsCart(self):
        hover_Cart = self.wait_element_clickable(HomePage.productsCard)
        action = ActionChains(self.driver)
        self.driver.execute_script("window.scrollBy(0, 200);") # scroll
        action.move_to_element(hover_Cart).perform()


    def add_productsCart(self):
        add_Cart = self.wait_element_clickable(HomePage.add_ProductsCard)

        add_Cart.click()


    def added_message(self):
        return self.wait_element_visibility(HomePage.added_cart).is_displayed()


    def continue_shopping(self):
        continue_shopping = self.wait_element_clickable(HomePage.continueShopping)
        continue_shopping.click()


    def open_cart(self):
        self.driver.execute_script("window.scrollBy(0, 0);")  # scroll
        cart = self.wait_element_clickable(HomePage.clickCart)
        cart.click()

    def visible_logged(self):
        return self.wait_element_visibility(HomePage.logged).is_displayed()


    def delete_account(self):
        delete_account = self.wait_element_clickable(HomePage.deleteAccount)
        delete_account.click()


    def account_deleted(self):
        return self.wait_element_visibility(HomePage.accountDeleted).is_displayed()

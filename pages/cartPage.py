from selenium.webdriver.common.by import By
from pages.PageBase import PageBase
import os

class CartPage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    cartMenu = (By.XPATH, "//*[@class='cart_menu']")
    Checkout = (By.XPATH, "//*[@class='btn btn-default check_out']")
    checkoutText = (By.XPATH, "//*[@class='modal-title w-100']")
    register_and_login = (By.XPATH, "(//*[@class='text-center'])[2]")
    billingAdress = (By.XPATH, "//*[@id='address_invoice']")
    deliveryAdress = (By.XPATH, "//*[@id='address_delivery']")
    textArea = (By.CLASS_NAME, "form-control")
    placeOrder = (By.XPATH, "//*[@class='btn btn-default check_out']")
    payment = (By.CLASS_NAME, "heading")
    cardName = (By.NAME, "name_on_card")
    cardNumber = (By.NAME, "card_number")
    cvc = (By.XPATH, "//*[@class='form-control card-cvc']")
    ExpirationMM = (By.XPATH, "//*[@class='form-control card-expiry-month']")
    ExpirationYYYY = (By.XPATH, "//*[@class='form-control card-expiry-year']")
    payAndComfirm = (By.XPATH, "//*[@class='form-control btn btn-primary submit-button']")
    orderPlaced = (By.XPATH, "//*[@class='title text-center']")
    downloadInvoice = (By.XPATH, "//*[@class='btn btn-default check_out']")
    continueButton = (By.XPATH, "//*[@class='btn btn-primary']")




    def visible_cartMenu(self):
        return self.wait_element_visibility(CartPage.cartMenu).is_displayed()



    def proceed_checkout(self):
        proceed_checkout = self.wait_element_clickable(CartPage.Checkout)
        proceed_checkout.click()


    def visible_checkoutText(self):
        return self.wait_element_visibility(CartPage.checkoutText).is_displayed()


    def register_button(self):
        register_button = self.wait_element_clickable(CartPage.register_and_login)
        register_button.click()


    def billing_address(self):
        first_name_last_name = self.driver.find_element(By.XPATH, "(//*[@class='address_firstname address_lastname'])[2]").text
        address = self.driver.find_element(By.XPATH, "(//*[@class='address_address1 address_address2'])[4]").text
        city_state_postcode = self.driver.find_element(By.XPATH, "(//*[@class='address_city address_state_name address_postcode'])[2]").text
        country = self.driver.find_element(By.XPATH, "(//*[@class='address_country_name'])[2]").text
        phone = self.driver.find_element(By.XPATH, "(//*[@class='address_phone'])[2]").text

        return f"{first_name_last_name}\n{address}\n{city_state_postcode}\n{country}\n{phone}"

    def delivery_address(self):
        first_name_last_name = self.driver.find_element(By.XPATH, "(//*[@class='address_firstname address_lastname'])[1]").text
        address = self.driver.find_element(By.XPATH, "(//*[@class='address_address1 address_address2'])[1]").text
        city_state_postcode = self.driver.find_element(By.XPATH,"(//*[@class='address_city address_state_name address_postcode'])[1]").text
        country = self.driver.find_element(By.XPATH, "(//*[@class='address_country_name'])[1]").text
        phone = self.driver.find_element(By.XPATH, "(//*[@class='address_phone'])[1]").text

        return f"{first_name_last_name}\n{address}\n{city_state_postcode}\n{country}\n{phone}"


    def review_order(self):


        description = self.driver.find_element(By.XPATH, "/html/body/section/div/div[5]/table/tbody/tr[1]/td[2]/h4/a").text
        price = self.driver.find_element(By.XPATH, "//*[@class='cart_price']").text
        total = self.driver.find_element(By.XPATH, "(//*[@class='cart_total_price'])[1]").text

        return  f"{description}, {price}, {total}"



    def assert_orderMenu(self):
      actual_menu = self.review_order()
      actual_menu_list = actual_menu.split(', ')
      expected_menu = ["Men Tshirt", "Rs. 400", "Rs. 400"]


      for i in range(len(expected_menu)):
          assert expected_menu[i] == actual_menu_list[i]



    def text_area(self):
        text_area = self.wait_element_visibility(CartPage.textArea)
        text_area.send_keys("You can leave my order to security.")


    def click_placeOrder(self):
        place_order = self.wait_element_clickable(CartPage.placeOrder)
        place_order.click()


    def visible_payment(self):
        return self.wait_element_visibility(CartPage.payment).is_displayed()


    def card_name(self):
        card_name = self.wait_element_visibility(CartPage.cardName)
        card_name.send_keys("Garanti")


    def card_number(self):
        card_number = self.wait_element_visibility(CartPage.cardNumber)
        card_number.send_keys("123456789456")

    def cvc_number(self):
        cvc_number = self.wait_element_visibility(CartPage.cvc)
        cvc_number.send_keys("546")


    def expiration_month(self):
        expiration_month = self.wait_element_visibility(CartPage.ExpirationMM)
        expiration_month.send_keys("05")


    def expiration_year(self):
        expiration_year = self.wait_element_visibility(CartPage.ExpirationYYYY)
        expiration_year.send_keys("2028")


    def pay_and_confirmOrder(self):
        pay_and_confirmOrder = self.wait_element_clickable(CartPage.payAndComfirm)
        pay_and_confirmOrder.click()

    def visible_orderPlaced(self):
        return self.wait_element_visibility(CartPage.orderPlaced).is_displayed()


    def download_invoice(self):
        download_invoice = self.wait_element_clickable(CartPage.downloadInvoice)
        download_invoice.click()


    def invoice_control(self):

        invoice_path = "C:\\Users\\kazms\\Downloads\\invoice.txt"
        return os.path.exists(invoice_path)

    def continue_button(self):
        contiune_button = self.wait_element_clickable(CartPage.continueButton)
        contiune_button.click()
import time

import pytest
from pages.accountPage import AccountPage
from pages.cartPage import CartPage
from pages.homePage import HomePage
from pages.signupPage import SignupPage


@pytest.mark.usefixtures("setUp")
class TestDownloadInvoice:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.homePage = HomePage(self.driver)
        self.cartPage = CartPage(self.driver)
        self.signupPage = SignupPage(self.driver)
        self.accountPage = AccountPage(self.driver)






    def test_case24(self):
        self.driver.get("http://automationexercise.com")
        assert self.homePage.visible_logo()
        self.homePage.scroll_down()
        self.homePage.hover_productsCart()
        self.homePage.add_productsCart()
        assert self.homePage.added_message()
        self.homePage.continue_shopping()
        self.homePage.open_cart()
        assert self.cartPage.visible_cartMenu()
        self.cartPage.proceed_checkout()
        assert self.cartPage.visible_checkoutText()
        self.cartPage.register_button()
        assert self.signupPage.visible_newUserText()
        self.signupPage.write_name()
        self.signupPage.write_email()
        self.signupPage.signup_button()
        assert self.accountPage.visible_account_Information()
        self.accountPage.select_Mr()
        self.accountPage.write_password()
        self.accountPage.select_Day()
        self.accountPage.select_Month()
        self.accountPage.select_Year()
        self.accountPage.select_newsletter()
        self.accountPage.select_partners()
        self.accountPage.write_firstName()
        self.accountPage.write_lastName()
        self.accountPage.write_company()
        self.accountPage.write_adress()
        self.accountPage.select_country()
        self.accountPage.write_state()
        self.accountPage.write_city()
        self.accountPage.write_zipcode()
        self.accountPage.write_mobileNumber()
        self.accountPage.create_account()
        assert self.accountPage.success_accountText()
        self.accountPage.continue_button()
        assert self.homePage.visible_logged()
        self.homePage.open_cart()
        self.cartPage.proceed_checkout()
        assert self.cartPage.delivery_address() == self.cartPage.billing_address()
        assert self.cartPage.assert_orderMenu()
        self.cartPage.text_area()
        self.cartPage.click_placeOrder()
        assert self.cartPage.visible_payment()
        self.cartPage.card_name()
        self.cartPage.card_number()
        self.cartPage.cvc_number()
        self.cartPage.expiration_month()
        self.cartPage.expiration_year()
        self.cartPage.pay_and_confirmOrder()
        assert self.cartPage.visible_orderPlaced()
        self.cartPage.download_invoice()
        time.sleep(2) # dosya indirmesini bekliyoruz.
        assert self.cartPage.invoice_control()
        self.cartPage.continue_button()
        self.homePage.delete_account()
        assert self.homePage.account_deleted()
        self.cartPage.continue_button()











































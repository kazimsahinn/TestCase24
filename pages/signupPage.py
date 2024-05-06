from selenium.webdriver.common.by import By
from pages.PageBase import PageBase


class SignupPage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    newUser_SignupText = (By.XPATH, "//h2[.='New User Signup!']")
    name = (By.NAME, "name")
    email = (By.XPATH, "(//*[@name='email'])[2]")
    signupButton = (By.XPATH, "(//*[@class='btn btn-default'])[2]")



    def visible_newUserText(self):
        return self.wait_element_visibility(SignupPage.newUser_SignupText).is_displayed()

    def write_name(self):
        write_name = self.wait_element_visibility(SignupPage.name)
        write_name.send_keys("Kazım")


    def write_email(self):
        write_email = self.wait_element_visibility(SignupPage.email)
        write_email.send_keys("kazmshn@gmail.com")


    def signup_button(self):
        signup_button = self.wait_element_clickable(SignupPage.signupButton)
        signup_button.click()
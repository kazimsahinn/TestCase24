from selenium.webdriver.common.by import By
from pages.PageBase import PageBase
from selenium.webdriver.support.ui import Select

class AccountPage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    account = (By.XPATH, "(//*[@class='title text-center'])[1]")
    genderMr = (By.XPATH, "//*[@id='id_gender1']")
    password = (By.XPATH, "//*[@id='password']")
    day = (By.XPATH, "//*[@name='days']")
    month = (By.XPATH, "//*[@name='months']")
    year = (By.XPATH, "//*[@name='years']")
    newsletter = (By.XPATH, "//*[@id='newsletter']")
    partners = (By.XPATH, "//*[@id='optin']")
    first_name = (By.XPATH, "//*[@id='first_name']")
    last_name = (By.XPATH, "//*[@id='last_name']")
    company = (By.XPATH, "//*[@id='company']")
    adress1 = (By.XPATH, "//*[@id='address1']")
    country = (By.XPATH, "//*[@id='country']")
    state = (By.XPATH, "//*[@id='state']")
    city = (By.XPATH, "//*[@id='city']")
    zipcode = (By.XPATH, "//*[@id='zipcode']")
    mobile_number = (By.XPATH, "//*[@id='mobile_number']")
    createAccount = (By.XPATH, "(//*[@class='btn btn-default'])[1]")
    succesAccount = (By.XPATH, "//*[@class='title text-center']")
    continueButton = (By.XPATH, "//*[@class='btn btn-primary']")






    def visible_account_Information(self):
        return self.wait_element_visibility(AccountPage.account).is_displayed()



    def select_Mr(self):
        select_genderMr = self.wait_element_clickable(AccountPage.genderMr)
        select_genderMr.click()


    def write_password(self):
        write_password = self.wait_element_visibility(AccountPage.password)
        write_password.send_keys("123456789")


    def select_Day(self):
        select_birthDay = self.wait_element_clickable(AccountPage.day)

        birthDay_select = Select(select_birthDay)
        birthDay_select.select_by_value("29")


    def select_Month(self):
        select_month = self.wait_element_clickable(AccountPage.month)

        birthMonth_select = Select(select_month)

        birthMonth_select.select_by_value("7")


    def select_Year(self):
        select_year = self.wait_element_clickable(AccountPage.year)

        birthYear_select = Select(select_year)

        birthYear_select.select_by_value("1994")


    def select_newsletter(self):
        select_newsletter = self.wait_element_clickable(AccountPage.newsletter)
        select_newsletter.click()


    def select_partners(self):
        select_partners = self.wait_element_clickable(AccountPage.partners)
        select_partners.click()


    def write_firstName(self):
        write_firstName = self.wait_element_visibility(AccountPage.first_name)
        write_firstName.send_keys("Kazım")


    def write_lastName(self):
        write_lastName = self.wait_element_visibility(AccountPage.last_name)
        write_lastName.send_keys("Şahin")


    def write_company(self):
        write_company = self.wait_element_visibility(AccountPage.company)
        write_company.send_keys("Moneytolia")


    def write_adress(self):
        write_adress = self.wait_element_visibility(AccountPage.adress1)
        write_adress.send_keys("Mehmet Akif Ersoy Mah. 2135.Sokak Esenyurt")

    def select_country(self):
        select_country = self.wait_element_clickable(AccountPage.country)

        country_select = Select(select_country)
        country_select.select_by_value("United States")

    def write_state(self):
        write_state = self.wait_element_visibility(AccountPage.state)
        write_state.send_keys("Florida")


    def write_city(self):
        write_city = self.wait_element_visibility(AccountPage.city)
        write_city.send_keys("Miami")


    def write_zipcode(self):
        write_zipcode= self.wait_element_visibility(AccountPage.zipcode)
        write_zipcode.send_keys("33101")



    def write_mobileNumber(self):
        write_mobileNumber = self.wait_element_visibility(AccountPage.mobile_number)
        write_mobileNumber.send_keys("+546487587")


    def create_account(self):
        create_account = self.wait_element_clickable(AccountPage.createAccount)
        create_account.click()


    def success_accountText(self):
        return self.wait_element_visibility(AccountPage.succesAccount).is_displayed()


    def continue_button(self):
        continue_button = self.wait_element_clickable(AccountPage.continueButton)
        continue_button.click()

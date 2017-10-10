from .base_page import BasePage, Locator

class LoginPage(BasePage):
    @property
    def page(self):
        return '/user/login'

    @property
    def username_locator(self):
        return Locator('name', 'username')

    @property
    def password_locator(self):
        return Locator('id', 'login_password')

    @property
    def login_anon_locator(self):
        return Locator('name', 'anonymous')

    @property
    def submit_locator(self):
        return Locator('xpath', '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/form/table/tbody/tr[4]/td/input')

    def navigate(self, base_url):
        self.driver.get(base_url + self.page)

    def enter_username(self, username):
        username_field = self.driver.find_element(by=self.username_locator.Type, value=self.username_locator.Value)
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(by=self.password_locator.Type, value=self.password_locator.Value)
        password_field.send_keys(password)

    def toggle_login_anonymously(self):
        anon_field = self.driver.find_element(by=self.login_anon_locator.Type, value=self.login_anon_locator.Value)
        anon_field.click()

    def submit(self):
        submit_button = self.driver.find_element(by=self.submit_locator.Type, value=self.submit_locator.Value)
        submit_button.click()

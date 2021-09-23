from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r'user-data-dir=C:\Users\office\AppData\Local\Google\Chrome\User Data\Default')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessa(self, site):
        self.chrome.get(site)

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details')
            perfil.click()
        except Exception as e:
            print('Erro ao clicar no perfil', e)

    def faz_logout(self):
        try:
            perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
            perfil.click()
        except Exception as e:
            print('Erro ao fazer logout', e)

    def clica_sign_in(self):
        try:
            btn_sign_up = self.chrome.find_element_by_link_text('Sign up')
            btn_sign_up.click()

            btn_sign_in = self.chrome.find_element_by_link_text('Sign in →')
            btn_sign_in.click()
        except Exception as e:
            print(e)

    def faz_login(self, login, senha):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            btn_login = self.chrome.find_element_by_name('commit')

            input_login.send_keys(login)
            input_password.send_keys(senha)

            btn_login.click()
        except Exception as e:
            print('Erro ao fazer login.', e)

    def verifica_usuario(self, usuario):
        profile_link = self.chrome.find_element_by_class_name('user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert usuario in profile_link_html

    def sair(self):
        self.chrome.quit()


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')
    chrome.clica_perfil()
    sleep(1)
    chrome.faz_logout()
    chrome.clica_sign_in()
    chrome.faz_login('email@email.com', 'senha123')
    chrome.clica_perfil()
    sleep(1)
    chrome.verifica_usuario('Ig0or')

    sleep(3)
    chrome.sair()

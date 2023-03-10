#https://dumskaya.net/
# Реєстрація на сайті без емейлу

# Працюючий варіант:
def register_user_without_email():
    import time

    from factory.new_user import User
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    import os

    my_user = User()
    error_no_email = 1
    options = ChromeOptions()
    foptions = FirefoxOptions()
    options.headless = True#True Запуск теста без включения браузера

    path = f'C:\\Users\\KaBaN\\PycharmProjects\\Test35_36\\drivers\\chromedriver'
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://dumskaya.net/'

    driver.maximize_window()
    driver.get(url)

    xpath_enter_button = '//a[@id="pp"]/b'
    xpath_enter_registration_button = '//a[@href="/register/"]'

    xpath_register_email = '//td/input[@name="email"]'
    xpath_register_nick = '//input[@name="nick"]'
    xpath_register_password = '//input[@name="password1"]'
    xpath_register_password2 = '//input[@name="password2"]'
    xpath_register_gender_male = '//input[@name="gender"][@value="m"]'
    xpath_register_gender_female = '//input[@name="gender"][@value="f"]'
    xpath_register_button = '//input[@type="submit"]/following::input[@type="submit"]'
    #XPath Axis         Ось XPath
    xpath_user_finish = '//a[@class="celluname1"]'
    xpath_user_exit = '//a[@class="exitlink"]'
    xpath_error_no_email = '//td[@class="newscol"]/div'

    if error_no_email == 1:
        my_user.email = ''


    enter_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_enter_button)))
    enter_button.click()
    enter_registration_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_enter_registration_button)))
    enter_registration_button.click()

    register_email_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_email)))
    register_email_field.send_keys(my_user.email)

    register_nick = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_nick)))
    register_nick.send_keys(my_user.nick)

    register_password = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_password)))
    register_password.send_keys(my_user.password)

    register_password2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_password2)))
    register_password2.send_keys(my_user.password)

    register_gender_male = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_gender_male)))
    register_gender_male.click()

    register_gender_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_button)))
    register_gender_button.click()

    error_textarea = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_error_no_email)))
    email = error_textarea.text
    error = '''Пользователь с таким адресом электронной почты уже зарегистрирован.\nУкажите е-mail. Он нужен для входа в сайт.'''




    driver.close()
    return  email, error
if __name__ == '__main__':
    print(register_user_without_email())

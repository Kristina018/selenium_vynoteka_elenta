import random
import unittest
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from bandymai import random_letter, random_string


class ElentaTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 10)
        self.acceptCookies()

    def test_1_positive(self):
        self.driver.get("https://elenta.lt/registracija")
        self.driver.find_element(By.ID, 'UserName').send_keys(f"Jurgio pyragai{random.randint(1000,9999)}" )
        self.driver.find_element(By.ID, 'Email').send_keys(f'ne@tavo{random.randint(1000,9999)}.lt')
        self.driver.find_element(By.ID, 'Password').send_keys('Aasrgt1!')
        self.driver.find_element(By.ID, 'Password2').send_keys('Aasrgt1!')
        self.driver.find_element(By.CLASS_NAME, 'bigNavBtn2').click()

        actual_text = self.driver.find_element(By.XPATH, '//*[@id="main-container"]/div[2]/h1/b').text
        expected_text = 'Jūs sėkmingai prisiregistravote!'

        self.assertEqual(actual_text, expected_text)
        print("1. testas")


    def test_2_mismatching_correct_password(self):
        self.driver.get("https://elenta.lt/registracija")
        self.driver.find_element(By.ID, 'UserName').send_keys(f"Jurgio pyragai{random.randint(1000, 9999)}")
        self.driver.find_element(By.ID, 'Email').send_keys(f'ne@tavo{random.randint(1000, 9999)}.lt')
        self.driver.find_element(By.ID, 'Password').send_keys('Aasrgt1!')
        self.driver.find_element(By.ID, 'Password2').send_keys('Aasrgt1!123')
        self.driver.find_element(By.CLASS_NAME, 'bigNavBtn2').click()

        actual_text = self.driver.find_element(By.XPATH, '//*[@id="main-container"]/form/fieldset/table/tbody/tr[8]/td[2]/span').text
        expected_text = 'Nesutampa slaptažodžiai. Pakartokite.'

        self.assertEqual(actual_text, expected_text)
        print("2. testas")

    def test_3_reg_form_2_letters_username(self):
        self.driver.get("https://elenta.lt/registracija")
        self.driver.find_element(By.ID, 'UserName').send_keys(f"{random.choice(string.ascii_lowercase)}{random.randint(0,9)}" )
        self.driver.find_element(By.ID, 'Email').send_keys(f'ne@tavo{random.randint(1000, 9999)}.lt')
        self.driver.find_element(By.ID, 'Password').send_keys('Aasrgt1!')
        self.driver.find_element(By.ID, 'Password2').send_keys('Aasrgt1!')
        self.driver.find_element(By.CLASS_NAME, 'bigNavBtn2').click()

        actual_text = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/h1/b').text
        expected_text = 'Netinkamas vartotojo vardas.'

        self.assertNotEqual(actual_text, expected_text)

        print("3. tikiuosi, kad NEleis sukurti")


    def test_4_reg_form_3_letters_username(self):
        self.driver.get("https://elenta.lt/registracija")
        self.driver.find_element(By.ID, 'UserName').send_keys(
            f"{random_string(19)}{random.randint(10, 99)}")
        self.driver.find_element(By.ID, 'Email').send_keys(f'ne@tavo{random.randint(1000, 9999)}.lt')
        self.driver.find_element(By.ID, 'Password').send_keys('Aasrgt1!')
        self.driver.find_element(By.ID, 'Password2').send_keys('Aasrgt1!')
        self.driver.find_element(By.CLASS_NAME, 'bigNavBtn2').click()

        actual_text = self.driver.find_element(By.XPATH, '//*[@id="main-container"]/div[2]/h1/b').text
        expected_text = 'Jūs sėkmingai prisiregistravote!'

        self.assertEqual(actual_text, expected_text)

        print("4. tikiuosi, kad leis sukurti")

    def test_5_reg_form_20_letters_username(self):
        self.driver.get("https://elenta.lt/registracija")
        self.driver.find_element(By.ID, 'UserName').send_keys(
            f"{random_letter(18)}{random.randint(10, 99)}")
        self.driver.find_element(By.ID, 'Email').send_keys(f'ne@tavo{random.randint(1000, 9999)}.lt')
        self.driver.find_element(By.ID, 'Password').send_keys('Aasrgt1!')
        self.driver.find_element(By.ID, 'Password2').send_keys('Aasrgt1!')
        self.driver.find_element(By.CLASS_NAME, 'bigNavBtn2').click()

        actual_text = self.driver.find_element(By.XPATH, '//*[@id="main-container"]/div[2]/h1/b').text
        expected_text = 'Jūs sėkmingai prisiregistravote!'

        self.assertEqual(actual_text, expected_text)
        self.

        print("5. tikiuosi, kad leis sukurti")

    def test_6_reg_form_21_letters_username(self):
        self.driver.get("https://elenta.lt/registracija")
        self.driver.find_element(By.ID, 'UserName').send_keys(
            f"{random_string(18)}{random.randint(100, 999)}")
        self.driver.find_element(By.ID, 'Email').send_keys(f'ne@tavo{random.randint(1000, 9999)}.lt')
        self.driver.find_element(By.ID, 'Password').send_keys('Aasrgt1!')
        self.driver.find_element(By.ID, 'Password2').send_keys('Aasrgt1!')
        self.driver.find_element(By.CLASS_NAME, 'bigNavBtn2').click()

        actual_text = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/h1/b').text
        expected_text = 'Netinkamas vartotojo vardas.'


        self.assertNotEqual(actual_text, expected_text)

        print("6. tikiuosi, kad NEleis sukurti")

    def tearDown(self):
        self.driver.quit()

    def acceptCookies(self):
        self.driver.get("https://elenta.lt")
        self.driver.find_element(By.CLASS_NAME, 'fc-cta-consent').click()
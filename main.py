from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import unittest


class CapstoneTesting(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.get("http://localhost:4200/")
        self.roll = "123456789"
        self.name = "This is a test Name"

    def test_page_title(self):
        driver = self.driver
        self.assertEqual("Student Database", driver.title)

    def test_Create_Operation(self):
        driver = self.driver
        button = driver.find_element_by_xpath(
            '/html/body/app-root/main/app-add-button/div/button')
        button.click()
        while True:
            try:
                roll_number_xpath = "/html/body/div/div[2]/div/mat-dialog-container/add-dialog/form/mat-dialog-content/mat-form-field[1]/div/div[1]/div/input"
                name_xpath = "/html/body/div/div[2]/div/mat-dialog-container/add-dialog/form/mat-dialog-content/mat-form-field[2]/div/div[1]/div/input"
                age_xpath = "/html/body/div/div[2]/div/mat-dialog-container/add-dialog/form/mat-dialog-content/mat-form-field[3]/div/div[1]/div/input"
                confirm_xpath = "/html/body/div/div[2]/div/mat-dialog-container/add-dialog/form/mat-dialog-actions/button[2]"

                self.driver.find_element_by_xpath(
                    roll_number_xpath).send_keys(self.roll)
                self.driver.find_element_by_xpath(
                    name_xpath).send_keys(self.name)
                self.driver.find_element_by_xpath(confirm_xpath).click()
                break

            except Exception as e:
                print(e)
                time.sleep(2)
                continue

    def test_Creation_Success(self):
        driver = self.driver
        left_xpath = "/html/body/app-root/main/app-todos/app-cards["
        right_xpath = "]/div/div/h3"
        while True:
            try:
                ele = driver.find_element_by_xpath(
                    "/html/body/app-root/main/app-todos/app-cards[3]/div/div/h3")
                self.assertEqual(ele.text, self.name)
                break
            except Exception as e:
                print(e)
                time.sleep(2)
                continue

    def test_Delete_Operation(self):
        driver = self.driver
        left_xpath = "/html/body/app-root/main/app-todos/app-cards["
        right_xpath = "]/div/div/h3"
        while True:
            try:
                element = driver.find_element_by_xpath(
                    "/html/body/app-root/main/app-todos/app-cards[3]/div/div/h3")
                element.click()
                driver.find_element_by_xpath(
                    "/html/body/div/div[2]/div/mat-dialog-container/app-update-dialog/form/mat-dialog-actions/button[1]").click()
                break
            except Exception as e:
                print(e)
                time.sleep(2)
                continue

    @classmethod
    def tearDownClass(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

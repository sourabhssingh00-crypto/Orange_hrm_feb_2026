
import allure
import pytest

from PageObjects.Login_Page import Login_page_class
from Utilities.logger import logger_class
# from Utilities import ReadConfig
from Utilities.readConfig import ReadConfig

# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_Login_001():
    driver = None
    ReadConfig = ReadConfig()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    # url = ReadConfig.get_url()
    url = ReadConfig.get_login_url()
    log = logger_class.get_logger()
    @allure.title("Verify OrangeHRM Login Page URL")
    @allure.description("This test verifies the URL of the OrangeHRM login page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("Navigate to OrangeHRM Login Page")
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", name="OrangeHRM Login Page")
    @allure.issue("https://github.com/allure-framework/allure-python/issues/123", name="Issue 123")
    @allure.testcase("https://github.com/allure-framework/allure-python/issues/123", name="Test Case 123")
    @allure.feature("OrangeHRM Login")
    @allure.story("Verify Login Page URL")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.flaky(reruns=1, reruns_delay=1)

    def test_verify_url_001(self):
        self.log.info("Starting Test_001: Verify OrangeHRM Login Page URL")
        self.log.info("Navigating to OrangeHRM Login Page")
        self.driver.get(self.url)
        self.log.info("OrangeHRM Login Page URL Loaded")
        if self.driver.title == "OrangeHRM":
            self.log.info("OrangeHRM Login Page URL Verified")
            self.driver.save_screenshot("screenshots\\test_verify_url_pass.png")
            self.log.info("Screenshot of passed Test Saved")
            allure.attach.file("screenshots\\test_verify_url_pass.png", name="test_verify_url_pass",
                               attachment_type=allure.attachment_type.PNG)
            assert True
        else:
            self.driver.save_screenshot("screenshots\\test_verify_url_fail.png")
            self.log.info("Screenshot of failed Test Saved")
            allure.attach.file("screenshots\\test_verify_url_fail.png", name="test_verify_url_fail",
                               attachment_type=allure.attachment_type.PNG)
            assert False
        self.log.info("Test Verify URL 001 Completed")
        self.log.info("===================================================================")

    @allure.title("Verify OrangeHRM Login")
    @allure.description("This test verifies the login functionality of the OrangeHRM application")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("Enter Username and Password and Click Login")
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", name="OrangeHRM Login Page")
    @allure.issue("https://github.com/allure-framework/allure-python/issues/123", name="Issue 123")
    @allure.testcase("https://github.com/allure-framework/allure-python/issues/123", name="Test Case 123")
    @allure.feature("OrangeHRM Login")
    @allure.story("Verify Login Functionality")
    @pytest.mark.smoke
    @pytest.mark.regressions
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    def test_OrangeHRM_Login_002(self):
        self.log.info("Starting Test_002: Verify OrangeHRM Login Functionality")
        self.log.info("Navigating to OrangeHRM Login Page")
        self.driver.get(self.url)
        self.log.info("OrangeHRM Login Page Loaded")
        lp = Login_page_class(self.driver)
        self.log.info("Entering Username and Password and Click Login")
        lp.Enter_username(self.username)
        self.log.info("Entering Password")
        lp.Enter_password(self.password)
        self.log.info("Clicking Login")
        lp.Click_login()
        self.log.info("Login Attempt Completed")
        if lp.verify_login() == "Login Successful":
            self.driver.save_screenshot("screenshots\\test_OrangeHRM_Login_002_pass.png")
            self.log.info("screenshot of passed Test Saved")
            allure.attach.file("screenshots\\test_OrangeHRM_Login_002_pass.png", name="test_OrangeHRM_Login_002_pass",
                               attachment_type=allure.attachment_type.PNG)
            lp.Click_Menu()
            lp.Click_logout()
            assert True
        else:
            self.driver.save_screenshot("screenshots\\test_OrangeHRM_Login_002_fail.png")
            self.log.info("screenshot of failed Test Saved")
            allure.attach.file("screenshots\\test_OrangeHRM_Login_002_fail.png", name="test_OrangeHRM_Login_002_fail",
                               attachment_type=allure.attachment_type.PNG)
            assert False

        self.log.info("Test OrangeHRM Login 002 Completed")
        self.log.info("===================================================================")




# pytest -v -n=auto --html=Html_Reports\OrangeHRM_Report.html --alluredir=Allure_Reports --browser chrome
# pytest -v --html=Html_Reports\OrangeHRM_Report.html --browser chrome
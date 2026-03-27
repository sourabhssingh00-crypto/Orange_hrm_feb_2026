

import pytest
import allure

from PageObjects.Login_Page import Login_page_class
from Utilities.XLUtils import XLUtils_class
from Utilities.logger import logger_class
from Utilities.readConfig import ReadConfig


@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_Login_DDT_002():
    driver = None
    ReadConfig = ReadConfig()

    url = ReadConfig.get_login_url()
    log = logger_class.get_logger()
    excel_file_path = "C:\credence\orange_hrm_framework\Test_Data\Orange_HRM_Test_Data.xlsx"
    sheet = "Sheet1"
    result = []

    def test_OrangeHRM_Login_DDT_003(self):
        self.log.info("Starting Test_002: Verify OrangeHRM Login Functionality")

        row_count = XLUtils_class.get_row_count(self.excel_file_path, self.sheet)
        self.log.info(f"Total Rows in Excel: {row_count}")
        result = []
        for i in range(2,row_count + 1):
            username = XLUtils_class.read_data(self.excel_file_path, self.sheet, i, 2)
            password = XLUtils_class.read_data(self.excel_file_path, self.sheet, i, 3)
            expected_result = XLUtils_class.read_data(self.excel_file_path, self.sheet, i, 4)
            self.log.info(f"Test Data: Username={username}, Password={password}, Expected Result={expected_result}")

            self.log.info("Navigating to OrangeHRM Login Page")
            self.driver.get(self.url)
            self.log.info("OrangeHRM Login Page Loaded")

            lp = Login_page_class(self.driver)
            lp.Enter_username(username)
            lp.Enter_password(password)
            lp.Click_login()

            actual_login_status = lp.verify_login()  # Should return "Login Successful" or "Login Failed"

            if actual_login_status == "Login Successful":
                self.log.info(f"Login Successful for {username}")
                # Save screenshot for success
                self.driver.save_screenshot(f"screenshots\\pass_{username}.png")

                # ONLY Click Menu and Logout if we are actually inside the app
                lp.Click_Menu()
                lp.Click_logout()

                actual_result = "Login Successful"
            else:
                self.log.error(f"Login Failed for {username}")
                self.driver.save_screenshot(f"screenshots\\fail_{username}.png")

                actual_result = "Login Failed"

            # Now compare Actual with Expected from Excel
            if actual_result == expected_result:
                self.log.info(f"Test matched for {username}")
                result.append("Pass")
                XLUtils_class.write_data(self.excel_file_path, self.sheet, i, 5, "Pass")
            else:
                self.log.error(f"Test mismatched for {username}")
                result.append("Fail")
                XLUtils_class.write_data(self.excel_file_path, self.sheet, i, 5, "Fail")



'''
            # if lp.verify_login() == expected_result:
            if lp.verify_login() == 
                self.log.info(f"Login Successful for {username}")
                self.driver.save_screenshot(f"screenshots\\test_OrangeHRM_Login_DDT_003_pass_{username}.png")
                allure.attach.file(f"screenshots\\test_OrangeHRM_Login_DDT_003_pass_{username}.png",name="Login Successful",attachment_type=allure.attachment_type.PNG)
                lp.Click_Menu()
                lp.Click_logout()

                actual_result = "Login Successful"
            else:
                self.log.error(f"Login Failed for {username}")
                self.driver.save_screenshot(f"screenshots\\test_OrangeHRM_Login_DDT_003_fail_{username}.png")
                allure.attach.file(f"screenshots\\test_OrangeHRM_Login_DDT_003_fail_{username}.png",name=f"test_OrangeHRM_Login_DDT_003_fail_{username}",attachment_type=allure.attachment_type.PNG)
                # lp.Click_Menu()
                # lp.Click_logout()
                actual_result = "Login Failed"

            if actual_result == expected_result:
                self.log.info(f"Test passed for Username={username}")
                test_status = "Pass"
                result.append("Pass")
            else:
                self.log.error(f"Test failed for Username={username}")
                test_status = "Fail"
                result.append("Fail")
            XLUtils_class.write_data(self.excel_file_path, self.sheet, i, 5, test_status)






        self.log.info(f"Test Results: {result}")


        assert "Fail" not in result
        self.log.info("Test OrangeHRM Login DDT 003 Completed")
        self.log.info("===================================================================")


'''



# pytest -v -n=auto --html=Html_Reports\OrangeHRM_Report.html --alluredir=Allure_Reports --browser chrome
# pytest -v --html=Html_Reports\OrangeHRM_Report.html --browser chrome
# pytest -v -k "DDT" --html=Html_Reports\OrangeHRM_Report.html --browser chrome
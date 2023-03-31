import pytest
from appium import webdriver
from utilities import read_utils


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        json_dic=read_utils.get_dic_from_json("../config_data/config.json")

        if json_dic["device"]=="local":
            des_cap = {
                "platformName": "android",
                "deviceName": "Pixel 4",
                "app": r"C:\Users\148592\OneDrive - Arrow Electronics, Inc\Desktop\python_training\Android_Demo_App.apk",
                "appPackage": "com.code2lead.kwad",
                "appActivity": "com.code2lead.kwad.MainActivity",
                #"appium:avd":"Pixel_4_API_33"
            }
            self.driver = webdriver.Remote(command_executor=f"http://localhost:{json_dic['port']}/wd/hub", desired_capabilities=des_cap)
        else:
            des_cap = {
                "app": "bs://2847652278840254af52d4312451c4313d1774ee",
                "platformVersion": "9.0",
                "deviceName": "Google Pixel 3",
                "bstack:options": {
                    "projectName": "First Python project",
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack first_test",
                    # Set your access credentials
                    "userName": "einfochipsshah_WXQDRT",
                    "accessKey": "poHrFr5ruP5gBvD73WyH"
                }
            }
            self.driver = webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub",
                                           desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()
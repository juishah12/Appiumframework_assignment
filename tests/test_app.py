import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from base.appium_listen import AppiumConfig


class TestAndroidDeviceLocal(AppiumConfig):
    # def test_invalid_login(self):
    #     print(self.driver.page_source)
    #     time.sleep(2)

    def test_valid_login(self):
        #Enter valid login and print admin name
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='LOGIN']").click()
        self.driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='Enter Email']").send_keys("admin@gmail.com")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter Password']").send_keys("admin123")
        self.driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='LOGIN']").click()
        # self.driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text,'Enter Admin']").send_keys("Masteradmin")
        # self.driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='SUBMIT']").click()
        actual_admin = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.code2lead.kwad:id/Tv_admin']").text
        print(actual_admin)

    def test_scroll_page(self):
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='ScrollView']").click()
        self.driver.implicitly_wait(0)
        while len(self.driver.find_elements(AppiumBy.XPATH, "//android.widget.Button[@text='BUTTON16']")) == 0:
            self.driver.swipe(986, 1948, 1008, 1036, 1000)

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='BUTTON16']").click()
        self.driver.implicitly_wait(30)

    def test_long_tap(self):
        action = TouchAction(self.driver)
        # first time find the element co-ordinates and tap 10 times
        action.tap(self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='LONG CLICK']")
                   , count=10).perform()
        action.long_press(self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='LONG CLICK']"),
                          duration=1000).perform()
        self.driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='SUBMIT']").click()
        time.sleep(5)

    def mobile_command(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("CONTACT US FORM")').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Enter Name")').send_keys('jui')
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Enter Email")').send_keys('jui@gmail.com')
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Enter Address")').send_keys('Ahmedabad')
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Enter Mobile No")').send_keys('9898167678')
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("SUBMIT")').click()

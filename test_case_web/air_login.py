# -*- encoding=utf8 -*-
__author__ = "yangcong"

from test_case_web import *


class WSTestcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not cli_setup():
            auto_setup(__file__, logdir=log_path + '/' + os.path.basename(__file__))
        pass

    def setUp(self) -> None:
        self.driver = WebChrome(chromedrive_path)
        self.driver.implicitly_wait(20)

    def test_login(self):
        driver = self.driver
        driver.maximize_window()

        # 以下可修改
        driver.get("https://yangcong345.com/xiaoxue/login")
        driver.assert_exist("//input[@placeholder='请输入手机号']", "xpath", "请输入手机号.")
        driver.assert_exist("//input[@placeholder='请输入验证码']", "xpath", "请输入验证码.")
        driver.assert_exist("//*[@id=\"root\"]/div/div/div/div/div/div/button/span", "xpath", "获取验码.")
        driver.assert_exist("//button[@type='submit']", "xpath", "登录.")
        driver.find_element_by_xpath("//input[@placeholder='请输入手机号']").send_keys('15311480776')
        driver.find_element_by_xpath("//input[@placeholder='请输入验证码']").send_keys(verification_code)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.assert_exist("//*[@id=\"root\"]/div/div[2]/div/div/div/div/img", "xpath", "大头像.")
        driver.assert_exist("//*[@id=\"root\"]/div/div[2]/div/div/div/div/div/span", "xpath", "用户名.")
        driver.assert_exist("//*[@id=\"root\"]/div/div[2]/div/div/div/div/div/span[2]", "xpath", "年级.")
        driver.assert_exist("//*[@id=\"root\"]/div/div/div/img[2]", "xpath", "小头像.")

    def tearDown(self) -> None:
        self.driver.close()

    @classmethod
    def tearDownClass(cls) -> None:
        pass
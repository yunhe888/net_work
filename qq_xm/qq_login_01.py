'''
created on 2019-08-14
@ author kzw
Project: unittest框架编写测试用例

'''
from selenium import webdriver
from HTMLTestRunnerNew import HTMLTestRunner
import time
import unittest

class Testemail(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()#打开火狐浏览器
        self.driver.maximize_window()#窗口最大化
        self.driver.implicitly_wait(5)#一直等到浏览器打开
        self.driver.get('https://mail.qq.com/')#返回网址页面


    def test_Login_01(self):
        driver=self.driver
        driver.switch_to.frame('login_frame')#进入登录iframe
        # driver.find_element_by_id('switcher_plogin').click()#点击账号密码登录,若没有登录扣扣不需要此步
        driver.find_element_by_id('u').clear()#清空账户
        time.sleep(2)#睡2秒
        driver.find_element_by_id('u').send_keys('')#输入账户
        time.sleep(2)
        driver.find_element_by_id('p').clear()#清空密码
        time.sleep(2)
        driver.find_element_by_id('p').send_keys('')#输入密码
        time.sleep(2)
        driver.find_element_by_id('login_button').click()#点击确定按钮
        time.sleep(2)
        txt=driver.find_element_by_id('err_m').text#获取元素对应文本
        print(txt)
        self.assertEqual(txt,'你还没有输入帐号！',msg='账号不能为空')#断言元素与文本是否一致
        driver.switch_to.default_content()#退出iframe

    def test_Login_02(self):
        self.driver.switch_to.frame('login_frame')
        # self.driver.find_element_by_id('switcher_plogin').click()
        self.driver.find_element_by_id('u').clear()
        time.sleep(2)
        self.driver.find_element_by_id('u').send_keys('643609953@qq.com')
        time.sleep(2)
        self.driver.find_element_by_id('p').clear()
        time.sleep(2)
        self.driver.find_element_by_id('p').send_keys('')
        time.sleep(2)
        self.driver.find_element_by_id('login_button').click()
        time.sleep(2)
        txt=self.driver.find_element_by_id('err_m').text
        self.assertEqual(txt,'你还没有输入密码！',msg='密码不能为空')
        self.driver.switch_to.default_content()


    def test_Login_03(self):
        self.driver.switch_to.frame('login_frame')
        # self.driver.find_element_by_id('switcher_plogin').click()
        self.driver.find_element_by_id('u').clear()
        time.sleep(2)
        self.driver.find_element_by_id('u').send_keys('643609953@qq.com')
        time.sleep(2)
        self.driver.find_element_by_id('p').clear()
        time.sleep(2)
        self.driver.find_element_by_id('p').send_keys('kangyuan13572456469')
        time.sleep(2)
        self.driver.find_element_by_id('login_button').click()
        time.sleep(2)
        self.driver.switch_to.default_content()
        time.sleep(2)
        txt=self.driver.find_element_by_xpath('//*[@id="composebtn"]').text
        time.sleep(2)
        self.assertEqual(txt,'写信',msg='登陆成功')



    def tearDown(self):
        self.driver.quit()




if __name__== "__main__":
    testunit = unittest.TestSuite()#调用用例套件函数
    testunit.addTest(Testemail("test_Login_01"))#添加用例test_Login_01
    testunit.addTest(Testemail("test_Login_02"))#添加用例test_Login_02
    testunit.addTest(Testemail("test_Login_03"))#添加用例test_Login_03
    now = time.strftime("%Y-%m-%d %H_%M_%S")#当前时间
    filename = './' + now + 'result.html'#文件存储位置及格式
    fp = open(filename, 'wb')#打开文件
    runner = HTMLTestRunner(stream=fp, tester="kzw",title='百度报告', description='用例执行结果:')#报告内容
    runner.run(testunit)#运行




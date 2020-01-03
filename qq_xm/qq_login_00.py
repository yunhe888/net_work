from selenium import webdriver
import time
browser=webdriver.Chrome()
browser.get('https://mail.qq.com/')
time.sleep(5)
browser.switch_to.frame('login_frame')
time.sleep(5)
browser.find_element_by_id('u').clear()
time.sleep(2)
browser.find_element_by_id('u').send_keys('370801466')
time.sleep(3)
browser.find_element_by_id('p').clear()
time.sleep(2)
browser.find_element_by_id('p').send_keys('yiyi-2012')
time.sleep(3)
browser.find_element_by_id('login_button').click()
time.sleep(2)
browser.switch_to.default_content()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="composebtn"]').click()
time.sleep(5)
browser.switch_to.frame('mainFrame')
time.sleep(2)
browser.switch_to.frame(browser.find_element_by_tag_name('iframe'))
time.sleep(5)
browser.find_element_by_css_selector('body').send_keys('作业做完啦')
time.sleep(2)
browser.switch_to.default_content()
time.sleep(2)
browser.switch_to.frame('mainFrame')
time.sleep(2)
browser.find_element_by_css_selector('#toAreaCtrl > div:nth-child(2) > input:nth-child(1)').send_keys('370801466@qq.com')
time.sleep(5)
browser.find_element_by_id('subject').send_keys('家庭作业')
time.sleep(3)
browser.find_element_by_xpath('/html/body/form[2]/div[3]/div/a[1]').click()
time.sleep(5)
browser.switch_to.default_content()
time.sleep(3)
browser.quit()

# ###################################################################
#
# from selenium import webdriver
# from time import sleep
# driver=webdriver.Firefox()
# driver.get("http://www.baidu.com/")
# driver.maximize_window()
# selenium_index=driver.current_window_handle   #当前句柄位置
# sleep(2)
# driver.find_element_by_id("kw").send_keys("QQ邮箱")
# driver.find_element_by_id("su").click()
# sleep(10)
# driver.find_element_by_link_text("登录QQ邮箱").click()
# sleep(20)
# driver.switch_to.window(selenium_index)
#
#
# ##################################################################
#
# #多窗口打开
# import time
# from selenium import webdriver
# browser = webdriver.Chrome()# 在当前浏览器中访问百度
# browser.get('https://www.baidu.com')# 新开一个窗口，通过执行新开一个窗口
# newwindow = 'window.open("https://www.sogou.com")'
# browser.execute_script(newwindow)# 输出当前窗口句柄（百度）
# baidu_handle = browser.current_window_handle# 获取当前窗口句柄集合（列表类型）
# handles = browser.window_handles
# print(handles)  # 输出句柄集合
# # 获取搜狗窗口
# sogou_handle = None
# for handle in handles:
#     if handle != baidu_handle:
#         sogou_handle = handle
# # 输出当前窗口句柄（搜狗）
# print('switch to ', handle)
# browser.switch_to.window(sogou_handle)
# time.sleep(10)
# browser.close() #关闭当前窗口（搜狗）
# # 切换回百度窗口
# browser.switch_to.window(baidu_handle)
# time.sleep(10)
# browser.quit()
#
#
# # coding=utf-8
# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Firefox()
# driver.maximize_window()
#
#
# driver.get("http://www.baidu.com/")
# time.sleep(1)
# ele = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')  # 触发ctrl + t
#
# time.sleep(1)

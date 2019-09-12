# -*-coding:UTF-8-*-
from selenium import webdriver
import time
# 扫描页面等待元素出现
import selenium.webdriver.support.ui as ui


# 打开浏览器
class login:
    # 打开谷歌浏览器
    browser = webdriver.Chrome()
    # 输入网址
    browser.get("https://test.epc1688.com")
    # 跳转登录
    browser.find_element_by_xpath('/html/body/header[1]/div/div[2]/a').click()

    # 采购人登录
    def purchaser_login(acu, pwd):
        # 选择采购人身份
        time.sleep(1)
        login.browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/ul/li[1]').click()
        login.accountAndPassword(acu, pwd)

    # 供应商
    def supplier_login(acu, pwd):
        # 选择供应商身份
        time.sleep(1)
        login.browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/ul/li[2]').click()
        login.accountAndPassword(acu, pwd)

    # 专家
    def expert_login(acu, pwd):
        # 选择专家
        time.sleep(1)
        login.browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/ul/li[3]').click()
        # 输入账号密码登陆
        login.accountAndPassword(acu, pwd)

    # 招标代理
    def agency_login(acu, pwd):
        # 选择代理
        time.sleep(1)
        login.browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/ul/li[4]').click()
        # 输入账号密码登录
        login.accountAndPassword(acu, pwd)

    # 输入账号密码
    def accountAndPassword(act, pwd):
        # 清除后再输入账号
        login.browser.find_element_by_class_name('el-input__inner').clear()
        login.browser.find_element_by_class_name('el-input__inner').send_keys(act)
        # 输入密码
        login.browser.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/div[2]/div[2]/form/div/div[2]/div/div/div/input').clear()
        login.browser.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/div[2]/div[2]/form/div/div[2]/div/div/div/input').send_keys(pwd)


    # 登录提醒
    def loginToRemind():
        login.browser.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/div[2]/div[2]/form/div/div[3]/div/div/button').click()

        # 扫描页面变化，等待元素出现
        wait = ui.WebDriverWait(login.browser, 10)
        wait.until(lambda driver: login.browser.find_element_by_xpath("/html/body/div/div/div/div[2]/div[4]"))


        # 判断div弹窗是否弹出
        login_spring = login.browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div[4]').is_displayed()
        print(login_spring)

        if login_spring:
            login.browser.find_element_by_xpath(
                '/html/body/div/div/div/div[2]/div[2]/div[2]/form/div/div[3]/div/div/button').click()
            print(login_spring)

        elif login_spring==False:
            # 同时登陆
            login.browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/span/button[1]').click()

            # 强制下线
            # login.browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div[4]/div/div[2]/span/button[2]').click()

# 关闭浏览器
def closeDrive():
    login.browser.quit()


login.purchaser_login(13110000001, 'epc1688')

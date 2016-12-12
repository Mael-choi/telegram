import threading
from selenium import webdriver
import time
import datetime
import telepot


TOKEN = "325945981:AAEu6dbSfL5WpoZZIyg2t6X0IJuG4TSc1eA"
bot = telepot.Bot(TOKEN)
end = False
def checklist():
    global end
    browser = webdriver.PhantomJS()
    browser.get("https://www.wellife.or.kr/")
    time.sleep(1)
    username = browser.find_element_by_class_name("inputId")
    password = browser.find_element_by_class_name("inputPw")
    username.send_keys("tm1256")
    password.send_keys("htm0870")
    login_attempt = browser.find_element_by_class_name("type-image")
    login_attempt.submit()
    time.sleep(1)
    browser.find_element_by_css_selector(".gnb_wrap .util a:nth-child(5)").click()
    browser.find_element_by_link_text("실시간신청").click()
    time.sleep(3)
    now = datetime.datetime.now()
    nowDateTime = now.strftime('%M_%S')
    today = int(now.strftime('%d'))
    i = 1
    roomList = []
    rs = browser.find_elements_by_css_selector("span em")
    for r in rs:
        roomList.append(r.text)
        i = i + 1
        if r.text != "0":
            if i >= -3*(today-12)+1+37 and i > -3*(today-12)+1+43:
                print("크리스마스에 자리가 있다!")
                bot.sendMessage(299950662, "크리스마스에 자리가 났다!")
                screenName = "Hi" + nowDateTime + ".png"
                browser.save_screenshot(screenName)
                sPath = "C:/Users/selam/PycharmProjects/untitled1/"+screenName
                f = open(sPath, 'rb')
                # bot.sendMessage(299950662, sPath)
                bot.sendPhoto(299950662, f)
                f.close()
                bot.sendMessage(299950662, "https://www.wellife.or.kr/resort/rst0403.do?submitEvent=init")
                end = True
            if i> -3*(today-12)+1+57 and i >= -3*(today-12)+1+60:
                print("연말에 자리가 있다!")
                bot.sendMessage(299950662, "연말에 자리가 났다!")
                screenName = "Hi" + nowDateTime + ".png"
                browser.save_screenshot(screenName)
                sPath = "C:/Users/selam/PycharmProjects/untitled1/"+screenName
                f = open(sPath, 'rb')
                # bot.sendMessage(299950662, sPath)
                bot.sendPhoto(299950662, f)
                f.close()
                bot.sendMessage(299950662, "https://www.wellife.or.kr/resort/rst0403.do?submitEvent=init")
                end = True
    print(roomList)
    print(str(count) + "번째 체크 완료....")
    browser.close()

count = 1
def execute_func(second=1.0):
    global end, count
    if end:
        return
    checklist()
    count = count + 1
    threading.Timer(second, execute_func, [second]).start()

execute_func(600.0)


##import required modules
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException,NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import datetime

class Trainticket():
        def __init__(self,  ID , start , destination) -> None:
             self.url = 'https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query'
             self.ID = ID
             self.start = start
             self.destination = destination
             
        def get_trin_info(self):
            """
            獲取列車時刻資訊
            """
            pass
        def calcluate_date(self):
            today = datetime.datetime.now()
            #開放購買四週後票
            buy_ticket_date = today + datetime.timedelta(weeks = 4)
            if buy_ticket_date.weekday() == 4:
                buy_ticket_date = buy_ticket_date
            else:
                buy_ticket_date = buy_ticket_date + datetime.timedelta((4-buy_ticket_date.weekday()) % 7)
        def login_text(self , start , end , date , num):
            #open TRA webpage
            train = webdriver.Chrome()
            train.get(self.url)
            username_ele = train.find_element("id" , 'pid')
            start_station = train.find_element('name', 'startStation')
            end_station = train.find_element('name', 'endStation')
            date_ele = train.find_element('id', 'rideDate1')
            train_num = train.find_element('id', 'trainNoList1')
            username_ele.send_keys("A229114022")
            start_station.send_keys("台北")
            end_station.send_keys("光復")
            date_ele.send_keys("20230212")
            train_num.send_keys(438)
            ##click on the checkbox
            train.find_element(By.TAG_NAME, 'iframe').click()
            
            time.sleep(1)
            #book
            train.find_element(By.CLASS_NAME , "btn-3d").send_keys(Keys.ENTER)
        def verify_box(self , train):
            """
            如果進到需要勾選的畫面，用這個函式解決
            """
            try:
                ##switch to recaptcha audio control frame
                frames = train.switch_to()
            except Exception as e:
                print("Error")
            
            
            
            
if __name__ == "__main__":
    
    browser = Trainticket()
    browser.login_text()
    
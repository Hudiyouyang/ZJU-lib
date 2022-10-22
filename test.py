from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from plyer import notification

driverfile_path = r'D:\Program Files\Python39\msedgedriver.exe'
driver = webdriver.Edge(executable_path=driverfile_path)

driver.get(r'https://zjuam.zju.edu.cn/cas/login?service=http://ic.zju.edu.cn')

driver.find_element('id','username').send_keys('xxxxxxx')           #在此输入学号
driver.find_element('id','password').send_keys('xxxxxxx')          #在此输入浙大通行证密码

driver.find_element('id','dl').click()

sleep(10)

seat_num = int(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[3]/div[2]/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div[1]/span').text)

while seat_num == 0:
    sleep(60)
    driver.refresh()
    sleep(10)
    seat_num = int(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[3]/div[2]/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div[1]/span').text)


notification.notify(
    title = '图书馆预约提醒',
    message = '三楼信息空间存在空位',
    app_icon = None,
    timeout = 10,
)



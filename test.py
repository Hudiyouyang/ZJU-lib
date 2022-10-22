from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from plyer import notification

seat_type = int(input("输入要预约的座位类型："))    #输入需要预约的座位类型
                            # 1：二楼外文 2：三楼任意座位 3:三楼显示器座位

driverfile_path = r'D:\Program Files\Python39\msedgedriver.exe'     #在此填入引擎驱动的绝对路径
driver = webdriver.Edge(executable_path=driverfile_path)

driver.get(r'https://zjuam.zju.edu.cn/cas/login?service=http://ic.zju.edu.cn')

driver.find_element('id','username').send_keys('xxxxxxx')           #在此输入学号
driver.find_element('id','password').send_keys('xxxxxxx')          #在此输入浙大通行证密码

driver.find_element('id','dl').click()

sleep(5)

if seat_type == 1:
    seat_num = int(driver.find_element(By.XPATH,
                                       '//*[@id="app"]/div[1]/div[3]/div[2]/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div[1]/span').text)

    while seat_num == 0:
        sleep(60)
        driver.refresh()
        sleep(10)
        seat_num = int(driver.find_element(By.XPATH,
                                           '//*[@id="app"]/div[1]/div[3]/div[2]/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div[1]/span').text)

    notification.notify(
        title='图书馆预约提醒',
        message='二楼外文存在空位',
        app_icon=None,
        timeout=10,
    )

if seat_type == 2:
    seat_num = int(driver.find_element(By.XPATH,
                                       '/html/body/div/div[1]/div[3]/div[2]/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div[1]/span').text)

    while seat_num == 0:
        sleep(60)
        driver.refresh()
        sleep(10)
        seat_num = int(driver.find_element(By.XPATH,
                                           '/html/body/div/div[1]/div[3]/div[2]/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div[1]/span').text)

    notification.notify(
        title='图书馆预约提醒',
        message='三楼信息空间存在空位',
        app_icon=None,
        timeout=10,
    )

if seat_type == 3:
    flag = 0

    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[2]/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div[1]/span').click()
    sleep(3)
    xpath_list = driver.find_elements(By.XPATH,'//*[@id="app"]/div[1]/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[1]/div')

    while flag == 0:
        for seat_id in range(77, 133):
            if xpath_list[seat_id - 1].get_attribute("class") == 'draggable green':
                flag = 1
                notification.notify(
                    title='图书馆预约提醒',
                    message='三楼显示器座位存在空位',
                    app_icon=None,
                    timeout=10,
                )
            break
        if flag == 0:
            sleep(60)
            driver.refresh()
            sleep(3)
            xpath_list = driver.find_elements(By.XPATH,
                                              '//*[@id="app"]/div[1]/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[1]/div')






import datetime
import json
import os
from re import search
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from utils import delete_empty_file

# 公众号账号
user_name = '2625538949@qq.com'
user_psw = '4972039.'

def connectchrome():
    options = Options()
    options.add_argument('log-level=3')
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox");
    options.add_argument("--disable-dev-shm-usage");
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    prefs = {
        'profile.default_content_setting_values': {
            'images': 1,
        }
    }
    options.add_experimental_option('prefs', prefs)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'")  # 进行UA伪装
    # driver_path = os.getcwd()+ "/chromedriver"
    # driver = webdriver.Chrome(executable_path=driver_path, options=options)
    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })
    driver.set_window_size(1280, 800)
    driver.set_window_position(100, 100)
    time.sleep(2)
    return driver


def login(driver):  # 登录
    driver.get(
        'https://mp.weixin.qq.com/')
    choice_button = driver.find_elements_by_xpath('//*[@id="header"]/div[2]/div/div/div[2]/a')[0]
    choice_button.click()
    input_email = driver.find_elements_by_xpath('//*[@id="header"]/div[2]/div/div/div[1]/form/div[1]/div[1]/div/span/input')[0]
    input_email.send_keys(user_name)
    time.sleep(1)
    # continue_button = driver.find_elements_by_xpath('//span[@id="continue"]')[0]
    # continue_button.click()
    time.sleep(3)
    password = driver.find_elements_by_xpath('//*[@id="header"]/div[2]/div/div/div[1]/form/div[1]/div[2]/div/span/input')[0]
    password.send_keys(user_psw)
    time.sleep(1)
    login_button = driver.find_elements_by_xpath('//*[@id="header"]/div[2]/div/div/div[1]/form/div[4]/a')[0]
    login_button.click()
    time.sleep(3)

def scan_qrcode(driver):
    # 等待扫描登录二维码
    try:
        while driver.find_elements_by_xpath('//*[@id="app"]/div[3]/div/div[2]/div[1]/div/img')[0] is not None:
            time.sleep(1)
    except:
        pass

def preoption(driver):
    btn1 = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[2]/div/div[1]')
    btn1.click()
    time.sleep(1)
    windows = driver.current_window_handle #定位当前页面句柄
    all_handles = driver.window_handles   #获取全部页面句柄
    for handle in all_handles:          #遍历全部页面句柄
        if handle != windows:          #判断条件
            driver.switch_to.window(handle)      #切换到新页面
    btn2 = driver.find_element_by_xpath('//*[@id="js_editor_insertlink"]')
    btn2.click()
    time.sleep(1)
    
def search(driver, crawl_goal):
    # 搜索公众号
    btn3 = driver.find_elements_by_xpath('//*[@id="vue_app"]/div[2]/div[1]/div/div[2]/div[2]/form[1]/div[4]/div/div/p/div/button')[0]
    btn3.click()
    time.sleep(1)
    inputline = driver.find_element_by_xpath('//*[@id="vue_app"]/div[2]/div[1]/div/div[2]/div[2]/form[1]/div[4]/div/div/div/div/div[1]/span/input')
    inputline.send_keys(crawl_goal)
    search_btn = driver.find_elements_by_xpath('//*[@id="vue_app"]/div[2]/div[1]/div/div[2]/div[2]/form[1]/div[4]/div/div/div/div/div[1]/span/span/button[2]')[0]
    search_btn.click()
    time.sleep(1)
    result_list = driver.find_elements_by_xpath('//*[@id="vue_app"]/div[2]/div[1]/div/div[2]/div[2]/form[1]/div[4]/div/div/div/div[2]/ul/li[1]')
    result_list[0].click()
    time.sleep(1)

def crawl_url(driver, file, status):
    # 获取文章url
    # url_list = []
    if 'page' in status:
        page = status['page']
    else:    
        page = 1
    status['finish'] = False
    # try:
    try: 
        while True:
            time.sleep(10)
            print(page)
            page_input = driver.find_element_by_xpath('//*[@class="weui-desktop-pagination__form"]//input')
            page_input.send_keys(Keys.CONTROL, 'a')
            page_input.send_keys(page)
            jump_btn = driver.find_element_by_xpath('//*[@id="vue_app"]/div[2]/div[1]/div/div[2]/div[2]/form[1]/div[5]/div/div/div[3]/span[2]/a')
            jump_btn.click()
            time.sleep(5) 
            result_list = driver.find_elements_by_xpath('//*[@class="weui-desktop-radio-group"]//a')
            if len(result_list) == 0:
                status['page'] = page
                print('访问被限制')
                return status
            for result in result_list:
                url = result.get_attribute('href')
                file.write(url + '\n')
                # url_list.append(url)
            if (page != 1 and len(driver.find_elements_by_xpath('//*[@class="weui-desktop-btn weui-desktop-btn_default weui-desktop-btn_mini"]')) < 2) or (page == 1 and len(driver.find_elements_by_xpath('//*[@class="weui-desktop-btn weui-desktop-btn_default weui-desktop-btn_mini"]')) < 1):
                status['page'] = page
                status['finish'] = True
                return status
            page += 1
    except Exception as e:
        print(e)
    finally:
        return status
    
save_file = 'url_file'
crawl_record_file = 'crawl_record.json' # 爬取状态记录
if os.path.isdir(save_file) is False:
    os.mkdir(save_file)

goal_list = ['军武次位面',
            '空军之翼',
            '北国防务',
            '雷曼军事现代舰船',
            '崎峻战史',
            '讲武堂',
            '军报记者',
            '人民武警',
            '环球军事',
            '蒋校长',
            '米尔观天下'
            ]

search_url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=10&createType=0&token=769130938&lang=zh_CN'

if __name__ == '__main__':
    if os.path.isfile(crawl_record_file) is False:
        crf = open(crawl_record_file, 'w', encoding='utf-8-sig')
        crawl_record = {}
    else:
        crf = open(crawl_record_file, 'r', encoding='utf-8-sig')
        crawl_record = json.load(crf)
    driver = connectchrome()
    # driver.get(search_url)
    login(driver)
    scan_qrcode(driver)
    preoption(driver)
    for goal in goal_list:
        print(goal)
        if goal in crawl_record:
            if crawl_record[goal] == {}:
                crawl_record[goal]['finish'] = False
            elif 'finish' in crawl_record[goal] and crawl_record[goal]['finish']:
                continue
        else:
            crawl_record[goal] = {}
        # if os.path.isfile(save_file+'/'+goal) is False:
        with open(save_file+'/'+goal+'_{}'.format(datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")), 'a+') as f:
            search(driver, goal)
            status = crawl_url(driver, f, crawl_record[goal])
            if status != {}:
                crawl_record[goal] = status
        crf = open(crawl_record_file, 'w', encoding='utf-8')
        json.dump(crawl_record, crf, indent=4, ensure_ascii=False)
    delete_empty_file('url_file')
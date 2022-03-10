from utils import *


if __name__ == '__main__':

    # 公众号账号
    user_name = '2625538949@qq.com'
    user_psw = '4972039.'

    driver = connectchrome()
    # driver.get(search_url)
    last_date = datetime.datetime.now().strftime("%Y%m%d")
    login(driver, user_name, user_psw)
    scan_qrcode(driver)
    preoption(driver)
    updateUrl = {}
    for goal in goal_list:
        print(goal)
        search(driver, goal)
        updateUrl[goal] = crawlUpdateUrl(driver, last_date)
    save_path = 'daily_url_file'
    if os.path.isdir(save_path) is False:
        os.makedirs(save_path)
    with open('{}/{}'.format(save_path, datetime.datetime.now().strftime("%Y%m%d")), 'w', encoding='utf-8') as f:
        json.dump(updateUrl, f, indent=4, ensure_ascii=False)
from utils import *

if __name__ == '__main__':

    # 公众号账号
    user_name = '2625538949@qq.com'
    user_psw = '4972039.'

    save_file = 'url_file'
    crawl_record_file = 'crawl_record.json' # 爬取状态记录
    if os.path.isdir(save_file) is False:
        os.mkdir(save_file)

    if os.path.isfile(crawl_record_file) is False:
        crf = open(crawl_record_file, 'w', encoding='utf-8-sig')
        crawl_record = {}
    else:
        crf = open(crawl_record_file, 'r', encoding='utf-8-sig')
        crawl_record = json.load(crf)
    driver = connectchrome()
    # driver.get(search_url)
    login(driver, user_name, user_psw)
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
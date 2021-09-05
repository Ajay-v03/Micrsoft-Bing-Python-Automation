import re
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.chrome.options import Options
import pymongo
chrome_options = Options()
from webdriver_manager.chrome import ChromeDriverManager
from multiprocessing import Pool


def bingDetailFetcher(name):
    final = []

    d1 = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    start_url = 'https://www.bing.com/?FORM=Z9FD1'
    d1.get(start_url)
    d1.maximize_window()

    platform = 'linkedin'

    search_tab = d1.find_elements_by_id('sb_form_q')[0]
    search_tab.send_keys(f'{name} {platform}')

    from selenium.webdriver.common.keys import Keys
    d1.find_element_by_id("sb_form_q").send_keys(Keys.ENTER)

    page_content = d1.find_elements_by_class_name("b_algo")

    result = []
    for x in page_content:
        result.append(x.text)

    for values in result:
        dic = {}
        name = values.split('\n')[0].replace('-', '@').replace('|', '@').split('@')[0].strip()
        if 'profiles' in name:
            name = ''
        else:
            name = name
        if name:
            dic['name'] = name

        if name:

            for val in values.split('\n'):
                if re.search(r'https:|http', val):
                    if len(val) >= 60:
                        pass
                    else:
                        profile_url = val.strip()
                        if profile_url:
                            profile_url = profile_url
                        else:
                            profile_url = None

                        dic['linkedin_url'] = profile_url

            for val in values.split('\n'):
                if re.search(r'Location|location', val):
                    location = val.split(':')[1].strip()
                    if location:
                        location = location
                    else:
                        location = None

                    dic['location'] = location

        if len(dic) > 0:
            final.append(dic)

    sleep(2)

    for i in range(9):

        element = d1.find_element_by_class_name('sb_pagN.sb_pagN_bp.b_widePag.sb_bp ')
        d1.execute_script("arguments[0].click();", element)

        page_content = d1.find_elements_by_class_name("b_algo")

        result = []
        for x in page_content:
            result.append(x.text)

        for values in result:
            dic = {}
            name = values.split('\n')[0].replace('-', '@').replace('|', '@').split('@')[0].strip()
            if 'profiles' in name:
                name = ''
            elif len(name) > 30:
                name = ''
            else:
                name = name
            if name:
                dic['name'] = name

            if name:

                for val in values.split('\n'):
                    if re.search(r'https:|http', val):
                        if len(val) >= 60:
                            pass
                        else:
                            profile_url = val.strip()
                            if profile_url:
                                profile_url = profile_url
                            else:
                                profile_url = None

                            dic['linkedin_url'] = profile_url

                for val in values.split('\n'):
                    if re.search(r'Location|location', val):
                        location = val.split(':')[1].strip()
                        if location:
                            location = location
                        else:
                            location = None
                        dic['location'] = location

            if len(dic) > 0:
                final.append(dic)

    final_dataset = {'data': final}
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["webdatas"]

    x = mycol.insert_one(final_dataset)
    x = mycol.find_one()
    print(x)
    print(len(final_dataset), final_dataset)
    print('Execution complete...')
    d1.close()
    d1.quit()
    return final_dataset


def csvHandler():

    name_list = []
    df = pd.read_csv('us_names.csv')
    list_data = df.values.tolist()

    for list_ in list_data:
        for value in list_:
            name_list.append(value)

    name_data = []
    count = 0
    for names in range(len(name_list)):
        name_pair = name_list[count:count + 3]
        count += 3
        if name_pair:
            name_data.append(name_pair)

    return name_data


name_data = csvHandler()
# names = ['Ajay', 'Ashish', 'Abhishek']
for names in name_data:
    pool = Pool(3)
    results = pool.map(bingDetailFetcher, names)
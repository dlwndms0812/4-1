from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime
import time


def CoffeeBean_store(result) :
    CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp"
    wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    for i in range(1, 51) :
        wd.get(CoffeeBean_URL)
        time.sleep(1)
        try :
            wd.execute_script("storePop2(%d)" %i)
            time.sleep(1)
            html = wd.page_source

            with open('testHtml.txt', 'w', encoding='utf8') as outfile :
                outfile.write(html)
            
            soupCB = BeautifulSoup(html, 'html.parser')
            store_name_h2 = soupCB.select("div.store_txt > h2")
            store_name = store_name_h2[0].string
            print(i, store_name)
            store_info = soupCB.select("div.store_txt > table.store_table > tbody > tr > td")
            store_address_list = list(store_info[2])
            store_address = store_address_list[0]
            store_phone = store_info[3].string
            result.append([store_name] + [store_address] + [store_phone])

        except :
            print(i, "fail")
            continue 
    return 


def main() :
    result = []
    print("CoffeeBean store crawling >>>>>>>>>>>>>>>>>")
    CoffeeBean_store(result)

    CB_tbl = pd.DataFrame(result, columns=('store', 'address', 'phone'))
    CB_tbl.to_csv('./CoffeeBean.csv', encoding='utf8', mode = 'w', index=True)


if __name__ == '__main__':
    main()
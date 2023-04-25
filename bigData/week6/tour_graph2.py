import os
import sys
import urllib.request
import datetime
import time
import json
import pandas as pd
import numpy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc #mac 폰트깨짐 해결위해 추가

ServiceKey = "SERVICE KEY"

def getRequestUrl(url) :
    req = urllib.request.Request(url)
    try :
        response = urllib.request.urlopen(req)
        if response.getcode() == 200 :
            print("[%s] Url Request Success " % datetime.datetime.now())
            return response.read().decode("utf-8")
    except Exception as e :
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None;


def getTourismStatsItem(yyyymm, national_code, ed_cd) :
    service_url = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"

    parameters = "?_type=json&serviceKey=" + ServiceKey
    parameters += "&YM=" + yyyymm
    parameters += "&NAT_CD=" + national_code
    parameters += "&ED_CD=" + ed_cd

    url = service_url + parameters
    print(url)
    retData = getRequestUrl(url)

    if (retData == None) :
        return None
    else :
        return json.loads(retData)


def getTourismStatsService(nat_cd, ed_cd, nStartYear, nEndYear) :
    jsonResult = []
    result = []
    natName = ''
    ed = ''
    dataEND = "{0}{1}".format(str(nEndYear), str(12))
    isDataEnd = 0

    for year in range(nStartYear, nEndYear + 1) :
        for month in range(1, 13) :
            if (isDataEnd == 1) :
                break
            yyyymm = "{0}{1:0>2}".format(str(year), str(month)) 
            jsonData = getTourismStatsItem(yyyymm, nat_cd, ed_cd)
            

            if (jsonData['response']['header']['resultMsg'] == 'OK') :
                if jsonData['response']['body']['items'] == "" :
                    isDataEnd = 1
                    dataEND = "{0}{1:0>2}".format(str(year), str(month-1))
                    print("데이터 없음...\n 제공되는 통계 데이터는 %s년 %s월까지 입니다." %(str(year), str(month-1)))
                    break

                print(json.dumps(jsonData, indent = 4, sort_keys = True, ensure_ascii = False))
                natName = jsonData['response']['body']['items']['item']['natKorNm']
                natName = natName.replace(' ', '')
                num = jsonData['response']['body']['items']['item']['num']
                ed = jsonData['response']['body']['items']['item']['ed']
                print("[ %s_%s : %s]" %(natName, yyyymm, num))

                print("----------------------------------------------")
                jsonResult.append({'nat_name' : natName, 'nat_cd' : nat_cd, 'yyyymm' : yyyymm, 'visit_cnt' : num})
                result.append([natName, nat_cd, yyyymm, num])

                print(result)
        
    return (jsonResult, result, natName, ed, dataEND)
        

def main() :
    jsonResult1 = []
    jsonResult2 = []
    result1 = []
    result2 = []
    natName1 = ''
    natName2 = ''

    print("<< 국내 입국한 외국인의 통계 데이터 수집 >>")
    nat_cd1 = input("국가 코드를 입력하세요(중국 : 112 / 일본 : 130 / 미국 : 275) : ")
    nat_cd2 = input("국가 코드를 입력하세요(중국 : 112 / 일본 : 130 / 미국 : 275) : ")
    
    nStartYear = int(input("데이터를 몇 년부터 수집할까요? : "))
    nEndYear = int(input("데이터를 몇 년까지 수집할까요? : "))
    ed_cd = "E"
    jsonResult1, result1, natName1, ed, dataEND = getTourismStatsService(nat_cd1, ed_cd, nStartYear, nEndYear)
    jsonResult2, result2, natName2, ed, dataEND = getTourismStatsService(nat_cd2, ed_cd, nStartYear, nEndYear)

    if (natName1 == '' or natName2 == '') :
        print("데이터가 수집되지 않았습니다")
    
    else :
        with open('./%s_%s_%d_%s.json' % (natName1, ed, nStartYear, dataEND), 'w', encoding = 'utf8') as outfile :
            jsonFile1 = json.dumps(jsonResult1, indent = 4, sort_keys = True, ensure_ascii = False)

            outfile.write(jsonFile1)
        with open('./%s_%s_%d_%s.json' % (natName2, ed, nStartYear, dataEND), 'w', encoding = 'utf8') as outfile :
            jsonFile1 = json.dumps(jsonResult2, indent = 4, sort_keys = True, ensure_ascii = False)

            outfile.write(jsonFile1)

        columns = ["입국자국가", "국가코드", "입국연월", "입국자 수"]
        result_df1 = pd.DataFrame(result1, columns = columns)
        result_df1.to_csv('./%s_%s_%d_%s.csv' % (natName1, ed, nStartYear, dataEND), index = False, encoding = 'utf8')
        
        result_df2 = pd.DataFrame(result2, columns = columns)
        result_df2.to_csv('./%s_%s_%d_%s.csv' % (natName2, ed, nStartYear, dataEND), index = False, encoding = 'utf8')
        

        rc('font', family='AppleGothic') #mac 폰트깨짐 해결위해 추가	 
        plt.rcParams['axes.unicode_minus'] = False  #mac 폰트깨짐 해결위해 추가

        #plt.plot(result_df["입국연월"], result_df["입국자 수"])
        #plt.title(natName + ed);
        #plt.xlabel("입국자 수")
        #plt.ylabel("입국연월")

        yyyymmList = result_df1["입국연월"].values.tolist()

        visitNumList1 = result_df1["입국자 수"].values.tolist()
        visitNumList2 = result_df2["입국자 수"].values.tolist()

        xlabel = numpy.arange(len(yyyymmList))

        plt.bar(xlabel, visitNumList1, label = natName1, color='r', width=0.2)
        plt.bar(xlabel+0.2, visitNumList2, label = natName2, color='b', width=0.2)
        plt.xticks(xlabel, yyyymmList);

        plt.legend(loc='upper right')
        plt.title('{0}-{1} 입국자 수'.format(str(yyyymmList[0]), str(yyyymmList[-1])))
        plt.xlabel("입국연월")
        plt.ylabel("입국자 수")


        plt.show()

if __name__ == '__main__' :
    main()

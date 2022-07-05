from flask import Flask, request, render_template
import threading
import start
from datetime import datetime
import datetime
import json
app = Flask(__name__)
import matplotlib.pyplot as plt
import random
import os, glob, time
import start
from tqdm import tqdm

import csv

from utils.processing_json import Processing_json
from utils.predict import Predict 

#누적 그래프 결과 페이지
@app.route('/resultPage', methods=['GET', 'POST'])
def result() :
    if request.method == 'GET':
        l = []
        s = []
        e = []
        # csv파일 읽어서 html로 값 전송
        with open(f'../main_program/static/search.csv', 'r',newline='', encoding='utf8') as f:
            re = csv.reader(f)
            for i in re :
                l.append(i[0]+i[1]+i[2])
            l.reverse()
            print(l)
        return render_template("./resultPage.html", search_list = l, start_day = s, end_day = e)

#사이트 설명 페이지
@app.route('/guide', methods=['GET', 'POST'])
def guide() :
    if request.method == 'GET':
        return render_template("./guide.html")
#모델 실행이 끝난 후 그래프 보여주는 페이지
@app.route('/graph', methods=['GET', 'POST'])
def graph():
    
    file = f'../main_program/result/naver_news/news_{search}_naver_{start_date}_{end_date}__{end_date[:6]}.json'
    while True :
        if os.path.isfile(file) :
            print("-"*30)
            print("[ json파일이 생성되었습니다. ]")
            print("-"*30)
            print("[ 감성분석을 시작합니다. ]")
            print("-"*30)

            ## 전처리 후 예측
            processing = Processing_json(f'../main_program/result/naver_news/news_{search}_naver_{start_date}_{end_date}__{end_date[:6]}.json')
            processed_dic = processing.dateNList()

            print(processed_dic)

            def dic_to_result(processed_dic):   
                predict = Predict()

                result_dic = {}
                result_happy = []
                result_bad = []

                for key in processed_dic.keys():
                    missing_value = False
                    positive = 0
                    negative = 0
                    if len(processed_dic[key]) == 0:
                        missing_value = True
                    for comment in processed_dic[key]:
                        if predict.predict(comment):
                            positive +=1
                        else:
                            negative +=1
                    if missing_value:
                        result_dic[key] = -1
                    else:
                        result_dic[key] = positive/(positive+negative)*100
                    
                    result_happy.append(positive)
                    result_bad.append(negative)
                    
                    positive = 0
                    negative = 0
                return result_dic,result_happy,result_bad   #ex) {'20220623':70, '20220624':-1(결측값)}
            
            result,happy_num,bad_num = dic_to_result(processed_dic)
            all_num = [x+y for x,y in zip(happy_num, bad_num)]

            print("감성분석 결과 입니다.")
            print(result)
            print(happy_num)
            print(bad_num)
            print(all_num)

            # 그래프 그리기--------------------------------------------
            startDate = start_date
            lastDate = end_date

            # 각 날짜를 리스트에 끊어서 저장
            # ex) 20220627 = ['2', '0', '2', '2', '0', '6', '2', '7']
            start_dateList = []
            for y in (startDate):
                start_dateList.append(y)
            last_dateList = []
            for y in (lastDate):
                last_dateList.append(y)

            # string 타입의 리스트를 int 타입으로 변환
            start_dateList = list(map(int, start_dateList))
            last_dateList = list(map(int, last_dateList))

            # 시작 날짜 정리
            thousand = start_dateList[0] * 1000
            hundred = start_dateList[1] * 100
            yten = start_dateList[2] * 10
            yone = start_dateList[3]
            mten = start_dateList[4] * 10
            mone = start_dateList[5]
            dten = start_dateList[6] * 10
            done = start_dateList[7]
            startYear = thousand + hundred + yten + yone
            startMonth = mten + mone
            startDay = dten + done

            # 마지막 날짜 정리
            thousand = last_dateList[0] * 1000
            hundred = last_dateList[1] * 100
            yten = last_dateList[2] * 10
            yone = last_dateList[3]
            mten = last_dateList[4] * 10
            mone = last_dateList[5]
            dten = last_dateList[6] * 10
            done = last_dateList[7]
            lastYear = thousand + hundred + yten + yone
            lastMonth = mten + mone
            lastDay = dten + done

            # datetime으로 적용
            startday = datetime.date(startYear, startMonth, startDay)
            lastday = datetime.date(lastYear, lastMonth, lastDay)

            # 두 날짜간 차이 계산
            dateResult = startday - lastday
            dateResult = abs(dateResult)

            # 날짜형 -> 문자형 변환 후 날짜간 차이를 정수형으로 저장
            strDate = str(dateResult)
            sstrDate = strDate.split(' ')
            intDate = int(sstrDate[0])      # 날짜간 차이(정수형)

            monthList = []      # 사용자가 지정한 month의 리스트
            dateList = []       # 사용자가 지정한 day의 리스트
            yearList = []

            #   1월 2월 3월 4월  5월 6월 7월 8월 9월 10월 11월 12월
            m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31,  30,  31]

            # 같은 달일때
            if startMonth == lastMonth and intDate < m[startMonth-1] :
                for i in range(startDay,lastDay+1) :
                    dateList.append(i)
                    monthList.append(startMonth)
                    yearList.append(startYear)
            # 다른 달일때
            elif startMonth != lastMonth :
                # 다른 연도
                if startYear != lastYear :
                    m_m = lastMonth - startMonth
                    m_m = abs(abs(m_m)-12)+1
                    for i in range(m_m) :
                        if i == 0 :
                            for j in range(startDay,m[((startMonth-1)+i)-12]+1):
                                dateList.append(j)
                                monthList.append((startMonth-1)+i+1)
                                yearList.append(startYear)

                        elif 0<i<m_m-1:
                            for j in range(1,m[((startMonth-1)+i)-12]+1):
                                dateList.append(j)
                                monthList.append(i)
                                
                                if ((startMonth-1)+i-12+1) < startMonth :
                                    yearList.append(lastYear)
                                

                        else :
                            for j in range(1,lastDay+1):
                                dateList.append(j)
                                yearList.append(lastYear)
                                monthList.append(i)            
                # 같은 연도
                else :
                    m_m = lastMonth - startMonth +1
                    for i in range(m_m) :
                        if i == 0 :
                            for j in range(startDay,m[startMonth-1]+1):
                                dateList.append(j)
                                monthList.append(startMonth)
                                yearList.append(startYear)
                        elif 0<i<m_m-1:
                            for j in range(1,m[startMonth-1+i]+1):
                                dateList.append(j)
                                monthList.append((startMonth-1)+1)
                                yearList.append(startYear)
                        else :
                            for j in range(1,lastDay+1):
                                dateList.append(j)
                                monthList.append((lastMonth-1)+1)
                                yearList.append(startYear)

            # 정수형 리스트를 문자열 리스트로 변환
            str_month_list = list(map(str, monthList))
            str_date_list = list(map(str, dateList))
            str_year_list = list(map(str, yearList))

            # n월 n일 형태로 출력
            listLen = len(str_month_list)
            resultList = []
            for i in range(listLen):
                if len(str_month_list[i]) != 2 and len(str_date_list[i]) != 2 :
                    resultList.append(str_year_list[i]+"0"+str_month_list[i]+ "0"+str_date_list[i])
                elif len(str_month_list[i]) != 2 and len(str_date_list[i]) == 2 :
                    resultList.append(str_year_list[i]+"0"+str_month_list[i]+str_date_list[i])
                elif len(str_month_list[i]) == 2 and len(str_date_list[i]) != 2 :
                    resultList.append(str_year_list[i]+str_month_list[i]+"0"+str_date_list[i])
                else :
                    resultList.append(str_year_list[i]+str_month_list[i]+ str_date_list[i])

            #html에 보내줄 값 저장
            happy = happy_num
            bad = bad_num
            all_n = all_num
            search_day = search + start_date + end_date
            print(resultList)

            #csv저장 = DB역할 
            with open(f'../main_program/static/search.csv', 'a',newline='', encoding='utf8') as f:
                wr = csv.writer(f)
                wr.writerow([search,start_date,end_date])
            
            #그래프 그린후 저장

            plt.clf()
            #긍정 그래프
            plt.plot(resultList,happy,color='blue',linestyle='-',marker='o')
            #plt.plot(resultList,bad,color='red',linestyle='-',marker='o')
            plt.xticks(resultList, rotation='90')  # x축 라벨의 이름 pow지움
            plt.title(f'{search} p graph', )  # 그래프 제목 설정
            plt.ylabel('happy_num',)  # y축에 설명 추가
            plt.tight_layout()
            #plt.ylim(0,max(max(happy),max(bad)))
            #C:\Users\g\ACIN_public\00_data\main_program\static\images
            plt.savefig(f'../main_program/static/images/{search}{start_date}{end_date}happy.jpg')
            plt.clf()
            # 부정 그래프
            plt.plot(resultList,bad,color='red',linestyle='-',marker='o')
            plt.xticks(resultList, rotation='90')  # x축 라벨의 이름 pow지움
            plt.title(f'{search} n graph', )  # 그래프 제목 설정
            plt.ylabel('bad_num',)  # y축에 설명 추가
            plt.tight_layout()
            plt.savefig(f'../main_program/static/images/{search}{start_date}{end_date}bad.jpg')
            plt.clf()
            # 관심도 그래프
            plt.plot(resultList,all_n,color='green',linestyle='-',marker='o')
            plt.xticks(resultList, rotation='90')  # x축 라벨의 이름 pow지움
            plt.title(f'{search} interest index graph', )  # 그래프 제목 설정
            plt.ylabel('interest index',)  # y축에 설명 추가
            plt.tight_layout()
            plt.savefig(f'../main_program/static/images/{search}{start_date}{end_date}all.jpg')
            plt.clf()
            return render_template("./graph_page.html", value = result,happy_value = happy_num,bad_value = bad_num, value_search = search, search_day = search_day)

#중간 로딩 페이지
@app.route('/loding', methods=['GET', 'POST'])
def lode():
    if request.method == 'GET':
        return render_template("./loding.html")

#처음 시작 페이지
@app.route('/', methods=['GET', 'POST'])
def goo():
    
    if request.method == 'GET':
        return render_template("./index.html")
    elif request.method == 'POST':
        global search
        global start_date
        global end_date
        global file
        search = request.form.get('keyword')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        
        start_date = start_date[:4] + start_date[5:7] + start_date[8:]
        end_date = end_date[:4] + end_date[5:7] + end_date[8:]
        print("[검색어, 날짜가 입력 되었습니다.]")
        print(search, start_date, end_date)

        #크롤러 실행 
        file = f'../main_program/result/naver_news/news_{search}_naver_{start_date}_{end_date}__{end_date[:6]}.json'
        threading.Thread(target=start.main, args=(search, start_date, end_date,)).start()
        print("[ 스레드 크롤러가 실행 되었습니다. ]")

        
        return render_template("./loding.html", search = search ,start_date = start_date,end_date = end_date,file = file)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80",debug=False, threaded=True )


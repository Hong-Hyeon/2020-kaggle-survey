import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import time

def data_prepro():
    data = pd.read_csv('./data/kaggle_survey_2020_responses.csv', low_memory=False)
    # 0번째 행은 질문들
    q = data.iloc[0,:]

    # 0번째 행은 drop하고 1행부터의 데이터를 담아놓음.
    data = data.drop([0])
    return data, q

def show_countplot(data, data_no, q, fsize=(10,6)):
    plt.figure(figsize=fsize)
    try:
        sns.countplot(data=data, y=data_no).set_title(q[data_no])
    except:
        sns.countplot(data=data, y=data_no)

def multiple_check(data,q, q_no):
    q_num = q.filter(regex=q_no)[0].split("-")[0]
    data_q = data.filter(regex=q_no)  # Q7의 data를 뽑아옴
    data_desc = data_q.describe()  # 요약본

    return data_q, q_num, data_desc

def age_data(data, q):
    check = int(input('''나이 데이터 확인입니다. 확인을 원하시는 데이터의 번호를 입력해주세요. 
                        (1:나이데이터 자체, 2:나이순으로 총 몇명이 있는가)'''))
    years_old = data.iloc[:, 1]
    if check == 1:
        print(years_old, end='\n\n')
        # 나이순 비율
        print("나이 비율 데이터")
        print(years_old.value_counts(normalize=True) * 100)
    elif check == 2:
        # 나이순으로 총 몇명이 있는지
        # print(years_old.value_counts()) # 수가 많은대로 정렬됨
        print(years_old.value_counts().sort_index(), end='\n\n') # 인덱스 순서대로 정렬됨
        # 나이순 비율
        print(years_old.value_counts(normalize=True) * 100)

        visual = int(input('''데이터를 시각화 하시겠습니까?(1: 예)'''))
        if visual == 1:
            # 나이 순 확인
            plt.title("what is your age?")
            plt.plot(years_old.value_counts().sort_index())
            plt.show(block=True)

            show_countplot(data=data,data_no="Q1", q=q)
            plt.show(block=True)

        else:
            print("나이 데이터 확인 끝.")
            return True
    else:
        print("잘못 입력하셨습니다.\n메뉴로 강제 이동됩니다.")
        return False

def sex_data(data, q):
    check = int(input('''성별 데이터 확인입니다. 확인을 원하시는 데이터의 번호를 입력해주세요. 
                        (1:성별데이터 자체, 2:성별 데이터 그래프)'''))
    if check == 1:
        # 성별 데이터 확인
        print(data["Q2"].value_counts())
    elif check == 2:
        show_countplot(data=data,data_no="Q2", q=q)
        plt.show(block=True)
    else:
        print("잘못 입력하셨습니다.\n메뉴로 강제 이동됩니다.")
        return False

def country_data(data, q):
    check = int(input('''나라 데이터 확인입니다. 확인을 원하시는 데이터의 번호를 입력해주세요. 
                        (1:나라데이터 자체, 2:나라 데이터 그래프)'''))
    if check == 1:
        # 나라 데이터 확인
        print(data["Q3"].value_counts())
    elif check == 2:
        show_countplot(data=data,data_no="Q3", q=q, fsize=(10,10))
        plt.show(block=True)
    else:
        print("잘못 입력하셨습니다.\n메뉴로 강제 이동됩니다.")
        return False

def edu_data(data,q):
    check = int(input('''교육 데이터 확인입니다. 확인을 원하시는 데이터의 번호를 입력해주세요. 
                        (1:교육데이터 자체, 2:교육 데이터 그래프)'''))
    if check == 1:
        # 교육 데이터 확인
        print(data["Q4"].value_counts())
    elif check == 2:
        show_countplot(data=data,data_no="Q4", q=q,fsize=(17,6))
        plt.show(block=True)
    else:
        print("잘못 입력하셨습니다.\n메뉴로 강제 이동됩니다.")
        return False

def job_data(data,q):
    check = int(input('''직업 데이터 확인입니다. 확인을 원하시는 데이터의 번호를 입력해주세요. 
                        (1:직업데이터 자체, 2:직업 데이터 그래프)'''))
    if check == 1:
        print(data["Q5"].value_counts())
    elif check == 2:
        show_countplot(data=data,data_no="Q5", q=q)
        plt.show(block=True)
    else:
        print("잘못 입력하셨습니다.\n메뉴로 강제 이동됩니다.")
        return False

def career_data(data,q):
    check = int(input('''경력 데이터 확인입니다. 확인을 원하시는 데이터의 번호를 입력해주세요. 
                        (1:경력데이터 자체, 2:경력 데이터 그래프)'''))
    if check == 1:
        print(data["Q6"].value_counts())
    elif check == 2:
        show_countplot(data=data,data_no="Q6", q=q)
        plt.show(block=True)
    else:
        print("잘못 입력하셨습니다.\n메뉴로 강제 이동됩니다.")
        return False

def lang_data(data,q):
    check = int(input('''프로그래밍 언어 데이터 확인입니다. 확인을 원하시는 데이터의 번호를 입력해주세요. 
                            (1:언어데이터 자체, 2:언어 데이터 그래프, 3:데이터사이언티스트가 되기 위해 처음 배우기 좋은 언어, 4:사용하고 있는 환경)'''))
    if check == 1:
        _ , q_no, data_desc = multiple_check(data=data, q=q, q_no="Q7")

        print(data_desc.loc[["top","count"]].T.set_index("top")) # T는 컬럼과 인덱스의 값을 바꿔주는 것
    elif check == 2:
        _ , q_no, data_desc = multiple_check(data=data, q=q, q_no="Q7")

        plt.figure(figsize=(10,6))
        plt.title(q_no)
        plt.plot(data_desc.loc[["top","count"]].T.set_index("top"))
        # sns.barplot(data=data_desc, y=data_desc.index, x="count")
        plt.show(block=True)
    elif check == 3:
        show_countplot(data=data, data_no="Q8", q=q)
        plt.show(block=True)
    elif check == 4:
        _ , q_no, data_desc = multiple_check(data=data, q=q, q_no="Q9")

        plt.figure(figsize=(10,6))
        plt.title(q_no)
        plt.plot(data_desc.loc[["top","count"]].T.set_index("top"))
        plt.xticks(fontsize=10, rotation=45)
        plt.show(block=True)
    else:
        print("잘못 입력하셨습니다.\n메뉴로 강제 이동됩니다.")
        return False

def project_data(data, q):
    print('''캐글 유저들이 프로젝트시 사용하는 컴퓨팅 플랫폼 데이터 확인입니다. 시각화하겠습니다.''', end='\n\n')

    show_countplot(data=data, data_no="Q11", q=q)
    plt.show(block=True)

def pay_data(data, q):
    print('''캐글 유저들의 연봉 데이터입니다. 시각화하겠습니다.''')

    show_countplot(data=data, data_no="Q24", q=q)
    plt.show(block=True)

def korean_data(data, q):
    check = int(input('''한국인 데이터 확인입니다. 확인을 원하시는 데이터의 번호를 입력해주세요. 
                            (1:한국사람 학력, 2:한국사람 직업, 3:한국사람 경력, 4:한국사람 성별, 5:한국사람들이 사용하는 프로그래밍 언어,
                            6:한국유저의 연봉)'''))
    data_ = data[data["Q3"] == "Republic of Korea"]

    if check == 1:
        show_countplot(data=data_, data_no="Q4", q=q, fsize=(17,6))
        plt.show(block=True)
    elif check == 2:
        show_countplot(data=data_, data_no="Q5", q=q)
        plt.show(block=True)
    elif check == 3:
        show_countplot(data=data_, data_no="Q6", q=q)
        plt.show(block=True)
    elif check == 4:
        show_countplot(data=data_, data_no="Q2", q=q)
        plt.show(block=True)
    elif check == 5:
        q7_cols = data_.filter(regex="Q7").describe().loc["top"].tolist()
        data__ = data_.filter(regex="Q7|Q2$").groupby("Q2").count()

        data__.columns = q7_cols
        # print(data__)
        # data__ = data__.loc[["Man","Woman"]].T
        # print(type(data__))
        sns.barplot(data=data__, ci=None)
        plt.xticks(fontsize=10, rotation=45)
        plt.show(block=True)

    elif check == 6:
        # 연봉
        # show_countplot(data=data_.sort_values(by="Q24"), data_no="Q24", q=q)
        # plt.show(block=True)
        # 성별 + 연봉
        sns.countplot(data=data_, x="Q24", hue="Q2")
        plt.xticks(fontsize=10, rotation=45)
        plt.show(block=True)
    else:
        print("잘못 입력하셨습니다.\n메뉴로 강제 이동됩니다.")
        return False

if __name__ == "__main__":
    data, q = data_prepro()

    while True:
        choice = int(input('''----- 2020 캐글 유저 설문조사 데이터입니다. -----
        확인하실 데이터를 골라주시기 바랍니다.
        0. 끝내기
        1. 캐글 유저들의 데이터
        2. 대한민국 유저들의 데이터'''))
        if choice == 0:
            print("프로그램 종료하겠습니다. 감사합니다.")
            break
        elif choice == 1:
            str = int(input('''
                                0. 나가기
                                1. 나이데이터
                                2. 성별데이터
                                3. 나라데이터
                                4. 교육데이터
                                5. 직업데이터
                                6. 경력데이터
                                7. 캐글 사용자들의 프로그래밍 언어 사용 데이터
                                8. 데이터 사이언스 프로젝트에 참여할 때 사용하는 컴퓨팅 플랫폼 데이터
                                9. 연봉 데이터'''))
            if str == 0:
                print("--- 캐글 유저 데이터 확인에서 나가겠습니다. ---", end='\n\n')
                time.sleep(1)
                continue
            elif str == 1:
                age_data(data=data, q=q)
            elif str == 2:
                sex_data(data=data, q=q)
            elif str == 3:
                country_data(data=data, q=q)
            elif str == 4:
                edu_data(data=data, q=q)
            elif str == 5:
                job_data(data=data, q=q)
            elif str == 6:
                career_data(data=data, q=q)
            elif str == 7:
                lang_data(data=data, q=q)
            elif str == 8:
                project_data(data=data, q=q)
            elif str == 9:
                pay_data(data=data, q=q)

        elif choice == 2:
            korean_data(data=data, q=q)
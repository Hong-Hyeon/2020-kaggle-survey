import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def data_prepro():
    data = pd.read_csv('./data/kaggle_survey_2020_responses.csv', low_memory=False)
    # 0번째 행은 질문들
    q = data.iloc[0,:]

    # 0번째 행은 drop하고 1행부터의 데이터를 담아놓음.
    data = data.drop([0])
    return data, q

def show_countplot(data, data_no, q, fsize=(10,6)):
    plt.figure(figsize=fsize)
    sns.countplot(data=data.sort_values("Q1"), y=data_no).set_title(q[data_no])

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

def korean_data(data, q):
    check = int(input('''한국인 데이터 확인입니다. 확인을 원하시는 데이터의 번호를 입력해주세요. 
                            (1:한국사람 학력, 2:한국사람 직업, 3:한국사람 경력, 4:한국사람 성별)'''))
    data = data[data["Q3"] == "Republic of Korea"]
    if check == 1:
        show_countplot(data=data, data_no="Q4", q=q, fsize=(17,6))
        plt.show(block=True)
    elif check == 2:
        show_countplot(data=data, data_no="Q5", q=q)
        plt.show(block=True)
    elif check == 3:
        show_countplot(data=data, data_no="Q6", q=q)
        plt.show(block=True)
    elif check == 4:
        show_countplot(data=data, data_no="Q2", q=q)
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
        1. 나이데이터
        2. 성별데이터
        3. 나라데이터
        4. 교육데이터
        5. 직업데이터
        6. 경력데이터
        7. 대한민국 유저들의 데이터(학력 등)'''))
        if choice == 0:
            print("프로그램 종료하겠습니다. 감사합니다.")
            break
        elif choice == 1:
            age_data(data=data, q=q)
        elif choice == 2:
            sex_data(data=data, q=q)
        elif choice == 3:
            country_data(data=data, q=q)
        elif choice == 4:
            edu_data(data=data, q=q)
        elif choice == 5:
            job_data(data=data, q=q)
        elif choice == 6:
            career_data(data=data, q=q)
        elif choice == 7:
            korean_data(data=data, q=q)

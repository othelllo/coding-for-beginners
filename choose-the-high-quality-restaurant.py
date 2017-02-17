Koreanfood = ["된장찌개","부대찌개","비빔밥"]
Chinesefood = ["짜장면", "짬뽕", "볶음밥"]
Japanesefood = ["초밥","돈까스","메밀소바"]

user_input = input("먹고 싶은 음식 종류를 한 가지 골라주세요(한식, 중식, 일식).")
import random

if user_input == "한식":
    print("추천 메뉴는 " + random.choice(Koreanfood)+ "입니다.")
elif user_input == "중식":
    print("추천 메뉴는 " + random.choice(Chinesefood)+ "입니다.")
elif user_input == "일식":
    print("추천 메뉴는 " + random.choice(Japanesefood)+ "입니다.")

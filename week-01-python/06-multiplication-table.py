# 1)사용자로부터 몇 단을 출력할 지 받을것
# 2) 해당 단을 곱하기 1에서 곱하기 9까지 실행할 것

dan = int(input("몇 단을 출력 하시겠습니까?"))
for num in range(1, 10): #range의 1,10에서 10은 생략, 9단이므로 9까지만
    print("{} * {} = {}".format(dan, num, dan * num))

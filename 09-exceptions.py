 # exception

# ZeroDivisionError
 # 1 / 0

def divide_by(first, second):
    try:
        return first / second
    # except:
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."
print(divide_by(4, 2))
print(divide_by(4, 0))

# 예외 만들기
# Exception

class EvenNumbeDivisionError(Exception): # Class의 변수는 대문자 활용한 변수
    pass

def divide_by_odd_number(first, second): # 함수에 사용하는 변수는 _로 구분
    if second % 2 == 0:
        raise EvenNumbeDivisionError # 에러를 일으킬 때를 특정하는 함수, 에러를 일부러 일으키게 하기 위한 함수 즉 에러를 발견하기 쉽게 하는 문구
    else:
        return first / second
print(divide_by_odd_number(6, 3))
print(divide_by_odd_number(6, 2))

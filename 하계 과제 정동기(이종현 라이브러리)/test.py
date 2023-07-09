import Calculator as Cal

"""
소개
Calculator는 간단한 사칙연산 기능을 제공하는 라이브러리입니다.
"""
a = 10; b = 5; c =0;

# 덧셈[add(a, b)]: 두 숫자를 더한 결과를 반환합니다.
print(Cal.add(a, b)) # 10 + 5 = 15
# 뺄셈[subtract(a, b)]: 첫 번째 숫자에서 두 번째 숫자를 뺀 결과를 반환합니다.
print(Cal.subtract(a, b)) # 10 - 5 = 5
# 곱셈[multiply(a, b)]: 두 숫자를 곱한 결과를 반환합니다.
print(Cal.multiply(a ,b)) # 10 * 5 = 50
# 나눗셈[divide_numbers(a, b)]: 첫 번째 숫자를 두 번째 숫자로 나눈 결과를 반환합니다. #divide() 함수는 0으로 나눌 수 없습니다
print(Cal.divide(a, b)) # 10 / 5 = 2 (산술 변환으로 실수)
print(Cal.divide(a, c)) # if 분모가 0이라면
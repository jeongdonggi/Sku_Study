import Calculator as cal
import random
# 간단한 게임
class simpleCal:

    def __init__(self, first: int, num: int):
        self.first = first
        self.num = num
        print("숫자 맞추기 게임")
        print("1. 1에서 10 사이의 값을 정한다.")
        print("2. 10에서 10 사이의 랜덤한 값을 보여준다.")
        print("3. 1에서 10 사이의 랜덤한 값을 준다.")
        print("4. 2번과 같은 값을 1번과 3번에서 받은 값과 산술 연산을 이용해 만든다.")
        print("5. 만약 만들지 못한다면 'P'를 누르고 다음 턴으로 가 새로운 랜덤 값을 받는다.")
        print("6. 만들면 게임 끝.")
        print("확인을 하였다면 'p'를 눌러 게임 시작.>")
        x = input()

    def operation(self, op, list):
        if (op == '+'):
            return cal.add(list[0], list[1])
        elif (op == '-'):
            return cal.subtract(list[0], list[1])
        elif (op == '*'):
            return cal.multiply(list[0], list[1])
        elif (op == '/'):
            return cal.divide(list[0], list[1])

    def first_game(self):
        while (True):
            first = int(input("1에서 10 사이의 값을 정하시오.>"))
            if (1 <= first and first <= 10):
                self.first = first
                break

    def middle_game(self):
        while(True):
            print("만들어야 하는 값 : {num}".format(num=self.num))  # 1 에서 10 사이
            result = 0
            list = [self.first]
            number = random.randrange(1,11)
            list.append(number)
            print("가지고 있는 수 {num1}, {num2}".format(num1=list[0], num2=list[1]))

            op = input("연산자를 정하시오.(ex: '+, -, *, / '만들 수 없다면 'p').>")
            if op == 'p':
                continue
            else:
                if (num == self.operation(op, list)):
                    print("정답입니다.")
                    break
                else:
                    print("오답입니다.")
                    continue




if __name__=="__main__":
    first = 0  # 처음 값
    num = random.randrange(1, 11)
    game = simpleCal(first, num)
    game.first_game()  # 게임 시작
    game.middle_game() # 게임 중

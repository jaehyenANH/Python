import random
number = random.randint(1,100)
n = 0

while True :

    t = int(input())

    if t == 0 :
        print("게임을 종료합니다.")
        
        break
    n += 1

    if t == number:
        print(f"#{n}: {t} 정답입니다")

        break

    elif t > number :
        print(f"#{n}: {t}보다 작은 수를 입력해주세요")

    elif t < number :

        print(f"#{n}: {t}보다 큰 수를 입력해주세요")

        continue

    

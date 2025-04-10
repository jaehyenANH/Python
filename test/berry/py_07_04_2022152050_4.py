import math
a = float(input("a를 입력해주세요:"))
b = float(input("b를 입력해주세요:"))
c = float(input("c를 입력해주세요:"))

if a==0 and b==0 and c==0:
    print("모든 수")

# 1차방정식 또는 해가 없는 경우(a=0)
elif a ==0:

# b도 0 이면 c가 0이 아니므로 해가 없다
    if b == 0:
        print("근이 없음")

    else:

    #1차 방정식
        x = -c / b
        print("근: {:.2f}", format(x))

else:

    #2차 방정식
    discriminant = b** - 4 * a * c
    if discriminant > 0:
    

        root1 = (-b + math.sqrt(discriminant)) / (2 * a)

        root2 = (-b - math.sqrt(discriminant)) / (2 * a)

        print("근1: {:.2f}".format(root1))
        print("근2: {:.2f}".format(root2))
        
    elif discriminant == 0:

    # 중근 인 경우
        root = -b / (2 * a)
        print("중근: {:.2f}".format(root))
    else:
    #허근인 경우(실근 없음)
        print("실근 없음")
    

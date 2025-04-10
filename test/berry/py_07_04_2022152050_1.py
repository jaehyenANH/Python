a = int(input("첫번째 숫자를 입력하세요."))
b = int(input("두번째 숫자를 입력하세요."))
c = int(input("세번째 숫자를 입력하세요."))

if a <=0 or b <=0 or c <=0:
    print("모든 숫자는 양수여야합니다.")

if (a+b>c) and (a+c>b) and (b+c>a):
    print("가능.")
else:
    print("불가능.")


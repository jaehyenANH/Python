import math

a = float(input("a 값을 입력하세요: "))
b = float(input("b 값을 입력하세요: "))
c = float(input("c 값을 입력하세요: "))

# 판별식 계산
discriminant = b**2 - 4*a*c

# 두 해 계산
root1 = (-b + math.sqrt(discriminant)) / (2 * a)
root2 = (-b - math.sqrt(discriminant)) / (2 * a)

# 해를 소수점 2째자리까지 출력
print(f"근1: {root1:.2f}")
print(f"근2: {root2:.2f}")

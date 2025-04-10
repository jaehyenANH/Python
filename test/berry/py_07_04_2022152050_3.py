parking_minutes = int(input("주차한 분 수를 입력하세요:"))

discount = input("저공해/경차 등 할인차량인가요? (yes 또는 no):")

fee = 2000
if parking_minutes > 30:
    extra_time = parking_minutes - 30

if extra_time % 10 == 0:
    extra_fee = extra_time //10
else:
    extra_fee = extra_time //10 + 1
    fee += extra_fee * 1000

if discount.lower() == 'yes':
    fee = fee //2
    
    
print("주차요금은", fee, "원입니다.")

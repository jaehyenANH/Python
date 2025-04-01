ymd = 20060326
y = ymd // 10000
d = ymd % 100
m = (ymd // 100) % 100
print(f"생일: {y}년 {m:02d}월 {d}일")


count = 0
for n in range(2, 1001) :
    prime=1
    for d in range(2, n):
        if n % d == 0:
            prime=0
            break
    if(prime==1):
         print(n, end=', ')
         count += 1

print(f"총 [{count}개]")
        

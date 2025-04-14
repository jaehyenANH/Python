bal=0

while True:
    a=int(input())


    if(a==0):
        break
    if(a>0):
        bal+=a
        print(f"입금: {a} 잔액: {bal}")
    else:
        if(a*(-1)>bal):
            print("잔액부족")
        else:
            bal+=a
            print(f"출금: {a*(-1)} 잔액: {bal}")

    

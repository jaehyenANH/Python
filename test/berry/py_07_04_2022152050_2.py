a = input('enter:')
o1, op, o2 = a.split()

o1 = float(o1)
o2 = float(o2)

if   op == '+':
    result = o1+o2
elif op =='-':
    result = o1-o2
elif op =='*':
    result = o1*o2
elif op =='/' :

    if o2 == 0 :
        print("0으로 나눌수 없습니다.")
    else:
        result = o1/o2
    
print(f"{o1} {op} {o2} = {result:.3f}")

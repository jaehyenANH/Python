votes = [0] * 15
total_votes = 0

while True:
    try:
        number = int(input())
    except:
        break
    
    

    if 1 <= number <= 15:
        
        votes[number -1] += 1
        
        total_votes += 1
        
    elif number == 0:
        break

print(f"Total_votes : {total_votes}")

# 득표수와 득표율을 출력 (기호, 득표수, 득표율)
for i in range(15):
    if votes[i] > 0:  # 득표수가 있는 후보만 출력
        rate = (votes[i] / total_votes) * 100
        print(f" # {i + 1:2d}   {votes[i]:7d}  {rate:6.3f}%")

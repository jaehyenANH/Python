dist = 149597870.7
speed = 299792.458

time = dist / speed
minutes = int(time // 60)
seconds = int(time % 60)

print(f"{minutes}분 {seconds}초")

ymd = 220 * 256 * 256 +20 *256 +60
y = ymd // (256*256)
d = ymd % 256
m = (ymd //256) % 256
print(f"ymd(10):{ymd:8d}")
print(f"ymd(16):{ymd:06x}")      
print(f"생일: {y:03d}년 {m:03d}월 {d:03d}일")
print(f"생일: {y:02x}년 {m:02x}월 {d:02x}일")

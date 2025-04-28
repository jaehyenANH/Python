seats = [False] * 20

#좌석 상태 출력 함수
def print_seats():
    for i in range(20):
        print(f"{i+1}[{seats[i]}]", end= " ")

# 메인 프로그램
while True:
    # 좌석 상태 출력
    print_seats()

    #좌석 번호 입력 받기
    seat_input = input("예약할 자리를 입력하세요(0입력하면 종료):")

    if seat_input == '0':
        print("프로그램을 종료합니다.")
        break

    # 입력값이 숫자인지 확인
    if seat_input.isdigit():
        seat_number = int(seat_input)
        
        # 유효한 좌석 번호 (1~20)
        if 1 <= seat_number <= 20:
            if seats[seat_number - 1] == 'O':  # 이미 예약된 좌석
                print(f"좌석 {seat_number}은 이미 예약되어 있습니다.")
            else:  # 좌석 예약
                seats[seat_number - 1] = 'O'
                print(f"좌석 {seat_number}을 예약하였습니다.")
        else:
            print("올바르지 않은 좌석번호입니다.")
    else:
        print("잘못된 입력입니다. 숫자를 입력해주세요.")

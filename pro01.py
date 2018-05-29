
print("=" * 30)
print("1.예금 | 2.출금 |3.잔고 |4.종료 ")
print("=" * 30)

account =0
while True:
    no = input("선택>>")
    if no == "1":
        check = int(input("예금액>>"))
        account += check

    elif no == "2":
        check = int(input("출금액>>"))
        account -= check

    elif no == "3":
        print(account)

    elif no == "4":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못입력하셨습니다.")


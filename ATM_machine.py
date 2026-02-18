def checkPin():
    Pin="1234"
    attempt = 3

    while attempt>0:
        enteredPin=input("Enter your Pin ")

        if enteredPin == Pin:
            print("Correct Pin entered")
            return True
        
        else:
            attempt-=1
            print("Invalid Pin.Enter correct pin")
            print("Attempts left",attempt)

    print("Too many wrong Pins entered!")
    return False


Amount = 10000.0

if checkPin():
    while True:
        print("\n!!__MENU__!!")
        print("1. To Deposit amount")
        print("2. To Credit amount")
        print("3. To Check amount")
        print("4. EXIT")

        choice = input("Enter any Above choices ")

        if choice=='1':
            try:
                depo=int(input("Enter the amount to deposit "))

            except ValueError:
                print("Enter Numbers only")
                continue

            if depo<=0:
                print("Please!Enter a valid deposit")
                continue

            Amount+=depo
            print("SuccessFully Deposited!\nYour current Balance is ",Amount)
            
        elif choice=='2':
            try:
                cred = int(input("Enter the amount to Credit "))

            except ValueError:
                print("Enter Numbers only")
                continue
            
            if cred<=0:
                print("Please!Enter a valid withdrawal Amount")
                continue
            if cred>Amount:
                print("Insufficient Balance!!")
                continue
            Amount-=cred
            print("SuccessFully Withdrawn!\nYour current Balance is ",Amount)

        elif choice=='3':
            print("Your current balance is ",Amount)

        elif choice=='4':
            print("Successfully Existed. Do visit again")
            break

        else:
            print("Enter a valid choice")
print("Answer the following by rating from 1-10")
loan = float(input("How large is the loan? "))
credit_history = int(input("How good is your credit history? "))
income = int(input("How large is your income? "))
down_payment = int(input("How large is your down payment? "))
loan_payment = False

if loan >= 5:
    if credit_history >= 7 and income >= 7:
        loan_payment = True
        print("Congratulations! You qualify for the loan.")
    elif (credit_history >= 7 or income >= 7) and down_payment >= 5:
        loan_payment = True
        print("Congratulations! You qualify for the loan.")
    else:
        print("Sorry, you do not qualify for the loan.")
else:
    if credit_history < 4:
        print("Sorry, you do not qualify for the loan.")
    elif income >= 7 or down_payment >= 7:
        loan_payment = True
        print("Congratulations! You qualify for the loan.")
    elif income >= 4 and down_payment >= 4:
        loan_payment = True
        print("Congratulations! You qualify for the loan.")
    else:
        print("Sorry, you do not qualify for the loan.")
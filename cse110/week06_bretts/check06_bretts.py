# Loan size: 8, Credit: 7, Income: 8, Down Payment: 1, Decision: "yes"
# Loan size: 5, Credit: 2, Income: 7, Down Payment: 5, Decision: "yes"
# Loan size: 8, Credit: 2, Income: 8, Down Payment: 3, Decision: "no"
# Loan size: 2, Credit: 4, Income: 1, Down Payment: 7, Decision: "yes"
# Loan size: 4, Credit: 5, Income: 5, Down Payment: 3, Decision: "no"


print()
print("Enter a rating from 1–10 on the following:")
print()
loan = int(input("How large is the loan? "))
credit = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down = int(input("How large is your down payment? "))

loan_approved = False

if loan >= 5:
    if credit >= 7 and income >= 7:
        loan_approved = True
    elif credit >= 7 or income >= 7:
        if down >= 5:
            loan_approved = True
        else:
            loan_approved = False
    else:
        loan_approved = False
else:
    if credit < 4:
        loan_approved = False
    else:
        if income >= 7 or down >= 7:
            loan_approved = True
        elif income >= 4 and down >= 4:
            loan_approved = True
        else:
            loan_approved = False

if loan_approved:
    print()
    print("You a get a loan...we now own you!")
    print()
else:
    print()
    print("No loan for you!")
    print()

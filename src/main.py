from loan import Loan

my_loan = Loan(principal=200000, interest_rate=0.045, term=360)
print(my_loan.monthly_payment())
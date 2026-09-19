class Loan:
    def __init__(self, principal, interest_rate, term):
        self.principal = principal
        self.interest_rate = interest_rate
        self.term = term

    def monthly_payment(self):
        monthly_rate = self.interest_rate / 12
        payment = self.principal * monthly_rate / (1-(1 + monthly_rate) ** -self.term)
        return round(payment, 2)
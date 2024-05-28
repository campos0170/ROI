
class ROI():

    """ 
    The ROI class calculates the return on investment on a property investment 

    ATTRIBUTES:

    - interest, expects an integer or a float.
    - loan, expects an integer.
    - income, expects a dictionary.
    - expenses, expects a dictionary.
    - down_payment, expects an integer.
    - closing_cost, expects an integer.
    - rehab_b, expects an integer
    - other, expects an integer and involves any other costs associated with the initial investment.
    - time, total time of the loan.
    - interest, interest accrued on the loan.
    - mortgage_payment, monthly mortgage payment.
    

    METHODS:

    The income and expenses are calculated as a monthly basis.

    - getIncome, takes in all the sources of income associated with the property.
    - getExpenses, takes in all of the expenses associated with the property.
    - cashFlow, calculates the monthly cash flow
    - cas_on_cash_roi, calculates the final Return Of Investment (ROI).
    - showIncome, delineates the income sources and corresponding amounts for the property.
    - showExpenses, delineates the expenses and amount corresponding to the property.
    
    
    """
    
    def __init__(self,loan,interest,down_payment,closing_cost,rehab_b,other = 0,income={},expenses={},time=30):
        self.interest = interest/100
        self.time = time # We set the standard time for the lifetime of the loan to be 30 yrs, this can be altered if needed.
        self.totalIncome_ = 0 # Initial counter for the total income.
        self.totalExpense_ = 0 # Initial counter for the total expense.
        self.loan = loan
        self.income = income
        self.expenses = expenses
        self.down_payment = down_payment
        self.closing_cost  = closing_cost
        self.rehab_b = rehab_b
        self.other = other # This attribute corresponds to any misc. amount associated with the initial investment.
        principal = self.loan - self.down_payment
        self.mortgage_payment = principal*(self.interest/12)/(1-(1+self.interest/12)**(-12*self.time))

    def getIncome(self):
        source = input("Please enter source of income: ")
        amount = int(input("Please enter the amount in dollars: "))
        self.income[source] = amount
        self.totalIncome_ += amount
            
    def getExpenses(self):
        expense = input("Please enter your expenses: ")
        amount = int(input("Please enter the amount in dollars: "))
        self.expenses[expense] = amount
        self.totalExpense_+= amount
    
    def cashFlow(self):
        cash = self.totalIncome_-self.totalExpense_
        return cash
        
    def cash_on_cash_roi(self):
        total_invest = self.down_payment + self.closing_cost + self.rehab_b + self.other
        annual_cash_flow = 12 * (self.totalIncome_ - (self.totalExpense_+self.mortgage_payment))
        roi_ = (annual_cash_flow/total_invest)*100
        print (f"Your return on investment is: {round(roi_,2)} %")
        
    def showIncome(self):
        for key,value in self.income.items():
            print("Income:\n")
            print(f"{key}: {value}")
            
    def showExpenses(self):
        print("Expenses:\n")
        for key,value in self.expenses.items():
            
            print(f"{key}: {value}")
    




brickell_property = ROI(200e3,5,40e3,3e3,7e3)



# Create a function to run our Object.

def run():

    while True:

        response = input("What would you like to do today? a. add Expenses b. add Income c. quit ")
        responses = ['a','b','c']
        if response == "c".lower():
            brickell_property.showExpenses()
            print('\n')
            brickell_property.showIncome()
            print('\n')
            brickell_property.cash_on_cash_roi()
            break

        elif response.lower() not in responses:
            print("Please enter a valid option")

        elif response.lower() == 'a':
            brickell_property.getExpenses()

        elif response.lower() == 'b':
            brickell_property.getIncome()

run()


            


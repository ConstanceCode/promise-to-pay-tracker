
from datetime import date, datetime, timedelta

#Variables needed
Name: input("Enter client name ")
Number: int(input("Please enter client phone number eg 07******* "))
Loan_amount: int(input("Please enter client's loan amount "))
Loan_repayment_period: int(input("How many months is the loan being paid? "))
Disbursal_date : date(input("Enter date of disbursal"))

#Calculations and Functions needed
def Installment_amount ():
    for installment in Installment_amount:
        i = Loan_amount/Loan_repayment_period
        return i

def Installments_paid ():
    for ins in Installments_paid:
        ns = Installment_amount * 

def Loan_remaining():

    for amount in Loan_remaining:
        a = Loan_amount - Installments_paid
        return a

def Total_paid():
    for totals in Total_paid:
        tp = Installments_paid
        return tp

def Arrear_days():
    
    days = date.today() - Disbursal_date
    return days

def Due_date_start():
    Start_date = Disbursal_date + timedelta(days=14) 
    return Start_date
    
def On_schedule():
    if Arrear_days == 0:
        print("Good standing")
    else:
        print("Bad standing")

def Arrear_amount():

#    Loan_amount -
#)


    
def ptp_reminder():
    for reminders in reminder:
        return

def calculate_arrear_amount():
    for arrears in arrear_amount:
        y = Loan_amount - expected_payment_upto_that_point,
        return(y)


client = {
    'Name': Name,
    'Number': Number,
    'LoanAmount': Loan_amount,
    'Days': Arrear_days,
    'TotalPaid': Total_paid,
    'LoanBalance':Loan_remaining
}
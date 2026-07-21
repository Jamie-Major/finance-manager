import json
import os

def read_transaction_file (file):

    if os.path.exists(file):
        with open(file, 'r', encoding = 'utf-8') as f:
            open_file = json.load(f)
            for x in open_file:
                print(list(x)[0],':', x.get('description'))
                print(list(x)[1],':', x.get('income_or_expense'))
                print(list(x)[2],':', x.get('amount'))
                print()
    else:
        print('NO TRANSACTIONS HAVE BEEN RECORDED')

def get_total (file):

    total_income = 0
    total_expense = 0
    total = 0

    if os.path.exists(file):
        with open(file, 'r', encoding = 'utf-8') as f:
            open_file = json.load(f)
            for x in open_file:
                if x['income_or_expense'] == 'income':
                    total_income = total_income + float(x.get('amount'))
                if x['income_or_expense'] == 'expense':
                    total_expense = total_expense + float(x.get('amount'))
            total = total_income - total_expense
            return print(f'The total amount in your account is: £{total:.2f}')
    else:
        print('NO TRANSACTIONS HAVE BEEN RECORDED')

def get_monthly_review (file):

    if os.path.exists(file):
        with open(file, 'r', encoding = 'utf-8') as f:
            open_file = json.load(f)
            month_date = input('Please enter the month and year you would like see (MM/YYYY): ')
            month_list =[]
            for x in open_file:
                if x['date'][3:] == month_date:
                    month_list.append(x)
            if month_list == []:
                print('THERE IS NO DATA FOR THE MONTH YOU HAVE SELECTED')
            for y in month_list:
                print(list(y)[0],':', y.get('description'))
                print(list(y)[1],':', y.get('income_or_expense'))
                print(list(y)[2],':', y.get('amount'))
                print()
    else:
        print('NO TRANSACTIONS HAVE BEEN RECORDED')
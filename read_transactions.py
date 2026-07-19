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

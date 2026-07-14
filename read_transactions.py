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
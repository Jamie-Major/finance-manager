from datetime import datetime
import json
import os

class transaction:
    def __init__(self, description, income_or_expense, amount):
        self.description = description
        self.income_or_expense = income_or_expense
        self.amount = amount
        self.date = datetime.now().strftime('%d/%m/%Y')

    #turns a transaction object into a dictionary seperately so the amount is set to two decimal places (eg: 16.37)
    def transaction_dictionary(self):
        dictionary_self ={'description': self.description,
                          'income_or_expense': self.income_or_expense,
                          'amount': f'{self.amount:.2f}',
                          'date': self.date}
        return dictionary_self

def save_transaction(t):

    filename = 'transaction_history.json'

    if os.path.exists(filename):
        with open(filename, 'r', encoding = 'utf-8') as f:
            transaction_list = json.load(f)
    else:
        transaction_list = []

    transaction_list.append(t.transaction_dictionary())

    with open(filename, 'w', encoding = 'utf-8') as f:
        json.dump(transaction_list, f, ensure_ascii= False, indent = 4)

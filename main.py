from transactions import transaction, save_transaction
def main ():

    print('================================')
    print('Welcome to your finance manager')
    print('================================')

    menu_selection = 0

    while menu_selection != 6:

        try:

            menu_selection = int(input('''Please select an option:
            1. Add Income
            2. Add Expense
            3. View Transactions
            4. View Balance
            5. Monthly Report
            6. Exit
            '''))

        except ValueError:

            print('INVALID INPUT PLEASE ENTER CORRECTLY')
            continue

        #user selects Add Income
        if menu_selection == 1:
            description = input('Please enter the transaction description')
            income_or_expense = input('Is your transaction an income or expense?')
            amount = int(input('Please enter the total'))

            t = transaction(description, income_or_expense, amount)

            save_transaction(t)

        #user selects Add Expense
        elif menu_selection == 2:
            print('Add Expense feature coming soon')

        #user selects View Transaction
        elif menu_selection == 3:
            print('View Transaction feature coming soon')

        #user selects View Balance
        elif menu_selection == 4:
            print('View Balance feature coming soon')

        #user selects Monthly Report
        elif menu_selection == 5:
            print('Monthly Report feature coming soon')
        else:
            print('INVALID INPUT PLEASE ENTER CORRECTLY')

    print('Have a nice day!')

main()
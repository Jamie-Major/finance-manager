from transactions import transaction, save_transaction
def main ():

    print('================================')
    print('Welcome to your finance manager')
    print('================================')

    menu_selection = 0

    while menu_selection != 5:

        try:

            menu_selection = int(input('''Please select an option:
            1. Add Income / Exepense
            2. View Transactions
            3. View Balance
            4. Monthly Report
            5. Exit
            '''))

        except ValueError:

            print('INVALID INPUT PLEASE ENTER CORRECTLY')
            continue

        #user selects Add Income / Expense
        if menu_selection == 1:
            description = input('Please enter the transaction description')
            income_or_expense = input('Is your transaction an income or expense?')

            while True:
                try:

                    amount = float(input('Please enter the total: £'))
                    break
                except:
                    print('INVALID INPUT PLEASE ENTER CORRECTLY')


            t = transaction(description, income_or_expense, amount)

            save_transaction(t)

        #user selects View Transaction
        elif menu_selection == 2:
            print('View Transaction feature coming soon')

        #user selects View Balance
        elif menu_selection == 3:
            print('View Balance feature coming soon')

        #user selects Monthly Report
        elif menu_selection == 4:
            print('Monthly Report feature coming soon')

        #user selects Exit
        elif menu_selection == 5:
            print('Have a nice day!')
            return
        else:
            print('INVALID INPUT PLEASE ENTER CORRECTLY')

main()
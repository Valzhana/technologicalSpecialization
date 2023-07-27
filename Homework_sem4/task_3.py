# Задание 3.

# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


balance = 0
DIVIDER = 50
WITHDRAWAL_PERCENT = 0.015
COMMISSION_MAX = 600
COMMISSION_MIN = 30
OPERATION_PERCENT = 0.03
NONE_TAX_AMOUNT = 5000000
count = 0
TAX = 0.1
operation = []


def get_commission(withdrawal):
    global balance
    if (withdrawal * WITHDRAWAL_PERCENT) <= COMMISSION_MIN:
        balance -= withdrawal + COMMISSION_MIN
    elif (withdrawal * WITHDRAWAL_PERCENT) >= COMMISSION_MAX:
        balance -= withdrawal + COMMISSION_MAX
    else:
        balance -= withdrawal * WITHDRAWAL_PERCENT
    return balance


def deposit_account() -> None | object:
    global balance, count, TAX, operation, NONE_TAX_AMOUNT, DIVIDER
    print(f'Balance: {balance}')
    deposit = int(input('Deposit banknotes in multiples of 50$: '))
    if count % 3 != 0 or count == 0:
        if deposit % DIVIDER == 0 and balance < NONE_TAX_AMOUNT:
            if (balance + deposit) >= NONE_TAX_AMOUNT:
                print('Wealth tax 10%')
                balance += deposit
                balance -= balance * TAX
            else:
                balance += deposit
            count += 1
            print(f'Balance: {balance}')
            operation.append(f'Replenishment: {deposit}$\n')
        elif deposit % DIVIDER == 0 and balance >= NONE_TAX_AMOUNT:
            balance += deposit
            balance -= balance * TAX
            count += 1
            print(f'Wealth tax 10%\nBalance: {balance}')
            operation.append(f'Replenishment: {deposit}$\n')
        else:
            count += 1
            print('Replenishment amounts are available in multiples of 50$')
    elif count >= 3 and count % 3 == 0:
        if deposit % DIVIDER == 0 and balance >= NONE_TAX_AMOUNT:
            balance += deposit
            balance -= balance * TAX
            balance += balance * OPERATION_PERCENT
            count += 1
            print(f'Accrued 3%\nWealth tax 10%\nBalance: {balance}')
            operation.append(f'Replenishment: {deposit}$\n')
        elif deposit % DIVIDER == 0 and balance < NONE_TAX_AMOUNT:
            balance += deposit
            balance += balance * OPERATION_PERCENT
            count += 1
            print(f'Accrued 3%\nBalance: {balance}')
            operation.append(f'Replenishment: {deposit}$\n')
        else:
            count += 1
            print('Replenishment amounts are available in multiples of 50$')
    return select_operation()


def withdraw_money() -> None | object:
    global balance, WITHDRAWAL_PERCENT, count, TAX, operation, COMMISSION_MIN, COMMISSION_MAX, NONE_TAX_AMOUNT, DIVIDER
    print(f'Balance: {balance}\nCommission 1.5%')
    withdrawal = int(input('Withdraw banknotes in multiples of 50$: '))
    if (count % 3 != 0 or count == 0) and balance > withdrawal:
        if withdrawal % DIVIDER == 0 and balance < NONE_TAX_AMOUNT:
            balance = get_commission(withdrawal)
            count += 1
            print(f'Balance: {balance}')
            operation.append(f'Withdrawal: {withdrawal}$\n')
        elif withdrawal % DIVIDER == 0 and balance >= NONE_TAX_AMOUNT:
            balance = get_commission(withdrawal)
            balance -= balance * TAX
            count += 1
            print(f'Wealth tax 10%\nBalance: {balance}')
            operation.append(f'Withdrawal: {withdrawal}$\n')
        else:
            count += 1
            print('Replenishment amounts are available in multiples of 50$')
    elif count >= 3 and count % 3 == 0:
        if withdrawal % DIVIDER == 0 and balance >= NONE_TAX_AMOUNT:
            balance = get_commission(withdrawal)
            balance -= balance * TAX
            balance += balance * OPERATION_PERCENT
            count += 1
            print(f'Accrued 3%\nWealth tax 10%\nBalance: {balance}')
            operation.append(f'Withdrawal: {withdrawal}$\n')
        elif withdrawal % DIVIDER == 0 and balance < NONE_TAX_AMOUNT:
            balance = get_commission(withdrawal)
            balance += balance * OPERATION_PERCENT
            count += 1
            print(f'Accrued 3%\nBalance: {balance}')
            operation.append(f'Withdrawal: {withdrawal}$\n')
    else:
        if balance <= withdrawal:
            print('Replenish the balance')
        else:
            print('Replenishment amounts are available in multiples of 50$')
            count += 1
    return select_operation()


def select_action(num: str) -> object | str:
    if num == '1':
        return deposit_account()
    elif num == '2':
        return withdraw_money()
    else:
        return 'Completed'


def select_operation() -> str:
    while True:
        select = input('Select operation:\n'
                       '1: Deposit\n'
                       '2: Withdraw\n'
                       '3: Exit\n')
        if not select.isdigit() or select > '3':
            print('Select numbers from 1 to 3: ')
            continue
        else:
            break

    return select


def main():
    flag = select_operation()
    while flag < '3':
        check = select_action(flag)
        if check is not None:
            flag = check
        else:
            flag = select_operation()
    else:
        print("Completed")
        print(*operation)
    return


main()

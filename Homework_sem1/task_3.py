# Задание 3. Напишите код, который запрашивает число и сообщает является ли оно простым
#       или составным. Используйте правило для проверки: “Число является простым,
#       если делится нацело только на единицу и на себя”.
#       Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

MIN_INPUT = 0
MAX_INPUT = 100000

while True:
    input_number = int(input('Enter the number from 0 to 100000: '))
    if not MIN_INPUT <= input_number <= MAX_INPUT:
        print('Enter the number from 0 to 100000: ')
        continue
    elif input_number == 0 or input_number == 1:
        print('The number is neither prime nor composite')
        continue
    else:
        count = 0
        for i in range(1, input_number):
            if input_number % i == 0:
                count += 1
        if count >= 3:
            print(f'The number {input_number} is composite ')
        else:
            print(f'The number {input_number} is prime')

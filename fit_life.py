# Объявление констант.
WATER_PER_KG = 30
ML_PER_L = 1000
# Запрос данных пользователя
user_name = input('Добро пожаловать в приложение FITLife. Как я могу к вам обращаться? ')
user_age = int(input('Укажите ваш возраст. '))  
user_weight = float(input('Укажите пожалуйста ваш вес в кг. '))
user_height = float(input('Укажите пожалуйста ваш рост в метрах, используя точку. (Для примера - 1.75) '))
# расчёт индекса массы тела.
bmi = round((user_weight / (user_height ** 2)), 1)
# расчёт нормы воды в литрах.
water_l = (user_weight * WATER_PER_KG) / ML_PER_L
# Вывод отчёта.
print('\n' * 20)
print("=" * 50)
print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l} л. в день')
print()
print('Расчет окончен. Будьте здоровы!')   
print("=" * 50)      

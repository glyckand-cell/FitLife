# Объявление констант.
WATER_PER_KG = 30
ML_PER_L = 1000


# Объявление функций для проверки значений
def get_name():
    """Запрашивает и проверяет имя пользователя."""
    while True:
        name = input('Добро пожаловать. Введите своё имя: ')
        name = name.strip()
        if name != "":
            return name
        else:
            print('Ошибка: Имя не может быть пустым. Попробуйте снова.')


def get_age():
    """Запрашивает и проверяет возраст пользователя."""
    while True:
        try:
            age = int(input('Укажите ваш возраст: '))
            if 0 < age < 130:
                return age
            else:
                print('Ошибка: Возраст должен быть от 1 до 129 лет. '
                      'Попробуйте снова.')
        except ValueError:
            print('Ошибка: Введите целое число. Попробуйте снова.')


def get_weight():
    """Запрашивает и проверяет вес пользователя."""
    while True:
        try:
            weight = float(input('Укажите ваш вес в кг, используя точку: '))
            if 10 <= weight <= 500:
                return weight
            else:
                print('Ошибка: Вес должен быть от 10 до 500 кг. '
                      'Попробуйте снова.')
        except ValueError:
            print('Ошибка: Введите число (используйте точку). '
                  'Попробуйте снова.')


def get_height():
    """Запрашивает и проверяет рост пользователя."""
    while True:
        try:
            height = float(input('Укажите ваш рост в метрах: '))
            if 0.5 <= height <= 2.5:
                return height
            else:
                print('Ошибка: Рост должен быть от 0.5 до 2.5 метров. '
                      'Попробуйте снова.')
        except ValueError:
            print('Ошибка: Введите число (используйте точку). '
                  'Попробуйте снова.')


def get_year_word(user_age):
    """Склонение слова 'год' по возрасту"""
    last_number = user_age % 10
    last_two = user_age % 100

    if 11 <= last_two <= 14:
        return "лет"
    if last_number == 1:
        return "год"
    elif 2 <= last_number <= 4:
        return "года"
    else:
        return "лет"


# Запрос данных пользователя
user_name = get_name()
user_age = get_age()
user_weight = get_weight()
user_height = get_height()
year_word = get_year_word(user_age)

# Расчёт индекса массы тела
bmi = round((user_weight / (user_height ** 2)), 1)

# Расчёт нормы воды в литрах
water_l = (user_weight * WATER_PER_KG) / ML_PER_L

# Вывод отчёта
print('\n' * 20)
print("=" * 50)
print(f'Отчет для пользователя: {user_name} ({user_age} {year_word}.)')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l:.1f} л в день')
print()
print('Расчет окончен. Будьте здоровы!')
print("=" * 50)

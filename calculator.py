import sys

# Функция для вычисления степени числа
def power(base, exponent):
    return base ** exponent

if __name__ == "__main__":
    # Проверяем, были ли переданы аргументы командной строки
    if len(sys.argv) != 3:
        print("Использование: calculator.py <основание> <степень>")
        sys.exit(1)

    try:
        # Преобразуем аргументы командной строки в числа с плавающей точкой
        base = float(sys.argv[1])
        exponent = float(sys.argv[2])
    except ValueError:
        # Если аргументы невозможно преобразовать в числа, выводим сообщение об ошибке
        print("Неверный ввод. И основание, и показатель степени должны быть числами.")
        sys.exit(1)

    # Вычисляем результат вызовом функции power
    result = power(base, exponent)
    print(f"Результат: {result}")
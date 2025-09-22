try:
    num_1 = float(input("Введите первое число: "))
    num_2 = float(input("Введите второе число: "))
    division_result = num_1 / num_2
except ValueError:
    print("Ошибка! Введите число")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
else:
    print(f"Результат: {division_result}")
finally:
    print("Программа завершена.")

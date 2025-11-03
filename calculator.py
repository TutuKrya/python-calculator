def input_number(promt):
    while 1:
        try:
            return float(input(promt))
        except ValueError:
            print("Ошибка ввода числа, возможно вы ввели текст")

def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2, None
    elif operation == "-":
        return num1 - num2, None
    elif operation == "*":
        return num1 * num2, None
    elif operation == "/":
        try:
            return num1 / num2, None
        except ZeroDivisionError:
            return None, "деление на ноль невозможно"
    elif operation == "**":
        return num1 ** num2, None
    elif operation == "//":
        return num1 // num2, None
    elif operation == "%":
        return num1 % num2, None
    else:
        return None, "неверная операция"

def format_result(num):
    if num == int(num):
        return int(num)
    return num

def do(history, action):
    if action == "yes":
        num1 = input_number("Введите первое число: ")
        print("Доступные операции: +, -, *, /, **, //, %")
        operation = input("Введите операцию: ")
        num2 = input_number("Введите второе число: ")

        result = calculate(num1, num2, operation)
        if result[0] is not None:
            print(f"Результат: {format_result(result[0])}")
            history.append(f"{format_result(num1)} {operation} {format_result(num2)} = {format_result(result[0])}")
        else:
            print(f"Произошла ошибка при вычислении - {result[1]}")
    elif action == "history":
        if len(history) == 0:
            print("История операций отсутсвует")
        else:
            print("\n" + "История операций:")
            for i in range(len(history)):
                print(f"{i + 1}.", history[i])
    elif action == "clear":
        history.clear()
        print("История успешно удалена")
    elif action == "exit":
        pass
    else:
        print('Неизвестная команда. Доступные: yes, exit, history, clear')

history = []
action = "yes"
while action != "exit":
    do(history, action)
    action = input("Продолжить? (yes, exit, history, clear): ")

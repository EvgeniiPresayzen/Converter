# ---------------- ФУНКЦИЯ ПЕРЕВОДА ИЗ РИМСКОГО ЧИСЛА В АРАБСКОЕ -------------------------------
def convert_roma_arab():
    roma = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    list = []
    j = 0
    replay = 0
    summa = 0
    # создание списка с разбиением символов и их вознесения в верхний регистр
    number = input("Введите римское число [от I до MMMCMXCIX]: ")
    list += number.upper()
    # перевод элементов списка в числа
    try:
        list = [roma[x] for x in list]
    except KeyError:
        print("Недопустим-ый/-е символ/-ы. Допустимые символы M, D, C, L, X, V, I!")
        return convert_roma_arab()
    # конвертирование в одно число
    while j <= len(list)-1:
        try:
            # проверка повторения одного символа подряд
            if replay > 2:
                print("Число повторов одного символа превышает допустимое значение!")
                return convert_roma_arab()
    # проверка елементов из списка и присвоение им нужной роли
            # M, C, X, I
            if list[j] == 1 or list[j] == 10 or list[j] == 100 or list[j] == 1000:
                # проверка на вычитание числа
                if list[j+1] == list[j] * 5 or list[j+1] == list[j] * 10:
                    # проверка на повторении меньшей цифры слева от большой
                    if replay > 0:
                        print("Повторения меньшей цифры не допускаются перед большей!")
                        return convert_roma_arab()
                    summa -= list[j]
                # проверка на правильную последовательность римских чисел
                elif list[j+1] > list[j] * 10:
                    print("Ошибка последовательности символом. IV, IX, XL, XC, CD, CM")
                    return convert_roma_arab()
                # иначе происходит сложение числа
                else:
                    summa += list[j]
                # счетчик повтора символов I, X, C, M
                if list[j] == list[j+1]:
                    replay += 1
                else:
                    replay = 0
            # D, L, V
            else:
                # проверка на правильную последовательность римских чисел
                if list[j] < list[j+1]:
                    print("Ошибка последовательности символом. M -> D -> C -> L -> X -> V -> I")
                    return convert_roma_arab()
                # проверка на повторимость чисел
                elif list[j] == list[j+1]:
                    print("Число повторов одного символа превышает допустимое значение!")
                    return convert_roma_arab()
                else:
                    summa += list[j]
        except IndexError:
            summa += list[j]
        finally:
            j += 1
    # вывод результата
    print("Арабское число: " + str(summa))
    return questions()


# ---------------- ФУНКЦИЯ ПЕРЕВОДА ИЗ АРАБСКОГО ЧИСЛА В РИМСКОЕ -------------------------------
def convert_arab_roma():
    roma = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I', ' ']
    arab = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1, 0]
    i = 0
    result = ''
    number = int(input("Введите арабское число [от 1 до 3999]: "))
    # проверка числа на допустимый диапазон
    if number >= 4000 or number <= 0:
        return print('Превышен допустимый диапазон чисел!')
    # переобразование арабского числа в римское
    while i < len(arab)-1:
        while number >= arab[i]:
            result += roma[i]
            number -= arab[i]
        i += 1
    print("Римское число: " +result)
    return questions()


# ------------------ ФУНКЦИЯ ДЛЯ ВЫБОРА КОНВЕРТИРОВАНИЯ ----------------------------------------
def questions():
    print('Введите (0) для перевода из Римского числа в арабское')
    print('Введите (1) для перевода из Арабского числа в Римское')
    print('Введите (exit) для выхода из программы')
    case = input('Ваш ответ: ')
    if case == '0':
        return convert_roma_arab()
    elif case == '1':
        return convert_arab_roma()
    elif case.upper() == 'EXIT':
        return print('Конец работы конвертера!')
    else:
        return print('Неверное значение!')


questions()


import math
from string import ascii_letters as asc


# **********************************************************************************************************************
# 1. Напишите программу на Python для проверки, является ли число простым
# **********************************************************************************************************************

def is_simpre_number(num: int) -> str:
    """
    Проверяет, является ли число простым
        :param num: Число, которое необходимо проверить
        :return: Строка о том, является число простым или нет
    """
    # делаем проверку на корректность переданного входного параметра
    if isinstance(num, int) and num > 0:
        # создаём пустой список, куда будем помещать делители числа, при делении на которые остаток равен 0
        lst = []
        # проходимся циклом по последовательности начиная с 1, т.к. деление на 0 математически запрещено
        for i in range(1, num):
            # делаем проверку на остаток деления
            if num % i == 0:
                # если остаток от деления равен нулю, то добавляем число в список
                lst.append(i)
            # проверяем длину списка: если больше 1 (число является простым, если имеет больше 2-х делителей
            # (единицы и самого себя), то вернем надпись о том, что число не является простым.
            # Т.к. мы в range() берём просто num, то это число не включается в последовательность, поэтому проверка
            # выполняется именно на > 1)
            if len(lst) > 1:
                return 'Число не является простым'
        # если по проверке условия длины списка мы не вышли из цикла, возвращаем надпись о том, что число простое
        return 'Число является простым'
    else:
        return 'Введите корректное целое число > 0'


# **********************************************************************************************************************
# 2. Напишите программу на питоне, которая посчитает количество различных(без учета регистра) букв в файле.
# **********************************************************************************************************************
# Тут двусмысленность возникла: посчитать количество каждой уникальной буквы в тексте или посчитать кол-во уникальных
# букв в тексте? Не беда, сделаем оба варианта :)

# Для начала запишем в файл рандомный текст, состоящий их русских и английских букв
with open('my_file.txt', 'w', encoding='utf-8') as file:
    data = """
    Лучше один раз увидеть, чем сто раз услышать — применимо для любого современного продукта. Сейчас у всех
    есть тест-драйвы, пробники и триалы.

    Банки — не исключение. Что можем порекомендовать изучить перед оформлением карточки:

    — Сравнить кешбэк. Тут все просто: сэкономил — значит заработал;
    — Проверить удобство переводов. Как быстро приходят, какой размер комиссии;
    — В целом работу онлайн-банка.

    ВТБ выпустил приложение, которое можно запустить и протестировать, даже если вы не клиент банка — «ВТБ Онлайн Лайт».
    План такой: вы устанавливаете его, понимаете насколько это удобно и принимаете решение. Можно сразу в режиме теста
    попробовать оплатить мобильную связь, например. Также после регистрации можно выпустить бесплатную карту с кешбэком
    и отслеживать статус заявки. С кешбэком и удобствами там, кстати, тоже все хорошо.

    «ВТБ Онлайн Лайт» можно запустить на iOS, Android и ПК. """
    file.write(data)


def calculate_unique_letters_in_text():
    """
    Считает кол-во количество каждой уникальной буквы в тексте и кол-во уникальных букв в тексте и выводит 2
    соответствующие строки
    """
    # для русского текста будем использовать соответственно русский алфавит, а английские буквы возьмем из встроенной
    # библиотеки
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    # открываем файлик на чтение и достаём из него строку
    with open('my_file.txt', 'r', encoding='utf-8') as txt_file:
        text = txt_file.read().lower()
    # создаём пустой словарь, в котором будем хранить полученные данные: буква - кол-во
    letters_counter_dict = {}
    # проходимся по списку букв в тексте
    for letter in text:
        # если буква находится в русско-английском букваре, то идём дальше (отсекаем не_буквы)
        if letter in alphabet + asc:
            # если буквы нет в словаре (key), добавим её, установив значение равное единице
            if letter not in letters_counter_dict:
                letters_counter_dict[letter] = 1
            # иначе увеличим счетчик (value) на единицу
            else:
                letters_counter_dict[letter] += 1
    print(f'Общее кол-во уникальных букв = {len(letters_counter_dict)}' + "\n" +
          f'Кол-во каждой уникальной буквы в тексте: {letters_counter_dict}')


# **********************************************************************************************************************
# 3.1 Можете написать функцию для генерации такой пирамиды? (пирамида - песочные часы)
# **********************************************************************************************************************

def get_stars_sequence(count: int):
    """
    Выводит песочные часы из звёздочек
        :param count: Число звёздочек в основании песочных часов
    """
    # На каждом уровне песочных часов убирается по 2 звездочки, поэтому для четного кол-ва звездочек в основании
    # песочных часов выведем предупреждение
    if count % 2 == 0:
        print('Так как число четное, на стыке будут красоваться по 2 звезды с каждой стороны')
    # переменная, которая будет заполнять пробелы
    fill = 0
    # переменная, которая отвечает за возврат песочных часов на обратной стороне к изначальному кол-ву звездочек
    length = count
    # этот цикл будет бегать до тех пор, пока не нарисует 1 или 2 звезды (зависит от четности/нечетности переданного
    # параметра)
    while count > 0:
        print(' ' * fill + '*' * count)
        count -= 2
        fill += 1
    # этот цикл будет бегать после первого и нарисует обратную сторону песочных часов
    while count < length:
        count += 2
        fill -= 1
        print(' ' * fill + '*' * count)


# **********************************************************************************************************************
# 3.2 Можете написать функцию для генерации такой пирамиды? (пирамида - бабочка)
# **********************************************************************************************************************
def get_reverse_stars_sequence(width: int):
    """
    Выводит пирамиду из звёздочек
        :param width: Ширина "рисунка"
    """
    # На каждом уровне обратной пирамиды добавляется по 2 звездочки, поэтому для нечетного кол-ва звездочек в основании
    # пирамиды выведем предупреждение
    if width % 2 != 0:
        print('Так как число нечетное, одной звёздочки будет не хватать')
    fill = 1
    # здесь алгоритм такой же, как и в прошлой задаче: заполняем на каждом проходе цикла нужное кол-во звёздочками,
    # а остальное пробелами. Затем запускаем и наслаждаемся :-)
    while fill < math.floor(width / 2):
        space_count = width - 2 * fill
        print('*' * fill + ' ' * space_count + '*' * fill)
        fill += 1
    while fill >= 0:
        space_count = width - 2 * fill
        print('*' * fill + ' ' * space_count + '*' * fill)
        fill -= 1

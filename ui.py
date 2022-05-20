
def init():
    surname = input("Ввудите Фамилию: ")
    name = input('Введите Имя: ')
    phone = input('Введите телефон: ')
    note = input('Введите описание: ')
    orient = input('Выберите метод заполнения (1 - вертикальный, 2 - горизонтальный): ')
    return(surname, name, phone, note, orient)
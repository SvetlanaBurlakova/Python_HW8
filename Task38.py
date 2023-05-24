"""Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести 
имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных"""

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Изменить данные абонента в справочнике\n"
          "6. Удалить абонента\n"
          "7. Сохранить справочник в текстовом формате\n"
          "8. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')
            
def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phone.txt')
    while (choice != 8):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            print(find_by_name(phone_book, name))
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_txt('phone.txt', phone_book)
        elif choice == 5:
            last_name = get_search_name()
            message = find_by_name(phone_book, last_name)
            print(message)   
            if message != 'Такой абонент отсутвует':
                print(change(phone_book,last_name))
        elif choice == 6:
            last_name = get_search_name()
            message = find_by_name(phone_book, last_name)
            print(message)   
            if message != 'Такой абонент отсутвует':
                phone_book = delete(phone_book,last_name)
            print(*phone_book)
        elif choice == 7:
            file_name = get_file_name()
            write_txt(file_name, phone_book)            
        choice = show_menu()

def print_result(phone_book):
    for item in phone_book:
        for key,value in item.items():
            print(f'{key}:{value}',end='\t')
        print()

def get_new_user():
    print('Введите информацию для добавления записи в справочник')
    last_name = input('Введите фамилию:')
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    description = input('Введите описание: ')
    user_data = f'{last_name},{name},{phone},{description}'
    return user_data

def get_search_name():
    name = input('Введите фамилию для поиска абонента: ')
    return name

def get_search_number():
    phone = input('Введите номер телефона для поиска абонента: ')
    return phone    

def get_file_name():
    file_name = input('Введите имя файла для сохранения справочника: ')
    return file_name
  
def find_by_name(data: list, last_name: str) -> str:
    for el in data:
        if el.get("Фамилия") == last_name:
            return f'{last_name}, {el.get("Имя")}, {el.get("Телефон")}, {el.get("Описание")}'
    return "Такой абонент отсутвует"
    
def find_by_number(data: list, phone_number: str) -> str:
    for el in data:
        if el.get("Телефон") == phone_number:
            return f'{el.get("Фамилия")}, {el.get("Имя")}'
    return "Такой абонент отсутвует"

def add_user(data: list, user_data: str):
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    record = dict(zip(fields, user_data.split(',')))
    data.append(record)
    return data

def change(phone_book,last_name):
    print('Выберите из списка параметр для изменения:\n'
          '1. Изменить Имя абонента\n'
          '2. Изменить Фамилию абонента\n'
          '3. Изменить Телефон абонента\n'
          '4. Изменить описание\n')
    change_choice = int(input())
    if change_choice == 1:
        new_name = input('Введите новое Имя абонента: ')
        phone_book = change_name(phone_book,last_name,new_name)
        return phone_book
    elif change_choice == 2:
        new_last_name = input('Введите новую Фамилию абонента: ')
        phone_book = change_family_name(phone_book,last_name,new_last_name)
        return phone_book
    elif change_choice == 3:
        new_phone = input('Введите новый Телефон абонента: ')
        phone_book = change_phone(phone_book,last_name,new_phone)
        return phone_book
    elif change_choice == 4:
        new_description = input('Введите новое Описание абонента: ')
        phone_book = change_description(phone_book,last_name,new_description)
        return phone_book
    
def change_name(data: list, last_name: str, new_name: str):
    for i in range(len(data)):
        if data[i].get("Фамилия") == last_name:
            data[i]["Имя"] = new_name
    return data
        
def change_family_name(data: list, last_name: str, new_last_name: str):
    for i in range(len(data)):
        if data[i].get("Фамилия") == last_name:
            data[i]["Фамилия"] = new_last_name
    return data  

def change_phone(data: list, last_name: str, new_phone: str):
    for i in range(len(data)):
        if data[i].get("Фамилия") == last_name:
            data[i]["Телефон"] = new_phone
    return data
   
def change_description(data: list, last_name: str, description: str):
    for i in range(len(data)):
        if data[i].get("Фамилия") == last_name:
            data[i]["Описание"] = description
    return data  

def delete(data: list, last_name):
    isDelete = input(f'Вы уверены, что хотите удалить абонента {last_name} (да/нет): ')
    if isDelete == 'да':
        new_phone_book = []
        for el in data:
            if el.get("Фамилия") != last_name:
                new_phone_book.append(el)
        return new_phone_book
    return data

work_with_phonebook()


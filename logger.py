from data_create import input_user_data


def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формате записать данные?\n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n'
                    f'2Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f' \nВаш выбор: '
                    ))
    if var == 1:
       with open("data_first_variant.csv", "a", encoding="utf-8") as file:
           file.write( f'{name}\n'
                       f'{surname}\n'
                       f'{phone}\n'
                       f'{adress}\n')  
    else:
        with open("data_second_variant.csv", "a", encoding="utf-8") as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')

def print_data():
    print("1 файл: ")
    with open("data_first_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            print(i, end="\n")
        
    print("2 файл: ")
    with open("data_second_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            if i != '\n':
                print(i, end="\n")

def find_data():
    os.system("cls")
    target = input("Input Item of Contact for searching: ")
    result = []
    with open("data_first_variant.csv", "r", encoding="UTF-8") as file:
        data = file.readlines()
        for person in data:
            if target in person:
                result.append(person)

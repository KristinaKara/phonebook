from logger import input_data, print_data, find_data

def  interface():
    print("Добрый день! Это бот-помощник. \n"
         "Что вы хотите сделать?\n"
         "1 - Записать данные \n"
         "2 - Вывести данные \n"
         "3 - Поиск контакта")
    command = int(input("Ваш выбор:  "))
    
    while  command < 1 or command  > 3:
        command = int(input("Ошибка! Ваш выбор:  "))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    if command == 3:
        find_data()




    
 
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и 
# Вы должны реализовать функционал для изменения и удаления данных


def console_menu():
    pass

def read_file():
    with open(path_file, 'r',encoding = 'UTF-8') as f:
        for line in f:
            print(line.strip())

def write_file():
    with open(path_file, 'a',encoding = 'UTF-8') as f:
        f.writelines('\n'+input())
       

def find_file():
    find_info = input()
    with open(path_file, 'r',encoding = 'UTF-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line)

def change_file():
    with open (path_file, 'r+',encoding = 'UTF-8') as f:
        old_data = f.read()
        new_data = old_data.replace('Иванов', 'петренко1')
    with open (path_file, 'w',encoding = 'UTF-8') as f:
        f.write(new_data) 

                            

def main():
    change_file()
    
path_file = r'homework_38/telephone_book.txt'
if __name__ == '__main__':
    main()

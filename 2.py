# #Реализовать поиск по авторам, выдавать результат С 2016 по 2018 год. Выдача до - 11
from csv import reader 

def search(table, search_line): 
    flag = 0 
    for row in table:
        if string_find(row[3], search_line) != -1 and row[6][6:10] in ['2016', '2017', '2018']:
            flag += 1
            print(row[1])
    if flag ==0: 
        print('Не найдено записей с 2016г по 2018г :(')
    else: 
        print(f'Найдено записей с 2016г по 2018г: {flag}')

def string_find(string, search_line): 
    lower_case = string.lower() 
    return lower_case.find(search_line.lower())

while True: 
    search_line = input('Какой автор Вас интересует?: ')
    if search_line in ['0', '']:
        break
    try:
        with open('books.csv', 'r') as csvfile: 
            table = reader(csvfile, delimiter=';') 
            search(table, search_line)
    except FileNotFoundError:
        print('Файл не найден')

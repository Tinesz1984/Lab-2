from csv import reader

def search(table): 
    flag = 0 
    for row in table:
        if len(row[1]) > 30:
            flag += 1
    if flag ==0: 
        print('Ничего не найдено :(')
    else: 
        print(f'Количество записей, в названии которых более 30 символов: {flag}')

with open('books.csv', 'r') as csvfile: 
    table = reader(csvfile, delimiter=';') 
    search(table)
from csv import reader 

def search(table): 
    list = []
    headers = next(table)
    for row in table:
        stroke = row[12].replace('# ', '#').split('#')
        for el in stroke: 
            if el!='' and list.count(el)==0: 
                list.append(el)
    if len(list)==0: 
        print('Ничего не найдено :(')
    else: 
        print(f'Количество различных тегов: {len(list)}')
    for el in list: 
        print(el)

with open('books.csv', 'r') as csvfile: 
    table = reader(csvfile, delimiter=';') 

    search(table)

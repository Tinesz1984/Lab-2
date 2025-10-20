from csv import reader 

def search(table): 
    n = s = 0
    output = open('result_book.txt', 'w')
    for row in table:
        n +=1 
        if n%470==0: 
            s+=1
            output.write(f'{s}){row[3]}. «{row[1]}» - {row[6][6:10]} год\n')
    output.close()

with open('books.csv', 'r') as csvfile: 
    table = reader(csvfile, delimiter=';') 
    search(table)
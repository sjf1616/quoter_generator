def insert_sql():
    import csv #import library csv to manipulation

    fieldnames = ['category', 'quoter'] #We defined the header of sql

    with open("prov_sql.csv", 'a', newline="", encoding="utf-8") as arquivo: #open sql in mode append
        sql_quoter = csv.DictWriter(arquivo, fieldnames=fieldnames) #defined content in sql as dictionary
        if arquivo.tell() == 0: #check if row in sql not is empty
            sql_quoter.writeheader() 
        
        ins_category = str(input('Write a category: ')).lower().strip() #input the category
        ins_quoter = str(input('Write a quoter: ')) #input the quoter
        sql_quoter.writerow({'category':ins_category, 'quoter':ins_quoter}) #write in a row the input
        
def choice_quoter():
    import csv #import library csv to manipulation
    from random import choice #import module choice from library random

    with open("prov_sql.csv", newline="", encoding="utf-8") as arquivo: #open sql in mode read
        
        sql_quoter = csv.DictReader(arquivo) #defined content in sql as dictionary

        category_input = str(input('Choice your category: ')).lower().strip() #input the category

        if sql_quoter: #check if sql_quoter not is empty
            choice_list = [x for x in sql_quoter if x['category'] == category_input] #assignment the value from sql_quoter if colum category equals category_input
            selected_quoter = choice(choice_list) #choice any value in choice_list and assignment in variable
            print(f'Frase escolhida: {selected_quoter['quoter']}') #print in screen the value choice
        
        else: #Case sql is empty return a error
            print(f'Error 0001 - Database not found')
        print()

def color_gui(color_text):
    colors = {
        'clean':'\033[m',
        'red':'\033[31m',
        'green':'\033[32m]',
    }

    return colors.get(color_text, '\033[m')

def list_category():
     import csv #import library csv to manipulation
     with open('prov_sql.csv', 'r', newline="", encoding="utf-8") as arquivo: ##open sql in mode read
        reader_sql = csv.DictReader(arquivo) #defined content in sql as dictionary
        for enum, line in enumerate(reader_sql): #loop in len of reader_sql dictionary
            print(f'{enum + 1} - {line['category'].capitalize()}') #print each category in sql_reader with first letter upper
        print()
        

def title(text):
    print('-' * 30)
    print(f'{text:^30}')
    print('-' * 30)


def menu():
    options = [
        'List Category',
        'Choice Quoter',
        'Insert Quoter',
        'Exit'
    ]
    title('Menu')
    for enum, line in enumerate(options):
        print(f'{enum + 1} - {line}')

    option_select = str(input('Wich your option?: ')).lower().strip()
    print()
    return option_select

def return_menu():
    from time import sleep
    print(f'Returning to Menu')
    for _ in range(5, 0, -1):
     print(f'\r{_}', end='', flush=True)
     sleep(1)
    print()
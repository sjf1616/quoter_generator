def insert_sql():
    import csv
    with open("prov_sql.csv", newline="", encoding="utf-8") as arquivo:
        sql_quoter = csv.DictWriter(arquivo)
        ins_category = str(input('Write a category: ')).lower().strip()
        ins_quoter = str(input('Write a quoter: '))
        sql_quoter['category'] = ins_category
        sql_quoter['quoter'] = ins_quoter


def choice_quoter():
    import csv
    from random import choice
    with open("prov_sql.csv", newline="", encoding="utf-8") as arquivo:
        #Transforma os dados dentro do .csv em dict
        sql_quoter = csv.DictReader(arquivo) 

        #Pede ao usuário inserir uma categoria para busca
        category_input = str(input('Choice your category: ')).lower().strip()

        if sql_quoter:
            choice_list = [x for x in sql_quoter if x['category'] == category_input]
            selected_quoter = choice(choice_list)
            print(f'Frase escolhida: {selected_quoter['quoter']}')
        
        else:
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
     import csv
     with open('prov_sql.csv', newline="", encoding="utf-8") as arquivo:
        reader_sql = sorted(csv.DictReader(arquivo))
        for enum, line in enumerate(reader_sql):
            print(f'{enum + 1} - {line['category'].capitalize()}')
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
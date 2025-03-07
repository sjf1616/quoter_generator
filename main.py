def choice_quoter():
    from random import randint
    import csv

    #Abre o arquivo 'prov_sql.csv' e nomea como 'arquivo'
    with open("prov_sql.csv", newline="", encoding="utf-8") as arquivo:

        #Transforma os dados dentro do .csv em dict
        sql_quoter = csv.DictReader(arquivo) 

        #Pede ao usuário inserir uma categoria para busca
        category_input = input('Choice your category: ').lower().strip()

        #Inseri em uma lista os dados que contém na coluna 'category'
        category_lists = [c['category'] for c in sql_quoter]

        #Verifica se o dado digitado pelo usuário existe nas categorias
        for i in sql_quoter:

            if category_input in i['category']:
                #Inseri em uma lista os dados são da categoria escolhida pelo usuário
                choice_list = list()
                choice_list.append(i.copy())
                
                if choice_list:
                    #Busca um número aleátorio
                    choice = randint(0, len(choice_list) - 1)

                    #Inseri o valor aleatório como index da lista escolhida pelo usuário
                    choice_quoter = choice_list[choice]

                    #Imprime na tela apenas a citação/quoter
                    print(choice_quoter['quoter'])
                else: 
                    print(f"No quotes available for the '{category_input}' category")
            else:
                print(f'Não existe {category_input} nas categorias')

choice_quoter()
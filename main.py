quoter = {
    'category':'',
    'quoter':''
}

sql = [{
    'category':'motivacional',
    'quoter':'Difficult roads lead to beatuful destinations'
    },{
    'category':'motivacional',
    'quoter':'the life snake'
    }]


def insert_sql(cat, quo):
    quoter['category'] = cat
    quoter['quoter'] = quo
    sql.append(quoter.copy())

def choice_quoter():
    from random import randint
    type = input('Choice your quoter: ').split()
    for _ in type:
        if _ in 'motivacional':
            choice_list = [ x for x in sql if x['category'] == 'motivacional']
            choice = randint(0, len(choice_list) - 1)
            choice_quoter = choice_list[choice]
            print(choice_quoter['quoter'])

choice_quoter()
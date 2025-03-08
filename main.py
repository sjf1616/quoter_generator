def main():
    from time import sleep
    from utility import color_gui, title, menu
    print(f'{color_gui('red')}Welcome a Quoter Generator! :){color_gui('clean')}')
    sleep(0.5)

    select_option = menu()
    while select_option not in 'exit' or select_option == '4':
        from utility import return_menu
        if select_option in 'list category' or select_option == '1':
            from utility import list_category
            list_category()
        elif select_option in 'choice quoter' or select_option == '2':
            from utility import choice_quoter
            choice_quoter()

        elif select_option in 'insert quoter' or select_option == '3':
            from utility import insert_sql
            insert_sql()
        
        return_menu()
        select_option = menu()
main()
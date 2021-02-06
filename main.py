def main():
    import os

    pac_name = 'Nacom'

    register_nom = './register.py'
    login_nom = './login.py'

    print('\r\n' + pac_name + '\r\n')

    def help():
        print('''nacom --help    ||    Shows this table
    nacom register  ||    Begins the registration proccess
    nacom login     ||    Login to an already existing user
    nacom logout    ||    Log out of the user
                ''')

    help()

    def user_input():
        nacom_input = input()
        
        if nacom_input == 'nacom --help':
            help()
        if nacom_input == 'nacom register':
            import register
            register()
        if nacom_input == 'nacom login':
            import login
            login()
        if nacom_input == 'nacom logout':
            import signout
            signout()
        
        user_input()



    user_input()
        
main()

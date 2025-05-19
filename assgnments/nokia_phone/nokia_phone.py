import functions_nokia

def handle_input(user_input):
    match user_input:
        case 1:
            functions_nokia.phonebook()
        case 2:
            functions_nokia.messages()
        case 3:
            functions_nokia.chat()
        case 4:
            functions_nokia.call_register()
        case 5:
            functions_nokia.tones()
        case 6:
            functions_nokia.settings()
        case 7:
            functions_nokia.call_divert()
        case 8:
            functions_nokia.games()
        case 9:
            functions_nokia.calculator()
        case 10:
            functions_nokia.reminder()
        case 11:
            functions_nokia.clock()
        case 12:
            functions_nokia.profiles()
        case 13:
            functions_nokia.sim_service()
        case _:
            print("Invalid number. Please enter a valid number from 0 to 13.")

while True:

        user_input = int(input("""
            ======================================
                      WELCOME TO TEGA'S PHONE
            ======================================

                       MAIN MENU

                  1  -> Phone Book
                  2  -> Messages
                  3  -> Chat
                  4  -> Call Register
                  5  -> Tones
                  6  -> Settings
                  7  -> Call Divert
                  8  -> Games
                  9  -> Calculator
                 10  -> Reminder
                 11  -> Clock
                 12  -> Profiles
                 13  -> SIM Services
                  0  -> Exit
            ======================================
                Kindly enter your choice below:
            ======================================
            """))

        if user_input == 0:
            print("Goodbye!")
            break
        else:
            handle_input(user_input)















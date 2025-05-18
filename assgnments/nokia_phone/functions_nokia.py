import middle_functions
def phonebook():
       # import nokia_phone
       while True:
            phoneBookInput = int(input("""
                1  - Search
                2  - Service Nos
                3  - Add Name
                4  - Eras
                5  - Edit
                6  - Assign Tone
                7  - Send b'card
                8  - Options
                9  - Speed dial
                10 - voice tags
                0 - enter 0 to go back to previous menu
                """))
            if phoneBookInput > 10:
                print("invalid Number, pleas choose:");
                continue
            match phoneBookInput:
                    case 0:
                        return
                    case 1:
                        while True:
                            print("Search");
                            enterNumber=int(input("enter 0 to go back to previous menu"))
                            if enterNumber == 0:
                                break
                            else:
                                print("invalid number");

                    case 2 :
                        while True:
                            print("Service Nos");
                            enterNumber=int(input("enter 0 to go back to previous menu"))
                            if enterNumber == 0:
                                break
                            else:
                                print("invalid number");
                    case 3 :
                        while True:
                            print("Add Name");
                            SenterNumber=int(input("enter 0 to go back to previous menu"))
                            if enterNumber == 0:
                                    break
                            else:
                                    print("invalid number");
                    case 4 :
                        while True:
                            print("Erase");
                            enterNumber=int(input("enter 0 to go back to previous menu"))
                            if enterNumber == 0:
                                    break
                            else:
                                print("invalid number");
                    case 5 :
                        while True:
                            print("Edit");
                            enterNumber=int(input("enter 0 to go back to previous menu"))
                            if enterNumber == 0:
                               break
                            else:
                               print("invalid number");
                    case 6 :
                        while True:
                                print("Assign Tone");
                                enterNumber=int(input("enter 0 to go back to previous menu"))
                                if enterNumber == 0:
                                    break
                                else:
                                    print("invalid number");
                    case 7 :
                        while True:
                            print("Send b'card");
                            enterNumber=int(input("enter 0 to go back to previous menu"))
                            if enterNumber == 0:
                                    break
                            else:
                                    print("invalid number");

                    case 8 : middle_functions.optionEight();

                    case 9 :

                        while True:
                            print("Speed dial");
                            enterNumber=int(input("enter 0 to go back to previous menu"))
                            if enterNumber == 0:
                                    break
                            else:
                                    print("invalid number");
                    case 10 :
                        while True:
                            print("Voice tags");
                            enterNumber=int(input("enter 0 to go back to previous menu"))
                            if enterNumber == 0:
                                    break
                            else:
                                    print("invalid number");

#......................................................................................................................



def messages():
    while True:
          userMessages = int(input("""
                1  - Write Messages
                2  - Inbox
                3  - Outbox
                4  - Picture messages
                5  - Templates
                6  - Smileys
                7  - Messages setting
                8  - Info service
                9  - Voice mailbox number
                10 - Services command editor
                0  - Go back to previous menu
                """))
          if userMessages > 10 :
                print("invalid Number, pleas choose:");
                continue

          match userMessages:
            case 0:
                return
            case 1:
                while True:
                    print("Write Messages")
                    enterNumber = int(input("Enter 0 to go back to messages menu"))
                    if enterNumber == 0:
                        break
                    else:
                        print("Invalid number")
            case 2:
                while True:
                    print("Inbox")
                    enterNumber = int(input("Enter 0 to go back to messages menu"))
                    if enterNumber == 0:
                        break
                    else:
                        print("Invalid number")
            case 3:
                while True:
                    print("Outbox")
                    enterNumber = int(input("Enter 0 to go back to messages menu"))
                    if enterNumber == 0:
                        break
                    else:
                        print("Invalid number")
            case 4:
                while True:
                    print("Picture messages")
                    enterNumber = int(input("Enter 0 to go back to messages menu"))
                    if enterNumber == 0:
                        break
                    else:
                        print("Invalid number")
            case 5:
                while True:
                    print("Templates")
                    enterNumber = int(input("Enter 0 to go back to messages menu"))
                    if enterNumber == 0:
                        break
                    else:
                        print("Invalid number")
            case 6:
                while True:
                    print("Smileys")
                    enterNumber = int(input("Enter 0 to go back to messages menu"))
                    if enterNumber == 0:
                        break
                    else:
                        print("Invalid number")
            case 7:
                middle_functions.optionSeven()
            case 8:
                while True:
                    print("Info service")
                    enterNumber = int(input("Enter 0 to go back to messages menu"))
                    if enterNumber == 0:
                        break
                    else:
                        print("Invalid number")
            case 9:
                while True:
                    print("Voice mailbox number")
                    enterNumber = int(input("Enter 0 to go back to messages menu"))
                    if enterNumber == 0:
                        break
                    else:
                        print("Invalid number")
            case 10:
                while True:
                    print("Services command editor")
                    enterNumber = int(input("Enter 0 to go back to messages menu"))

# ................................................................................
def chat():
    while True:
        print("Chat")
        goBack=int(input("Enter 0 to go back to the previous menu"))

        if goBack == 0:
           return
        else:
            print("Invalid input")
            continue

# .....................................................................................
def games():
    while True:
        print("Games")
        goBack=int(input("Enter 0 to go back to the previous menu"))

        if goBack == 0:
           return
        else:
            print("Invalid input")
            continue
# ......................................................................................
def calculator():
    while True:
        print("Calculator")
        goBack=int(input("Enter 0 to go back to the previous menu"))

        if goBack == 0:
           return
        else:
            print("Invalid input")
            continue
# ...........................................................................................
def reminder():
    while True:
        print("Reminder")
        goBack=int(input("Enter 0 to go back to the previous menu"))

        if goBack == 0:
           return
        else:
            print("Invalid input")
            continue
# ...............................................................................
def profiles():
    while True:
        print("Profiles")
        goBack=int(input("Enter 0 to go back to the previous menu"))

        if goBack == 0:
           return
        else:
            print("Invalid input")
            continue
# ..........................................................................................
def sim_service():
    while True:
        print("Sim Service")
        goBack=int(input("Enter 0 to go back to the previous menu"))

        if goBack == 0:
           return
        else:
            print("Invalid input")
            continue

# ......................................................................................................
def call_divert():
    while True:
            print("call Divert")
            goBack=int(input("Enter 0 to go back to the previous menu"))

            if goBack == 0:
               return
            else:
                print("Invalid input")
                continue

# ........................................................................................................

def call_register():
    while True:
        print("""
            1  - Missed calls
            2  - Received calls
            3  - Dialed Numbers
            4  - Erase recent call list
            5  - Show call duration
            6  - Show call cost
            7  - Call cost setting
            8  - Prepaid credit
            0  - Go back to main menu
        """)

        input_option = int(input())
        if input_option > 8 or input_option < 0:
                print("invalid Number, pleas choose:");
                continue

        match input_option:
            case 0:
                return
            case 1:
                while True:
                    print("Missed calls")
                    if int(input("Enter 0 to go back: ")) == 0:
                        break
                    else:
                        print("Invalid number")
                        continue
            case 2:
                while True:
                    print("Received calls")
                    if int(input("Enter 0 to go back: ")) == 0:
                        break
                    else:
                        print("Invalid number")
                        continue
            case 3:
                while True:
                    print("Dialed Numbers")
                    if int(input("Enter 0 to go back: ")) == 0:
                        break
                    else:
                        print("Invalid number")
                        continue
            case 4:
                while True:
                    print("Erase recent call list")
                    if int(input("Enter 0 to go back: ")) == 0:
                        break
                    else:
                        print("Invalid number")
                        continue
            case 5:
                middle_functions.option_five()
            case 6:
                while True:
                    print("""
                        1  - Show last call
                        2  - All call cost
                        3  - Clear counters
                        0  - Go back

                    """)

                    choice = int(input())
                    if choice > 3 or choice < 0:
                        print("invalid Number, pleas choose:");
                        continue

                    match choice:
                        case 0:
                            break
                        case 1:
                            while True:
                                print("Show last call")
                                if int(input("Enter 0 to go back: ")) == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue
                        case 2:
                            while True:
                                print("All call cost")
                                if int(input("Enter 0 to go back: ")) == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue
                        case 3:
                            while True:
                                print("Clear counters")
                                if int(input("Enter 0 to go back: ")) == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue

            case 7:
                while True:
                    print("""
                        1  - Call cost limits
                        2  - Show cost in
                        0  - Go back

                    """)

                    choice = int(input())
                    if choice > 2 or choice < 0:
                        print("invalid Number, pleas choose:");
                        continue

                    match choice:
                        case 0:
                            break

                        case 1:
                            while True:
                                print("Call cost limits")
                                if int(input("Enter 0 to go back: ")) == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue
                        case 2:
                            while True:
                                print("Show cost in")
                                if int(input("Enter 0 to go back: ")) == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue

            case 8:
                while True:
                    print("Prepaid credit")
                    if int(input("Enter 0 to go back: ")) == 0:
                        break
                    else:
                        print("Invalid number")
                        continue


# .................................................................................................
def tones():
    while True:
        print("""
            1  - Ringing tone
            2  - Ringing volume
            3  - Incoming call alert
            4  - Composer
            5  - Messages alert tone
            6  - Keypad tones
            7  - Warning and games tones
            8  - Vibrating alert
            9  - Screen saver
            0  - Go back to previous menu
        """)

        user_input = int(input("Enter your choice: "))
        if user_input > 9 or user_input < 0:
                print("invalid Number, pleas choose:");
                continue

        match user_input:
            case 0:

                return
            case 1:
                while True:
                    print("Ringing tone")
                    if input("Enter 0 to go back: ") == '0':
                        break
                    else:
                        print("Invalid input.")
                        continue
            case 2:
                while True:
                    print("Ringing volume")
                    if input("Enter 0 to go back: ") == '0':
                        break
                    else:
                        print("Invalid input.")
                        continue
            case 3:
                while True:
                    print("Incoming call alert")
                    if input("Enter 0 to go back: ") == '0':
                        break
                    else:
                        print("Invalid input.")
                        continue
            case 4:
                while True:
                    print("Composer")
                    if input("Enter 0 to go back: ") == '0':
                        break
                    else:
                        print("Invalid input.")
                        continue
            case 5:
                while True:
                    print("Messages alert tone")
                    if input("Enter 0 to go back: ") == '0':
                        break
                    else:
                        print("Invalid input.")
                        continue
            case 6:
                while True:
                    print("Keypad tones")
                    if input("Enter 0 to go back: ") == '0':
                        break
                    else:
                        print("Invalid input.")
                        continue
            case 7:
                while True:
                    print("Warning and games tones")
                    if input("Enter 0 to go back: ") == '0':
                        break
                    else:
                        print("Invalid input.")
                        continue
            case 8:
                while True:
                    print("Vibrating alert")
                    if input("Enter 0 to go back: ") == '0':
                        break
                    else:
                        print("Invalid input.")
                        continue
            case 9:
                while True:
                    print("Screen saver")
                    if input("Enter 0 to go back: ") == '0':
                        break
                    else:
                        print("Invalid input.")
                        continue

# .............................................................

def settings():
    while True:
        print("""
            1  - Call setting
            2  - Phone setting
            3  - Security setting
            4  - Restore factory setting
            0  - Go back to previous menu
        """)
        user_tones = int(input("Enter your choice: "))
        if user_tones > 4 or user_tones < 0:
                print("invalid Number, pleas choose:");
                continue

        match user_tones:
            case 0:
                return

            case 1:
                while True:
                    print("""
                        1  - Automatic redial
                        2  - Speed dialing
                        3  - Call waiting response
                        4  - Own number sending
                        5  - Phone line in use
                        6  - Automatic answer
                        0  - Go back
                    """)
                    call_setting = int(input("Enter your choice: "))
                    if call_setting > 6 or call_setting < 0:
                        print("invalid Number, pleas choose:");
                        continue


                    match call_setting:
                        case 0:
                            break
                        case 1:
                            while True:
                                print("Automatic redial")
                                back = int(input("Enter 0 to go back to previous menu:"))
                                if back == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue
                        case 2:
                            while True:
                                print("Speed dialing")
                                back = int(input("Enter 0 to go back to previous menu:"))
                                if back == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue
                        case 3:
                            while True:
                                print("Call waiting response")
                                back = int(input("Enter 0 to go back to previous menu:"))
                                if back == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue
                        case 4:
                            while True:
                                print("Own number sending")
                                back = int(input("Enter 0 to go back to previous menu:"))
                                if back == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue
                        case 5:
                            while True:
                                print("Phone line in use")
                                back = int(input("Enter 0 to go back to previous menu:"))
                                if back == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue
                        case 6:
                            while True:
                                print("Automatic answer")
                                back = int(input("Enter 0 to go back to previous menu:"))
                                if back == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue


            case 2:
                while True:
                    print("""
                        1  - Language
                        2  - Cell info display
                        3  - Welcome note
                        4  - Network selection
                        5  - Lights
                        6  - Confirm SIM service actions
                        0  - Go back
                    """)
                    phone_setting = int(input("Enter your choice: "))
                    if phone > 6 or phone < 0:
                        print("invalid Number, pleas choose:");
                        continue


                    match phone_setting:
                        case 0:
                            break
                        case 1:
                            while True:
                                print("Language")
                                back = int(input("Enter 0 to go back to previous menu:"))
                                if back == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue

                            while True:
                                print("Cell info display")
                                back = int(input("Enter 0 to go back to previous menu:"))
                                if back == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue

                        case 3:
                            while True:
                                print("Welcome note")
                                back = int(input("Enter 0 to go back to previous menu:"))
                                if back == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue

                        case 4:
                            while True:
                                print("Network selection")
                                back = int(input("Enter 0 to go back to previous menu:"))
                                if back == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue

                        case 5:
                            while True:
                                print("Lights")
                                back = int(input("Enter 0 to go back to previous menu:"))
                                if back == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue

                        case 6:
                            while True:
                                print("Confirm SIM service actions")
                                back = int(input("Enter 0 to go back to previous menu:"))
                                if back == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue


            case 3:
                while True:
                    print("""
                        1  - PIN code request
                        2  - Call barring service
                        3  - Fixed dialing
                        4  - Closed user group
                        5  - Phone security
                        6  - Change access codes
                        0  - Go back
                    """)
                    security_setting = int(input("Enter your choice: "))
                    if security_setting > 6 or security_setting < 0:
                        print("invalid Number, pleas choose:");
                        continue

                    match security_setting:
                        case 0:
                            break
                        case 1:
                            while True:
                                print("PIN code request")
                                back = int(input("Enter 0 to go back to previous menu:"))
                                if back == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue

                        case 2:
                            while True:
                                print("Call barring service")
                                back = int(input("Enter 0 to go back to previous menu:"))
                                if back == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue

                        case 3:
                            while True:
                                print("Fixed dialing")
                                back = int(input("Enter 0 to go back to previous menu:"))
                                if back == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue

                        case 4:
                            while True:
                                print("Closed user group")
                                back = int(input("Enter 0 to go back to previous menu:"))
                                if back == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue

                        case 5:
                            while True:
                                print("Phone security")
                                back = int(input("Enter 0 to go back to previous menu:"))
                                if back == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue

                        case 6:
                            while True:
                                print("Change access codes")
                                back = int(input("Enter 0 to go back to previous menu:"))
                                if back == 0:
                                    break
                                else:
                                    print("Invalid number")
                                    continue


            case 4:
                while True:
                    print("Restore factory settings")
                    back = int(input("Enter 0 to go back to previous menu:"))
                    if back == 0:
                        break
                    else:
                        print("Invalid number")
                        continue

# ..........................................................................................................................
def clock():
    while True:
        print("""
            1  - Alarm clock
            2  - Clock setting
            3  - Date setting
            4  - Stopwatch
            5  - Countdown timer
            6  - Auto update of date and time
            0  - Go back to previous menu
        """)
        user_input = int(input())
        if user_input > 6 or user_input < 0:
                print("invalid Number, pleas choose:");
                continue

        match user_input:
            case 0:
                return
            case 1:
                while True:
                    print("Alarm clock")
                    back = int(input("Enter 0 to go back to previous menu:"))
                    if back == 0:
                        break
                    else:
                        print("Invalid number")
                        continue
            case 2:
                while True:
                    print("Clock setting")
                    back = int(input("Enter 0 to go back to previous menu:"))
                    if back == 0:
                        break
                    else:
                        print("Invalid number")
                        continue
            case 3:
                while True:
                    print("Date setting")
                    back = int(input("Enter 0 to go back to previous menu:"))
                    if back == 0:
                        break
                    else:
                        print("Invalid number")
                        continue
            case 4:
                while True:
                    print("Stopwatch")
                    back = int(input("Enter 0 to go back to previous menu:"))
                    if back == 0:
                        break
                    else:
                        print("Invalid number")
                        continue
            case 5:
                while True:
                    print("Countdown timer")
                    back = int(input("Enter 0 to go back to previous menu:"))
                    if back == 0:
                        break
                    else:
                        print("Invalid number")
                        continue
            case 6:
                while True:
                    print("Auto update of date and time")
                    back = int(input("Enter 0 to go back to previous menu:"))
                    if back == 0:
                        break
                    else:
                        print("Invalid number")
                        continue










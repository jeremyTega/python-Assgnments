def optionEight():
    while True:
         card = int(input("""
            1  -> Type of view
            2  -> Memory status
               -> enter 0 to go back to previous menu
               -> enter 99 to go back to main menu:
                        """))
         match card:
            case 0 :
                return
            # case 0:
            #     continue

            case 1 :
               while True:
                    print("Type of view");
                    enterNumber=int(input("enter 0 to go back to previous menu: "))
                    if enterNumber == 0:
                            break
                    else:
                           print("invalid number");
            case 2 :
                while True:
                    print("Memory status");
                    enterNumber=int(input("enter 0 to go back to previous menu: "))
                    if enterNumber == 0:
                         break
                    else:
                        print("invalid number");
#.............................................................................................................................


def optionSeven():
    while True:
        print("""
            1 -> Set 1
            2 -> Common
            0 -> Go back to messages menu

        """)
        messageSetting = int(input("Enter your choice: "))
        if messageSetting < 0 or messageSetting > 2:
            print("Invalid input. Please enter a number.")
            continue

        if messageSetting == 0:
            return

        elif messageSetting == 1:
            while True:
                print("""
                    1 - Message center number
                    2 - Message sent as
                    3 - Message validity
                    0 - Go back to previous menu

                """)

                set_choice = int(input("Enter your choice: "))
                if set_choice < 0 or set_choice > 3:
                    print("Invalid input. Please enter a number.")
                    continue

                if set_choice == 0:
                    break
                elif set_choice == 1:
                    while True:
                        print("Message center number")
                        back = int(input("Enter 0 to go back: "))
                        if back == 0:
                            break
                        else:
                            print("Invalid number")
                            continue
                elif set_choice == 2:
                    while True:
                        print("Message sent as")

                        back = int(input("Enter 0 to go back: "))

                        if back == 0:
                            break
                        else:
                            print("Invalid number")
                            continue
                elif set_choice == 3:
                    while True:
                        print("Message validity")

                        back = int(input("Enter 0 to go back: "))

                        if back == 0:
                            break
                        else:
                            print("Invalid number")
                            continue
                else:
                    print("Invalid input")
        elif messageSetting == 2:
            while True:
                print("""
                    1 - Delivery report
                    2 - Reply via same center
                    3 - Character support
                    0 - Go back to previous menu
                                    """)

                common_choice = int(input("Enter your choice: "))
                if common_choice < 0 or common_choice > 3:
                    print("Invalid input. Please enter a number.")
                    continue

                if common_choice == 0:
                    break
                elif common_choice == 1:
                    while True:
                        print("Delivery report")

                        back = int(input("Enter 0 to go back: "))

                        if back == 0:
                            break
                        else:
                            print("Invalid number")
                            continue
                elif common_choice == 2:
                    while True:
                        print("Reply via same center")

                        back = int(input("Enter 0 to go back: "))

                        if back == 0:
                            break
                        else:
                            print("Invalid number")
                            continue
                elif common_choice == 3:
                    while True:
                        print("Character support")

                        back = int(input("Enter 0 to go back: "))

                        if back == 0:
                            break
                        else:
                            print("Invalid number")
                            continue
                else:
                    print("Invalid input")
                    continue
        else:
            print("Invalid input. Please select 1, 2, or 0.")

# ...............................
def option_five():
    while True:
        print("""
                1  - Last call duration
                2  - All call's duration
                3  - Received call's duration
                4  - Dialed call's duration
                5  - Clear counters
                0  - Go back to previous menu

                """)

        call_duration = int(input("Choose an option: "))
        if call_duration < 0 or call_duration > 5:
                    print("Invalid input. Please enter a number.")
                    continue

        match call_duration:
            case 0:
                return

            case 1:
                while True:
                    print("Last call duration")
                    if int(input("Enter 0 to go back: ")) == 0:
                        break
                    else:
                        print("Invalid number")
                        continue
            case 2:
                while True:
                    print("All call's duration")
                    if int(input("Enter 0 to go back: ")) == 0:
                        break
                    else:
                        print("Invalid number")
                        continue
            case 3:
                while True:
                    print("Received call's duration")
                    if int(input("Enter 0 to go back: ")) == 0:
                        break
                    else:
                        print("Invalid number")
                        continue
            case 4:
                while True:
                    print("Dialed call's duration")
                    if int(input("Enter 0 to go back: ")) == 0:
                        break
                    else:
                        print("Invalid number")
                        continue
            case 5:
                while True:
                    print("Clear counters")
                    if int(input("Enter 0 to go back: ")) == 0:
                        break
                    else:
                        print("Invalid number")
                        continue


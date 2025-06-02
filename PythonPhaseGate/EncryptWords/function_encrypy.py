def encrypt(text):

    print("this is text", text)
    letters = "abcdefghijklmnopqrstuvwxyz"
    upperLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []

    for character in text:
        if character in letters:

            index = letters.index(character)
            print("this is it" , index + 1)
            new_index = (index + 13) %26

            print("new index",new_index)
            result.append(letters[new_index])

        elif character in upperLetters:

            index = upperLetters.index(character)
            print("this is it" , index + 1)
            new_index = (index + 13) %26

            print("new index",new_index)
            result.append(upperLetters[new_index])

        else:
            result.append(character)

    return ''.join(result)

print(encrypt('Hello.World'))





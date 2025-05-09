valid_input = 0
invalid_input = 0

while True:
    userNumber = input("Please enter '1' or '2', enter 0 to stop: ")
    if userNumber == '0':
        break
    elif userNumber == '1' or userNumber == '2':
        valid_input += 1
    else:
        invalid_input += 1

print(f'Valid inputs entered: {valid_input}')
print(f'Invalid inputs entered: {invalid_input}')

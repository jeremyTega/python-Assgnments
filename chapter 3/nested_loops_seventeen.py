# for row in range(1, 10):
#     for column in range(row):
#         print('*' , end ='')
#
#     print ()
#
#
#
#
# for row2 in range(10, -1, -1):
#     for column2 in range(row2):
#         print('*' , end ='')
#
#     print ()
#
# n = 10
#
# for i in range(n, 0, -1):
#     for j in range(i):
#         print('*', end='')
#     print()

n = 10

for i in range(1, n + 1):

    left = '*' * i + ' ' * (n - i)
    right = ' ' * (n - i) + '*' * i
    inv_left = '*' * (n - i + 1) + ' ' * (i - 1)
    inv_right = ' ' * (i - 1) + '*' * (n - i + 1)

    print(left + '   ' + right + '   ' + inv_left + '   ' + inv_right)



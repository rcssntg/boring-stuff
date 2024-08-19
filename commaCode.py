# def format_list(items):
#     if len(items) == 0:
#         return ''
#     elif len(items) ==1:
#         return items[0]
#     else:
#         return ', '.join(items[:-1]) + ', and ' + items[-1]





# spam = ['apples', 'bananas', 'tofu', 'cats', '42', 'True']
# # spam = []
# # spam = ['apples']
# result = format_list(spam)
# print(result)

grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]


for y in range(len(grid[0])):
    for x in range(len(grid)):
        print(grid[x][y], end='')
    print()
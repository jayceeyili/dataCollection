import xlrd
from os import listdir

path = "/Users/yili/Desktop/test/"

matrix = []
for files in listdir(path):
    book_path = path + files
    book = xlrd.open_workbook(book_path, on_demand=True)
    t38 = book.sheet_by_name("38.0C").cell_value(0, 1)
    t0 = book.sheet_by_name("-5.0C").cell_value(0, 1)
    t65 = book.sheet_by_name("65.0C").cell_value(0, 1)
    win_cal = book.sheet_by_name("Sum").row_values(8, 6, 9)
    matrix.append([t0, t38, t65])
    matrix.append(win_cal)

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

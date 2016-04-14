import xlrd
import xlwt
from os import listdir

cal_path = "/Users/yili/Desktop/HW/calcheck/"
bss_path = "/Users/yili/Desktop/HW/bss/"

sn_matrix = []
matrix = []
for files in listdir(cal_path):
    book_path = cal_path + files
    book = xlrd.open_workbook(book_path, on_demand=True)
    t38 = book.sheet_by_name("38.0C").cell_value(0, 1)
    t0 = book.sheet_by_name("-5.0C").cell_value(0, 1)
    t65 = book.sheet_by_name("65.0C").cell_value(0, 1)
    win_cal = book.sheet_by_name("Sum").row_values(8, 6, 9)
    sn = eval(files[4: 12])
    sn_matrix.append([sn, " "])
    matrix.append([t0, t38, t65])
    matrix.append(win_cal)

bss_matrix = []
for files in listdir(bss_path):
    bookbss_path = bss_path + files
    bookbss = xlrd.open_workbook(bookbss_path, on_demand=True)
    sn = bookbss.sheet_by_name("25C").cell_value(0, 1)
    t25 = bookbss.sheet_by_name("25C").cell_value(0, 2)
    win_bss = bookbss.sheet_by_name("Win Data").cell_value(0, 12)
    bss_matrix.append([t25, win_bss])

book = xlwt.Workbook()
sheet1 = book.add_sheet('result', cell_overwrite_ok=True)

l = [item for sublist in bss_matrix for item in sublist]
s = [item for sublist in sn_matrix for item in sublist]

for i, row in enumerate(matrix):
    row.insert(0, l[i])
    row.insert(0, s[i])

for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        sheet1.write(i, j, col)

book.save("/Users/yili/Desktop/result.xls")

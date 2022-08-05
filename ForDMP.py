import openpyxl
import pandas as pd
from openpyxl.comments import Comment
import os


file = input('Пример: C:/Users/davyd/Desktop/DigitalMediaPlanner.xlsx\nПуть до DMP с полным названием: ')
try:
    p = pd.read_excel(file, engine='openpyxl',
                                         header=5)
    a = p["Категория Клиента"].tolist()
    wb = openpyxl.load_workbook(filename=file, data_only=True)
    ws = wb.active
    data = []
    for row in list(ws)[7:len(p)+7]:
        for cell in row:
            if str(cell.comment) != 'None':
                cell = str(cell)
                data.append(cell[cell.rfind('.')+1:-1])
    with open("comments.txt", 'w') as f:
        f.write(' '.join(data))
except:
    print("Не правильно указан путь")

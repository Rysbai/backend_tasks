import openpyxl
import matplotlib.pyplot as plt

wd = openpyxl.load_workbook('example.xlsx')
sheet =  wd.get_sheet_by_name('Лист1')

c = sheet['A2']
x_labels = [x for x in range(2, 5)]
y_labels = [sheet.cell(row=i, column=2).value for i in x_labels]
plt.plot(x_labels, y_labels, c='yellow')

x_labels = [x for x in range(2, 5)]
y_labels = [sheet.cell(row=i, column=3).value for i in x_labels]
plt.plot(x_labels, y_labels, c='red')

plt.show()
import pygal 
import openpyxl

filename = 'data.xlsx'

wb = openpyxl.load_workbook(filename)
sheets = wb.get_sheet_names()

index = 1
for sh in sheets:
    sheet =  wb.get_sheet_by_name(sh)

    for row in range(2, sheet.max_row + 1):
        x_labels = [sheet.cell(row=1, column=i).value for i in range(2, sheet.max_column + 1)]
        y_labels = [sheet.cell(row=row, column=i).value for i in range(2, sheet.max_column + 1)]
        time = sheet.cell(row=row, column=1).value

        hist = pygal.HorizontalBar()
        hist.title = sheet.title
        hist.x_title = 'Өлчөө убактысы: ' + time
        hist.x_labels = x_labels

        hist.add('(мг/м3)', y_labels)
        file_name = str(index) + '_graph'

        hist.render_to_png('graphs/{}.png'.format(file_name))
        index += 1

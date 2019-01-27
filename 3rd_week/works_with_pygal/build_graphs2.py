import pygal 
import openpyxl

filename = 'data2.xlsx'

wb = openpyxl.load_workbook(filename)
sheets = wb.get_sheet_names()
sh_number = 1
for sh in sheets:
    sheet =  wb.get_sheet_by_name(sh)
    for col in range(1, sheet.max_column, 2):   
        x_labels = [sheet.cell(row=i, column=col).value for i in range(2, sheet.max_row + 1) if i != None]
        rows = [sheet.cell(row=i, column=col+1).value for i in range(2, sheet.max_row + 1) if i != None]
        device = sheet.cell(row=1, column=col).value

        hist = pygal.Bar()
        hist.title = sheet.title
        hist.x_labels = x_labels
        hist.add(device, rows)
        device = device + str(sh_number)
        hist.render_to_png('graphs2/{}.png'.format(device))
        print(device)
    sh_number +=1
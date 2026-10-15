import openpyxl

from config.config import EXCEL_FILE, SHEET_NAME


def get_workbook():
    work_book = openpyxl.load_workbook(EXCEL_FILE)
    work_sheet = work_book[SHEET_NAME]

    data=[]

    keys = [cell.value for cell in work_sheet[2]]
    for row in work_sheet.iter_rows(min_row=3,values_only=True):
        dict_data = dict(zip(keys,row))
        if dict_data['is_true']:
            data.append(dict_data)

    work_book.close()
    return data
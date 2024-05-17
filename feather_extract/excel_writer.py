import openpyxl

def save_to_excel(formatted_data, file_name):
    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    if formatted_data:
        headers = ['Item', 'Quantity', 'Location']
        worksheet.append(headers)

        for row in formatted_data:
            worksheet.append(row)
    else:
        print("No data to save to Excel.")

    workbook.save(file_name)
import openpyxl

def organize_into_excel(input_text_file, output_excel_file):
    # Create a new Excel workbook
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Read the content from the text file
    with open(input_text_file, 'r') as file:
        lines = file.readlines()

    # Extract header from the first line
    header = [cell.strip() for cell in lines[0].split('|') if cell.strip()]

    # Write header to Excel sheet
    sheet.append(header)

    # Iterate through each line in the text file and add it to the Excel sheet
    for line in lines[2:]:  # Start from the third line to skip the header separator
        # Split the line into cells and remove empty strings
        data = [cell.strip() for cell in line.split('|') if cell.strip()]

        # Write data to Excel sheet
        sheet.append(data)

    # Save the Excel file
    workbook.save(output_excel_file)

if __name__ == "__main__":
    # Replace 'input_combined.txt' with the path to your combined text document
    input_text_file = 'input.txt'

    # Replace 'output_combined.xlsx' with the desired name for your combined Excel file
    output_excel_file = 'output.xlsx'

    organize_into_excel(input_text_file, output_excel_file)


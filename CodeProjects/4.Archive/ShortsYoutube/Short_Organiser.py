import pandas as pd
from io import StringIO
from tabulate import tabulate

# Specify the path to your text file containing the table
text_file_path = 'Short1.txt'

# Read the table from the text file into a DataFrame
with open(text_file_path, 'r') as file:
    # Assuming the table is stored in the text file as a simple table without any extra formatting
    lines = file.readlines()
    markdown_table = ''.join(lines)

# Convert the Markdown table to a plain text table
plain_text_table = tabulate([line.strip().split('|') for line in lines if '|' in line], headers="firstrow", tablefmt="plain")

# Read the plain text table into a DataFrame
df = pd.read_table(StringIO(plain_text_table), sep='\s\s+', engine='python')

# Clean up column names
df.columns = [col.strip() for col in df.columns]

# Specify the Excel file path
excel_file_path = 'output_table_from_text.xlsx'

# Write the DataFrame to an Excel file
df.to_excel(excel_file_path, index=False)

print(f"Excel file '{excel_file_path}' created successfully.")

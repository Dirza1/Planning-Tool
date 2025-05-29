from openpyxl import load_workbook
from collections import defaultdict

def main():
    wb = load_workbook(filename = "Value Stream 02Apr2025.xlsx")
    ws = wb.active
    print(wb.sheetnames)





if __name__ == "__main__":
    main()
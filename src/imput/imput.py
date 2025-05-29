from openpyxl import load_workbook
from collections import defaultdict

def main():
    wb = load_workbook(filename = "Value Stream 02Apr2025.xlsx")
    print(wb.sheetnames)
    for name in wb.sheetnames:
        if name == "California (50)":
            print (name)
        else:
            print ("not California mate")





if __name__ == "__main__":
    main()
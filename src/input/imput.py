from openpyxl import load_workbook
from collections import defaultdict
from gui.program_selection import program_selection

def value_stream():
    wb = load_workbook(filename = "Value Stream 02Apr2025.xlsx")
    posible_programs = wb.sheetnames
    selected_programs:list[str] = program_selection(posible_programs)

    for program in selected_programs:
        ws = wb[program]
        c = ws["A2"]
        thaw_date = input(f"What is the thaw date of {program}? Please use DD-MMM-YYYY format. ")
        c.value = thaw_date
        print(f"The thaw date is: {c.value}")

        wb.save("Value Stream 02Apr2025.xlsx")




if __name__ == "__main__":
    value_stream()
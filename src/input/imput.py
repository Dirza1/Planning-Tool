from openpyxl import load_workbook
from collections import defaultdict
from gui.program_selection import program_selection

def value_stream():
    wb = load_workbook(filename = "Value Stream 02Apr2025.xlsx")
    posible_programs:list[str] = wb.sheetnames
    selected_programs:list[str] = program_selection(posible_programs)

    for program in selected_programs:
        ws = wb[program]
        c = ws["A2"]
        
        thaw_date:str = input(f"What is the thaw date of {program}? Please use DD-Mmm-YYYY format. ")
        batch_number:str = input(f"What is the batch number of {program}? Please put in the full batch number in xx(x).xxx(x) format. ")
        c.value = thaw_date

        for row in ws.iter_rows():
            for cel in row:
                if not isinstance(cel.value, str):
                    continue
                data:str = cel.value.strip()
                words:list = data.split(" ")
                new_words = [batch_number if word == "XX.XXX" else word for word in words]
                joined: str = " ".join(new_words)

                if joined != cel.value:
                    cel.value = joined

        wb.save("Value Stream 02Apr2025.xlsx")





if __name__ == "__main__":
    value_stream()
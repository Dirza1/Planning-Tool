from openpyxl import load_workbook
from collections import defaultdict
from gui.program_selection import program_selection
from datetime import datetime
from datetime import date

def value_stream():
    value_stream_file = load_workbook(filename = "Value Stream 02Apr2025.xlsx", data_only=True)
    daily_planning_file = load_workbook(filename="Daily planning.xlsx", data_only=True)
    posible_programs:list[str] = value_stream_file.sheetnames
    selected_programs:list[str] = program_selection(posible_programs)

    for program in selected_programs:
        batch_number:str = input(f"What is the batch number of {program}? Please put in the full batch number in xx(x).xxx(x) format. ")
        program_sheet = value_stream_file[program]
        replace_batch_number(program_sheet, program, batch_number)
        

        for col in program_sheet.iter_cols():
            column_date = (col[1].value)
            column_week_number:int = column_date.isocalendar()[1]
            column_year:int = column_date.isocalendar()[0]
            for cel in col:
                if cel.row < 3:
                    pass
                if cel.column < 2:
                    pass
                if cel.value == "":
                    break
                week_planning = daily_planning_file[f"Week {column_week_number} of {column_year}"]
                
                for coll in week_planning.iter_cols():
                    if col[0] != column_date:
                        continue
                    for cell in coll:
                        if cell[2].value == "sv":
                            break
                        elif cell.row < 10:
                            continue
                        elif cell.value != "":
                            continue
                        else:
                            pass





                
    reset_batch_number(program_sheet, program, batch_number)
    value_stream_file.save("Value Stream 02Apr2025.xlsx")


def replace_batch_number(program_sheet, batch_number):
    
    for row in program_sheet.iter_rows():
        for cel in row:
            if not isinstance(cel.value, str):
                continue
            data:str = cel.value.strip()
            words:list = data.split(" ")
            new_words = [batch_number if word == "XX.XXX" else word for word in words]
            joined: str = " ".join(new_words)

            if joined != cel.value:
                cel.value = joined

def reset_batch_number(program_sheet, batch_number):

    for row in program_sheet.iter_rows():
        for cel in row:
            if not isinstance(cel.value, str):
                continue
            data:str = cel.value.strip()
            words:list = data.split(" ")
            new_words = ["XX.XXX" if word == batch_number else word for word in words]
            joined: str = " ".join(new_words)

            if joined != cel.value:
                cel.value = joined


if __name__ == "__main__":
    value_stream()
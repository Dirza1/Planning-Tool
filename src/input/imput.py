from openpyxl import load_workbook
from collections import defaultdict
from gui.program_selection import program_selection
from datetime import datetime
from datetime import date

def value_stream():
    value_stream_file = load_workbook(filename = "Value Stream 02Apr2025.xlsx", data_only=True)
    posible_programs:list[str] = value_stream_file.sheetnames
    selected_programs:list[str] = program_selection(posible_programs)

    for program in selected_programs:
        program_sheet = value_stream_file[program]
        
        """
        batch_number:str = input(f"What is the batch number of {program}? Please put in the full batch number in xx(x).xxx(x) format. ")
        
        for row in program_sheet.iter_rows():
            for cel in row:
                if not isinstance(cel.value, str):
                    continue
                data:str = cel.value.strip()
                words:list = data.split(" ")
                new_words = [batch_number if word == "XX.XXX" else word for word in words]
                joined: str = " ".join(new_words)

                if joined != cel.value:
                    cel.value = joined"""
        
        
        for col in program_sheet.iter_cols():
            column_date_value:str = str(col[1].value)
            print(type(column_date_value))
            column_date = datetime.strptime(column_date_value.strip(),"%d-%b-%Y")
            column_week_number:int = column_date.isocalendar()[1]
            print(f"{column_week_number=}")
            """for cel in col:
                if cel.row < 2:
                    pass
                if cel.column < 3:
                    pass
                if cel.value == "":
                    break"""

                

        value_stream_file.save("Value Stream 02Apr2025.xlsx")





if __name__ == "__main__":
    value_stream()
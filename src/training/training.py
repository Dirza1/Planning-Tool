import csv
from collections import defaultdict

def main() -> None:
    """
    This function is to create a default dict. This dict contains the operator name as a key and then a list of tupols with training status.
    This tupol is (Curiculum name, Bool). This dictionary will be passed on to the function that will display if people are trained.
    """
    
    training_status: defaultdict = defaultdict(list)
    with open("report (46).csv","r",encoding="utf-8",errors="ignore") as file:
        reader = csv.DictReader(file,delimiter=",")
        for row in reader:
            name = row["First Name"] + row["Last Name"] 
            
            if any(row["Curriculum Title"] == t for t, _ in training_status[name]):
                continue

            if row["Curriculum Complete"] == "Yes":
                training_status[name].append((row["Curriculum Title"],True))
            else:
                training_status[name].append((row["Curriculum Title"],False))
    
    for name,training in training_status.items():
        for check in training: 
            print(f"{name} is {check[1]} voor {check[0]}")

if __name__ == "__main__":
    main()
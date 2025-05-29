import csv
from collections import defaultdict

def main():

    daily_tasks: defaultdict = defaultdict(list)
    with open("imput.csv", encoding="UTF-8", errors="ignore") as file:
        raw_reader = csv.reader(file)
        raw_headers = next(raw_reader)
        clean_headers = [h.strip().lstrip('\ufeff') for h in raw_headers]
        reader = csv.DictReader(file, fieldnames=clean_headers, delimiter=",")
        
        for row in reader:
            task_name = row["task"]
            task_duration = row["duration (in hours)"]
            task_title = row["title"]
            task_related_quriculum = row["related quriculum"]

            total_task = (task_duration, task_title, task_related_quriculum)
            daily_tasks[task_name] = total_task
        
    
    print(daily_tasks)



if __name__ == "__main__":
    main()
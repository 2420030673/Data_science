import pandas as pd

data = {
    "roll_no": [101, 102, 103, 104, 105],
    "name": ["Dhana", "Rahul", "Anjali", "Kiran", "Sneha"],
    "age": [19, 20, 19, 20, 19],
    "section": ["A", "B", "A", "C", "B"],
    "branch": ["CSE", "CSE", "ECE", "IT", "CSE"]
}

df = pd.DataFrame(data)
df.to_csv('student.csv')


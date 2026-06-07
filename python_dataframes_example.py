import pandas as pd

students = {
	"name": ["ramesh", "riya", "haran", "krishmi"],
	"age": [35, 31, 5, 2],
	"CGPA":[8,9,10,9.5]
}

df = pd.DataFrame(students)

print(df)
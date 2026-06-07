import pandas as pd

students = {
	"name": ["ramesh", "riya", "haran", "krishmi"],
	"age": [35, 31, 5, 2],
	"CGPA":[8,9,10,9.5]
}

df = pd.DataFrame(students, index=["ochaye", "pachaye", "pochaye", "supaye"])

print(df)

print(df.loc["pachaye"])

print(df.iloc[1])

df["medium"] = ["Tamil", "English", "english", "English"]

new_student = {
	"name": "pecha",
	"age":20,
	"CGPA":9,
	"medium":"tamil"
}

std4 = pd.DataFrame(new_student, index=["apsulkaro"])

df = pd.concat([df, std4])

print(df)
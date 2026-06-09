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

df1 = pd.read_csv("customers-100.csv", index_col="Customer Id")

#print(df1.loc["DD37Cf93aecA6Dc", ["First Name", "Last Name"]])

#print(df1[["Email","First Name"]])


#df2 = pd.read_json("airports.json")

#print(df2)





df1 = pd.read_csv("customers-100.csv", index_col="Customer Id")

df2 = pd.read_json("airports.json")

#print(df2)

#print(df1)


result = df1[ (df1['Index'] >= 90) & (df1['Subscription Date'] > "2020-06-02") ]

#print(result)





print(df["CGPA"].min())



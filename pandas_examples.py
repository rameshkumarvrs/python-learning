import pandas as pd


#age = [25,28,35,37]

age ={
	"ramesh": 35,
	"riya":28,
	"haran": 5
}


series = pd.Series(age)


print(series)


print(series[series<20])
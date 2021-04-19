import json
import pandas as pd

def getCategory(bmi):

	if bmi <= 18.4:
		return "Underweight"

	elif (18.5 <= bmi and bmi <= 24.9):
		return "Normal weight"

	elif (25 <= bmi and bmi <= 29.9):
		return "Overweight"

	elif (30 <= bmi and bmi <= 34.9):
		return"Moderately Obese"

	elif (35 <= bmi and bmi <= 39.9):
		return "Severly Obese"

	else:
		return "Very Severly Obese"

def getRisk(bmi):

	if bmi <= 18.4:
		return "Malnutrition Risk"

	elif (18.5 <= bmi and bmi <= 24.9):
		return "Low risk"

	elif (25 <= bmi and bmi <= 29.9):
		return "Enhanced risk"

	elif (30 <= bmi and bmi <= 34.9):
		return "Medium risk"

	elif (35 <= bmi and bmi <= 39.9):
		return "High risk"

	else:
		return "High risk"

def getOverallBMIData(json_bmi_data):

	## convert json array to dataframwe
	df = pd.json_normalize(json.loads(json_bmi_data))

	## calculation of bmi
	df["BM_in_kg_per_m2"] = df["WeightKg"]/((df["HeightCm"] / 100)**2) # since height is in cm and bmi is 
	
	## get category and risk using calculated bmi value
	df["Category"] = df["BM_in_kg_per_m2"].apply(getCategory)
	df["Risk"] = df["BM_in_kg_per_m2"].apply(getRisk)

	## get overweight count
	overweight_count = df[df["Category"] == "Overweight"].shape[0]

	## convert back to json
	result = df.to_json(orient = "records") # to make list of json objets
	json_array = json.loads(result)

	## append overweight count
	json_array.append({"Overweight Count": overweight_count})

	return json_array

bmi_data = """[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, 
				{"Gender": "Male", "HeightCm": 161, "WeightKg": 85 }, 
				{"Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, 
				{"Gender": "Female", "HeightCm": 166, "WeightKg": 62}, 
				{"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, 
				{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
			"""

getOverallBMIData(bmi_data)
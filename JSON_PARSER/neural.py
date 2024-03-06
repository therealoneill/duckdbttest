import json
import pandas as pd

with open('D:\github\JSON_PARSER\sucker.json', 'r') as f:
	json_object = json.load(f)

json_components = json_object.get('components',[])

rows =[]

for comps in json_components:
	#print(comps['name'] + comps['type'])
	row = [
		comps.get('name',''),
		comps.get('type','')
	]
	rows.append(row)

df = pd.DataFrame(rows, columns=['Name', 'Type'])

#print(json_components)
print(df)

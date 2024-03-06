import json

def flatten_json(obj):
	ret = {}

	def flatten(x, flattened_key=""):
		if type(x) is dict:
			for current_key in x:
				flatten(x[current_key], flattened_key + "_")
		if type(x) is list:
			i = 0
			for elem in x:
				flatten(elem, flattened_key + str(i) + "_")
		else:
		### x === string, integer, etc
			ret[flattened_key[:-1]] = x

	flatten(obj)
	return ret


if __name__ == "__main__":
	file = 'D:\github\JSON_PARSER\sucker.json'
	with open(file) as file:
		data = json.loads(file)
	flatten_json(data)

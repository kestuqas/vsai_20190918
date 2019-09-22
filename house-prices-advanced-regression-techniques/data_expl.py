def expl():
	file = '/home/kestutis/projects/vsai_20190918/house-prices-advanced-regression-techniques/data.txt'
	with open(file, 'r') as f:
		data = f.readlines()
	data_dict = {} 
	for term in data:
		term = term.strip()
		term = term.split(':')
		data_dict[term[0]] = term[1]
	return data_dict

def expl(file_loc = './data.txt'):
	with open(file_loc, 'r') as f:
		data = f.readlines()
	data_dict = {} 
	for term in data:
		term = term.strip()
		term = term.split(':')
		data_dict[term[0]] = term[1]
	return data_dict
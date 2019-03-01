file_name = 'Adjusted net national income per capita (databank.worldbank.org).txt'

f = open(file_name, 'r', encoding='utf8')

start = 1970
end = 2016
result = [[] for i in range(end-start+1)]

first = True
for line in f.readlines():
	if first:
		first = False
		continue
	token = line.split('\t')
	name = token[2]
	code = token[3]
	data = token[4:]
	for i in range(len(data)):
		value = data[i]
		if value == '..':
			value = '-'
		result[i].append({
			'label': name,
			'value': value.strip()
		})
f.close()

f = open('result.json', 'w', encoding='utf8')

f.write('[')
for i, day in enumerate(result):
	f.write('[')
	for j, row in enumerate(day):
		f.write('{{label: \'{}\', value: \'{}\'}}'.format(row['label'], row['value']))
		if j < len(day) - 1:
			f.write(', ')
	f.write(']')
	if i < len(result) - 1:
		f.write(', ')
f.write(']')

f.close()
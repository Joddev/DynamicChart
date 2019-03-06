import sys

class NameFilter:
	filter_dict = {
		'Egypt, Arab Rep.': 'Egypt',
		'Iran, Islamic Rep.': 'Iran',
		'Korea, Dem. People’s Rep.': 'North Korea',
		'Korea, Rep.': 'South Korea',
		'Venezuela, RB': 'Venezuela',
		'Yemen, Rep.': 'Yemen',
		'United Arab Emirates': 'UAE',
		'United Kingdom': 'UK',
		'United States': 'USA',
		'Syrian Arab Republic': 'Syria'
	}
	
	@classmethod
	def filter(cls, name):
		try:
			return cls.filter_dict[name].replace('\'','\\\'')
		except KeyError:
			return name.replace('\'','\\\'')

if len(sys.argv) < 2:
	raise Exception('need file as argument')

file_name = sys.argv[1]

f = open(file_name, 'r', encoding='utf8')

start = 1960
end = 2017
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
		value = data[i].strip()
		if value == '..':
			value = '-'
		result[i].append({
			'label': NameFilter.filter(name),
			'value': value
		})
f.close()

f = open('../../src/data/result.js', 'w', encoding='utf8')

f.write('const stats = [')
for i, day in enumerate(result):
	f.write('[')
	for j, row in enumerate(day):
		f.write('{{label: \'{}\', value: \'{}\'}}'.format(row['label'], row['value']))
		if j < len(day) - 1:
			f.write(', ')
	f.write(']')
	if i < len(result) - 1:
		f.write(', ')
f.write(']\n')
f.write('const dates = [')
for date in range(start, end + 1):
	f.write('\'{}\''.format(date))
	if date < end:
		f.write(', ')
f.write(']\n')
f.write('export { stats, dates }\n')

f.close()

f = open('Life expeectancy at birth(databank.worldbank.org).txt', 'r', encoding='utf8')

result = [[] for i in range(18)]

cand = [
	'Australia',
	'Austria',
	'Bermuda',
	'Canada',
	'Cyprus',
	'Faroe Islands',
	'France',
	'Greece',
	'Hong Kong SAR, China',
	'Iceland',
	'Ireland',
	'Israel',
	'Italy',
	'Japan',
	'Korea, Rep.',
	'Liechtenstein',
	'Luxembourg',
	'Macao SAR, China',
	'Malta',
	'Netherlands',
	'New Zealand',
	'Norway',
	'Singapore',
	'Spain',
	'Sweden',
	'Switzerland',
]

first = True
for line in f.readlines():
	if first:
		first = False
		continue
	token = line.split('\t')
	name = token[2]
	code = token[3]
	data = token[4:-2]
	if name not in cand:
		continue
	for i in range(len(data)):
		value = data[i]
		if value == '..':
			value = '-'
		result[i].append({
			'label': name,
			'value': value
		})
f.close()

f = open('result.json', 'w', encoding='utf8')

f.write('[')
for day in result:
	f.write('[')
	for i, row in enumerate(day):
		f.write('{{label:"{}",value:"{}"}},'.format(row['label'], row['value']))
	f.write('],')
f.write(']')

f.close()
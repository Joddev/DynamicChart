import sys

if len(sys.argv) < 2:
   raise Exception("Need input file")


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


class CountryData:
   def __init__(self, name, value):
      self.name = NameFilter.filter(name)
      self.value = value
   
   def json(self):
      return '{{label: \'{}\', value: \'{}\'}}'.format(self.name, self.value)

file_name = sys.argv[1]
title = ''
data = {}
with open(file_name, 'r') as fr:   
   for i, line in enumerate(fr.readlines()):
      tokens = line.split('\t')
      # header
      if i == 0:
         years = [index.split()[0] for index in tokens[4:]]
         print(years)
      # content
      else:
         if title == '':
            title = tokens[0]
         value_by_year = tokens[4:]
         country_name = tokens[2].strip()
         for j, value in enumerate(value_by_year):
            try:
               value = float(value)
            except ValueError:
               value = '-'
            try:
               data[years[j]].append(CountryData(country_name, value))               
            except KeyError:
               data[years[j]] = [CountryData(country_name, value)]

data_year_filtered = {year: values for year, values in data.items() if len([d for d in values if d.value != '-']) > 0}
top = set()
maximum = 0
for values in data_year_filtered.values():
   values.sort(key=lambda d: d.value if d.value != '-' else -10, reverse=True)
   maximum = max(maximum, values[0].value)
   for d in values[:10]:
      top.add(d.name)

dates = [date for date in data_year_filtered.keys()]
dates.sort()
print(dates)

with open('../../src/data/result.js', 'w') as fw:
   fw.write('const stats = [')
   for year in dates:
      fw.write('[')
      filtered = [data for data in data_year_filtered[year] if data.name in top]
      print(year, [data.value for data in filtered])
      for data in filtered:
         fw.write(data.json())
         if data != filtered[-1]:
            fw.write(', ')
      fw.write(']')
      if year != dates[-1]:
         fw.write(', ')
   fw.write(']\n')
   fw.write('const dates = [')
   for year in dates:
      fw.write('\'{}\''.format(year))
      if year != dates[-1]:
         fw.write(', ')
   fw.write(']\n')
   fw.write('const maximum = {}\n'.format(maximum))
   fw.write('export { stats, maximum, dates }\n')
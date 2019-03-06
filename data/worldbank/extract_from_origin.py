import sys

if len(sys.argv) < 2:
   raise Exception("Need input file")


class NameFilter:
   filter_dict = {
      # 'American Samoa': 'Sa\'moa'
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
with open(file_name, 'r', encoding='utf-8') as fr:   
   for i, line in enumerate(fr.readlines()):
      tokens = line.split('\t')
      # header
      if i == 0:
         years = [index.split()[0] for index in tokens[4:]]
      # content
      else:
         if title == '':
            title = tokens[0]
         value_by_year = tokens[4:]
         country_name = tokens[2].strip()
         for i, value in enumerate(value_by_year):
            try:
               value = float(value)
            except ValueError:
               value = '-'
            try:
               data[years[i-1]].append(CountryData(country_name, value))               
            except KeyError:
               data[years[i-1]] = [CountryData(country_name, value)]

data_year_filtered = {year: values for year, values in data.items() if len([d for d in values if d.value != '-']) > 0}
top = set()
for values in data_year_filtered.values():
   values.sort(key=lambda d: d.value if d.value != '-' else -10, reverse=True)
   for d in values[:6]:
      top.add(d.name)

dates = [date for date in data_year_filtered.keys()]
dates.sort()

with open('resulst.txt', 'w', encoding='utf-8') as fw:
   fw.write('const stats = [')
   for year in dates:
      fw.write('[')
      filtered = [data for data in data_year_filtered[year] if data.name in top]
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
   fw.write('export { stats, dates }\n')
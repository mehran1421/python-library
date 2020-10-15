import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

#
plt.style.use('fivethirtyeight')

data=pd.read_csv('data.csv')

ids=data['tedad']
lang_responses=data['zaban']

language_counter=Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))


# with open('data.csv') as csv_file:
#     csv_reader=csv.DictReader(csv_file)
#
#     language_counter=Counter()
#
#     for row in csv_reader:
#         language_counter.update(row['zaban'].split(';'))
#
language=[]
popularity=[]
# most_common=تعداد زبان هایی که بیشترین رای را دارند را نمایش میدهد
for item in language_counter.most_common(7):
    language.append(item[0])
    popularity.append(item[1])

# print(language_counter)
# Counter({'python': 5, 'java': 4, 'cpp': 3, 'html': 2, 'django': 2, 'css': 1})
# print(language_counter.most_common(3))
# [('python', 5), ('java', 4), ('cpp', 3)]
# plt.bar(language,popularity)
plt.barh(language,popularity)

plt.xlabel("Ages")
# plt.ylabel("Median Salary (USD)")
plt.title("Median Salary (USD) by Age")

plt.show()
print("===================================================")
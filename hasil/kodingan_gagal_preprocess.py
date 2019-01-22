import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# https://www.effectiveperlprogramming.com/2011/08/know-the-difference-between-utf8-and-utf-8/
import datetime
dataset = pd.read_csv("dataset.csv")
print(repr(dataset))
print(dataset.describe(include='all'))
# dataset_with_dummies = pd.get_dummies(dataset,prefix_sep='--')
# dataset_with_dummies = pd.get_dummies(dataset,prefix_sep='--')
# print(dataset_with_dummies.head())
print(dataset.keys())
attributes = ['URL', 'URL_LENGTH', 'NUMBER_SPECIAL_CHARACTERS', 'CHARSET', 'SERVER',
       'CONTENT_LENGTH', 'WHOIS_COUNTRY', 'WHOIS_STATEPRO', 'WHOIS_REGDATE',
       'WHOIS_UPDATED_DATE', 'TCP_CONVERSATION_EXCHANGE',
       'DIST_REMOTE_TCP_PORT', 'REMOTE_IPS', 'APP_BYTES', 'SOURCE_APP_PACKETS',
       'REMOTE_APP_PACKETS', 'SOURCE_APP_BYTES', 'REMOTE_APP_BYTES',
       'APP_PACKETS', 'DNS_QUERY_TIMES', 'Type']

encoding = ["CHARSET", "SERVER", "WHOIS_COUNTRY", "WHOIS_STATEPRO", 'WHOIS_REGDATE',
       'WHOIS_UPDATED_DATE']
fmt = '%d/%m/%Y %H:%M'

date_key =lambda x: datetime.datetime.strptime(x, fmt)

# nyoba
charset = []
server = []
whois_country = []
whois_statepro = []
whois_regdate = []
whois_updated_date = []
malform_whois_regdate = []
malform_whois_updated_date = []
dataset['SERVER'] = dataset['SERVER'].factorize()[0]

for index, row in dataset.iterrows():
   # print(attributes[7], row[attributes[7]])
   # print(tes, row[tes])
	if(row["CHARSET"] not in charset and row["CHARSET"] != "None"):
		charset.append(row["CHARSET"])
	if(row["SERVER"] not in server and row["SERVER"] != "None"):
		print(index, row["SERVER"])
		server.append(row["SERVER"])
	if(row["WHOIS_COUNTRY"] not in whois_country and row["WHOIS_COUNTRY"] != "None"):
		whois_country.append(row["WHOIS_COUNTRY"])
	if(row["WHOIS_STATEPRO"] not in whois_statepro and row["WHOIS_STATEPRO"] != "None"):
		whois_statepro.append(row["WHOIS_STATEPRO"])
	if(row["WHOIS_REGDATE"] not in whois_regdate and row["WHOIS_REGDATE"] != "None"):
		try:
			date_key(row["WHOIS_REGDATE"])				
			whois_regdate.append(row["WHOIS_REGDATE"])
		except:
			malform_whois_regdate.append(row["WHOIS_REGDATE"])
	if(row["WHOIS_UPDATED_DATE"] not in whois_updated_date and row["WHOIS_UPDATED_DATE"] != "None"):
		whois_updated_date.append(row["WHOIS_UPDATED_DATE"])
		try:
			date_key(row["WHOIS_UPDATED_DATE"])				
			whois_updated_date.append(row["WHOIS_UPDATED_DATE"])
		except:
			malform_whois_updated_date.append(row["WHOIS_UPDATED_DATE"])



# charset.sort()

sorted(charset)
sorted(server)
sorted(whois_country)
sorted(whois_statepro)
sorted(whois_regdate, date_key)
sorted(whois_updated_date, date_key)

# print(charset)
# print(server)
# print(whois_country)
# print(whois_statepro)
# print(whois_regdate)
# print(whois_updated_date)
# print(malform_whois_regdate)
# print(malform_whois_updated_date)


exit()
# print(charset.index("None"))
charset_dict = dict()
charset_dict["None"] = "None"

index = 0

for i in charset:
	index += 1
	charset_dict[charset[index-1]] = index

print(charset_dict)


# change
for index, row in dataset.iterrows():
	dataset.loc[[index], "CHARSET"] = charset_dict[row["CHARSET"]]

for index, row in dataset.iterrows():
   print(tes, row[tes])

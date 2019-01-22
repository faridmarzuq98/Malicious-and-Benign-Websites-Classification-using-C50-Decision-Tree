import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# https://www.effectiveperlprogramming.com/2011/08/know-the-difference-between-utf8-and-utf-8/
import datetime
import pprint
dataset = pd.read_csv("dataset.csv")
# print(repr(dataset))
# print(dataset.describe(include='all'))
# dataset_with_dummies = pd.get_dummies(dataset,prefix_sep='--')
# dataset_with_dummies = pd.get_dummies(dataset,prefix_sep='--')
# print(dataset_with_dummies.head())
# print(dataset.keys())
attributes = ['URL', 'URL_LENGTH', 'NUMBER_SPECIAL_CHARACTERS', 'CHARSET', 'SERVER',
       'CONTENT_LENGTH', 'WHOIS_COUNTRY', 'WHOIS_STATEPRO', 'WHOIS_REGDATE',
       'WHOIS_UPDATED_DATE', 'TCP_CONVERSATION_EXCHANGE',
       'DIST_REMOTE_TCP_PORT', 'REMOTE_IPS', 'APP_BYTES', 'SOURCE_APP_PACKETS',
       'REMOTE_APP_PACKETS', 'SOURCE_APP_BYTES', 'REMOTE_APP_BYTES',
       'APP_PACKETS', 'DNS_QUERY_TIMES', 'Type']

encoding = ["CHARSET", "SERVER", "WHOIS_COUNTRY", "WHOIS_STATEPRO", 'WHOIS_REGDATE',
       'WHOIS_UPDATED_DATE']

dict_charset = dict()
dict_server = dict()
dict_whois_country = dict()
dict_whois_statepro = dict()
dict_whois_regdate = dict()
dict_whois_updated_date = dict()

dataset["CHARSET"], uniq_charset = dataset['CHARSET'].factorize(sort = True)
dataset["SERVER"], uniq_server  = dataset['SERVER'].factorize(sort = True)
dataset["WHOIS_COUNTRY"], uniq_whois_country = dataset['WHOIS_COUNTRY'].factorize(sort = True)
dataset["WHOIS_STATEPRO"], uniq_whois_statepro = dataset['WHOIS_STATEPRO'].factorize(sort = True)
dataset["WHOIS_REGDATE"], uniq_whois_regdate = dataset['WHOIS_REGDATE'].factorize(sort = True)
dataset["WHOIS_UPDATED_DATE"], uniq_whois_updated_date = dataset['WHOIS_UPDATED_DATE'].factorize(sort = True)

# print(list(a))
# dict_server[list(a)] = list(b)
index = 0
for i in list(uniq_charset):
	# print()
	dict_charset[index] = i
	index += 1

index = 0
for i in list(uniq_server):
	# print()
	dict_server[index] = i
	index += 1

index = 0
for i in list(uniq_whois_country):
	# print()
	dict_whois_country[index] = i
	index += 1

index = 0
for i in list(uniq_whois_statepro):
	# print()
	dict_whois_statepro[index] = i
	index += 1

index = 0
for i in list(uniq_whois_regdate):
	# print()
	dict_whois_regdate[index] = i
	index += 1

index = 0
for i in list(uniq_whois_updated_date):
	# print()
	dict_whois_updated_date[index] = i
	index += 1

pprint.pprint("charset")
pprint.pprint(dict_charset)
pprint.pprint("server")
pprint.pprint(dict_server)
pprint.pprint("whois country")
pprint.pprint(dict_whois_country)
pprint.pprint("whois statepro")
pprint.pprint(dict_whois_statepro)
pprint.pprint("whois regdate")
pprint.pprint(dict_whois_regdate)
pprint.pprint("whois updated date")
pprint.pprint(dict_whois_updated_date)

#dataset.to_csv("dataset_encoded.csv")
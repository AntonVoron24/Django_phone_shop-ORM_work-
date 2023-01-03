import csv
with open('phones.csv', 'r') as file:
	phones = list(csv.DictReader(file, delimiter=';'))

	for phone in phones:
		print(phone.get('lte_exists'))
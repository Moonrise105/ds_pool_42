import sys

def searchByKeyValue():
	companies_orig = {
	'Apple' : 'AAPL',
	'Microsoft' : 'MSFT',
	'Netflix' : 'NFLX',
	'Tesla' : 'TSLA',
	'Nokia' : 'NOK'
	}
	stocks_orig = {
	'AAPL' : 287.73,
	'MSFT' : 173.79,
	'NFLX' : 416.90,
	'TSLA' : 724.88,
	'NOK' : 3.37
	}
	companies = {k.lower():v.lower() for k,v in companies_orig.items()}
	stocks = {k.lower():v for k,v in stocks_orig.items()}
	av = sys.argv
	ac = len(av)
	if (ac != 2):
		sys.exit()

	arg = av[1].lower()
	try:
		ind = list(companies.values()).index(arg)
	except ValueError:
		print("Unknown ticker")
		sys.exit()
	print(list(companies_orig.keys())[ind], stocks[arg])

if __name__ == '__main__':
	searchByKeyValue()
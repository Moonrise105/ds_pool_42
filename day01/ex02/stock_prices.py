import sys

def searchByKey():
	companies = {
	'Apple' : 'AAPL',
	'Microsoft' : 'MSFT',
	'Netflix' : 'NFLX',
	'Tesla' : 'TSLA',
	'Nokia' : 'NOK'
	}
	stocks = {
	'AAPL' : 287.73,
	'MSFT' : 173.79,
	'NFLX' : 416.90,
	'TSLA' : 724.88,
	'NOK' : 3.37
	}
	companies = {k.lower():v.lower() for k,v in companies.items()}
	stocks = {k.lower():v for k,v in stocks.items()}
	av = sys.argv
	ac = len(av)
	if (ac != 2):
		sys.exit()

	if av[1].lower() in companies:
		print(stocks[companies[av[1].lower()]])
	else:
		print("Unknown company")

if __name__ == '__main__':
	searchByKey()
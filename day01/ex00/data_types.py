def data_type():
	lst = [type(0), type(""), type(.1), type(True), type([]), type(dict()), type(()), type(set())]
	print('[' + ', '.join(map(lambda x: str(x).split("\'")[1], lst)) + ']')

if __name__ == "__main__":
	data_type()

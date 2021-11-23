
def replaceByPos(s, pos, char):
	return s[:pos] + char + s[pos+1:] 	

def replacer():
	open('ds.tsv', 'w').close()
	with open("ds.csv", "r") as inp:
		with open("ds.tsv", "a") as out:
			for row in inp:
				q = False
				j = 0
				for i in row:
					if i == '\"':
						q = not q
					elif i == ',' and not q:
						row = replaceByPos(row, j, "\t")
				
					j += 1
				out.write(row)

if __name__ == '__main__':
	replacer()
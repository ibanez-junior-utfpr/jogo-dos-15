linha1 = [ 1, 2, 3, 4 ]
linha2 = [ 5, 6, 7, 8 ]
linha3 = [ 9, 10, 11, 12 ]
linha4 = [ 13, 14, 15, 0 ]
tabela = [ linha1, linha2, linha3, linha4 ]
txt = "{:>5}"
for x in tabela:
	det = ""
	for y in x:
    	det += txt.format(str(y))
	print(det)

print(tabela[3][3])
print(tabela[2][2])
print(tabela[1][1])
print(tabela[0][0])

def ind(numbers):
	wnum = str(numbers).replace("-","")

	result = ""
	mins="Minus "
	words = ["Nol","Satu","Dua","Tiga","Empat","Lima","Enam","Tujuh","Delapan","Sembilan"]
	head="Se"
	tail1=["","Puluh","Ratus","Ribu","Puluh","Ratus","Juta","Puluh Juta","Ratus Juta","Miliar","Puluh Miliar","Ratus Miliar","Triliun"]
	tail2=["Belas"]

	bol = True
	for y,x in zip(range(len(wnum)-1,-1,-1),wnum):
		if words[int(x)]=="Nol":
			if 3<=y<=5 and bol:
				result+="Ribu "
				bol = False
			else:
				bol = True
		else:
			result += words[int(x)] +" "+ tail1[y] + " "

	return result
print(ind(int(input())))
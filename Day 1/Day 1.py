with open("data.txt", "r") as f:
	data = f.readlines()
	increases = 0
	for i, val in enumerate(data):
		data[i] = int(val)
		if i > 0:
			if data[i] > data[i-1]:
				increases += 1
	print(increases)
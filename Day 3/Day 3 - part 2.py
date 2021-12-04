with open("data.txt", "r") as f:
	data = f.readlines()
	
	most_common, gamma, epsilon = [0 for i in range(len(data[0]))], [0 for i in range(len(data[0]))], [0 for i in range(len(data[0]))]

	for val in data:
		for i in range(len(val)):
			if val[i] == "1":
				most_common[i] += 1
			elif val[i] == "0":
				most_common[i] -= 1

	for i, val in enumerate(most_common):
		gamma[i] = 1 if val > 0 else 0
		epsilon[i] = 0 if val > 0 else 1

	gamma = [str(i) for i in gamma]
	epsilon = [str(i) for i in epsilon]

	print(int("".join(gamma[:-1]), 2)*int("".join(epsilon[:-1]), 2))
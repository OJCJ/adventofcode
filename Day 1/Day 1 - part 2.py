with open("data.txt", "r") as f:
	data = f.readlines()
	increases = 0
	measurement_windows = []
	for i, val in enumerate(data):
		data[i] = int(val)
	while len(data) > 0:
		measurement_windows.append(sum(data[:min(len(data),3)]))
		data = data[1:]
	for i, val in enumerate(measurement_windows):
		if i > 0:
			if val > measurement_windows[i-1]:
				increases += 1
	print(increases)
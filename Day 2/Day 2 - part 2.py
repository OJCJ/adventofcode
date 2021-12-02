depth, horizontal, aim = 0, 0, 0

def forward(val):
	global horizontal, depth, aim
	horizontal += val
	depth += val*aim

def up(val):
	global aim
	aim -= val

def down(val):
	global aim
	aim += val

function_dictionary = {"forward":forward, "up":up, "down":down}

with open("data.txt", "r") as f:
	data = f.readlines()
	for i in data:
		cmd, val = i.split(" ")
		function_dictionary[cmd](int(val))

print(depth*horizontal)
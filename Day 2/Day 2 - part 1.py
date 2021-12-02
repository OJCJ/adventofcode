depth, horizontal = 0, 0

def forward(val):
	global horizontal
	horizontal += val

def up(val):
	global depth
	depth -= val

def down(val):
	global depth
	depth += val

function_dictionary = {"forward":forward, "up":up, "down":down}

with open("data.txt", "r") as f:
	data = f.readlines()
	for i in data:
		cmd, val = i.split(" ")
		function_dictionary[cmd](int(val))

print(depth*horizontal)
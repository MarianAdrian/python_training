


def histogram(values,names):
	if len(values) == len(names):
		for index in range(len(values)):
			print names[index] + "|" + "*" * values[index]




histogram([4, 9, 7],["horizontal","vertical","empty"])



"""
horizontal | ****
vertical | *********
empty | *******
"""




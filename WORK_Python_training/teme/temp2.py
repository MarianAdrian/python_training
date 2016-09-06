def walk(input):
	if len(input) != 0:
		if type(input[0]) != list:
			return [input[0]] + walk(input[1:])
		else:
			return walk(input[0]) + walk(input[1:])

	return []

print walk([4,[45,[67,7,[9],6,[8,9,[12,3]]],[5,9]]])

from pprint import pprint


data={
		"Frame1":{
					"id":2,
					"Signals":[
								{"Sgn1":[1,2]},
								{"Sgn2":[1,4]},
								]
				},
		"Frame2":{
					"id":5,
					"Signals":[
								{"Sgn1":[1,2]},
								{"Sgn3":[1,4]},
								]
				}
	}

def print_unique_signals(data):

	names=[]

	for frame in data:
		for signal in data[frame]["Signals"]:
			names += signal.keys()

	print list(set(names))

# print_unique_signals(data)
pprint(data)
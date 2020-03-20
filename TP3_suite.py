

from TP3 import *
import datetime
import json



#with open('data.txt','w') as outfile:
#	json.dump(data,outfile)


def farm_factory(farm_name, animal_description):

	my_current_farm = Farm(Farm_name)

	# for each animal in animal_description add it to the farm
	for my_animal in animal_description:
		my_current_farm.add_animal(my_animal[0], my_animal[1] , my_animal[2])
		
	return my_current_farm


if __name__ == "__main__":


	# Load JSON file into a variable
	import json
	with open ('C:/Users/marin/Desktop/JSON_test.json') as json_file:
		ata = json.load(json_file)


	print (data)
	
	# Create farms list
	farm_list = []

	# For each farm in JSON file, create it and add it to the farm list

	for my_farm in data["list_farms"]:

		farm_list.append(farm_factory(['Ferme de Marine'], ['animal list']))


	# The rest is the same as before.

	# We print the list of farms (and animals)
	for current_farm in farm_list:
		print(current_farm)


	# We start travelling to the future
	print("\nWe start the time...:\n")

	time_iteration = 0

	while time_iteration < 0:

		# Advance time of 28 days = 4 weeks
		future_farms_date = current_farms_date + datetime.timedelta(days = 28)

		print("\n\tAdvancing to : " + str(future_farms_date))

		time_iteration += 1

		for current_farm in farm_list:
			current_farm.pass_time(datetime.timedelta(weeks = 4))


		current_farms_date = future_farms_date



	# We print the list of farms (and animals)
	for current_farm in farm_list:
		print(current_farm)





def Remove(duplicate):
	final_list = []
	for num in duplicate:
		if num not in final_list:
			final_list.append(num)
	return final_list
	
duplicate = [-12, -78, -35, -42,-42,-12]
print(Remove(duplicate))

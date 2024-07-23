def create_list_of_tuples(lower_range, upper_range):
    return [(num, num**2) for num in range(lower_range, upper_range + 1)]

lower_range = int(input("Enter the lower range: "))
upper_range = int(input("Enter the upper range: "))


list_of_tuples = create_list_of_tuples(lower_range, upper_range)

print("List of tuples:", list_of_tuples)

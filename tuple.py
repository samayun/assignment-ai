def get_elements(tuple_data):
    fourth_from_start = tuple_data[3]
    fourth_from_end = tuple_data[-4]
    return fourth_from_start, fourth_from_end

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result = get_elements(my_tuple)
print(f"4th element from start: {result[0]}, 4th element from end: {result[1]}")
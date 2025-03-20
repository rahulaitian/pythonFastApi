def sort_by_second_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])
data = [(1, 5), (3, 2), (4, 8), (2, 1)]
sorted_data = sort_by_second_element(data)

print(sorted_data)
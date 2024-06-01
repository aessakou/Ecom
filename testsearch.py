import timeit

list_a = ["word" + str(i) for i in range(1000)]
list_b = ["word" + str(i) for i in range(500, 1500)]

# Method 1: Set Intersection
def method_set_intersection():
    set_b = set(list_b)
    return [word for word in list_a if word in set_b]

# Method 2: List Comprehension
def method_list_comprehension():
    return [word for word in list_a if word in list_b]

# Method 3: Set Intersection for both
def method_both_sets():
    set_a = set(list_a)
    set_b = set(list_b)
    return list(set_a & set_b)

# Timing the methods
time_set_intersection = timeit.timeit(method_set_intersection, number=1000)
time_list_comprehension = timeit.timeit(method_list_comprehension, number=1000)
time_both_sets = timeit.timeit(method_both_sets, number=1000)

print(f"Set Intersection: {time_set_intersection}")
print(f"List Comprehension: {time_list_comprehension}")
print(f"Both Sets Intersection: {time_both_sets}")

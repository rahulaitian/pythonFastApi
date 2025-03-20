# Find the sum of all even numbers from 1 to 100 using list comprehension.
sum_even = sum([x for x in range(1, 101) if x % 2 == 0])
print(sum_even)
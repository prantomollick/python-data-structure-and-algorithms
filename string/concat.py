from functools import reduce




test_list = ["best", "Gfg", "for", "is", "geeks"]

sort_order = [1, 3, 0, 2] 

print("The original list is: " + str(test_list))

# initializing join order 
sort_order = [1, 3, 0, 2, 4]

result = ''

for order in sort_order:
    result += test_list[order]




#list comprehension

result2 = ''.join(test_list[i] for i in sort_order)



test_list = [5, 6, "gfg ", 8, (5, 7), ' is', 9, ' best']

# String concatenation in Heterogeneous list
# using loop + conditions

result3 = ''

for ele in test_list: 
    if type(ele) == str:
        result3 += ele






result4 = "".join(filter(lambda i: isinstance(i, str), test_list))


result5 = reduce(lambda x, y: x + y if type(y) == str else x, test_list, "")


result6 = ''.join([ele for ele in test_list if isinstance(ele, str)])

print(result6)
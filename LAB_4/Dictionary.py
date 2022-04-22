dictionary = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81,
10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256,
17: 289, 18: 324, 19: 361, 20: 400, 21: 441, 22: 484, 23: 529,
24: 576, 25: 625, 26: 676, 27: 729, 28: 784, 29: 841, 30: 900}

# part a
print(dictionary)
# part b
for key, value in dictionary.items():
    print(key, value)

sum = 0
# part c
for value in dictionary:
    sum = sum + dictionary.get(value)
    print(sum)
# part d

dictionary.pop(10)
print(dictionary)


# Question 4
dictionary1 = {'Tony': 41, 'Steve': 39, 'Nat': 35}
dictionary2 = {'Bruce': 41, 'Clint': 35, 'Thor': 38}


merged_dictionary = dict()
merged_dictionary.update(dictionary1)
merged_dictionary.update(dictionary2)

for key, value in merged_dictionary.items():
    print(key, ":", value)

merged_dictionary.pop('Nat')
print(merged_dictionary)
# I cannot use 'reverse=' in my computer, I dont know why but I learned how can I use it.
sorted_dict = sorted(merged_dictionary.values())
print(sorted_dict)

print("Maximum element: ")
maximum = sorted_dict[-1]
print(maximum)

print("Minimum element: ")
minimum = sorted_dict[0]
print(minimum)









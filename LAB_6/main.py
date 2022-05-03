x = int(input("Please enter a number: "))
my_list = []

for i in range(x):
    my_list.append(i+1)



print(my_list)
sigma_list = []
sigma_value = (lambda n: ((n - 3) / pow(n, 2)))
for i in range(x):
    sigma_list.append(sigma_value(i+1))

print(sigma_list)
total = 0
for i in range(x):

    total = total + sigma_list[i]


print(total)

#Question 2

pi_list = []
pi_value = (lambda n: ((n / (n + 2))-10))

for i in range(x):
    pi_list.append(float(pi_value(i+1)))

print(pi_list)
total2 = 1
for i in range(x):

    total2 = total2 * pi_list[i]

print(total2)











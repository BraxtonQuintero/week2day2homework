# Exercise 1
# Use the following list - [1,11,14,5,8,9]

lists = [1,11,14,5,8,9]

expected_list = []

for list in lists:

    if list < 10:
        expected_list.append(list)

print(expected_list)

expected_list = [lists for list in lists if list < 10]
print(expected_list.append())


# Exercise 2

names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']

names_1 = []

def long_words(n, names):
	names_1 = []
	names = str.split(" ")
	for name in names:
		if len(name) > 3:
			names_1.append(names)
	return(names)
print(names_1)
 
names = [names for name in names if len(name) > 3 return]
print(names_1.append)
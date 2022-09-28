# Exercise 1
# Use the following list - [1,11,14,5,8,9]

lists = [1, 11, 14, 5, 8, 9]

expected_list = []

for list in lists:

    if list < 10:
        expected_list.append(list)

print(expected_list)

new_list = [list for list in lists if list < 10]
print(new_list)


# Exercise 2

names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']

def long_words(n, names):
    names_1 = []
    for name in names:

        if len(name) > n:
            names_1.append(name.capitalize())
    return (names_1)

expected_names = long_words(3, names)
print(expected_names)

new_names = [name.capitalize() for name in names if len(name) > 3]
print(new_names)

# Brian helped me with capitalization 
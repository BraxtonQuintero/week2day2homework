# Exercise 1
# Use the following list - [1,11,14,5,8,9]

lists = [1, 11, 14, 5, 8, 9]

expected_list = []

for list in lists:

    if list < 10:
        expected_list.append(list)

print(expected_list)

#new_list = [lists for list in lists if list < 10]
#print(new_list.append())


# Exercise 2

names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']

names_1 = []


def long_words(n, names):
    names_1 = []
    for name in names:

        if len(name) > n:
            names_1.append(name)
    return (names_1)

print(long_words(3, names))
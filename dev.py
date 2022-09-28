names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']



def long_words(n, names):
    for name in names:

        if len(name) <= n:
            names.remove(name)
    return (names)

print(long_words(3, names))
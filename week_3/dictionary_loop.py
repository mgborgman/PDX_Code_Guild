dict = {
    'matt': {'age': 27},
    'ashley': {'age': 26},
    'kevin': {'age': 27},
}

for index, name in dict.items():
    print index, name['age']


print dict.items()

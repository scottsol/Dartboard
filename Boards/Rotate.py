x = [
    ["9 1",    "7 0",    "7 2",  "pass",       "9 0",  "9 2",  "7 1",  "14 2"],
    ["13 1",   "17 0",   "17 2", "Bullseye 0", "13 0", "13 2", "17 1", "8 2" ],
    ["11 1",   "20 0",   "20 2", "14 1",       "11 0", "11 2", "20 1", "14 0"],
    ["10 1",   "18 0",   "18 2", "8 1",        "10 0", "10 2", "18 1", "8 0" ],
    [ "5 1",   "12 0",   "12 2", "pass",       "5 0",  "5 0",  "12 1", "6 2" ],
    [ "3 1",   "1 0",    "1 2",  "Bullseye 0", "3 0",  "3 2",  "1 1",  "15 2"],
    [ "2 1",   "4 0",    "4 2",  "6 1",        "2 0",  "2 2",  "4 1",  "6 0" ],
    ["16 1",   "19 0",   "19 2", "15 1",       "16 0", "16 2", "19 1", "15 0"],
]

z = [
    ['9 1', '13 1', '11 1', '10 1', '5 1', '3 1', '2 1', '16 1'],
    ['7 0', '17 0', '20 0', '18 0', '12 0', '1 0', '4 0', '19 0'],
    ['7 2', '17 2', '20 2', '18 2', '12 2', '1 2', '4 2', '19 2'],
    ['pass', 'Bullseye 0', '14 1', '8 1', 'pass', 'Bullseye 0', '6 1', '15 1'], ['9 0', '13 0', '11 0', '10 0', '5 0', '3 0', '2 0', '16 0'],
    ['9 2', '13 2', '11 2', '10 2', '5 0', '3 2', '2 2', '16 2'],
    ['7 1', '17 1', '20 1', '18 1', '12 1', '1 1', '4 1', '19 1'],
    ['14 2', '8 2', '14 0', '8 0', '6 2', '15 2', '6 0', '15 0']
]


y = [[], [], [], [], [], [], [], []]

num = 0
for i in x:
    for j in i:
        y[num].append(j)
        num = (num + 1) % 8

print(y)

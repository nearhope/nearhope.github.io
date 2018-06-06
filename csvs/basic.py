import csv
with open('basic.csv', 'r') as csvfile:
    our_reader = csv.reader(csvfile)
    names = [row for row in our_reader]
print(names)

print(len(names))

# find the length of each first name
for row in names:
    print(len(row[2]))

# find the longest first name
longest = ""
for row in names:
    if len(row[2]) > len(longest):
        longest = row[2]
print(longest)

# construct a new list consisting of only the first names we have here.
first_names = [row[2] for row in names]
first_names.reverse()
print(first_names)

new_row = [2,'wayne','graham','meh']
names.append(new_row)
print(names)



a_row = [3,'fox','eliza','SO COOL']
names + a_row

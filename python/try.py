fruits=("kiwi","banana","plum","apple","peach")

# results=[]
# for item in fruits:
#    results.append(item)
#
# print(results)

numbers=[1,2,3,4,5]
#results=[]
#
results=[number-10 for number in numbers]
# for item in numbers:
#     results.append(item+5)
#
print(results)

# numbers=[1,2,3,4,5]
# data=[]
#
# for number in numbers:
#     data.append(number-10)
#
# print(data)
# print()



letters=["a","b","c","d","e"]
test=[]

for letter in letters:  test.append(letter + " ha ha ha")

print("how the Count says the alphabet:")
print(test)
print()

travelList=["China", "Prague", "home", "Iceland"]

for place in travelList:
    print("I would like to visit " + place + ".")
print()

for fruit in fruits:
    if fruit=="plum":
        print(fruit)
    else:
        print("wrong fruit")

#Create a list named hiltClass that contains the name of the people next to youself.
hiltClass=["Emily","Andy","Tony"]
myName="Andy"

for name in hiltClass:
    if name == myName:
        print(name)
        print()

hiltClass.append("George")

for name in hiltClass:
    print(name)

print()

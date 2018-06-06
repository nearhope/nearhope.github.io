#method to do a simple addition
def add(x,y):   #methods start with def  methodName(param):
    print(x+y)  #do something here

number=4        #variable
(add(3,number)) #repeat methodName (besure to include parameter values)
print()

def add(x,y):
    print(x+y)

def sayHello(name):
    print("Hi, I'm " + name + ".")

sayHello("Andy")

def sayHello(name):
    print("Hi, I'm " + name + ".")

names=["Andy", "Joe", "Sally"]
myName="Sally"

for name in names:
    if name==myName:
        sayHello(name)



def setMyName(myName):
    myName=name

name="Andy"
setMyName(name)


def printMyName():
    print(name)

printMyName()


def setMessages(m):
    m=messages

messages={"1630":"howdy","1640":"hello","1650":"we don't want any"}

setMessages(messages)

def printMessage():
    for year, message in messages.items():
        if year=="1640":
            print(message)

printMessage()

def greeting(year):
    if year <1900:
        print("tell me about it")
    elif year >= 1900 and year <= 2020:
        print("oh")
    else:
        print("greetings from the future")

greeting(1640)
greeting(1940)
greeting(2350)

birthDates={"Billy":1953,"georgia":1901,"Frank": 1926,"Hugo": 1889}

def countDates():
    nineteenth=0
    twentieth=0
    for name, year in birthDates.items():
        if year in range (1800,1900):       #this works
            nineteenth += 1
        elif year >= 1900 and year < 2000:  #same as this
            twentieth += 1

    print("there are " + str(nineteenth) + " 19th-c. births and " + str(twentieth) + " 20th-c births in my collection")

countDates()

def addBirthDate(name,year):
    birthDates[name]=year

addBirthDate("Yosef",1845)
addBirthDate("Brooke",1999)
addBirthDate("Andy",1934)

countDates()

#put list in dictionary
nameAndDates={
    "andy":[1981,1982],
    "ethan":[1990,1920]
    }

def addNameAndDates(name,d1,d2):

    nameAndDates[name]=[d1,d2]
addNameAndDates("Billy",1953,2017)

print(nameAndDates)

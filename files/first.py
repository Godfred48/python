people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

age = []
name = []



for item in people:
    ech = item.split(" ")
    namee = ech[0]
    agee = int(ech[1])

    age.append(agee)
    name.append(namee)

youngest = age[0]

for i in range(len(age)):
    if age[i] < youngest:
        youngest = age[i] 
print(youngest)       






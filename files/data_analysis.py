h_age = []
cc = []
yy = []
entry = int(input("Enter your exxpected year: "))

with open("life-expectancy.csv") as life:
    next(life)
    for line in life:
        data = line.split(",")
        country = data[0]
        code = data[1]
        years = int(data[2])
        expectancy = float(data[3]) 

        h_age.append(expectancy)
        cc.append(country)
        yy.append(years)

highest = h_age[0]
for i in range(len(h_age)):
    if h_age[i] > highest:
        highest = h_age[i]
        territory = cc[i]
        yearly = yy[i]
print(f"The highest life expectancy is {highest} years from {territory} in {yearly}")


current_year = []
current_age = []
current_country = []

for i in range(len(yy)):
    if entry == yy[i]:
        current_age.append(h_age[i])
        current_country.append(cc[i])

oldest = current_age[0]
youngest = current_age[0]


for i in range(len(current_age)):
    if current_age[i] > oldest:
        oldest = current_age[i]
        nation = current_country[i]

for ii in range(len(current_age)):
    if current_age[ii] < youngest:
        youngest = current_age[ii]
        country = current_country[ii]

print(f"In the year {entry}, The highest expectancy was {oldest} in {nation}")
print(f"In the year {entry}, The lowest expectancy was {youngest} in {country}")








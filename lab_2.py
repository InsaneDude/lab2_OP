with open("testing_new.csv", "r") as csvfile:
    inforeaded = []
    for readed_now in csvfile:
        inforeaded.append(readed_now.split(";"))
    for k in range(len(inforeaded)):
        inforeaded[k] = list(map(lambda s: s.strip(), inforeaded[k]))
    while '' in inforeaded[0]:
        inforeaded[0].remove('')


number_of_countries = inforeaded.pop(0)
for i in range(len(inforeaded)):
    print(inforeaded[i])


every_country_points = []
points_of_every_country = [[k+1, 0] for k in range(int(number_of_countries[0]))]
print(points_of_every_country)

for counting in range(1, len(inforeaded)+1):
    temp_var = []
    for counting_next in range(int(number_of_countries[0])):
        temp_var.append(int(inforeaded[counting_next][counting]))
    print(temp_var)


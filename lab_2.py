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
for counting in range(1, len(inforeaded)):
    temp_var = 0
    for counting_next in range(1, int(number_of_countries[0])):
        temp_var += int(inforeaded[counting_next][counting])
    every_country_points.append(temp_var)
print(every_country_points)
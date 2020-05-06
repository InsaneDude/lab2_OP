with open("testing_new.csv", "r") as csvfile:
    inforeaded = []
    for readed_now in csvfile:
        inforeaded.append(readed_now.split(";"))
    for k in range(len(inforeaded)):
        inforeaded[k] = list(map(lambda s: s.strip(), inforeaded[k]))
    while '' in inforeaded[0]:
        inforeaded[0].remove('')


number_of_countries = inforeaded.pop(0)
# for i in range(len(inforeaded)):
#     print(inforeaded[i])
countries = []
for k in range(len(inforeaded)):
    countries.append(inforeaded[k][0])
print(countries)
points_of_every_country = [[countries[k], 0] for k in range(int(number_of_countries[0]))]
# print(points_of_every_country)

for counting in range(1, len(inforeaded)+1):
    temp_collecting_columns = []
    for counting_next in range(int(number_of_countries[0])):
        temp_collecting_columns.append(int(inforeaded[counting_next][counting]))
        points_of_every_country[counting_next - 1][1] += 1
    winner_1 = max(temp_collecting_columns)
    index_of_winner = temp_collecting_columns.index(winner_1)
    points_of_every_country[index_of_winner][1] += 11
    temp_collecting_columns.pop(index_of_winner)
    winner_2 = max(temp_collecting_columns)
    index_of_winner = temp_collecting_columns.index(winner_2)
    points_of_every_country[index_of_winner-1][1] += 9
print(points_of_every_country)

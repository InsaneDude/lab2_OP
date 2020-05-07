import os


way_to_directory = str(input("Введіть шлях до папки : "))
files_in_dir_list = os.listdir(way_to_directory)
inforeaded = []
os.chdir(way_to_directory)
for i in range(len(files_in_dir_list)):
    with open(files_in_dir_list[i], "r") as csvfile:
        for readed_now in csvfile:
            inforeaded.append(readed_now.split(";"))
        for k in range(len(inforeaded)):
            inforeaded[k] = list(map(lambda s: s.strip(), inforeaded[k]))
inforeaded.sort()
for checking_array in range(int(len(inforeaded)/2)):
    inforeaded.pop(0)


number_of_countries = len(inforeaded)
countries = []
for k in range(len(inforeaded)):
    countries.append(inforeaded[k][0])
points_of_every_country = [[countries[k], 0] for k in range(number_of_countries)]
for counting in range(1, len(inforeaded)+1):
    temp_collecting_columns = []
    for counting_next in range(number_of_countries):
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
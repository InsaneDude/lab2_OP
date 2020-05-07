import os


way_to_directory_open = str(input("Введіть шлях до папки, де ви хочете зчитати файли : "))
files_in_dir_list = os.listdir(way_to_directory_open)
inforeaded = []
os.chdir(way_to_directory_open)
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


os.chdir(r"C:\Users\insane_dude\Documents\GitHub\lab2_OP\yay_final_result")
with open("final_result.csv", "w") as output_file:
    for k in range(len(inforeaded)):
        output_file.write(str(points_of_every_country[k][0])), output_file.write(";")
    output_file.write("\n")
    for z in range(len(inforeaded)):
        output_file.write(str(points_of_every_country[z][1])), output_file.write(";")
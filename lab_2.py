with open("testing_new.csv", "r") as csvfile:
    inforeaded = []
    for readed_now in csvfile:
        inforeaded.append(readed_now.split(";"))
    for k in range(len(inforeaded)):
        inforeaded[k] = list(map(lambda s: s.strip(), inforeaded[k]))
    while '' in inforeaded[0]:
        inforeaded[0].remove('')
    for i in range(len(inforeaded)):
        print(inforeaded[i])


moving_to_next = 0
for k in range(len(inforeaded)):
    while str in inforeaded[k]:
        inforeaded[k][moving_to_next] = int(inforeaded[k][moving_to_next])
        # if TypeError:
        #    continue
        moving_to_next += 1
    moving_to_next = 0
print(inforeaded)
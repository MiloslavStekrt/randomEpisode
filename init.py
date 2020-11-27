import random
# file = open("series.txt", "r")
file = open("series_raw.txt","r")

series = [int(i, base=16) for i in file.read().split(".")]

serie = random.randint(1, len(series))

episode = random.randint(1,series[serie-1]-6)

print(str(serie) + " - " + str(episode))

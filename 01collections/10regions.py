file = open("data/volby.csv", encoding="utf-8")
data = file.read()
file.close()

rows = data.split("\n")

regions = []

for row in rows[1:]:
    columns = row.split(";")
    name = columns[0].strip('"')
    count = int(columns[1])
    total = 0
    for number in columns[1:]:
        total += int(number)
    percent = (count / total) * 100
    region = (name, percent)
    regions.append(region)

i = 1
while i <= len(regions) - 1:
    j = i - 1
    while j >= 0 and regions[i][1] > regions[j][1]:
        j -= 1
    region = regions.pop(i)
    regions.insert(j + 1, region)
    i += 1

file = open("data/okresy.csv", "w")
for region in regions:
    (name, percent) = region
    file.write(name + ";" + str(round(percent, 2)) + "\n")
file.close()

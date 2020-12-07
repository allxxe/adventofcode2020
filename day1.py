lines=[]
with open('day1_2020.txt', 'r') as file:
  for line in file: 
    lines.append(line)

for line in lines:
    line = line.strip()
    value = int(line)
    answer = 2020 - value 
    for line2 in lines:
      line2 = line2.strip()
      value2 = int(line2)
      if value2 == answer:
        print(value, value2)
        print(value * value2)

for line in lines:
  line = line.strip()
  value = int(line)
  for line2 in lines:
    line2 = line2.strip()
    value2 = int(line2)
    for line3 in lines:
      line3 = line3.strip()
      value3 = int(line3)
      found = 2020
      if (value + value2 + value3 == 2020):
        print(value, value2, value3)
        print(value * value2 * value3)
        



    








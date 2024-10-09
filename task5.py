import csv

with open("task5.csv", "w", newline="") as file:
 writer = csv.writer(file)
 while True:
  name = input("Enter name (type 'quit' to exit): ")
  if name.lower() == "quit":
   break 
  writer.writerow([name])

with open("task5.csv", "r") as file:
 reader = csv.reader(file)
 for row in reader:
  print(row[0])

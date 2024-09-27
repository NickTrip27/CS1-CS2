import csv
columns = {}
columns['alphabet'] = ["a", "b", "c", "d", "e", "f", "g"]
columns['numbers'] = ["1", "2", "3", "4", "5", "6", "7"]

rows = zip(columns['alphabet'],columns['numbers'])

with open('my_file.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['letters', 'numbers'])
    writer.writerows(rows)

import csv

print("Hello Weightlifting")

# open a csv file
with open ('benches.csv') as csvfile:
    # create a reader of the csv file, quotechar can be almost anything that isn't in the dataset
    values = csv.reader(csvfile)
    # for every row in the reader value
    for row in values:
        print( row)

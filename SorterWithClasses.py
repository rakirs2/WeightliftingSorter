import csv
from LifterClasses import WeightLiftingMeetResult

#change file name here
with open ('datafull.csv') as csvfile:
    values = csv.reader(csvfile)
    LifterMeetResults = {}
    next(values)
    for row in values:
        print(row)
        lifter = WeightLiftingMeetResult(row[0], row[1],row[2],row[3],row[4], row[5], row[6],row[7], row[8], row[9], row[10])
        print(lifter.snatch1)
        if lifter.category in LifterMeetResults:
            LifterMeetResults[lifter.category].append([lifter.total, lifter.category, lifter.name, lifter.date])
            LifterMeetResults[lifter.category].sort(reverse = True)
        else:
            LifterMeetResults[lifter.category] = []
            LifterMeetResults[lifter.category].append([lifter.total, lifter.category, lifter.name, lifter.date])

    
    
with open('results.csv', 'w', newline='', encoding='utf-8') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    for i in LifterMeetResults:
        for k in LifterMeetResults[i]:
            csvwriter.writerow(k)
import csv
from LifterClasses import WeightLiftingMeetResult

with open ('data.csv') as csvfile:
    values = csv.reader(csvfile)
    # Creating an 'object/container (officially called a list)' to store all of your results in
    # Just for context, the maximum allowed size on your computer for this is at least 536,870,912 results so you should be well within that bound
    LifterMeetResults = {}
    # for every row in the reader value
    next(values)
    for row in values:
        # What do you think this line does?
        print(row)
        lifter = WeightLiftingMeetResult(row[0], row[1],row[2],row[3],row[4], row[5], row[6],row[7], row[8], row[9], row[10])
        print(lifter.snatch1)
        if lifter.category in LifterMeetResults:
            LifterMeetResults[lifter.category].append([lifter.total, lifter.name, lifter.date])
            LifterMeetResults[lifter.category].sort()
        else:
            LifterMeetResults[lifter.category] = []
            LifterMeetResults[lifter.category].append([lifter.total, lifter.name, lifter.date])

    
    
with open('results.csv', 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    
    for i in LifterMeetResults:
        csvwriter.writerow(i)
        for k in LifterMeetResults[i]:
            print(k)
            csvwriter.writerows(k)
    # for result in LifterMeetResults:
    #     print(result.Name + " is a " + result.Sex + " athlete who lifted at this competition with a total of " + result.BestSquatKg+result.BestDeadliftKg  )
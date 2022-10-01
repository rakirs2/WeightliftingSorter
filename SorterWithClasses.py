import csv
from LifterClasses import WeightLiftingMeetResult

with open ('data1.csv') as csvfile:
    values = csv.reader(csvfile)
    # Creating an 'object/container (officially called a list)' to store all of your results in
    # Just for context, the maximum allowed size on your computer for this is at least 536,870,912 results so you should be well within that bound
    LifterMeetResults = []
    # for every row in the reader value
    next(values)
    for row in values:
        # What do you think this line does?
        lifter = WeightLiftingMeetResult(row[0], row[1])
        print(lifter)
        LifterMeetResults.append(lifter)
    # for result in LifterMeetResults:
    #     print(result.Name + " is a " + result.Sex + " athlete who lifted at this competition with a total of " + result.BestSquatKg+result.BestDeadliftKg  )
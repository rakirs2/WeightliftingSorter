import csv
from LifterClasses import PowerLiftingMeetResult

with open ('benches.csv') as csvfile:
    values = csv.reader(csvfile)
    # Creating an 'object/container (officially called a list)' to store all of your results in
    # Just for context, the maximum allowed size on your computer for this is at least 536,870,912 results so you should be well within that bound
    LifterMeetResults = []
    # for every row in the reader value
    for row in values:
        # What do you think this line does?
        LifterMeetResults.append( PowerLiftingMeetResult(row[0], row[1], row[2], row[3], row[4],row[5],row[6],row[7]))
    
    # for result in LifterMeetResults:
    #     print(result.Name + " is a " + result.Sex + " athlete who lifted at this competition with a total of " + result.BestSquatKg+result.BestDeadliftKg  )
    
    MaleLifterResults = []
    FemaleLifterResults = []

    #Can you think of a way to optimize this?
    for result in LifterMeetResults:
        if result.Sex == 'F':
            # print(result.Name + " is a Female athlete who lifted at this competition with a total of " + result.BestSquatKg+result.BestDeadliftKg  )
            FemaleLifterResults.append(result)
    for result in LifterMeetResults:
        if result.Sex == 'M':
            # print(result.Name + " is a Male athlete who lifted at this competition with a total of " + result.BestSquatKg+result.BestDeadliftKg  )
            MaleLifterResults.append(result)
    for result in LifterMeetResults:
        # What happened here?
        if result.Sex not in {'M','F'}:
             print(result.Name + " is a " + result.Sex + " athlete who lifted at this competition with a total of " + result.BestSquatKg+result.BestDeadliftKg  )
print(len(MaleLifterResults))
print(len(FemaleLifterResults))
# These are off by one. Can you figure out why?
print(len(LifterMeetResults))
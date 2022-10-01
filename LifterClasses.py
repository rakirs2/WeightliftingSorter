from functools import singledispatch


class WeightLiftingMeetResult:
    def __init__(self, meet, date, category, name, bodyweight, snatch1, snatch2, snatch3, clean1, clean2, clean3):
        self.meet = meet
        self.date = date
        self.category = category
        self.name = name
        self.bodyweight = bodyweight

        self.snatch1 = convertToInt(snatch1)
        self.snatch2 = convertToInt(snatch2)
        self.snatch3 = convertToInt(snatch3)
        self.maxSnatch = max(0, self.snatch1, self.snatch2, self.snatch3)
        self.clean1 = convertToInt(clean1)
        self.clean2 = convertToInt(clean2)
        self.clean3 = convertToInt(clean3)
        self.maxClean = max(0, self.clean1, self.clean2, self.clean3)
        self.total = self.maxSnatch+ self.maxClean
    def __str__(self):
        return self.meet + ", " + self.date+", " + self.category + ", " + self.category + ", " + self.bodyweight + ", " + str(self.maxSnatch)+", " +str(self.maxClean) + ", " +str(self.total)

def convertToInt(val):
    try:
        return int(val)
    except:
        return 0
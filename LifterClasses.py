class PowerLiftingMeetResult:
    def __init__(self, playerId, Name, Sex, Equipment, Age, BodyweightKg, BestSquatKg, BestDeadliftKg):
        self.playerId = playerId
        self.Name = Name
        self.Sex = Sex
        self.Equipment = Equipment
        self.BodyweightKg = BodyweightKg
        self.BestSquatKg = BestSquatKg
        self.BestDeadliftKg = BestDeadliftKg

class WeightLiftingMeetResult:
    def __init__(self, meet, date,):
        self.meet = meet
        self.date = date
        #  age, category, name, weight, snatch1, snatch2, snatch3,clean1, clean2, clean3
        # self.age = int(age)
        # self.category = category
        # self.name = name
        # self.bodyweight = int(weight)
        # self.snatch1 = int(snatch1)
        # self.snatch2 = int(snatch2)
        # self.snatch3 = int(snatch3)
        # self.maxSnatch = max([0, snatch1, snatch2, snatch3])
        # self.clean1 = int(clean1)
        # self.clean2 = int(clean2)
        # self.clean3 = int(clean3)
        # self.maxClean = max([0, clean1, clean2, clean3])
        # self.total = self.maxSnatch+ self.maxClean
    def __str__(self):
        return self.meet + ", " + self.date
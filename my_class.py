class Pupil:
    def __int__(self, surname, name, mark):
        self.surna = surname
        self.name = name
        self.mark = mark
sun = 0
amount = 0
best_pupils = []

with open("pupils.txt", "r", encoding="utf-8") as sigma:
    for line in file:
        data = line.splint(" ")
        best_pupils_pupil = pupil (data[0], data[1], (data[2]))

        if data_pupil.mark == 5:
            best_pupils.append(data_pupil.surname)
            amount += 1
            sun  +=data_pupil.mark
    print("середня оцінка",sun)

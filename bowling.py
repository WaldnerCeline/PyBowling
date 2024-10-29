from frame import Frame


class Bowling:
    def __init__(self):
        self.nb_tour = 10
        self.frames = []
        self.score_tour = []


    def getScores(self):
        return []


    def newFrame(self):
        self.frames.append(Frame(len(self.frames)))


    def score(self, frame_index: int):
        """Recalcule à chaque tour du score de la frame en fonction ds bonus des règles du bowling.
        """
        for i in range(frame_index+1):
            if self.frames[i].isStrike == True:
                bonus = self.calculate_strike_bonus(i)
            elif self.frames[i].isSpare == True:
                bonus = self.calculate_spare_bonus(i)
            else:
                bonus = 0
            self.score_tour[i] = self.frames[i].score + bonus


    def calculate_strike_bonus(self, frame_index: int):
        """Calcule le bonus pour un strike."""
        bonus = 0
        if len(self.frames[frame_index:])>1:
            if self.frames[frame_index+1].isStrike:
                if len(self.frames[frame_index:]) > 2:
                    bonus += self.frames[frame_index + 1].score + self.frames[frame_index + 2].score
            else:
                bonus += self.frames[frame_index+1].score
        return bonus


    def calculate_spare_bonus(self, frame_index: int):
        """Calcule le bonus pour un spare."""
        bonus = 0
        if len(self.frames[frame_index:]) > 1 and self.frames[frame_index + 1].lancer1 is not None:
                bonus += self.frames[frame_index + 1].lancer1
        return bonus


    def addFrameBonus(self):
        print("LANCE BONUS !")
        if self.frames[self.nb_tour - 1].isStrike:
            frame_bonus = Frame(self.nb_tour)
            frame_bonus.roll()
            self.frames.append(frame_bonus)

            if frame_bonus.isStrike:
                frame_bonus2 = Frame(self.nb_tour + 1)
                frame_bonus2.roll(only_one_lancer=True)
                self.frames.append(frame_bonus2)
                self.score_tour[self.nb_tour - 1] += frame_bonus.lancer1 + frame_bonus2.lancer1
            else:
                self.score_tour[self.nb_tour - 1] += frame_bonus.lancer1 + frame_bonus.lancer2

        elif self.frames[self.nb_tour - 1].isSpare:
            frame_bonus = Frame(self.nb_tour)
            frame_bonus.roll(only_one_lancer=True)
            self.frames.append(frame_bonus)
            self.score_tour[self.nb_tour - 1] += frame_bonus.lancer1


    def printScore(self, frame_index: int):
        self.score(frame_index)
        index_str = "| Tours\t|"
        score_str = "| Score\t|"
        lancers_str = "| Lancé\t|"
        scoreFrame = 0

        for i in range(frame_index + 1):
            scoreFrame += self.score_tour[i]
            index_str += "\t\tTour " + str(i + 1) + "\t\t|"
            score_str += "\t\t" + str(scoreFrame) + "\t\t|"
            lancers_str += "\t\t" + str(self.frames[i].lancer1) + "/"
            if self.frames[i].isStrike:
                lancers_str +="-"
            else:
                lancers_str += str(self.frames[i].lancer2)
            lancers_str += "\t\t|"

        line = "".join(["-" for i in range(4 * len(score_str))])

        # Affichage du tableau final jusqu'à la frame frame_index
        print(line)
        print(index_str)
        print(line)
        print(score_str)
        print(line)
        print(lancers_str)
        print(line)

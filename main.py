from bowling import Bowling

def main():
    bowling = Bowling()

    for i in range(bowling.nb_tour): # Initialisation du nombre de tours
        bowling.newFrame()
        bowling.score_tour.append(0)

    for i in range(len(bowling.frames)):
        frame = bowling.frames[i]
        frame.roll()
        bowling.printScore(i)

        if frame == bowling.frames[bowling.nb_tour - 1]:
            bowling.addFrameBonus()
            bowling.printScore(bowling.nb_tour - 1)

if __name__ == "__main__":
    main()
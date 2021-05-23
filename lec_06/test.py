
score = 200
name = 'jon'
name_score = str(name) + ': ' + str(score)


def scoreboard_check():
    with open('C:\infa_2021\lection_6\Scoreboard') as file:
        for line in file:
            line = line.strip()
            print('line: "', line, '"')


scoreboard_check()

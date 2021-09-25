import random


def main():
    players = [
        'Denz',
        'Turtle',
        'Doppie',
        'Drei',
        'Sean',
        'Omi',
        'Kwos',
        'GD',
        'Benny',
        'Bernstein'
    ]

    teams = [ [], [] ]

    max_num_team_members = 5
    for i in range(len(players)):
        assigned_team = random.randint(0, 1)
        if len(teams[assigned_team]) >= max_num_team_members:
            teams[(assigned_team + 1) % 2].append(players[i])
        else:
            teams[assigned_team].append(players[i])

    print('====================================')
    print('==         CS:GO 5v5 Match        ==')
    print('====================================')
    print('= TEAM DENZ NUTS | TEAM ADIK       =')
    print('====================================')
    for teamA, teamB in zip(teams[0], teams[1]):
        print(f'= {teamA:15}| {teamB:15} =')
    print('====================================')
    print('== LET\'S GET READY TO RUMBLLLLEEE ==')
    print('====================================')

main()

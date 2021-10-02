import random


def team_weight(team):
    return max(sum([ member[1] for member in team ]), 1)


def main():
    # 1 - best
    # 5 - worst
    players = [
        [ 'Sean', 4 ],
        [ 'Doppie', 2 ],
        [ 'Denz', 1 ],
        [ 'pao', 1 ],
        [ 'Tortle', 3 ],
        [ 'Kwos', 3 ],
        [ 'Omi', 1 ],
        [ 'Jeremy', 3 ],
        [ 'Drei', 2 ],
        [ 'Sora', 1 ]
    ]

    teams = [ [], [] ]

    max_num_team_members = 5
    for i in range(len(players)):
        team_weights = [ team_weight(teams[0]), team_weight(teams[1]) ]
        assigned_team = random.choices(
            [ 0, 1 ], team_weights
        )[0]
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
        print(f'= {teamA[0]:15}| {teamB[0]:15} =')
    print('====================================')
    print('== LET\'S GET READY TO RUMBLLLLEEE ==')
    print('====================================')

main()

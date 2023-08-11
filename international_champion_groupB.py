import numpy as np
from collections import OrderedDict


# create initial list data
team_name = ['Iran', 'Portugal', 'Spain', 'Morocco']
team_wins = [0, 0, 0, 0]
team_loses = [0, 0, 0, 0]
team_draws = [0, 0, 0, 0]
team_goal_differences = [0, 0, 0, 0]
team_points = [0, 0, 0, 0]

# create list of games result
game_result_list = []
for n in range(6):
    game_result = input()
    game_result = game_result.split('-')
    game_result_list.append(game_result)
game_result_list = np.int_(game_result_list)

# completing data of three list (team_wins, team_loses, team_draws)
result = []
for n in range(len(game_result_list)):
    if (game_result_list[n][0] < game_result_list[n][1]):
        if n == 0:
            team_wins[2] += 1
            team_loses[0] += 1
        elif n == 1:
            team_wins[1] += 1
            team_loses[0] += 1
        elif n == 2:
            team_wins[3] += 1
            team_loses[0] += 1
        elif n == 3:
            team_wins[1] += 1
            team_loses[2] += 1
        elif n == 4:
            team_wins[3] += 1
            team_loses[2] += 1
        elif n == 5:
            team_wins[3] += 1
            team_loses[1] += 1
    elif (game_result_list[n][0] > game_result_list[n][1]):
        if n == 0:
            team_wins[0] += 1
            team_loses[2] += 1
        elif n == 1:
            team_wins[0] += 1
            team_loses[1] += 1
        elif n == 2:
            team_wins[0] += 1
            team_loses[3] += 1
        elif n == 3:
            team_wins[2] += 1
            team_loses[1] += 1
        elif n == 4:
            team_wins[2] += 1
            team_loses[3] += 1
        elif n == 5:
            team_wins[1] += 1
            team_loses[3] += 1
    elif (game_result_list[n][0] == game_result_list[n][1]):
        if n == 0:
            team_draws[0] += 1
            team_draws[2] += 1
        elif n == 1:
            team_draws[0] += 1
            team_draws[1] += 1
        elif n == 2:
            team_draws[0] += 1
            team_draws[3] += 1
        elif n == 3:
            team_draws[2] += 1
            team_draws[1] += 1
        elif n == 4:
            team_draws[2] += 1
            team_draws[3] += 1
        elif n == 5:
            team_draws[1] += 1
            team_draws[3] += 1

# completing data of team_goal_differences list
#iran
team_goal_differences[0] = (game_result_list[0][0] + game_result_list[1][0] + game_result_list[2][0]) - (game_result_list[0][1] + game_result_list[1][1] + game_result_list[2][1])
#portugal
team_goal_differences[1] = (game_result_list[1][1] + game_result_list[3][1] + game_result_list[5][0]) - (game_result_list[1][0] + game_result_list[3][0] + game_result_list[5][1])
#spain
team_goal_differences[2] = (game_result_list[0][1] + game_result_list[3][0] + game_result_list[4][0]) - (game_result_list[0][0] + game_result_list[3][1] + game_result_list[4][1])
#morocco
team_goal_differences[3] = (game_result_list[2][1] + game_result_list[4][1] + game_result_list[5][1]) - (game_result_list[2][0] + game_result_list[4][0] + game_result_list[5][0])

# completing data of team_points list
prod_list = [3, 3, 3, 3]
team_win_points = [x * y for x, y in zip(team_wins, prod_list)]
team_points = [x + y for x, y in zip(team_win_points, team_draws)]


# create dictionary for print output
all_teams = OrderedDict()
for ind, name in enumerate(team_name):
    all_teams[name] = []
    if team_wins[ind] is not None:
        all_teams[name].append(team_wins[ind])
    if team_loses[ind] is not None:
        all_teams[name].append(team_loses[ind])
    if team_draws[ind] is not None:
        all_teams[name].append(team_draws[ind])
    if team_goal_differences[ind] is not None:
        all_teams[name].append(team_goal_differences[ind])
    if team_points[ind] is not None:
        all_teams[name].append(team_points[ind])

# sorted teams as: 1-points  2-wins  3-alphabet
dic_sorted = {k : v for k,v in sorted(all_teams.items(), key= lambda item: (int(-item[1][4]), int(-item[1][1]), item[0]))}

# print sorted output
for i, j in dic_sorted.items():
    print(f'{i} wins:{j[0]} , loses:{j[1]} , draws:{j[2]} , goal difference:{j[3]} , points:{j[4]}')
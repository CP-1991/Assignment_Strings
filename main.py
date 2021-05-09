# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Part1
player_1 = 'Gullit'
player_2 = 'Van Basten'
goal_1 = 32
goal_2 = 54
goals = player_1 + ' ' + str(goal_1) + ', ' + player_2 + ' ' + str(goal_2)
print(goals)
report = player_1 + ' scored in the ' + str(goal_1) + 'nd minute' + '\n' + player_2 + ' scored in the ' + str(goal_2) + 'th minute'
print(report)

#Part2
player = 'Jan Wouters'
first_name = player [0:player.find(" ")]
print(first_name)
last_name_len = len(player [player.find(" ")+1 :len(player)])
print(last_name_len)
name_short = player [0] + '. ' + player [player.find(" ")+1 :len(player)]
print(name_short)
chant = (first_name + '! ') * len(first_name)
print(chant)
good_chant = ((first_name + '! ') * len(first_name))[:-1]
print(good_chant)
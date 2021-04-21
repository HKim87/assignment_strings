# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scoorder1 = 'Ruud Gullit'
scoorder2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = scoorder1 + " " + str(goal_0) + ', ' + scoorder2 + " " + str(goal_1)

report = f'{scoorder1} scored in the {goal_0}nd minute\n{scoorder2} scored in the {goal_1}th minute'

player = 'Ronald Koeman'
first_name = player[0:player.find(' ')]

last_name_len = len(player[player.find(' ')+1:])

name_short = first_name[0] + ". " + player[player.find(' ')+1:]
chant_metspace = (first_name + '! ') * len(first_name)
chant = chant_metspace.strip()
good_chant = chant[-1] != " "



# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#Part 1
#1
player_0 = 'Ruud Gullit'
player_1 = 'Marco van Basten'
#2
goal_0 = 32
goal_1 = 54
#3
scorers = f'{player_0} {goal_0}, {player_1} {goal_1}'
print(scorers)
#4 using f strings
report = f'{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute'
print(report)


#Part 2
#1
player = player_0
#2
find_space = player.find(" ")
first_name = player[:find_space]
print(first_name)
first_name_len = len(first_name)
#3
last_name = player[find_space:]
last_name_len = len(last_name)-1
print(last_name_len)
#4
initial = player[0] + '.'
name_short = initial + last_name
print(name_short)

#5
chant = ((first_name + '! ') * first_name_len)[:-1] 
print(chant)

#6
good_chant = chant[len(chant)-1] != " "
print(good_chant)
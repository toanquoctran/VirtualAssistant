you = 'hello'

if you == '':
    robot_brain = "I can't hear you, try again"
elif you == 'hello':
    robot_brain = "Hello Toan Tran"
elif you == 'today':
    robot_brain = "Tuesday"
else:
    robot_brain = "I'm good. How are you?"

print(robot_brain)
n = int(input())
for test_case in range(1, n+1) :
    s = input().split()[1:]
    commands = []
    for i in range(0, len(s), 2) :
        order = i//2
        robot = s[i]
        index = int(s[i+1])
        commands += [(order, robot, index)]

    robotB_cmds = []
    robotO_cmds = []
    for x in commands :
        if x[1] == 'O' :
            robotO_cmds += [x]
        else :
            robotB_cmds += [x]
    
    current_B = 1
    current_O = 1
    total_time = 0
    for i in range(0, len(commands)) :
        movetime = 0
        if not robotO_cmds or (robotB_cmds and (robotB_cmds[0] < robotO_cmds[0])) :
            # for this case, do robot B; move robot O
            cmd = robotB_cmds[0]
            robotB_cmds = robotB_cmds[1:]
            to_index = cmd[2]
            movetime += abs(current_B - to_index)
            current_B = to_index
            movetime += 1 # pressing

            if robotO_cmds :
                # now use the movetime to move the other robot
                distancemax = movetime
                distance_to_move = abs(robotO_cmds[0][2] - current_O)
                distance_to_move = min(distancemax, distance_to_move)
                # direction positive: right (+), negative: left (-)
                direction = robotO_cmds[0][2] - current_O
                if direction > 0 :
                    # right
                    current_O += distance_to_move
                else :
                    current_O -= distance_to_move
        else :
            # do robot O; move robot B
            cmd = robotO_cmds[0]
            robotO_cmds = robotO_cmds[1:]
            to_index = cmd[2]
            movetime += abs(current_O - to_index)
            current_O = to_index
            movetime += 1 # pressing

            # now use the movetime to move the other robot
            if robotB_cmds :
                distancemax = movetime
                distance_to_move = abs(robotB_cmds[0][2] - current_B)
                distance_to_move = min(distancemax, distance_to_move)
                # direction positive: right (+), negative: left (-)
                direction = robotB_cmds[0][2] - current_B
                if direction > 0 :
                    # right
                    current_B += distance_to_move
                else :
                    current_B -= distance_to_move

        total_time += movetime
        # print('>>', robotB_cmds)
        # print('> ', robotO_cmds)
        # print(movetime)
        # print('B:', current_B, 'O:', current_O)

    print('Case #%d:' % (test_case), total_time)


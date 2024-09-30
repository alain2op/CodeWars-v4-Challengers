from random import randint, choice
import numpy as np
from math import tan, pi

name = 'best'

def moveTo(x , y , Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1
    
def positionInIsland(pirate):
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    right = pirate.investigate_right()
    left = pirate.investigate_left()
    if up[0][:-1] == "island" and down[0][:-1] == "island" and right[0][:-1] == "island" and left[0][:-1] == "island":
        return "c"    
    if up[0][:-1] != "island" and right[0][:-1] == "island" and left[0][:-1] != "island" and down[0][:-1] == "island":
        return "nw"
    if up[0][:-1] != "island" and right[0][:-1] != "island" and left[0][:-1] == "island" and down[0][:-1] == "island":
        return "ne"
    if up[0][:-1] == "island" and right[0][:-1] != "island" and left[0][:-1] == "island" and down[0][:-1] != "island":
        return "se"
    if up[0][:-1] == "island" and right[0][:-1] == "island" and left[0][:-1] != "island" and down[0][:-1] != "island":
        return "sw"
    if up[0][:-1] == "island" and down[0][:-1] == "island" and left[0][:-1] == "island" and right[0][:-1] != "island":
        return "e"
    if up[0][:-1] == "island" and down[0][:-1] == "island" and left[0][:-1] != "island" and right[0][:-1] == "island":
        return "w"
    if up[0][:-1] != "island" and down[0][:-1] == "island" and left[0][:-1] == "island" and right[0][:-1] == "island":
        return "n"
    if up[0][:-1] == "island" and down[0][:-1] != "island" and left[0][:-1] == "island" and right[0][:-1] == "island":
        return "s"

def wtd_dir(quad, theta):
    dir = {'ul':[3,2], 'ur':[3,4], 'dl':[1,2], 'dr':[1,4]}
    res = 100
    res_y = round(res*tan(theta))
    return ([dir[quad][1]]*res + [dir[quad][0]]*res_y)

def spread(pirate):
    rays = 7
    sorted_pir = int(pirate.getID()) % rays
    pir_sig = pirate.getSignal()
    if pir_sig == '' :
        return 0
    else:
        dir_opn = [wtd_dir(pir_sig, i*(pi/(2*(rays+1)))) for i in range(1, rays+1)]
        return choice(dir_opn[sorted_pir])

def ActPirate(pirate):

    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    x, y = pirate.getPosition()
    
    # set signal
    if up == 'wall' and left == 'wall' :
        pirate.setSignal('ul')
    elif up == 'wall' and right == 'wall':
        pirate.setSignal('ur')
    elif down == 'wall' and left == 'wall' :
        pirate.setSignal('dl')
    elif down == 'wall' and right == 'wall':
        pirate.setSignal('dr')

    s = pirate.trackPlayers()
    team_s = pirate.getTeamSignal()
    split = team_s.split(',')
    
    if (
        (up == "island1" and s[0] != "myCaptured")
        or (up == "island2" and s[1] != "myCaptured")
        or (up == "island3" and s[2] != "myCaptured")
    ):
        island_no = int(up[-1])
        island_status_index = island_no * 3 - 2
        if split[island_status_index] == "":
            split[island_status_index] = "-1" 
            split[island_status_index + 1] = str(x)
            split[island_status_index + 2] = str(y - 1)
            team_s = ','.join(split)
            pirate.setTeamSignal(team_s)

        
    if (
        (down == "island1" and s[0] != "myCaptured")
        or (down == "island2" and s[1] != "myCaptured")
        or (down == "island3" and s[2] != "myCaptured")
    ):
        island_no = int(down[-1])
        island_status_index = island_no * 3 - 2
        if split[island_status_index] == "":
            split[island_status_index] = "-1" 
            split[island_status_index + 1] = str(x)
            split[island_status_index + 2] = str(y + 1)
            team_s = ','.join(split)
            pirate.setTeamSignal(team_s)

    if (
        (left == "island1" and s[0] != "myCaptured")
        or (left == "island2" and s[1] != "myCaptured")
        or (left == "island3" and s[2] != "myCaptured")
    ):
        island_no = int(left[-1])
        island_status_index = island_no * 3 - 2
        if split[island_status_index] == "":
            split[island_status_index] = "-1" 
            split[island_status_index + 1] = str(x - 1)
            split[island_status_index + 2] = str(y)
            team_s = ','.join(split)
            pirate.setTeamSignal(team_s)

    if (
        (right == "island1" and s[0] != "myCaptured")
        or (right == "island2" and s[1] != "myCaptured")
        or (right == "island3" and s[2] != "myCaptured")
    ):
        island_no = int(right[-1])
        island_status_index = island_no * 3 - 2
        if split[island_status_index] == "":
            split[island_status_index] = "-1" 
            split[island_status_index + 1] = str(x + 1)
            split[island_status_index + 2] = str(y)
            team_s = ','.join(split)
            pirate.setTeamSignal(team_s)

    if (right == 'wall' and pirate.getSignal() == 'ul') :
        pirate.setSignal('ur')
    if (right == 'wall' and pirate.getSignal() == 'dl') :
        pirate.setSignal('dr')
    if (left == 'wall' and pirate.getSignal() == 'ur') :
        pirate.setSignal('ul')
    if (left == 'wall' and pirate.getSignal() == 'dr') :
        pirate.setSignal('dl')
    if (up == 'wall' and pirate.getSignal() == 'dl') :
        pirate.setSignal('ul')
    if (up == 'wall' and pirate.getSignal() == 'dr') :
        pirate.setSignal('ur')
    if (down == 'wall' and pirate.getSignal() == 'ul') :
        pirate.setSignal('dl')
    if (down == 'wall' and pirate.getSignal() == 'ur') :
        pirate.setSignal('dr')

    current_pos = pirate.investigate_current()[0]
    if current_pos[:-1] == "island":

        island_no = int(current_pos[-1])
        island_x_index = 3 * island_no - 1
        island_y_index = 3 * island_no

        position_in_island = positionInIsland(pirate)
        pirate_x, pirate_y = pirate.getPosition()

        if position_in_island == "n":
            split[island_y_index] = str(pirate_y + 1)
        elif position_in_island == "ne":
            split[island_x_index] = str(pirate_x - 1)
            split[island_y_index] = str(pirate_y + 1)
        elif position_in_island == "e":
            split[island_x_index] = str(pirate_x - 1)
        elif position_in_island == "se":
            split[island_x_index] = str(pirate_x - 1)
            split[island_y_index] = str(pirate_y - 1)
        elif position_in_island == "s":
            split[island_y_index] = str(pirate_y - 1)
        elif position_in_island == "sw":
            split[island_x_index] = str(pirate_x + 1)
            split[island_y_index] = str(pirate_y - 1)
        elif position_in_island == 'w':
            split[island_x_index] = str(pirate_x + 1)
        elif position_in_island == 'nw':
            split[island_x_index] = str(pirate_x + 1)
            split[island_y_index] = str(pirate_y + 1)

        team_signal = ','.join(split)
        pirate.setTeamSignal(team_signal)

    island1_status = split[1] 
    island2_status = split[4] 
    island3_status = split[7] 

    F = 200
    thresh = 5
    if pirate.getCurrentFrame() >= F:
        found_i1 = split[2] != ""
        found_i2 = split[5] != ""
        found_i3 = split[8] != ""

        if found_i1 and island1_status != "1":
            pirate_x, pirate_y = pirate.getPosition()
            island_x, island_y = split[2:4]
            island_x = int(island_x)
            island_y = int(island_y)
            required = abs(pirate_x - island_x + pirate_y - island_y) + abs(pirate_x - island_x - pirate_y + island_y) < 2 * thresh
            if required:
                return moveTo(island_x, island_y, pirate)
        
        if found_i2 and island2_status != "1":
            pirate_x, pirate_y = pirate.getPosition()
            island_x, island_y = split[5:7]
            island_x = int(island_x)
            island_y = int(island_y)
            required = abs(pirate_x - island_x + pirate_y - island_y) + abs(pirate_x - island_x - pirate_y + island_y) < 2 * thresh
            if required:
                return moveTo(island_x, island_y, pirate)

        if found_i3 and island3_status != "1":
            pirate_x, pirate_y = pirate.getPosition()
            island_x, island_y = split[-2:]
            island_x = int(island_x)
            island_y = int(island_y)
            required = abs(pirate_x - island_x + pirate_y - island_y) + abs(pirate_x - island_x - pirate_y + island_y) < 2 * thresh
            if required:
                return moveTo(island_x, island_y, pirate)
            
    return spread(pirate)

# island code -1 means that we have discovered the island
# island code 2 represents opp is capturing or has captured the island
# island code 1 means that we have captured the island 

def ActTeam(team):
    island_status = team.trackPlayers()

    signal = team.getTeamSignal()
    if signal == "":
        signal = "," * 9

    spawn_x, spawn_y = team.getDeployPoint()
    if spawn_x == 0 and spawn_y == 0:
        quad = 1
    if spawn_x != 0 and spawn_y == 0:
        quad = 2
    if spawn_x == 0 and spawn_y != 0:
        quad = 3
    if spawn_x != 0 and spawn_y != 0:
        quad = 4

    split = signal.split(',')
    split[0] = str(quad)

    F = 200
    if team.getCurrentFrame() >= F:
        team.buildWalls(1)
        team.buildWalls(2)
        team.buildWalls(3)

        i1_status, i2_status, i3_status = split[1:8:3]
        # if we have discovered an island, and opp is capturing or has captured, set island state to 2
        if i1_status != "" and (island_status[3] == "oppCapturing" or island_status[3] == "oppCaptured"):
            split[1] = "2"
        if i2_status != "" and (island_status[4] == "oppCapturing" or island_status[4] == "oppCaptured"):
            split[4] = "2"
        if i3_status != "" and (island_status[5] == "oppCapturing" or island_status[5] == "oppCaptured"):
            split[7] = "2"

        # if island status is 2, but opp didnt capture, set island status to -1
        if i1_status == "2" and island_status[3] == "":
            split[1] = "-1"
        if i2_status == "2" and island_status[4] == "":
            split[4] = "-1"
        if i3_status == "2" and island_status[5] == "":
            split[7] = "-1"
        
        if island_status[0] == 'myCaptured':
            split[1] = "1"
        if island_status[1] == 'myCaptured':
            split[4] = "1"
        if island_status[2] == 'myCaptured':
            split[7] = "1"
       
    signal = ','.join(split)
    team.setTeamSignal(signal)
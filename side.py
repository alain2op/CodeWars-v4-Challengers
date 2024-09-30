import random
import math
#2 ideas, one is spread ie from the start point, each pirate goes on a lines of diff slope and move to farthest corner
#other is circling around when opponent builds walls

name = "a_script"
#teamsignal 0-12 chars island coords
#piratesignal 0-4 chars target
#piratesignal 4-7 chars work

def moveTo(x, y, pirate):
    position = pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    else:
        up = pirate.investigate_up()
        down = pirate.investigate_down()
        left = pirate.investigate_left()
        right = pirate.investigate_right()
        if random.randint(1,2) == 1:
            if(int(pirate.getTeamSignal()[50:53])<30):
                if(position[0] > x):
                    if(left[1] == "blank" or "enemy" or "both"):
                        return 4
                    else:
                        if(position[1]>y):
                            if(up[1] == "blank"or "enemy" or "both"):
                                return 1
                            else:
                                if(down[1] == "blank"or "enemy" or "both"):
                                    return 3
                                else:
                                    if random.randint(1, 2) == 1:
                                        return (position[0] > x) * 2 + 2
                                    else:
                                        return (position[1] < y) * 2 + 1
                        if(position[1]<y):
                            if(down[1] == "blank" or "enemy" or "both"):
                                return 3
                            else:
                                if(up[1] == "blank" or "enemy" or "both"):
                                    return 1
                                else:
                                    if random.randint(1, 2) == 1:
                                        return (position[0] > x) * 2 + 2
                                    else:
                                        return (position[1] < y) * 2 + 1
                if(position[0] < x):
                    if(right[1] == "blank"or "enemy" or "both"):
                        return 2
                    else:
                        if(position[1]>y):
                            if(up[1] == "blank"or "enemy" or "both"):
                                return 1
                            else:
                                if(down[1] == "blank"or "enemy" or "both"):
                                    return 3
                                else:
                                    if random.randint(1, 2) == 1:
                                        return (position[0] > x) * 2 + 2
                                    else:
                                        return (position[1] < y) * 2 + 1
                        if(position[1]<y):
                            if(down[1] == "blank"or "enemy" or "both"):
                                return 3
                            else:
                                if(up[1] == "blank"or "enemy" or "both"):
                                    return 1
                                else:
                                    if random.randint(1, 2) == 1:
                                        return (position[0] > x) * 2 + 2
                                    else:
                                        return (position[1] < y) * 2 + 1
            if(int(pirate.getTeamSignal()[50:53])>30):
                if(position[0] > x):
                    if(left[1] == "blank"):
                        return 4
                    else:
                        if(position[1]>y):
                            if(up[1] == "blank"):
                                return 1
                            else:
                                if(down[1] == "blank"):
                                    return 3
                                else:
                                    if random.randint(1, 2) == 1:
                                        return (position[0] > x) * 2 + 2
                                    else:
                                        return (position[1] < y) * 2 + 1
                        if(position[1]<y):
                            if(down[1] == "blank"):
                                return 3
                            else:
                                if(up[1] == "blank"):
                                    return 1
                                else:
                                    if random.randint(1, 2) == 1:
                                        return (position[0] > x) * 2 + 2
                                    else:
                                        return (position[1] < y) * 2 + 1
                if(position[0] < x):
                    if(right[1] == "blank"):
                        return 2
                    else:
                        if(position[1]>y):
                            if(up[1] == "blank"):
                                return 1
                            else:
                                if(down[1] == "blank"):
                                    return 3
                                else:
                                    if random.randint(1, 2) == 1:
                                        return (position[0] > x) * 2 + 2
                                    else:
                                        return (position[1] < y) * 2 + 1
                        if(position[1]<y):
                            if(down[1] == "blank"):
                                return 3
                            else:
                                if(up[1] == "blank"):
                                    return 1
                                else:
                                    if random.randint(1, 2) == 1:
                                        return (position[0] > x) * 2 + 2
                                    else:
                                        return (position[1] < y) * 2 + 1
        else:
            if(int(pirate.getTeamSignal()[50:53])<30):
                if(position[1] > y):
                    if(up[1] == "blank" or "enemy" or "both"):
                        return 1
                    else:
                        if(position[0]>x):
                            if(left[1] == "blank"or "enemy" or "both"):
                                return 4
                            else:
                                if(right[1] == "blank"or "enemy" or "both"):
                                    return 2
                                else:
                                    if random.randint(1, 2) == 1:
                                        return (position[0] > x) * 2 + 2
                                    else:
                                        return (position[1] < y) * 2 + 1
                        if(position[0]<x):
                            if(right[1] == "blank" or "enemy" or "both"):
                                return 2
                            else:
                                if(left[1] == "blank" or "enemy" or "both"):
                                    return 4
                                else:
                                    if random.randint(1, 2) == 1:
                                        return (position[0] > x) * 2 + 2
                                    else:
                                        return (position[1] < y) * 2 + 1
                if(position[1] < y):
                    if(down[1] == "blank" or "enemy" or "both"):
                        return 3
                    else:
                        if(position[0]>x):
                            if(left[1] == "blank"or "enemy" or "both"):
                                return 4
                            else:
                                if(right[1] == "blank"or "enemy" or "both"):
                                    return 2
                                else:
                                    if random.randint(1, 2) == 1:
                                        return (position[0] > x) * 2 + 2
                                    else:
                                        return (position[1] < y) * 2 + 1
                        if(position[0]<x):
                            if(right[1] == "blank" or "enemy" or "both"):
                                return 2
                            else:
                                if(left[1] == "blank" or "enemy" or "both"):
                                    return 4
                                else:
                                    if random.randint(1, 2) == 1:
                                        return (position[0] > x) * 2 + 2
                                    else:
                                        return (position[1] < y) * 2 + 1
            if(int(pirate.getTeamSignal()[50:53])>30):
                if(position[1] > y):
                    if(up[1] == "blank"):
                        return 1
                    else:
                        if(position[0]>x):
                            if(left[1] == "blank"):
                                return 4
                            else:
                                if(right[1] == "blank"):
                                    return 2
                                else:
                                    if random.randint(1, 2) == 1:
                                        return (position[0] > x) * 2 + 2
                                    else:
                                        return (position[1] < y) * 2 + 1
                        if(position[0]<x):
                            if(right[1] == "blank"):
                                return 2
                            else:
                                if(left[1] == "blank"):
                                    return 4
                                else:
                                    if random.randint(1, 2) == 1:
                                        return (position[0] > x) * 2 + 2
                                    else:
                                        return (position[1] < y) * 2 + 1
                if(position[1] < y):
                    if(down[1] == "blank"):
                        return 3
                    else:
                        if(position[0]>x):
                            if(left[1] == "blank"):
                                return 4
                            else:
                                if(right[1] == "blank"):
                                    return 2
                                else:
                                    if random.randint(1, 2) == 1:
                                        return (position[0] > x) * 2 + 2
                                    else:
                                        return (position[1] < y) * 2 + 1
                        if(position[0]<x):
                            if(right[1] == "blank"):
                                return 2
                            else:
                                if(left[1] == "blank"):
                                    return 4
                                else:
                                    if random.randint(1, 2) == 1:
                                        return (position[0] > x) * 2 + 2
                                    else:
                                        return (position[1] < y) * 2 + 1
    # if random.randint(1, 2) == 1:
    #     return (position[0] > x) * 2 + 2
    # else:
    #     return (position[1] < y) * 2 + 1


def moveAway(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return random.randint(1, 4)
    if random.randint(1, 2) == 1:
        return (position[0] < x) * 2 + 2
    else:
        return (position[1] > y) * 2 + 1


def moveAway(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return random.randint(1, 4)
    if random.randint(1, 2) == 1:
        return (position[0] < x) * 2 + 2
    else:
        return (position[1] > y) * 2 + 1

def circleAround(x, y, radius, Pirate, initial="abc", clockwise=True):
    position = Pirate.getPosition()
    rx = position[0]
    ry = position[1]
    pos = [[x + i, y + radius] for i in range(-1 * radius, radius + 1)]
    pos.extend([[x + radius, y + i] for i in range(radius - 1, -1 * radius - 1, -1)])
    pos.extend([[x + i, y - radius] for i in range(radius - 1, -1 * radius - 1, -1)])
    pos.extend([[x - radius, y + i] for i in range(-1 * radius + 1, radius)])
    if [rx, ry] not in pos:
        if initial != "abc":
            return moveTo(initial[0], initial[1], Pirate)
        if rx in [x + i for i in range(-1 * radius, radius + 1)] and ry in [
            y + i for i in range(-1 * radius, radius + 1)
        ]:
            return moveAway(x, y, Pirate)
        else:
            return moveTo(x, y, Pirate)
    else:
        index = pos.index([rx, ry])
        return moveTo(
            pos[(index + (clockwise * 2) - 1) % len(pos)][0],
            pos[(index + (clockwise * 2) - 1) % len(pos)][1],
            Pirate,
        )
    
def checkIsland1(pirate):
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    left = pirate.investigate_left()
    right = pirate.investigate_right()
    if (up[0:-1] == "island" or down[0:-1] == "island") and (left[0:-1] == "island" or right[0:-1] == "island"):
        return True
    else:
        return False
def quadrant(point):
    # 1 2
    # 4 3
    x=point[0]
    y=point[1]
    if(x<dims[0]/2):
        if(y<dims[0]/2):
            return 1
        else:
            return 4
    else:
        if(y<dims[0]/2):
            return 2
        else:
            return 3
def checkIsland(pirate):
    dirs=[pirate.investigate_up()[0][:-1]=="island",pirate.investigate_ne()[0][:-1]=="island",pirate.investigate_right()[0][:-1]=="island",pirate.investigate_se()[0][:-1]=="island",pirate.investigate_down()[0][:-1]=="island",pirate.investigate_sw()[0][:-1]=="island",pirate.investigate_left()[0][:-1]=="island",pirate.investigate_nw()[0][:-1]=="island"]
    x,y=int(pirate.getPosition()[0]),int(pirate.getPosition()[1])
    if(dirs.count(1)==1):
        if(dirs[1]):
            return (x+2,y-2)
        elif dirs[3]:
            return (x+2,y+2)
        elif dirs[5]:
            return (x-2,y+2)
        elif dirs[7]:
            return (x-2,y-2)
        else:
            return (0,0)
    elif (dirs.count(1)==3):
        if(dirs[0] and dirs[1] and dirs[-1]):
            return (x,y-2)
        elif(dirs[2] and dirs[1] and dirs[3]):
            return (x+2,y)
        elif (dirs[4] and dirs[3] and dirs[5]):
            return (x,y+2)
        elif (dirs[6] and dirs[5] and dirs[3]):
            return (x-2,y)
        else:
            return (0,0)
    elif (dirs.count(1)==2):
        if(dirs[0] and dirs[1]):
            return (x+1, y-2)
        elif(dirs[1] and dirs[2]):
            return (x+2, y-1)
        elif(dirs[2] and dirs[3]):
            return (x+2, y+1)
        elif(dirs[3] and dirs[4]):
            return (x+1, y+2)
        elif(dirs[4] and dirs[5]):
            return (x-1, y+2)
        elif(dirs[5] and dirs[6]):
            return (x-2, y+1)
        elif(dirs[6] and dirs[7]):
            return (x-2, y-1)
        elif(dirs[7] and dirs[0]):
            return (x-1, y-1)
        else:
            return (0,0)
    else:
        return (0,0)
def f1(arr):
    for i in range(len(arr)):
        if arr[i] == 1:
            return i
def vertexMove(bx,by,pirate):
    id=int(pirate.getID())
    dx, dy = pirate.getDimensionX(), pirate.getDimensionY()
    if id % 17 == 0:
        mx, my = dx -1 -bx, dy -1 -by
        string=str(mx).zfill(2)+str(my).zfill(2)+pirate.getSignal()[4:100]
        pirate.setSignal(string)
        return moveTo(mx, my, pirate)
    else:
        if id % 2 == 0:
            n = (id%17)/2
            kx,ky=dx -1 -bx, dy -1 -by
            lx,ly=dx-1-bx,by
            mx,my=int(((n-1)*kx+(9-n)*lx)/8),int(((n-1)*ky+(9-n)*ly)/8)
            string=str(mx).zfill(2)+str(my).zfill(2)+pirate.getSignal()[4:100]
            pirate.setSignal(string)
            return moveTo(mx, my, pirate)
        else:
            n = (id%17+1)/2
            kx,ky=dx -1 -bx, dy -1 -by
            lx,ly=bx,dy-1-by
            mx,my=int(((n-1)*kx+(9-n)*lx)/8),int(((n-1)*ky+(9-n)*ly)/8)
            string=str(mx).zfill(2)+str(my).zfill(2)+pirate.getSignal()[4:100]
            pirate.setSignal(string)
            return moveTo(mx, my, pirate)

def movePirate(pirate):
    bx , by = pirate.getDeployPoint()   
    dx, dy = pirate.getDimensionX(), pirate.getDimensionY()
    id = int(float(pirate.getID()))
    if pirate.getSignal() == "":
        string="0"*100
        pirate.setSignal(string)
        return vertexMove(bx,by,pirate)
    else:
            tx,ty=int(float(pirate.getSignal()[0:2])),int(float(pirate.getSignal()[2:4]))
            px,py=pirate.getPosition()
            if (px==tx) and (py==ty):
                if( px==0 or px==dx-1 ) and (py==0 or py==dy-1):
                    return vertexMove(px,py,pirate)
                else:
                    if (px==0 or px==dx-1):
                        mx=(dx-1)*(1-bool(px))
                        my=random.randint(0,dy-1)
                        string=str(mx).zfill(2)+str(my).zfill(2)+pirate.getSignal()[4:100]
                        pirate.setSignal(string)
                        return moveTo(mx,my,pirate)
                    elif (py==0 or py==dy-1):
                        my=(dy-1)*(1-bool(py))
                        mx=random.randint(0,dx-1)
                        string=str(mx).zfill(2)+str(my).zfill(2)+pirate.getSignal()[4:100]
                        pirate.setSignal(string)
                        return moveTo(mx,my,pirate)
                    else:
                        mx=int(px<(dx-1)/2)*(dx-1)
                        my=int(py<(dy-1)/2)*(dy-1)
                        string=str(mx).zfill(2)+str(my).zfill(2)+pirate.getSignal()[4:100]
                        pirate.setSignal(string)                        
                        return moveTo(mx,my,pirate)
            else:
                return moveTo(tx,ty,pirate)


def ActPirate(pirate):
    # complete this function
    # track=pirate.trackPlayers()
    # dirs1=[int(pirate.investigate_up()[0][:-1]=="island"),int(pirate.investigate_ne()[0][:-1]=="island"),int(pirate.investigate_right()[0][:-1]=="island"),int(pirate.investigate_se()[0][:-1]=="island"),int(pirate.investigate_down()[0][:-1]=="island"),int(pirate.investigate_sw()[0][:-1]=="island"),int(pirate.investigate_left()[0][:-1]=="island"),int(pirate.investigate_nw()[0][:-1]=="island")]
    # directions=[pirate.investigate_up(),pirate.investigate_ne(),pirate.investigate_right(),pirate.investigate_se(),pirate.investigate_down(),pirate.investigate_sw(),pirate.investigate_left(),pirate.investigate_nw()]
    # if((1 in dirs1) and checkIsland(pirate)!=(0,0)):
    #     island=int(directions[f1(dirs1)][0][-1])
    #     start=84+island*4
    #     if(pirate.getTeamSignal()[start:start+4])=="0000":
    #         point=checkIsland(pirate)
    #         #print(dirs1,"inside")
    #         isignal=str(point[0]).zfill(2)+str(point[1]).zfill(2)
    #         s=pirate.getTeamSignal()
    #         s=s[:start]+isignal+s[start+4:]
    #         # print(s)
    #         pirate.setTeamSignal(s)
    # enemy=[track[3]=="oppCapturing",track[4]=="oppCapturing",track[5]=="oppCapturing"]
    # run=enemy[int(pirate.getID())%3]
    # if (pirate.getCurrentFrame()>125) and run and (pirate.getTeamSignal()[88+(int(pirate.getID())%3)*4:92+(int(pirate.getID())%3)*4]!="0000"):
    #     destination=(int(pirate.getTeamSignal()[88+(int(pirate.getID())%3)*4:90+(int(pirate.getID())%3)*4]),int(pirate.getTeamSignal()[90+(int(pirate.getID())%3)*4:92+(int(pirate.getID())%3)*4]))
    #     return moveTo(destination[0],destination[1],pirate)
    # else:
    #     if(pirate.getSignal()==""):
    #         id=((int(pirate.getID())-1)%24)
    #         pointx=int(pirate.getTeamSignal()[id*4:id*4+2])
    #         pointy=int(pirate.getTeamSignal()[id*4+2:id*4+4])
    #         string=str(pointx).zfill(2)+str(pointy).zfill(2)+str(id)
    #         pirate.setSignal(string)
    #         return moveTo(pointx,pointy,pirate)
    #     else:
    #         targetx,targety=int(pirate.getSignal()[0:2]),int(pirate.getSignal()[2:4])
    #         if(targetx==pirate.getPosition()[0] and targety==pirate.getPosition()[1]):
    #             signal=pirate.getSignal()
    #             id=signal[4:]
    #             id=(int(id)+1)%22
    #             newpointx,newpointy=int(pirate.getTeamSignal()[id*4:id*4+2]),int(pirate.getTeamSignal()[id*4+2:id*4+4])
    #             newstring=str(newpointx).zfill(2)+str(newpointy).zfill(2)+str(id)
    #             pirate.setSignal(newstring)
    #             return moveTo(newpointx,newpointy,pirate)
    #         else:
    #             return moveTo(targetx,targety,pirate)
        id=int(pirate.getID())
        dirs1=[int(pirate.investigate_up()[0][:-1]=="island"),int(pirate.investigate_ne()[0][:-1]=="island"),int(pirate.investigate_right()[0][:-1]=="island"),int(pirate.investigate_se()[0][:-1]=="island"),int(pirate.investigate_down()[0][:-1]=="island"),int(pirate.investigate_sw()[0][:-1]=="island"),int(pirate.investigate_left()[0][:-1]=="island"),int(pirate.investigate_nw()[0][:-1]=="island")]         
        directions=[pirate.investigate_up(),pirate.investigate_ne(),pirate.investigate_right(),pirate.investigate_se(),pirate.investigate_down(),pirate.investigate_sw(),pirate.investigate_left(),pirate.investigate_nw()]
        track=pirate.trackPlayers()
        if (1 in dirs1 and checkIsland(pirate)!=(0,0)):
            island=int(directions[f1(dirs1)][0][-1])
            start=(island-1)*4
            if(pirate.getTeamSignal()[start:start+4])=="0000":
                string=pirate.getSignal[:3+island]+"1"+pirate.getSignal()[4+island:]
                pirate.setSignal(string)
                point=checkIsland(pirate)
                isignal=str(point[0]).zfill(2)+str(point[1]).zfill(2)
                s=pirate.getTeamSignal()
                s=s[:start]+isignal+s[start+4:]
                pirate.setTeamSignal(s)
        work=pirate.getSignal()[4:7]!="000"
        island=100
        if(work):
            s=pirate.getSignal()[4:7]
            island=s.index('1')+1
        if(work) and (pirate.trackPlayers()[island-1]!="myCaptured"):
            x,y=int(pirate.getTeamSignal()[(island-1)*4:(island-1)*4+2]),int(pirate.getTeamSignal()[(island-1)*4+2:(island-1)*4+4])
            return(moveTo(x,y,pirate))
        elif(work) and (pirate.trackPlayers()[island-1]=="myCaptured"):
            string=pirate.getSignal()[:4]+"000"+pirate.getSignal()[7:]
            pirate.setSignal(string)
        if(track[id%3+3]=="oppCapturing" and pirate.getTeamSignal()[(id%3)*4:(id%3)*4+4]!="0000" ):
            x,y=pirate.getTeamSignal()[(id%3)*4:(id%3)*4+2],pirate.getTeamSignal()[(id%3)*4+2:(id%3)*4+4]
            return moveTo(x,y,pirate)



#movement
        return(movePirate(pirate))
        pass
def ActTeam(team):
    if team.getTeamSignal()=="":
        string='0'*100
        team.setTeamSignal(string)
    if(team.getCurrentFrame()<2):
        global dp,dims,odp,tq,oq #deploy point, opponent deploy point,team quadrant, opponent quadrant
        dp=(team.getDeployPoint())
        dims=(team.getDimensionX(),team.getDimensionY())
        odp = (int(not dp[0])*(dims[0]-1),int(not dp[1])*(dims[1]-1))
        tq=quadrant(dp)
        oq=quadrant(odp)

    #     string = '0' * 100

    #     string = str(int((dp[0]*3+odp[0])/4)).zfill(2) + string[2:]
    #     string = string[:2] + str(int((dp[1]+odp[1]*3)/4)).zfill(2) + string[4:]
    #     string = string[:4] + str(int((dp[0]+odp[0])/2)).zfill(2) + string[6:]
    #     string = string[:6] + str(int((dp[1]))).zfill(2) + string[8:]
    #     string = string[:8] + str(int((dp[0]+odp[0]*3)/4)).zfill(2) + string[10:]
    #     string = string[:10] + str(int((dp[1]+odp[1]*3)/4)).zfill(2) + string[12:]
    #     string = string[:12] + str(int((dp[0]*0+odp[0]*4)/4)).zfill(2) + string[14:]
    #     string = string[:14] + str(int((dp[1]*4+odp[1]*0)/4)).zfill(2) + string[16:]
    #     string = string[:16] + str(int((dp[0]*3+odp[0]*1)/4)).zfill(2) + string[18:]
    #     string = string[:18] + str(int((dp[1]*3+odp[1]*1)/4)).zfill(2) + string[20:]
    #     string = string[:20] + str(int((dp[0]*0+odp[0]*4)/4)).zfill(2) + string[22:]
    #     string = string[:22] + str(int((dp[1]*2+odp[1]*2)/4)).zfill(2) + string[24:]
    #     string = string[:24] + str(int((dp[0]*2+odp[0]*2)/4)).zfill(2) + string[26:]
    #     string = string[:26] + str(int((dp[1]*0+odp[1]*4)/4)).zfill(2) + string[28:]
    #     string = string[:28] + str(int((dp[0]*1+odp[0]*3)/4)).zfill(2) + string[30:]
    #     string = string[:30] + str(int((dp[1]*3+odp[1]*1)/4)).zfill(2) + string[32:]
    #     string = string[:32] + str(int((dp[0]*4+odp[0]*0)/4)).zfill(2) + string[34:]
    #     string = string[:34] + str(int((dp[1]*2+odp[1]*2)/4)).zfill(2) + string[36:]
    #     string = string[:36] + str(int((dp[0]*0+odp[0]*4)/4)).zfill(2) + string[38:]
    #     string = string[:38] + str(int((dp[1]*0+odp[1]*4)/4)).zfill(2) + string[40:]
    #     string = string[:40] + str(int((dp[0]*2+odp[0]*2)/4)).zfill(2) + string[42:]
    #     string = string[:42] + str(int((dp[1]*2+odp[1]*2)/4)).zfill(2) + string[44:]
    #     string = string[:44] + str(int((dp[0]*4+odp[0]*0)/4)).zfill(2) + string[46:]
    #     string = string[:46] + str(int((dp[1]*0+odp[1]*4)/4)).zfill(2) + string[48:]
    #     string = string[:48] + str(int((dp[0]*3+odp[0]*1)/4)).zfill(2) + string[50:]
    #     string = string[:50] + str(int((dp[1]*3+odp[1]*1)/4)).zfill(2) + string[52:]
    #     string = string[:52] + str(int((dp[0]*2+odp[0]*2)/4)).zfill(2) + string[54:]
    #     string = string[:54] + str(int((dp[1]*4+odp[1]*0)/4)).zfill(2) + string[56:]
    #     string = string[:56] + str(int((dp[0]*1+odp[0]*3)/4)).zfill(2) + string[58:]
    #     string = string[:58] + str(int((dp[1]*3+odp[1]*1)/4)).zfill(2) + string[60:]
    #     string = string[:60] + str(int((dp[0]*0+odp[0]*4)/4)).zfill(2) + string[62:]
    #     string = string[:62] + str(int((dp[1]*2+odp[1]*2)/4)).zfill(2) + string[64:]
    #     string = string[:64] + str(int((dp[0]*0+odp[0]*4)/4)).zfill(2) + string[66:]
    #     string = string[:66] + str(int((dp[1]*4+odp[1]*0)/4)).zfill(2) + string[68:]
    #     string = string[:68] + str(int((dp[0]*3+odp[0]*1)/4)).zfill(2) + string[70:]
    #     string = string[:70] + str(int((dp[1]*1+odp[1]*3)/4)).zfill(2) + string[72:]
    #     string = string[:72] + str(int((dp[0]*4+odp[0]*0)/4)).zfill(2) + string[74:]
    #     string = string[:74] + str(int((dp[1]*2+odp[1]*2)/4)).zfill(2) + string[76:]
    #     string = string[:76] + str(int((dp[0]*2+odp[0]*2)/4)).zfill(2) + string[78:]
    #     string = string[:78] + str(int((dp[1]*4+odp[1]*0)/4)).zfill(2) + string[80:]
    #     string = string[:80] + str(int((dp[0]*3+odp[0]*1)/4)).zfill(2) + string[82:]
    #     string = string[:82] + str(int((dp[1]*3+odp[1]*1)/4)).zfill(2) + string[84:]
    #     string = string[:84] + str(int((dp[0]*4+odp[0]*0)/4)).zfill(2) + string[86:]
    #     string = string[:86] + str(int((dp[1]*4+odp[1]*0)/4)).zfill(2) + string[88:]

    #     team.setTeamSignal(string)
    #print(team.getTeamSignal())
    pass
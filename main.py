#https://docs.google.com/document/d/1c2sKY1Q4PDsK8h_j1TRbw3K_OkEq5jbrHTj6mb4z3LY/edit?tab=t.0
from items.oreuh import nts,no_rock,placed_rock,rock,dark_rock,charium_ore,nevelium_ore,decante_ore,charcor_ore,void,dirt,chest,chest52
from items.itemuh import hts,pick,charcor_pick,nevelium_pick,sword,charcor_sword,charium_sword,nevelium_sword,burb
from base_funcs import *
from bobs import xny,bobs
from Loot.looter import gitStf

from time import sleep
from random import randint,choice

import saveus.piler as piler
import sys
import keyboard
def roll():
    rolled=[]
    while len(rolled)<randint(3,9):
        ch=choice(gitStf())
        if randint(0,100)<=ch[1]:
            rolled.append([ch[0],randint(ch[2][0],ch[2][1])])
    roll2=[]
    for i in rolled:
        if str(i[0])[-1]=="0":
            roll2.append([nts[int(i[0]/10)],i[1]])
        else:
            roll2.append([hts[int(i[0]/10)],i[1]])
    return roll2
#this makes cool shapes
def get_dir(n):
    if n==0:#up
        return choice([3,1,2])
    elif n==1:#right
        return choice([2,0,3])
    elif n==2:#left
        return choice([1,0,3])
    elif n==3:#down
        return choice([0,1,2])
class tiles:
    def __init__(self):
        self.mw=10
        self.mh=10
        self.ben=[]
        self.bit=[[2 for j in range(self.mw)]for i in range(self.mh)]
        self.do_gen2()
    #get the neighbors of a tile
    def gNbr(self,x,y):
        tkn=[[-1,-1,-1],[-1,-2,-1],[-1,-1,-1],]
        for y1 in range(-1,1):
            for x1 in range(-1,1):
                if inr(x+x1,0,self.mw) and inr(x+y1,0,self.mh):
                    if self.bit[y+y1][x+x1]!=-1 :#and y1!=0 and x1!=0:
                        tkn[y1+1][x1+1]=self.bit[y+y1][x+x1]
                else:
                    tkn[y1+1][x1+1]=-2
        return tkn
    #is the map fully generated?
    def gtg(self):
        # gd=False
        for i in self.bit:
            if -1 in i:
                # gd=True
                return True
        return False
    #generates a single tile of the map
    def gen(self,cx=-1,cy=-1):
        #0-no_rock
        #1-placed rock
        #2-rock
        #3-dark rock
        #4-charium ore
        #5-nevlium ore
        #6-decante ore
        #7-charcor ore
        #just get the right x/y
        if cx==-1 or cy==-1:
            cx=randint(0,self.mw-1)
            cy=randint(0,self.mh-1)
        if cx>=self.mw:
            cx=self.mw-1
        if cy>=self.mh:
            cy=self.mh-1
        #this makes it so it dosen't try to place where its been
        if [cx,cy]in self.ben:
            return [-1,-1]
        else:
            self.ben.append([cx,cy])
        #gte its neighbors
        tkn=self.gNbr(cx,cy)
        cnt={-2:[],-1:[],0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
        for y,i in enumerate(tkn):
            for x,j in enumerate(i):
                cnt[j].append([x,y])
        if self.bit[cy][cx]!=-1:
            c=choice(cnt[-1])
            return cx+c[0]-1,cy+c[1]-1
        #get the most popular one, caus thats probally whats next!
        mp=[-1,0]
        for i in cnt:
            if i!=-1 and i!=-2:
                if len(cnt[i])>mp[1]+randint(-2,2):
                    mp=[i,len(cnt[i])]
        #But we gotta make sure its a good number, and rocks are more common!
        tl=mp[0]
        if tl==-1 or tl==8:
            tl=randint(0,len(nts)-1)
        if randint(0,3)==0:
            tl=3
        if randint(0,1)==0:
            tl=2
        #add it and return your face
        if self.bit[cy][cx]==-1:
            self.bit[cy][cx]=tl
        if len(cnt[-1])>0:
            c=choice(cnt[-1])
            return cx+c[0]-1,cy+c[1]-1
        else:
            return [-1,-1]
    #this just runs the generator
    def do_gen(self):
        #start genering at a random point
        x=randint(0,self.mw-1)
        y=randint(0,self.mh-1)
        q=[x,y]
        #generates it all
        while self.gtg():# and ir<500:
            ir+=1
            q=self.gen(q[0],q[1])
    #a better gen?
    def do_gen2(self):
        #how many spots
        clpr=(self.mw+self.mh)//2#+randint(-1,1)
        #run through them
        for i in range(clpr):
            #get a random spot/id for the stuff your adding
            tk=[randint(0,self.mw-1),randint(0,self.mh-1),randint(0,len(nts)-1),0]
            #we dont want placed rocks cause no people her right?
            if tk[2]==1 or tk[2]==8:
                continue
            #how many?
            tk[3]=nts[tk[2]].spr+randint(-1,1)
            #add a brick for each thingy
            grw=randint(0,3)
            for i in range(tk[3]):
                grw=get_dir(grw)
                #choose a dir^ and make the new x and y to place
                tk[0]=constrain(tk[0]+gd(grw)[0],0,self.mw-1)
                tk[1]=constrain(tk[1]+gd(grw)[1],0,self.mh-1)
                self.bit[tk[1]][tk[0]]=tk[2]
class MP:
    def __init__(self):
        self.mw=2
        self.mh=2
        self.mp=[[tiles() for j in range(self.mw)]for i in range(self.mh)]
        self.bit=[]
        self.tl=xny(0,0)
        self.data={}
        self.exp()
        self.bit[0][0]=0
        self.bit[0][1]=10
        self.datar()
    #add to the map on top
    def addUp(self):
        self.mh+=1
        self.tl.y+=1
        self.mp.append([tiles() for i in range(self.mw)])
        # self.mh+=1
        # plr.y+=1
        # self.mp.insert([-1 for i in range(self.mw)],0)
        # for i in range(self.mw):
        #     self.gen(i,0)
    #add to the map on the right
    def addRgt(self):
        self.mw+=1
        for i in range(self.mh):
            self.mp[i].append(tiles())
        self.mw+=1
        # for i in range(self.mh):
        #     self.mp[i].append(-1)
        # for i in range(self.mh):
        #     self.gen(self.mw-1,i)
    #add to the map on bottom
    def addDwn(self):
        self.mh+=1
        self.mp.append([tiles() for i in range(self.mw)])
        # self.mh+=1
        # self.mp.append([-1 for i in range(self.mw)])
        # for i in range(self.mw):
        #     self.gen(i,self.mh-1)
    #add to the map on the left
    def addLft(self):
        self.mw+=1
        self.tl.x+=1
        for i in range(self.mh):
            self.mp[i].insert(0,tiles())
        # self.mw+=1
        # plr.x+=1
        # for i in range(self.mh):
        #     self.mp[i].append(-1)
        # for i in range(self.mh):
        #     self.gen(self.mw-1,i)
    #Do all the adds
    def addOn(self,dirr):
        if dirr==0:
            self.addUp()
        elif dirr==1:
            self.addRgt()
        elif dirr==2:
            self.addDwn()
        elif dirr==3:
            self.addLft()
        if dirr in [0,1,2,3]:
            self.exp()
        move(0,12)
        print(dirr,self.tl)
    #not needed, would expand the map. idk if well finish and add
    def exp(self):
        # exp=[]
        # for i in range(self.mh*2):
        #     exp.append([])
        #     for j in range(self.mw*2):
        #         exp[-1].append(-1)
        # self.mp=exp.copy()
        #we want every top of the tiles across
        #then next, than next and so on till the bottom
        self.bit=[]
        for i in self.mp:
            #goes down
            for k in range(len(self.mp[0][0].bit)):
                #goes across each tile in the spot
                self.bit.append([])
                for j in i:
                    self.bit[-1].append(j.bit[k])
                    #goes across
        bit2=[]
        for i in self.bit:
            bit2.append([])
            # print(i)
            for j in i:
                # print(j)
                # for k in j:
                # print(k)
                bit2[-1]+=j
        self.bit=bit2.copy()
    def datar(self):
        for a,i in enumerate(self.bit):
            for b,j in enumerate(i):
                if j==10:
                    self.data[f"{b},{a}"]=chest52("chest","C",1,10,"chest",0,roll())
        #             print(f"{b},{a}")
        # input()
    #runs the save code for JUST THE MAP, must be implemetned with the player and entity save codes!
    def save(self):
        return str(self.mp),str(self.mw),str(self.mh)
    def getTile(self):
        return self.mp[self.tl.y][self.tl.x]
# print("   |")
# print("   |")
# print("   |")
# for i in range(3):
#     for j in range(3):
#         move(i+1,j)
#         print(i)
class plr:
    def __init__(self):
        self.x=0
        self.y=0
        self.tx=0
        self.ty=0
        self.dir=1
        self.us=["^",">","V","<"]
        self.hl=0
        self.hold=[
            [itm(void,0),itm(void,0),itm(void,0),itm(void,0),itm(void,0),],[itm(void,0),itm(void,0),itm(void,0),itm(void,0),itm(void,0),],[itm(void,0),itm(void,0),itm(void,0),itm(void,0),itm(void,0),],[itm(void,0),itm(void,0),itm(void,0),itm(void,0),itm(void,0),],[itm(void,0),itm(void,0),itm(void,0),itm(void,0),itm(void,0),],
            [itm(burb,1),itm(void,0),itm(void,0),itm(void,0),itm(void,0),],]
        #exli(exli(itm(void,0),5),5)
    def dr(self,ox,oy):
        # [oy][ox]
        move((ox)%10+1,(oy)%10+1)
        print(no_rock)
        move((self.x)%10+1,(self.y)%10+1)
        print(self.us[self.dir])
        # move(0,13)
        # print("\033[48;5;240m")
        for b,j in enumerate(self.hold[5]):
            prat(("\033[48;5;240m"if b==self.hl else"")+"|"+str(j)+("\033[0m"if b==self.hl else""),(b)*16+1,11)
    def move(self,d):
        global mp
        if d=="b":
            dr=gd(self.dir)
            nx,ny=self.x+dr[0],self.y+dr[1]
            self.addItm()
            mp.getTile().bit[ny][nx]=0
            move(nx+1,ny+1)
            print(no_rock)
            # move(0,10)
            # print("\n\n",self.dir,dr,self.x,self.y,nx,ny)
            # return
        elif d=="u":
            self.dir=0
        elif d=="r":
            self.dir=1
        elif d=="d":
            self.dir=2
        elif d=="l":
            self.dir=3
        ox,oy=self.x,self.y
        dx=self.x+gd(self.dir)[0]
        dy=self.y+gd(self.dir)[1]
        tk=0
        if dx>=0 and dx<=9 and dy>=0 and dy<=9:
            tk=mp.getTile().bit[dy][dx]
        # move(0,11)
        # print(tk,gd(self.dir),self.dir," "*10)
        if tk==0:
            self.x,self.y=dx,dy
        self.dr(ox,oy)
    def oub(self):
        global mp,pr
        isd=False
        if self.dir==0 and self.y<0:
            self.y=9
            mp.tl.y-=1
            isd=True
        elif self.dir==1 and self.x>9:
            self.x=0
            mp.tl.x+=1
            isd=True
        elif self.dir==2 and self.y>9:
            self.y=0
            mp.tl.y+=1
            isd=True
        elif self.dir==3 and self.x<0:
            self.x=9
            mp.tl.x-=1
            isd=True
        if isd:
            mp.addOn(self.dir)
            pr(0,0)
    def mover(self,d):
        global mp
        if d.isdigit() and inr(int(d)-1,0,5):
            self.hl=int(d)-1
            # print(self.hl)
            self.y=0 if self.y+mv[1]<0 else(len(mp.bit)-2 if self.y+mv[1]>=len(mp.bit)-1 else self.y)
            self.x=0 if self.x+mv[0]<0 else(len(mp.bit[self.y+mv[1]])-2 if self.x+mv[0]>=len(mp.bit[self.y+mv[1]])-1 else self.x)
            self.dr(self.x,self.y)
            return
        elif d=="s":
            return
        elif d=="":
            return
        elif d=="i":
            self.prInv()
            return
        elif d=="o":
            mv=gd(self.dir)
            if self.y+mv[1]<0 or self.y+mv[1]>len(mp.bit)-1:
                return
            if self.x+mv[0]<0 or self.x+mv[0]>len(mp.bit[self.y+mv[1]])-1:
                return
            if mp.bit[self.y+mv[1]][self.x+mv[0]]==10:
                c=mp.data[f"{self.x+mv[0]},{self.y+mv[1]}"]
                c.prHold(self)
                pr(self.x,self.y)
            return
        elif d=="p":
            mv=gd(self.dir)
            if self.y+mv[1]<0 or self.y+mv[1]>len(mp.bit)-1:
                return
            if self.x+mv[0]<0 or self.x+mv[0]>len(mp.bit[self.y+mv[1]])-1:
                return
            if mp.bit[self.y+mv[1]][self.x+mv[0]]==0:
                if not self.hnd().tp.idd in [0,8]:
                    mp.bit[self.y+mv[1]][self.x+mv[0]]=self.hnd().tp.idd
                    self.hold[5][self.hl].no-=1
                    self.fixInv()
            return
        elif d=="b":
            dr=gd(self.dir)
            nx,ny=self.x+dr[0],self.y+dr[1]
            if ny<0 or ny>len(mp.bit)-1:
                return
            if nx<0 or nx>len(mp.bit[ny])-1:
                return
            if self.hnd().tp.ms>=nts[mp.bit[ny][nx]].ml:
                self.addItm(nts[mp.bit[ny][nx]])
                mp.bit[ny][nx]=0
                move(nx+1,ny+1)
                print(no_rock)
        elif d in "urld":
            self.dir={"u":0,"r":1,"d":2,"l":3}[d]
        mv=gd(self.dir)
        drw=(self.x%10 and self.dir==1) or ((self.x-1)%10 and self.dir==3)or(self.y%10 and self.dir==2) or ((self.y-1)%10 and self.dir==0)
        self.y=0 if self.y+mv[1]<0 else(len(mp.bit)-2 if self.y+mv[1]>=len(mp.bit)-1 else self.y)
        self.x=0 if self.x+mv[0]<0 else(len(mp.bit[self.y+mv[1]])-2 if self.x+mv[0]>=len(mp.bit[self.y+mv[1]])-1 else self.x)
        if self.y+mv[1]>=0 and self.y+mv[1]<len(mp.bit) and self.x+mv[0]>=0 and self.x+mv[0]<len(mp.bit[self.y+mv[1]]):
            if mp.bit[self.y+mv[1]][self.x+mv[0]]==0:
                self.y,self.x=self.y+mv[1],self.x+mv[0]
        self.dr(self.x-mv[0],self.y-mv[1])
        if drw:
            pr(self.x,self.y)
    def prInv(self):
        # for i in self.hold:
        #     for j in i:
        #         print(j)
        # intput()
        while True:
            print("\033c")
            for b in range(5):
                prat(b+1,b*16+3,1)
            for a,i in enumerate(self.hold):
                prat(a+1,1,a+(3 if a==5 else 2))
                for b,j in enumerate(i):
                    prat("|"+str(j),(b)*16+3,(a)+(3 if a==5 else 2))
            print("Row 6 is the bar you can access anytime!")
            dor=intput("Would you like to move an item or exit? (move,exit)")
            if dor=="move":
                x1,y1=gtInt("What is the X coordinate of the item?"),gtInt("Whats the Y?")
                x2,y2=gtInt("What is the X coordinate of where you to move it?"),gtInt("What is the Y?")
                # print(x1,y1,x2,y2)
                it1=self.hold[y1-1][x1-1]
                it2=self.hold[y2-1][x2-1]
                if it1.tp.nm==it2.tp.nm:
                    it1.no+=it2.no
                    it2=itm(void,0)
                self.hold[y1-1][x1-1],self.hold[y2-1][x2-1]=it2,it1
            elif dor=="exit":
                print("Exiting...")
                return
    def prInv1(self):
        for b in range(5):
            prat(b+1,b*16+3,1)
        for a,i in enumerate(self.hold):
            prat(a+1,1,a+(3 if a==5 else 2))
            for b,j in enumerate(i):
                prat("|"+str(j),(b)*16+3,(a)+(3 if a==5 else 2))
    def addItm(self,item):
        if not isinstance(item,itm):
            item=itm(item,1)
        if item.tp.idd==0:
            return
        for i in range(5,-1,-1):
            for j in range(5):
                if self.hold[i][j].tp.nm==item.tp.nm:
                    self.hold[i][j].no+=item.no
                    return
        for i in range(5,-1,-1):
            for j in range(5):
                if self.hold[i][j].tp.nm=="void":
                    self.hold[i][j]=item
                    return
    def fixInv(self):
        for a,i in enumerate(self.hold):
            for b,j in enumerate(i):
                if j.no<=0:
                    self.hold[a][b]=itm(void,0)
    def hnd(self):
        return self.hold[5][self.hl]
p=plr()
# p.hold[0][0]=itm(rock,10)
# p.hold[5][0]=itm(rock,10)
# p.addItm(itm(rock,2))
# p.addItm(itm(placed_rock,5))
# p.prInv()
# quit()
mp=MP()
def pr(x,y):
    print("\033c")
    move(1,1)
    x2=int(x/10)*10
    y2=int(y/10)*10
    # yn=max(0,y)
    yx=min(y2+10,len(mp.bit))
    for i in range(y2,yx):
        for j in range(x2,min(x2+10,len(mp.bit[i]))):
            # move(i+2,j+2)
            tp=mp.bit[i][j]
            aired=tp in[0,1,8,10] or (i>0 and mp.bit[i-1][j]in[0,1,8]) or (i<len(mp.bit)-1 and mp.bit[i+1][j]in[0,1,8]) or (j>0 and mp.bit[i][j-1]in[0,1,8]) or (j<len(mp.bit[i])-1 and mp.bit[i][j+1]in[0,1,8])
            if aired:
                print(nts[tp],end="")
            else:
                print("#",end="")
            # sleep(1)
        # print("|",end="")
        print("|")
    move(1,13)
    # print(x2,min(x2+10,len(mp.bit[i])-1),y2,yx,len(mp.bit),len(mp.bit[0]),[i for i in range(x2,min(x2+10,len(mp.bit[i])-1))])
    # print("Drawin")
    p.dr(p.x,p.y)
    # for i in mp.getTile(x,y).bit:
    #     for j in i:
    #         print(nts[j],end="")
    #     print()
    # print("\033c")
    # yn=min(max(y-10,0),len(mp.mp)-10)
    # yx=min(max(y+10,10),len(mp.mp))
    # for i in range(yn,yx):
    #     xn=min(max(x-10,0),len(mp.mp[i])-10)
    #     xx=min(max(x+10,10),len(mp.mp[i]))
    #     for j in range(xn,xx):
    #         # print(j)
    #         print(nts[mp.mp[i][j]],end="")
    #     print()
def getSave():
    global mp
    b=""
    print("\033c")
    with open("saveus/save.pile","r")as sv:
        # sv.write(str(mp.bit))
        b=sv.readlines()[0].replace("\n","")
    # print(b)
    mp.bit=eval(piler.dec(b))
    mp.datar()
def writSave():
    global mp
    with open("saveus/save.pile","w")as sv:
        sv.write(piler.enc(mp.bit))
# writSave()
getSave()
# piler.saver(mp.bit)
pr(p.x,p.y)
p.dr(p.x,p.y)
# dpt=runTimer(10)
# rkt=runTimer(0)
do=""
while True:
    prat("average fps: "+str(calcfps()),12,1)
    # if dpt.run():
    for i in bobs:
        i.run(mp.bit,[],p)
    p.mover(do)
    # move(0,12)
    # if rkt.run():
    do=keyboard.read_key()#input("u-up,r-right,d-down,l-left,b-break,i-inventory,1-5-held,p-place")
    prat(do,1,15)
    if do=="s":
        writSave()
    
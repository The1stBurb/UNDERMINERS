# no_rock=" "
# rock="◻"
# dark_rock="█"
# charium_ore="≈"
# nevelium_ore="¤"
# decante_ore="⋇"
# charcor_ore="◘"
# placed_rock=" "
from base_funcs import prat,intput,gtInt,itm
from zlooter import roll
# from itemuh import *

class brck:
    def __init__(self,nm,disp,sprd,num,pronc,mnLvl):#name,what is displayed,the spread of a section, the id/num of place in nts list, how to pronounce,what level it takes to mine
        self.nm=nm
        self.txt=disp
        self.spr=sprd
        self.idd=num
        self.pro=pronc
        self.ml=mnLvl
        self.ms=0
        # print(nm,disp,sprd,num,pronc)
        # quit()
    def __str__(self):
        return f"{self.txt}"
    def __repr__(self):
        return self.nm
class no_rock52(brck):
    pass
    # def __init__(self,nm,disp,sprd):
    #     super().__init__(nm,disp,sprd)
class placed_rock52(brck):
    pass
    # def __init__(self,nm,disp,sprd):
    #     super().__init__(nm,disp,sprd)
class rock52(brck):
    pass
    # def __init__(self,nm,disp,sprd):
    #     super().__init__(nm,disp,sprd)
class dark_rock52(brck):
    pass
    # def __init__(self,nm,disp,sprd):
    #     super().__init__(nm,disp,sprd)
class charium_ore52(brck):
    pass
    # def __init__(self,nm,disp,sprd):
    #     super().__init__(nm,disp,sprd)
class nevelium_ore52(brck):
    pass
    # def __init__(self,nm,disp,sprd):
    #     super().__init__(nm,disp,sprd)
class decante_ore52(brck):
    pass
    # def __init__(self,nm,disp,sprd):
    #     super().__init__(nm,disp,sprd)
class charcor_ore52(brck):
    pass
    # def __init__(self,nm,disp,sprd):
    #     super().__init__(nm,disp,sprd)
class dirt52(brck):
    pass
class chest52(brck):
    def __init__(self,nm,disp,sprd,num,pronc,mnLvl):
        super().__init__(nm,disp,sprd,num,pronc,mnLvl)
        self.holds=[
            [itm(dirt,10),itm(void,0),itm(void,0),],
            [itm(void,0),itm(void,0),itm(void,0),],
            [itm(void,0),itm(void,0),itm(void,0),],
            ]
        r=roll()
        roll2=[]
        for i in rolled:
            if str(i[0])[-1]=="0":
                roll2.append([nts[int(i[0]/10)],i[1]])
            else:
                roll2.append([hts[int(i[0]/10)],i[1]])
        r=roll2
        while len(r)>0:
            x,y=randint(0,2),randint(0,2)
            if self.holds[y][x].tp.nm=="void":
                ch=choice(r)
                self.holds[y][x]=itm(ch[0],ch[1])
                r.remove(ch)
    def prHold(self,p):
        while True:
            print("\033c")
            p.prInv1()
            for b in range(3):
                prat(b+1,b*16+3,9)
            for a,i in enumerate(self.holds):
                prat(a+1,1,a+10)
                for b,j in enumerate(i):
                    prat("|"+str(j),b*16+3,a+10)
            dor=intput("\nWould you like to move an item or exit? (move,exit)")
            if dor=="move":
                inor=intput("Is it into your inventory or into the chest? (inv,chest)")
                x1,y1=gtInt("What is the X coordinate of the item in "+("your inventory"if inor=="chest" else "the chest")+"?",1,(3 if inor=="inv" else 5)),gtInt("Whats the Y?",1,(3 if inor=="inv" else 6))
                x2,y2=gtInt("What is the X coordinate of where you want to move it"+(" into your inventory"if inor=="inv" else " into the chest")+"?",1,(5 if inor=="inv" else 3)),gtInt("What is the Y?",1,(6 if inor=="inv" else 3))
                # print(x1,y1,x2,y2)
                it1=self.holds[y1-1][x1-1]
                it2=p.hold[y2-1][x2-1]
                if it1.tp.nm==it2.tp.nm:
                    it1.no+=it2.no
                    it2=itm(void,0)
                self.holds[y1-1][x1-1],p.hold[y2-1][x2-1]=it2,it1
            elif dor=="exit":
                print("Exiting...")
                return
no_rock=no_rock52("air"," ",10,0,"air",0)
placed_rock=placed_rock52("placed rock","_",0,1,"placed rock",1)
rock=rock52("rock","%",-1,2,"rock",1)#◻
dark_rock=dark_rock52("dark rock","$",2,3,"dark rock",2)#█
charium_ore=charium_ore52("charium ore","=",7,4,"ch-arh-ee-um ore",3)#≈
nevelium_ore=nevelium_ore52("nevelium ore","o",5,5,"neh-vel-ee-um ore",3)#
decante_ore=decante_ore52("decante ore","⋇",3,6,"dee-cant ore",4)
charcor_ore=charcor_ore52("charcor ore","&",10,7,"ch-arh-kor ore",1)#◘

void=brck("void"," ",0,8," ",1234567890)

dirt=dirt52("dirt","@",15,9,"dirt",0)

chest=chest52("chest","C",1,10,"chest",0)
nts=[no_rock,placed_rock,rock,dark_rock,charium_ore,nevelium_ore,decante_ore,charcor_ore,void,dirt,chest]
# print(rock+dark_rock+placed_rock+charium_ore+nevelium_ore+decante_ore+charcor_ore)
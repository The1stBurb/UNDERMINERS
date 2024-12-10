#nm,idd
class held:
    def __init__(self,nm,idd2,ms,dmg,bfy=[["","","",{}]]):#name of, id of,mine strength, attack damage
        self.nm,self.idd,self.id,self.ms,self.dmg=nm,-1,idd2,ms,dmg
    def __str__(self):
        return self.nm
    def __repr__(self):
        return self.nm
class pick52(held):
    def __init__(self,nm,idd2,ms,dmg):
        super().__init__(nm,idd2,ms,dmg)
        self.bfy=[
            "rrr",
            " r ",
            " r ",
            {" ":}
        ]
    # def __init__(idd2,ms):
class charcor_pick52(held):
    pass
class nevelium_pick52(held):
    pass

class sword52(held):
    pass
class charcor_sword52(held):
    pass
class charium_sword52(held):
    pass
class nevelium_sword52(held):
    pass
pick=pick52("Pickaxe",0,1,1)
charcor_pick=charcor_pick52("Charcor Pickaxe",1,2,1)
nevelium_pick=nevelium_pick52("Nevelium Pickaxe",2,3,2)
burb=pick52("Burbaxe",-1,10,10)
sword=sword52("Sword",3,0,3)
charcor_sword=charcor_sword52("Charcor Sword",4,0,5)
charium_sword=charium_sword52("Charium Sword",5,0,7)
nevelium_sword=nevelium_sword52("Nevelium Sword",6,1,8)
# _sword=_sword52("",7,1,10)
hts=[pick,charcor_pick,nevelium_pick,sword,charcor_sword,charium_sword,nevelium_sword]
class p:
    def __init__(self):
        self.holds=
def craft(hav):

class friends:
    def __init__(self,schoolfriends,collegefriends,brightfriends):
        self.schoolfriends=schoolfriends
        self.collegefriends=collegefriends
        self.brightfriends=brightfriends
    def invite(self):
        print("hai",self.schoolfriends,"bye",self.collegefriends,"hello",self.brightfriends)
# x=friends("irfana","shbeen","rameez")
# x.invite()
#class hajeera(friends):
 
#   pass
#x=hajeera("irfana","shabeen","rameez")
#x.invite()
class hajeera(friends):
    def __init__(self,schoolfriends,collegefriends,brightfriends,neighbouringfriends,phonefriends):
        self.neighbourfriends=neighbouringfriends
        self.cellfriends=phonefriends


        super().__init__(schoolfriends, collegefriends, brightfriends)
    def thanks(self):
            print("hi buddies",self.schoolfriends,"hello family",self.collegefriends,"how r u all",self.brightfriends,"are u ready to language learning",self.neighbourfriends,"come we r ready to talk",self.cellfriends,"we are ready to chat")
x=hajeera("pavi","yasmin","raja","vinothini","jothika")
x.thanks()
x.invite()

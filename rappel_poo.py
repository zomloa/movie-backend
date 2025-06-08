#### Classe ###
# %%
class Chien:
    pass
# %%

#### Objet (Instance) ####
# %%
mon_chien = Chien()
type(mon_chien)
# %%

### Attributs ###
# %%
class Chien : 
    def __init__(self, nom, race):
        self.nom = nom
        self.race = race
# %%
mon_chien = Chien("Pipo", "Labrador")
print(mon_chien.nom)
print(mon_chien.race)
# %%
class Chien : 
    def __init__(self, nom, race):
        self.nom = nom
        self.race = race
    def aboyer(self):
        print(f"{self.nom} aboie ! ")
# %%
rex = Chien("Rex", "Berger Ewondo")
print(rex.aboyer())
# %%

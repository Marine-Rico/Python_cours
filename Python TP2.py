class animal:
    def __init__(self,name,nombre,nb_pattes,regime_alimentaire,quantite_nourriture,domestique):
        self.name = name
        self.nombre = nombre
        self.nb_pattes = nb_pattes
        self.regime_alimentaire = regime_alimentaire
        self.quantite_nourriture = quantite_nourriture
        self.domestique = domestique

    def __str__(self):
        return "Cet animal est " + self.name + ", il y en a " + str(self.nombre) + " dans le zoo, il a " + str(self.nb_pattes) + " pattes, il est " + self.regime_alimentaire + ", il mange pour " +str(self.quantite_nourriture) + " g et il est " + self.domestique

class mammifere(animal):
    pass

class aquatique(animal):
    pass


if __name__ == "__main__":


    mon_zoo = {}
    mon_zoo["1_"]=mammifere("humain",2,2,"omnivore",600,"non-domestique")
    mon_zoo["2_"]=mammifere("lion",1,4,"carnivore",3000,"non-domestique")
    mon_zoo["3_"]=mammifere("lapin",7,4,"omnivore",100,"domestique")
    mon_zoo["4_"]=mammifere("mouton",5,4,"omnivore",500,"non-domestique")
    mon_zoo["5_"]=mammifere("chien",2,4,"omnivore",500,"domestique")
    mon_zoo["6_"]=aquatique("pieuvre",1,"aucune","carnivore",200,"non-domestique")
    mon_zoo["7_"]=animal("serpent",2,"aucune","omnivore",200,"domestique")
    mon_zoo["8_"]=animal("autruche",4,2,"omnivore",1000,"non-domestique")
    mon_zoo["9&é"]=animal("poule",8,2,"omnivore",200,"domestique")

    for my_key in mon_zoo:
        print(my_key+""+str(mon_zoo[my_key]))

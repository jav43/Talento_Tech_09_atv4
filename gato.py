from animal import Animal
class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.__Raca=raca

    def setRaca(self, raca):
        self.__Raca=raca
    def getRaca(self):
        return self.__Raca
    def mostrar(self):
        return (f"Nome do Gato: {self.getNome()}, Idade: {self.getIdade()} e Raça: {self.getRaca()}")
#g =Gato("Rex","7 anos", "Pit Bull")
#print(g.mostrar())

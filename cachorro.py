from animal import Animal
class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.__Porte=porte

    def setPorte(self, porte):
        self.__Porte=porte
    def getPorte(self):
        return self.__Porte
    def mostrar(self):
        return (f"Nome do Cachorro: {self.getNome()}, Idade: {self.getIdade()} e Porte: {self.getPorte()}")
#c =Cachorro("Rex","7 anos", "Pit Bull")
#print(c.mostrar())
    
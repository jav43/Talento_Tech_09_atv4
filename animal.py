from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, nome, idade):
        self.__nome=nome
        self.__Idade=idade
        
    def getNome(self):
        return self.__nome
    def getIdade(self):
        return self.__Idade
    def setNome(self,nome):
        self.__nome=nome
    def setIdade(self,Idade):
        self.__Idade=Idade
    
    @abstractmethod
    def mostrar(self):
        pass
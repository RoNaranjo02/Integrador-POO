class Materia:
    __dni = 0
    __nombreM = None
    __fecha = None
    __nota = 0
    __aprobacion = None
    
    def __init__(self, dni=0, nombreM=None, fecha=0, nota = 0, aprobacion=None):
        self.__dni = dni
        self.__nombreM = nombreM
        self.__fecha = fecha
        self.__nota= int(nota)
        self.__aprobacion = aprobacion
        
    def getDNI(self):
        return self.__dni
    def getnombreM(self):
        return self.__nombreM
    def getfecha(self):
        return self.__fecha
    def getnota(self):
        return self.__nota
    def getaprobacion(self):
        return self.__aprobacion
    
class Alumno:
    __dni = 0
    __apellido = None
    __nombre = None
    __carrera = None
    __amoCarrera = 0
    
    def __init__(self, dni=0,apellido=None,nombre=None, carrera=None, amoCarrera=0):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__amoCarrera = amoCarrera
        
    def getDni(self):
        return self.__dni
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getCarrera(self):
        return self.__carrera
    def getAmoCarrera(self):
        return self.__amoCarrera
    def __lt__(self, name):
        return self.getAmoCarrera() < name.getAmoCarrera()

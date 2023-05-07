import numpy as np
import csv
from claseAlumnos import Alumno
class manejAlum:
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    def __init__(self, dimension, incremento=5):
        self.__alum = np.empty(dimension, dtype=Alumno)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento=incremento
    def agregarAlumno(self, a):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__alum.resize(self.__dimension)
        self.__alum[self.__cantidad]=a
        self.__cantidad += 1
    def readFileAlum(self):
        archivo = open("alumnos.csv")
        reader = csv.reader(archivo,delimiter=";")
        for fila in reader:
            a = Alumno(fila[0], fila [1], fila[2], fila[3], fila[4])
            self.agregarAlumno(a)
    def listar (self):
        lista = self.__alum.tolist()
        lista.sort()
        for alum in lista:
            print("{} {} Año que cursa: {}".format(alum.getapellido()))
    def getAlum(self, dni):
        i=0
        flag = False
        alum = None
        while i<=len(self.__alum) and flag == False:
            if self.__alum[i].getDni()==str(dni):
                flag = True
                alum = self.__alum[i]
                i+=1
        return(alum)
    
        
        
        
            
            
        

import numpy as np
import csv
from claseMateria import Materia
from manejadorAlumnos import manejAlum
import math

class manejMaterias:    
    __mat = []
    def __init__(self):
        self.__mat = []
    def readFileMat(self):
        archivo = open("materiasAprobadas.csv")
        reader = csv.reader(archivo,delimiter=";")
        for fila in reader:
            b = Materia(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__mat.append(b)
        archivo.close()

    def promedio (self):
     promApl = 0
     promSApl = 0
     cont = 0
     contS=0
     dni = input("Ingrese DNI del alumno: ")
     for i in range(len(self.__mat)):
            if (dni == self.__mat[i].getDNI()):
                if (self.__mat[i].getnota() >= 7):
                    promSApl += self.__mat[i].getnota()
                    contS += 1
                promApl += self.__mat[i].getnota()
                cont +=1
     notaAp = (promApl/cont)
     notasap = (promSApl/contS)
     print("Promedio con aplazos: ", notaAp)
     print("Promedio sin aplazos: ", notasap)

     
    def promociones(self):
         a=manejAlum(10)
         a.readFileAlum()
         nombre = input("Ingrese nombre de materia: ")
         for i in range (len(self.__mat)):
             if (self.__mat[i].getnombreM() == nombre):
              if (self.__mat[i].getaprobacion() == 'P'):
                     print(f"{self.__mat[i].getDNI() : <20}")
                     print(f"{a.getAlum(self.__mat[i].getDNI()).getAlum() : <30}")
                     print(f"{self.__mat[i].getfecha() : <15}")
                     print(f"{self.__mat[i].getnota() : < 4}")
                     print(f"{a.getAlum(self.__mat[i].getdni()).getcursado}")
                     

    
        
                
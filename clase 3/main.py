edades = [35, 12, 15, 40, 20]  

def promedio_edades(edades):
    suma = 0
    for n in edades:
        suma = suma + n
    return suma / len(edades)

promedio = promedio_edades(edades)
print(f"El promedio de las edades es {promedio}")
      
      





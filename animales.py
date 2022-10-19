import pandas
import os.path
#Si existe el documento, Leer
if os.path.isfile('data.csv'):
    df = pandas.read_csv('data.csv',header=0)
#Si no existe, crear uno nuevo
else:
    data = {'Nombre':['Alice'],
            'Especie':['Panda'],
            'Tipo de alimento':['Bamboo'],
            'Tiempo en aire libre':[45],
            'Tiempo entre comidas':[20]}
    df = pandas.DataFrame(data)
    #Guardar Documento
    df.to_csv('data.csv',index=False)
print(df.to_string()) 
def save():
    df.to_csv('data.csv',index=False)
    
def add(nombre, especie, alimento, tiempo,comida):
    df.loc[len(df.index)] = [nombre,especie,alimento,tiempo,comida]
    save()
def read(nombre):
    name = df.loc[df['Nombre'] == nombre]
    print(name)
def delete(nombre):
    index = df[df["Nombre"].str.contains(nombre)].index
    df.drop(index, inplace=True)
    save()
def show():
    df = pandas.read_csv('data.csv',header=0)
    print(df.to_string())
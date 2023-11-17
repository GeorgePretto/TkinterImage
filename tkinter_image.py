from tkinter import *
from PIL import ImageTk,Image
import os 




root =Tk()
#Lista para os arquivos da pasta de imagens
arquivos = os.listdir("imagens")


#Variavel para armazenar as imagens
imagens = []


#Percorre a lista de arquivos
for arquivo in arquivos:
    #Abre a imagem
    img = Image.open("imagens/"+arquivo)
    #Adiciona imagem a lista
    imagens.append(ImageTk.PhotoImage(img))


#Exibe arquivos em um Label
img_label = Label(root, image=imagens[1])

img_label.pack()

root.mainloop()
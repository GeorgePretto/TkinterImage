from tkinter import *
from PIL import ImageTk,Image,ImageOps
import os 



root =Tk()
#Lista para os arquivos da pasta de imagens
arquivos = os.listdir("imagens")


root.iconbitmap("galeria.ico")



root.title("Galeria")
#Variavel para armazenar as imagens
imagens = []

#varialvel de controle do indice da imagem atual
imagem_atual = 0




#Percorre a lista de arquivos
for arquivo in arquivos:
    try:

        img = Image.open("imagens/"+arquivo)
    except Exception as e:
        pass
        img=ImageOps.contain(img,(500,500))
    #Adiciona imagem a lista
    imagens.append(ImageTk.PhotoImage(img))


#Exibe arquivos em um Label
img_label = Label(root, image=imagens[imagem_atual])

img_label.grid(column=0,row=0,columnspan=3)






def prev_image():
    global imagem_atual
    global img_label
    global imagens

#verefica se é a primeira imagem, se sim, volta para aultima.
   
    if imagem_atual == 0:
        imagem_atual = len (imagens) -1
    else:imagem_atual -= 1

    img_label.grid_forget()

    img_label = Label(root, image=imagens[imagem_atual])
    img_label.grid(column=0,row=0,columnspan=3)





def pro_image():
    global imagem_atual
    global img_label
    global imagens

#verefica se é a primeira imagem, se sim, volta para aultima.
   
    if imagem_atual == len(imagens) -1:
        imagem_atual =0
    else:
        imagem_atual += 1

    
    img_label.grid_forget()

    img_label = Label(root, image=imagens[imagem_atual])
    img_label.grid(column=0,row=0,columnspan=3)




try:
    btn= Button(root, text="Prev",command=prev_image,bg="blue",fg="white",font="Arial")
    btn.grid(column=0,row=1,sticky=E+W)
except:
    print("Algo de errado não está certo")

btn= Button(root, text="Sair",command=root.quit,bg='red',fg="white",font="Verdana")
btn.grid(column=1,row=1,sticky=E+W)

btn= Button(root, text="Próximo",command=pro_image,bg="blue",fg="white",font="Arial")
btn.grid(column=2,row=1,sticky=E+W)

root.mainloop()
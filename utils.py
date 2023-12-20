
from tkinter import *
from PIL import ImageTk,Image,ImageOps
from tkinter import messagebox
from tkinter import filedialog
import os 

#Variavel para armazenar as imagens
imagens = []

#varialvel de controle do indice da imagem atual
imagem_atual = 0


#Varialvel para armazenar o label da imagem
img_label = None


#variavel para armazenar o caminho da pasta da imagem
img_folder = ""



#função para carregar as imagens
def load_images(root):
    global img_folder
    global imagens
    global img_label

    if img_folder:
        imagens.clear()
    #Lista para os arquivos da pasta de imagens
        arquivos = os.listdir(img_folder)
    #Percorre a lista de arquivos
        for arquivo in arquivos:
            try:

                img = Image.open(os.path.join(img_folder,arquivo))
            except Exception as e:
                print(e)
                continue
            else:
                img=ImageOps.contain(img,(500,500))
        #Adiciona imagem a lista
                imagens.append(ImageTk.PhotoImage(img))
    else:
        #cria uma imagem 
        img = Image.new("RGB",(500,500),color="red")
        #adiciona a imagem na lista
        imagens.append(ImageTk.PhotoImage(img))
    #Exibe arquivos em um Label
    img_label = Label(root, image=imagens[imagem_atual])

    img_label.grid(column=0,row=0,columnspan=3)

#definir função
def open_folder(root):
    folder_path = filedialog.askdirectory()

    if folder_path:
        load_images(root)
        global img_folder
        img_folder=folder_path
        messagebox.showinfo(
            title="abrindo",
            message=f'O arquivo selecionado foi: {folder_path}')
    else:
        messagebox.showerror(
            title="erro",
            message="Nenhum diretório foi selecionado"
        )


def prev_image(root):
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
    
def pro_image(root):
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



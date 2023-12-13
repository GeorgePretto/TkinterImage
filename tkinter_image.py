from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image,ImageOps
import os 
from tkinter import filedialog

#Variavel para armazenar as imagens
imagens = []

#varialvel de controle do indice da imagem atual
imagem_atual = 0


#Varialvel para armazenar o label da imagem
img_label = None


#variavel para armazenar o caminho da pasta da imagem
img_folder = ""


#função para carregar as imagens
def load_images():
    global img_folder
    global imagens

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
        img = Image.new("RGB",(500,500))
        #adiciona a imagem na lista
        imagens.append(ImageTk.PhotoImage(img))
    #Exibe arquivos em um Label
    img_label = Label(root, image=imagens[imagem_atual])

    img_label.grid(column=0,row=0,columnspan=3)





#definir função
def open_folder():
    folder_path = filedialog.askdirectory()

    if folder_path:
        load_images()
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

root =Tk()


#Criar menu
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Open",
                     command=open_folder)
filemenu.add_command(label="Save")
filemenu.add_command(label="Exit")

menubar.add_cascade(label="File",menu=filemenu)

root.config(menu=menubar)

load_images()


root.iconbitmap("galeria.ico")



root.title("Galeria")





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




#dar funções para o botão do teclado passar para a proxima imagem



root.bind('<Right>',lambda event: pro_image())
root.bind('<Left>',lambda event: prev_image())
root.bind('<Escape>',lambda event: root.quit())





root.mainloop()
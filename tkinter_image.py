from tkinter import *
from utils import *





root =Tk()


#Criar menu
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Open",
                     command=lambda:open_folder(root))
filemenu.add_command(label="Save")
filemenu.add_command(label="Exit")

menubar.add_cascade(label="File",menu=filemenu)

root.config(menu=menubar)

load_images(root)


root.iconbitmap("galeria.ico")



root.title("Galeria")










try:
    btn= Button(root, text="Prev",command=lambda: prev_image(root),bg="blue",fg="white",font="Arial")
    btn.grid(column=0,row=1,sticky=E+W)
except:
    print("Algo de errado não está certo")

btn= Button(root, text="Sair",command=root.quit,bg='red',fg="white",font="Verdana")
btn.grid(column=1,row=1,sticky=E+W)

btn= Button(root, text="Próximo",command=lambda: pro_image(root),bg="blue",fg="white",font="Arial")
btn.grid(column=2,row=1,sticky=E+W)




#dar funções para o botão do teclado passar para a proxima imagem



root.bind('<Right>',lambda event: pro_image(root))
root.bind('<Left>',lambda event: prev_image(root))
root.bind('<Escape>',lambda event: root.quit(root))





root.mainloop()
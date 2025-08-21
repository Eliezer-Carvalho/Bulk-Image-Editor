import tkinter as tk                                                    #INTERFACE
from tkinter import filedialog, messagebox                              #INTERFACE
import cv2                                                              #CONTRAST AND LUMINOSITY 
from pathlib import Path                                                #PATH FROM PC MEMORY
from PIL import Image, ImageTk                                          #HANDLE IMAGES




def carregar_imagem():
    
    global imagem_original

    extensões = [".jpg", ".png", ".tiff", ".jpeg"]

    caminho = filedialog.askopenfilename(filetypes = [("Imagens", extensões)])
    
    if caminho:
        imagem_original = cv2.imread(caminho)
        largura_nova = 400
        altura_nova = 580
        imagem_original  = cv2.resize(imagem_original, (largura_nova, altura_nova), interpolation = cv2.INTER_AREA)
        ajustar_imagem()




def ajustar_imagem():

    global imagem_original, tk_imagem
    
    alpha = contraste.get()      
    beta = luminosidade.get()          
    
    imagem_editada = cv2.convertScaleAbs(imagem_original, alpha = alpha, beta = beta)
    
    imagem_PILLOW = Image.fromarray(cv2.cvtColor(imagem_editada, cv2.COLOR_BGR2RGB))

    tk_imagem = ImageTk.PhotoImage(imagem_PILLOW)
    label_imagem.config(image = tk_imagem)
    label_imagem.image = tk_imagem



def guardar_def ():

    global definições

    definições = {

        "alpha": contraste.get(),      
        "beta": luminosidade.get() 

    }



def aplicar_pasta ():


    extensões = [".jpg", ".png", ".tiff", ".jpeg"]

    caminho = filedialog.askdirectory()
    pasta = Path(caminho)


    saída = pasta / f"{pasta.name}_Editadas"
    saída.mkdir (exist_ok = True) 


    for ficheiro in pasta.iterdir():
        if ficheiro.suffix.lower() in extensões:

            img = cv2.imread(str(ficheiro))

            img_editada = cv2.convertScaleAbs (img, alpha = definições ["alpha"], beta = definições ["beta"])

   
            caminho_saída = saída / ficheiro.name 
            cv2.imwrite(str(caminho_saída), img_editada)


    messagebox.showinfo ("Sucesso")




janela = tk.Tk()
janela.title("Editor de Imagens em Massa - Eliezer Carvalho")
janela.geometry("1200x1200")
janela.config(bg = "#F7E773")

botão_carregar_imagem = tk.Button(janela, text = "CARREGAR UMA IMAGEM DE EXEMPLO", command = carregar_imagem, bg = "#F7E773", fg = "#F35D66", font = ("Arial", 9, "bold")).pack(pady = (10, 0))



luminosidade = tk.Scale(janela, from_ = -50, to = 100, length = 500, width = 20, orient = "horizontal", bg = "#F7E773", fg = "#F35D66", label = "LUMINOSIDADE", troughcolor = "#F35D66", highlightbackground = "#F7E773", command = lambda x: ajustar_imagem())
luminosidade.set(0)
luminosidade.pack()

contraste = tk.Scale(janela, from_ = 0.5, to = 2.0, resolution = 0.1, length = 500, width = 20, orient = "horizontal", bg = "#F7E773", fg = "#F35D66", label = "CONTRASTE", troughcolor = "#F35D66", highlightbackground = "#F7E773", command = lambda x: ajustar_imagem())
contraste.set(1.0)
contraste.pack()

label_imagem = tk.Label(janela)
label_imagem.pack(pady = (10, 0))


botão_guardar_definições = tk.Button (janela, text = "GUARDAR DEFINIÇÕES", bg = "#F7E773", fg = "#F35D66", font = ("Arial", 9, "bold"), command = guardar_def).pack(pady = (10, 0))


aplicar_a_uma_pasta = tk.Button (janela, text = "APLICAR DEFINIÇÕES A UMA PASTA", bg = "#F7E773", fg = "#F35D66", font = ("Arial", 9, "bold"), command = aplicar_pasta).pack(pady = (5, 0))



imagem_original = None
tk_imagem = None

janela.mainloop()
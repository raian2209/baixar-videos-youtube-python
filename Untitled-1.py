from tkinter import *
from tkinter import ttk

# importando pillow

from PIL import image, ImageTk


# cores  usadas ---------------------
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
fundo = "#3b3b3b"

# Definindo a janela
janela = Tk()
janela.title()
janela.geometry('500x300')
janela.configure(bg=fundo)

# Criando uma linha orizontal
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=250)

# Dividindo a janela em 2

frame_cima = Frame(janela, width=500, height=110, bg=fundo, pady=5, padx=0)
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=500, height=300, bg=fundo, pady=12, padx=0)
frame_baixo.grid(row=2, column=0, sticky=NW)

# configurando o frame cima

#logo = Image.open('images/youtube.png')
#logo = logo.resize((50,50), Image.ANTIALIAS)
#logo = ImageTk.PhotoImage(logo)

#l_logo = Label(frame_cima, image=logo, compund=LEFT, bg='white', font=('Ivy 10 bold'), anchar='nw')
#l_logo.place(x=65, y=15)

l_name = Label(frame_cima, text="Youtube Dowload app", width=32,
               bg=fundo, fg=co1, font=('Ivy 10 bold'), anchar='nw')
l_name.place(x=65, y=15)


janela.mainloop()

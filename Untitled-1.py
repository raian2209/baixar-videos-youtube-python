from tkinter import ttk
from tkinter import *
from urllib import request

# importando pillow

#from PIL import image, ImageTk

from pytube import YouTube

import datetime
import calendar

import requests

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

#l_logo = Label(frame_cima, image=logo, compund=LEFT, bg=fundo, font=('Ivy 10 bold'), anchar='nw')
#l_logo.place(x=5, y=5)

l_name = Label(frame_cima, text="Youtube Dowload app", width=32,
               bg=fundo, fg=co1, font=('Ivy 10 bold'), anchor='nw')
l_name.place(x=65, y=15)


def pesquisar():
    # pegando o link
    url = e_url.get()
    yt = YouTube(url)

    # titlo
    titlo = yt.title

    # visualizações
    view = yt.views

    # duração do video
    duracao = str(datetime.timedelta(seconds=yt.length))

    # descrição do video
    informacao = yt.description

    # foto
    foto = yt.thumbnail_url

    img = Image.open(requests.get(foto, stream=True).raw)

    l_titlo['text'] = "Titulo :" + titlo
    l_views['text'] = "Views :" + str('{:,}'.format(view))
    l_time['text'] = "Duração :" + duracao


l_url = Label(frame_cima, text="Entre o link", bg=fundo,
              fg=co1, font=('Ivy 10 bold'), anchor='nw')
l_url.place(x=10, y=80)
e_url = Entry(frame_cima, width=50, justify='left', relief=SOLID)
e_url.place(x=100, y=80)

b_pesquisar = Button(frame_cima, command=pesquisar, text="Pesquisar", width=10,
                     bg=co2, fg=co1, font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE,)
b_pesquisar.place(x=404, y=80)

# operações

# l_imagem = Label(frame_baixo, image=logo, compund=LEFT,
#               bg=fundo, font=('Ivy 10 bold'), anchar='nw')
#l_imagem.place(x=5, y=5)

l_titlo = Label(frame_baixo, text="titlo do video", height=2, wraplength=225, compound=LEFT,
                bg=fundo, fg=co1, font=('Ivy 10 bold'), anchor='nw')
l_titlo.place(x=250, y=15)

l_views = Label(frame_baixo, text="10,100,10",
                bg=fundo, fg=co1, font=('Ivy 8 bold'), anchor='nw')
l_views.place(x=250, y=60)

l_time = Label(frame_baixo, text="00:02:50",
               bg=fundo, fg=co1, font=('Ivy 8 bold'), anchor='nw')
l_time.place(x=250, y=85)


#down = Image.open('images/download_2.png')
#down = down.resize((50, 50), Image.ANTIALIAS)
#down = ImageTk.PhotoImage(down)

b_down = Button(frame_baixo, text="Dowload", compound=LEFT,
                bg=fundo, font=('Ivy 10 bold'), overrelief=RIDGE)
b_down.place(x=400, y=85)


janela.mainloop()

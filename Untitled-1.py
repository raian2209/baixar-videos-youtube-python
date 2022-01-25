import tkinter
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Progressbar
from urllib import request

# importando pillow

from PIL import Image, ImageTk

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

logo = Image.open('images/youtube.png')
logo = logo.resize((50, 50), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)

l_logo = Label(frame_cima, image=logo, compound=LEFT,
               bg=fundo, font=('Ivy 10 bold'), anchor='nw')
l_logo.place(x=5, y=5)

l_name = Label(frame_cima, text="Youtube Dowload app", width=32,
               bg=fundo, fg=co1, font=('Ivy 10 bold'), anchor='nw')
l_name.place(x=65, y=15)

# função de pesquisa no youtube


def pesquisar():
    global img
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
    img = img.resize((230, 150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    l_imagem['image'] = img

    l_titlo['text'] = "Titulo :" + titlo
    l_views['text'] = "Views :" + str('{:,}'.format(view))
    l_time['text'] = "Duração :" + duracao


# -------mostrar progresso do download
previusprogress = 0


def on_progress(stream, chunk, bytes_remaining):
    global previusprogress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining

    liveprogress = (int)(bytes_downloaded / total_size * 100)
    if liveprogress > previusprogress:
        previusprogress = liveprogress
        print(liveprogress)

        bar.place(x=250, y=120)
        bar['value'] = liveprogress
        janela.update_idletasks()

#   Para fazer o download do video no youtube


def download():
    url = e_url.get()
    yt = YouTube(url)

    # chama é atualisa a barra de progresso
    yt.register_on_progress_callback(on_progress)

    yt.streams.filter(file_extension='mp4')
    yt.streams.get_by_itag(22).download()
    # faz o download do video
    # yt.streams.filter(only_audio=False).first().download()


l_url = Label(frame_cima, text="Entre o link", bg=fundo,
              fg=co1, font=('Ivy 10 bold'), anchor='nw')
l_url.place(x=10, y=80)
e_url = Entry(frame_cima, width=50, justify='left', relief=SOLID)
e_url.place(x=100, y=80)

b_pesquisar = Button(frame_cima, command=pesquisar, text="Pesquisar", width=10,
                     bg=co2, fg=co1, font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE,)
b_pesquisar.place(x=404, y=80)

# operações

l_imagem = Label(frame_baixo, image=logo, compound=LEFT,
                 bg=fundo, font=('Ivy 10 bold'), anchor='nw')
l_imagem.place(x=5, y=5)

l_titlo = Label(frame_baixo, text="", height=2, wraplength=225, compound=LEFT,
                bg=fundo, fg=co1, font=('Ivy 10 bold'), anchor='nw')
l_titlo.place(x=250, y=15)

l_views = Label(frame_baixo, text="",
                bg=fundo, fg=co1, font=('Ivy 8 bold'), anchor='nw')
l_views.place(x=250, y=60)

l_time = Label(frame_baixo, text="",
               bg=fundo, fg=co1, font=('Ivy 8 bold'), anchor='nw')
l_time.place(x=250, y=85)


#down = Image.open('images/download_2.png')
#down = down.resize((50, 50), Image.ANTIALIAS)
#down = ImageTk.PhotoImage(down)

b_down = Button(frame_baixo, command=download, text="Dowload", compound=LEFT,
                bg=fundo, font=('Ivy 10 bold'), overrelief=RIDGE)
b_down.place(x=400, y=85)

style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='#00E676')
style.configure("TProgressbar", thickness=6)

bar = Progressbar(frame_baixo, length=190,
                  style='black.Horizontal.TProgressbar')

janela.mainloop()

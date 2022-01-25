from pytube import YouTube

import datetime
import calendar
import re


def pesquisar():

    YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
    yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')

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

    print(titlo, "\n", view, "\n", duracao, "\n", foto)


def achar_melhor_resolução():
    yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
    print(yt.streams.filter(file_extension='mp4',
          type="video", mime_type="video/mp4", res="1080p"))


re.compile('(1)?')
achar_melhor_resolução()

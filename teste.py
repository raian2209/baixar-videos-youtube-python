from pytube import YouTube

import datetime
import calendar


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

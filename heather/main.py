# adele.heather.main.py
# Hellen Wagmacker
from _spy.vitollino.main import Texto, Elemento, Cena
NOVA_YORK = "https://s3-media4.fl.yelpcdn.com/bphoto/Y7P32v34MaACfkvwUmO2xg/o.jpg"
Heather = "https://vignette.wikia.nocookie.net/hijotee827/images/8/84/Nice_Heather.png/revision/latest?cb=20140609233018"
Barney = "https://c7.uihere.com/files/30/808/836/neil-patrick-harris-choose-your-own-autobiography-how-i-met-your-mother-barney-stinson-desi-collings-how-i-met-your-mother.jpg"
def Historia():
    cenanovayork = Cena(NOVA_YORK)
    elementoGuardaChuva = Elemento(img= Heather,
                                  tit="Heather",
                                  style=dict(left=150, width=60, height=100))

    cenanovayork = Cena(NOVA_YORK)
    elementoBarney = Elemento(img= Barney,
                                  tit="Barney",
                                  style=dict(left=150, width=60, height=100))

    cenanovayork.vai()
    elementoBarney.entra(cenanovayork)
    elementoGuardaChuva.entra(cenanovayork)
Historia()
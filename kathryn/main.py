# adele.kathryn.main.py
# yasmin lemos
from _spy.vitollino.main import Texto, Elemento, Cena
LONDRES = "https://mapadelondres.org/wp-content/uploads/2011/11/londres-tower-bridge-neve-istock.jpg"
HANNA = "https://png2.kisspng.com/20180525/jfu/kisspng-ashley-benson-hanna-marin-pretty-little-liars-aria-5b0844e7477e04.1931477415272685832929.png"

def Historia():
    cenaLondres = Cena(LONDRES)
    elementoHanna = Elemento(img=HANNA,
                             tit="Girl",
                             style=dict(left=150, top=60, width=60, heigth=200))
    elementoHanna.entra(cenaLondres)                     
    cenaLondres.vai()
Historia()
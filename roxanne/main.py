# adele.roxanne.main.py
# Cibele Ribeiro
from _spy.vitollino.main import Texto, Elemento, Cena
ARGENTINA = "https://i0.wp.com/aquimequedo.com.br/wp-content/uploads/2018/06/Bar-Sur-P1020365.jpg?resize=1024%2C683"
TANGO = "https://i1.wp.com/www.donaheys.co.uk/wp-content/uploads/Strictly-Come-Dancing-Robin-Windsor-Kristina-Rihanoff-290px.gif?fit=187%2C300"

def Historia():
    cenaArgentina = Cena(ARGENTINA)
    elementoTango = Elemento(img=TANGO,
                            tit="Casal",
                            style=dict(left=80, top=60, width=80, height=200))
    elementoTango.entra(cenaArgentina) 
    cenaArgentina.vai()
Historia()
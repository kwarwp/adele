# adele.roxanne.main.py
# Cibele Ribeiro
from _spy.vitollino.main import Texto, Elemento, Cena
ARGENTINA = "https://i0.wp.com/aquimequedo.com.br/wp-content/uploads/2018/06/Bar-Sur-P1020365.jpg?resize=1024%2C683"
TANGO = "https://i1.wp.com/www.donaheys.co.uk/wp-content/uploads/Strictly-Come-Dancing-Robin-Windsor-Kristina-Rihanoff-290px.gif?fit=187%2C300"
SAMBA = "https://st2.depositphotos.com/8348572/11686/v/950/depositphotos_116863036-stock-illustration-brazilian-couple-performing-samba-dance.jpg"
def Historia():
    cenaArgentina = Cena(ARGENTINA)
    elementoTango = Elemento(img=TANGO,
                            tit="Casal",
                            style=dict(left=180, top=30, width='120px', height='260px'))
    elementoTango.entra(cenaArgentina) 
    txttango = Texto(cenaArgentina,"Quem dança seus males espanta!"
    elementoTango.vai = txttango.vai    
    cenaSamba = Cena(SAMBA, direita=cenaArgentina)
    cenaArgentina.esquerda = cenaSamba
    cenaArgentina.vai()
Historia()
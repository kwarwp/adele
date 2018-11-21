# adele.naomi.main.py
#Mariana Reigada
from _spy.vitollino.main import Texto, Elemento, Cena 
PRAIA = "https://http2.mlstatic.com/mega-banner-painel-decoraco-festa-240x150-praia-D_NQ_NP_826579-MLB25851925736_082017-F.jpg"
ESTRELA = "https://www.aixalonjadeartesania.pt/_articulos/estrella-de-mar-espina-15-18-cm--0002289.png"

def Historia():
    cenaPraia = Cena(PRAIA)
    elementoEstrela = Elemento(img=ESTRELA,
                              tit="Estrela do mar",
                              style=dict(left=150, top=60, width=60, height=200))
    elementoEstrela.entra(cenaPraia)                              
    cenaPraia.vai()
Historia()    

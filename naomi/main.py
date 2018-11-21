# adele.naomi.main.py
#Mariana Reigada
from _spy.vitollino.main import Texto, Elemento, Cena 
PRAIA = "https://http2.mlstatic.com/mega-banner-painel-decoraco-festa-240x150-praia-D_NQ_NP_826579-MLB25851925736_082017-F.jpg"
ESTRELA = "https://www.aixalonjadeartesania.pt/_articulos/estrella-de-mar-espina-15-18-cm--0002289.png"
CONCHA = "http://2.bp.blogspot.com/-apjmp3RvCgY/Vdjmxg-f-EI/AAAAAAAAlPM/ygNA64bGuyU/s1600/concha-em-png-vetorizado-queroimagem-cei%25C3%25A7a-crispim.png"

def Historia():
    cenaPraia = Cena(PRAIA)
    elementoEstrela = Elemento(img=ESTRELA,
                              tit="Estrela do mar",
                              style=dict(left=15, width=60, height=50))
    elementoConcha = Elemento(img=CONCHA,
                              tit="Concha",
                              style=dict(left=22, top=30, widht=60))
    elementoEstrela.entra(cenaPraia)
    elementoConcha.entra(cenaPraia)
    cenaPraia.vai()
Historia()    

# adele.julia.main.py
# Julia Pereira Soares 
from _spy.vitollino.main import Texto, Elemento, Cena 
CASTELO = "https://http2.mlstatic.com/fundo-fotografico-painel-lona-castelo-dentro-6x3-displays-D_NQ_NP_153815-MLB25311821030_012017-F.jpg"
VALSA = "http://4.bp.blogspot.com/-leQ5oaWmMqw/Ua-S6mJJ4BI/AAAAAAAADTg/HhAtv_nrD1A/s640/bela_fera.gif"

def Historia():
    cenaCastelo = Cena(CASTELO)
    elementoValsa = Elemento(img=VALSA,
                            tit="amor",
                            style=dict(left=150, top=60, width=60, height=200))
                            
    elementoValsa.entra(cenaCastelo)                        
    cenaCastelo.vai()
Historia()


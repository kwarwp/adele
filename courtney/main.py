# adele.courtney.main.py
# Arthur Balberino Vidal de Negreiros
from _spy.vitollino.main import Texto, Elemento, Cena 
MARACANA="https://i.ytimg.com/vi/nY-BUXppCSU/maxresdefault.jpg" 
FLAMENGO= "https://fla-bucket-s3-us.s3.amazonaws.com/public/images/players/2/1524238563.png" 
BAR= "https://augustonobuteco.files.wordpress.com/2011/11/dsc05501reduzida1.jpg"
def Historia():
    cenaMaracana = Cena(MARACANA)
    elementoFlamengo = Elemento(img=FLAMENGO, 
                       tit="Torcida do Flamengo",
                       style=dict(left=150, width=60, heigth=70))
    elementoFlamengo.entra(cenaMaracana)
    txtflamengo = Texto(cenaMaracana, "Vamos Flamengo")
    elementoFlamengo.vai =txtflamengo.vai
    cenaBAR = Cena(BAR, direita=cenaMaracana)
    cenaMaracana.esquerda = cenaBAR
    
    cenaMaracana.vai()
Historia()

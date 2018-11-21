# adele.heather.main.py
# Hellen Wagmacker
from _spy.vitollino.main import Texto, Elemento, Cena
GUARDA_CHUVA = "https://banner2.kisspng.com/20180301/lkq/kisspng-yellow-umbrella-angle-umbrella-5a980c04733553.3837393615199139884719.jpg"
NOVA_YORK = "https://s3-media4.fl.yelpcdn.com/bphoto/Y7P32v34MaACfkvwUmO2xg/o.jpg"
Heather = "https://vignette.wikia.nocookie.net/hijotee827/images/8/84/Nice_Heather.png/revision/latest?cb=20140609233018"
Barney = "https://icon2.kisspng.com/20180530/ipc/kisspng-neil-patrick-harris-barney-stinson-how-i-met-your-barney-stinson-5b0e55230325a2.0860035615276659550129.jpg"
Cabra = "https://banner2.kisspng.com/20171220/qte/goat-png-5a3af391b0bd49.43952778151381288172398118.jpg"
Abacaxi = "https://banner2.kisspng.com/20171127/382/pineapple-png-vector-clipart-image-5a1c46718ae5b2.5079999715118024815689.jpg"
Cabra1 = "https://banner2.kisspng.com/20180909/vop/kisspng-goat-milk-goat-milk-cattle-sheep-png-5b95d3ba0db405.8161898815365457220561.jpg"
def Historia():
    cenanovayork = Cena(NOVA_YORK)
    elementoGuardaChuva = Elemento(img= Cabra,
                                  tit="Cabra",
                                  style=dict(left=150, width=60, height=100))
    cenanovayork.vai()
    elementoGuardaChuva.entra(cenanovayork)
Historia()
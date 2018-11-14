#adele.stacy.main.py
#Vitória Oliveira
from _spy.vitollino.main import Texto, Elemento, Cena 

PRAIA = "data:image/jpeg;base64,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"
VOLEI="https://banner2.kisspng.com/20180224/kiw/kisspng-download-cartoon-beach-volleyball-5a9121fa45b002.2392557315194608582855.jpg"

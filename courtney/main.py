# adele.courtney.main.py
# Arthur Balberino Vidal de Negreiros
from _spy.vitollino.main import Texto, Elemento, Cena 
MARACANÃ="https://i.ytimg.com/vi/nY-BUXppCSU/maxresdefault.jpg"
FLAMENGO= "data:image/jpeg;base64,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" 
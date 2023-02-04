from liquidificador import Liquidificador
from batedeira import Batedeira
from secador import Secador

liq = Liquidificador('Vermelho', 250, 220, 100)
bat = Batedeira('Azul', 300, 127, 150)
sec = Secador('Preta', 400, 127, 290)

print(f'O liquidificador {liq.cor} custa {liq.preco}')
print(f'A batedeira {bat.cor} custa {bat.preco}')
print(f'O secador {sec.cor} custa {sec.preco}')

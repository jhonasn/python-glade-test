# -*- coding: utf-8 -*-
from interface.main import Interface


class App:
    def __init__(self):
        self.interface = Interface()
        self.interface.builder.connect_signals({
            'onVai': self.vai,
            'onFazAlgo': self.faz_algo,
            'onJanelinhaClose': self.janelinha_close,
        })
        
        self.interface.start()
    
    def vai(self, button):
        texto = self.interface.texto.get_text()
        if texto == '':
            self.interface.dialogo.set_text('Você não digitou nada!')
        else:
            self.interface.dialogo.set_text('Você digitou:')
        self.interface.labelzinho.set_text(texto)
        self.interface.janelinha.show()

    def faz_algo(self, button):
        self.interface.janelinha.hide()

    def janelinha_close(self, dialog):
        self.faz_algo()

try:
    app = App()
except error:
    print('Error')
    print(error)


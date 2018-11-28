
{'date': 'Wed Nov 21 2018 11:42:56.370 GMt-0200 (Horário de Verão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 13
  cenaSamba = (SAMBA, dir=cenaArgentina)
                                        ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Nov 21 2018 11:43:26.114 GMt-0200 (Horário de Verão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 16
    Historia()
  module <module> line 13
    cenaSamba = Cena(SAMBA, dir=cenaArgentina)
  module _spy.vitollino.main line 778
    Cena.c(**kwargs)
  module _spy.vitollino.main line 821
    imagem, kwargs = (imagem, {}) if isinstance(imagem, str) \
AttributeError: 'Cena' object has no attribute '__getitem__'
'''},
{'date': 'Wed Nov 28 2018 10:25:08.734 GMt-0200 (Horário de Verão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 13
  txttango = Texto(cenaArgentina,"Quem dança seus males espanta!"
                                                                       ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Nov 28 2018 10:56:53.953 GMt-0200 (Horário de Verão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 19
    Historia()
  module <module> line 13
    INVENTARIO.bota(elementoTango)
NameError: name 'INVENTARIO' is not defined
'''},
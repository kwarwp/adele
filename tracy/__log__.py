
{'date': 'Mon Dec 10 2018 11:49:18.499 GMt-0200 (Horário de Verão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 9
  Historia()    
  ^
IndentationError: expected an indented block
'''},
{'date': 'Mon Dec 10 2018 11:53:45.627 GMt-0200 (Horário de Verão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 10
    Historia()    
  module <module> line 6
    BABY = Cena(BABY)
UnboundLocalError: local variable 'BABY' referenced before assignment
'''},
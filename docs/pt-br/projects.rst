======================
Criando novos projetos
======================

.. ATTENTION::
   Antes de começar, certifique-se de que o pyglet e o Batma estejam instalados corretamente no seu computador, conforme descrito na seção :doc:`installing`.

O Batma é instalado acompanhado de um ajudante para criação de novos projetos, ele o ajudará criando a estrutura básica para criação de seu jogo ou aplicação. Esse ajudante é chamado **Robi** (*lol*) e deve ser usado via linha de comando::

    $ robi <nome do projeto>

Substitua o ``<nome do projeto>`` e crie um projeto chamado "mygame", o Robi vai criar a seguinte estrutura de arquivos::

    mygame/
        mygame.py
        resources/

O diretório ``resources`` será utilizado para colocar todas as imagens, sons, fontes e outros recursos do seu jogo. Note também que o robi criou um arquivo python (``.py``) com o mesmo nome do projeto, abra-o e você verá o seguinte conteúdo::

    import batma

    class MyGame(batma.Game):
        def initialize(self):
            batma.add_resource_path('resources')
        
        def load_content(self):
            pass

        def update(self, tick):
            pass

        def draw(self):
            pass

    game = MyGame()
    batma.run()

.. NOTE::
   Observe que os 4 métodos vistos no :doc:`introduction` já foram criados.

Execute o seu jogo pelo terminal com ``python mygame.py``, ou no windows com dois cliques no arquivo.

.. image:: _static/empty_batma.png
   :alt: An empty Batma game
   :align: center
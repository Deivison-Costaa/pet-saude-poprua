## options.rpy — PET-Saúde: Pop Rua
## Configurações do projeto

define config.name = _("Caminhos do Cuidado")
define gui.show_name = True
define config.version = "0.3"

define gui.about = _p("""
Visual novel educacional sobre o cuidado à população em situação de rua.
PET-Saúde · GT6 Pop Rua · UFPB — Frente TI
""")

define build.name = "petsaude-pop-rua"

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

default preferences.text_cps = 0
default preferences.afm_time = 15

define config.save_directory = "petsaude-pop-rua"
define config.window_icon = "gui/window_icon.png"

init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    ## Material de planejamento fica fora dos pacotes do jogo
    build.classify('docs/**', None)
    build.classify('assets-gerados/**', None)
    build.classify('README.md', None)
    build.classify('*.docx', None)
    build.classify('*.png', None)
    build.classify('*.txt', None)
    build.classify('01-07/**', None)
    build.classify('Imagens-*/**', None)
    ## Ferramentas e saídas de build que ficam na pasta do projeto.
    ## O CI extrai o SDK em renpy-sdk/ dentro do workspace e passa o próprio
    ## workspace como projeto para o distribute. Como a regra final do Ren'Py
    ## é um catch-all ("**", "all"), sem estas linhas o SDK inteiro (3532
    ## arquivos, ~340 MB) vai empacotado dentro de cada build do jogo.
    build.classify('renpy-sdk/**', None)
    build.classify('dist/**', None)
    build.classify('AppDir/**', None)
    build.classify('appimagetool', None)
    build.documentation('*.html')

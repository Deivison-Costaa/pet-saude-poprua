## options.rpy — PET-Saúde: Pop Rua
## Configurações do projeto

define config.name = _("PET-Saúde: Pop Rua")
define gui.show_name = True
define config.version = "0.1"

define gui.about = _p("""
Jogo educacional desenvolvido no âmbito do PET-Saúde.
GT6 — Pop Rua | Frente TI
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
    build.documentation('*.html')
    build.documentation('*.txt')

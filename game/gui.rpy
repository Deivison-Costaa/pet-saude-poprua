################################################################################
## gui.rpy — PET-Saúde: Pop Rua
## Baseado no template do Ren'Py 8.5 (the_question), paleta azul SUS.
################################################################################

init offset = -2
init python:
    gui.init(1280, 720)

define config.check_conflicting_properties = True


################################################################################
## Cores
################################################################################

define gui.accent_color = '#1A6B9A'           ## azul SUS
define gui.idle_color = '#888888'
define gui.idle_small_color = '#aaaaaa'
define gui.hover_color = '#4A9BC0'
define gui.selected_color = '#ffffff'
define gui.insensitive_color = '#5555557f'
define gui.muted_color = '#0A3050'
define gui.hover_muted_color = '#1A5080'
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


################################################################################
## Fontes (decisão registrada na issue #36)
## Duas famílias, separadas por função — não por decoração:
## - Atkinson Hyperlegible (OFL): interface, menu, corpo de texto e rodapé —
##   desenhada para máxima legibilidade; acentuação PT-BR completa.
## - Roboto Bold: título da tela inicial e cabeçalhos de seção — mesma
##   linguagem sans-serif limpa da placa "UPA 24h" pintada no fundo do menu,
##   com peso de destaque para não competir com o menu.
## KaushanScript-Regular.ttf permanece em fonts/ mas não é usada: uma fonte
## script/pincel destoaria da sinalização sans-serif do próprio cenário e
## perderia legibilidade nos tamanhos pequenos da variante mobile.
################################################################################

define gui.text_font = "fonts/AtkinsonHyperlegible-Regular.ttf"
define gui.name_text_font = "fonts/AtkinsonHyperlegible-Bold.ttf"
define gui.interface_text_font = "fonts/AtkinsonHyperlegible-Regular.ttf"
define gui.titulo_font = "fonts/Roboto-Bold.ttf"

define config.font_replacement_map = {
    ("fonts/AtkinsonHyperlegible-Regular.ttf", True,  False) : ("fonts/AtkinsonHyperlegible-Bold.ttf",       False, False),
    ("fonts/AtkinsonHyperlegible-Regular.ttf", False, True)  : ("fonts/AtkinsonHyperlegible-Italic.ttf",     False, False),
    ("fonts/AtkinsonHyperlegible-Regular.ttf", True,  True)  : ("fonts/AtkinsonHyperlegible-BoldItalic.ttf", False, False),
}

define gui.text_size = 26
define gui.name_text_size = 31
define gui.interface_text_size = 25
define gui.label_text_size = 29
define gui.notify_text_size = 17
define gui.title_text_size = 36

## Tela inicial — hierarquia título > menu > rodapé (issue #36)
define gui.main_menu_title_size = 48
define gui.main_menu_subtitle_size = 16
define gui.navigation_button_text_size = 22
define gui.main_menu_footer_text_size = 14
define gui.main_menu_footer_version_size = 12


################################################################################
## Menu principal e de jogo
################################################################################

define gui.main_menu_background = "gui/main_menu.webp"
define gui.game_menu_background = "gui/game_menu.webp"
define gui.main_menu_text_color = "#5ab8f5"


################################################################################
## Diálogos
################################################################################

## Caixa mais alta: 24 das 221 falas passam de 200 caracteres, e a maior (284)
## ocupa 4 linhas. Antes o texto batia nos botões do menu rápido e era cortado.
define gui.textbox_height = 260
define gui.textbox_yalign = 1.0

define gui.name_xpos = 110
define gui.name_ypos = 14
define gui.name_xalign = 0.0

define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(5, 5, 5, 5)
define gui.namebox_tile = False

define gui.dialogue_xpos = 110
define gui.dialogue_ypos = 58
define gui.dialogue_width = 1060
define gui.dialogue_text_xalign = 0.0


################################################################################
## Botões
################################################################################

define gui.button_width = None
define gui.button_height = 36
define gui.button_borders = Borders(4, 4, 4, 4)
define gui.button_tile = False

define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color
define gui.button_text_xalign = 0.0

define gui.radio_button_borders = Borders(25, 4, 4, 4)
define gui.check_button_borders = Borders(25, 4, 4, 4)
define gui.confirm_button_text_xalign = 0.5
define gui.page_button_borders = Borders(10, 4, 10, 4)
define gui.quick_button_borders = Borders(16, 10, 16, 6)
define gui.quick_button_text_size = 18
define gui.quick_button_text_idle_color = '#e4edf4'
define gui.quick_button_text_selected_color = gui.accent_color


################################################################################
## Botões de escolha
################################################################################

define gui.choice_button_width = 790
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 5, 100, 5)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
## Placas aquarela claras: texto escuro no repouso, claro no hover (placa azul)
define gui.choice_button_text_idle_color = "#1d3d5c"
define gui.choice_button_text_hover_color = "#f4f1ea"


################################################################################
## Slots de save/load
################################################################################

define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color

define config.thumbnail_width = 256
define config.thumbnail_height = 144
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


################################################################################
## Posicionamento e espaçamento
################################################################################

define gui.navigation_xpos = 40
define gui.skip_ypos = 10
define gui.notify_ypos = 45
define gui.choice_spacing = 22
define gui.navigation_spacing = 4
define gui.pref_spacing = 10
define gui.pref_button_spacing = 0
define gui.page_spacing = 0
define gui.slot_spacing = 10
define gui.main_menu_text_xalign = 0.0


################################################################################
## Frames
################################################################################

define gui.frame_borders = Borders(4, 4, 4, 4)
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)
define gui.skip_frame_borders = Borders(16, 5, 50, 5)
define gui.notify_frame_borders = Borders(16, 5, 40, 5)
define gui.frame_tile = False


################################################################################
## Barras, scrollbars, sliders
################################################################################

define gui.bar_size = 36
define gui.scrollbar_size = 12
define gui.slider_size = 30

define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)
define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)

define gui.unscrollable = "hide"


################################################################################
## Histórico
################################################################################

define config.history_length = 250
define gui.history_height = 140
define gui.history_name_xpos = 150
define gui.history_name_ypos = 0
define gui.history_name_width = 150
define gui.history_name_xalign = 1.0
define gui.history_text_xpos = 170
define gui.history_text_ypos = 5
define gui.history_text_width = 740
define gui.history_text_xalign = 0.0


################################################################################
## NVL
################################################################################

define gui.nvl_borders = Borders(0, 10, 0, 20)
define gui.nvl_height = 115
define gui.nvl_spacing = 10
define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0
define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_text_xalign = 0.0
define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0
define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0

define gui.language = "unicode"


################################################################################
## Variantes mobile
################################################################################

init python:
    @gui.variant
    def touch():
        ## Alvo de toque maior: nos testes no Android o acerto dos botões
        ## recebeu a pior nota do questionário.
        gui.quick_button_borders = Borders(40, 22, 40, 14)

    @gui.variant
    def small():
        gui.text_size = 30
        gui.name_text_size = 36
        gui.notify_text_size = 25
        gui.interface_text_size = 36
        gui.button_text_size = 34
        gui.label_text_size = 36
        gui.title_text_size = 44
        gui.main_menu_title_size = 64
        gui.main_menu_subtitle_size = 22
        gui.navigation_button_text_size = 30
        gui.main_menu_footer_text_size = 20
        gui.main_menu_footer_version_size = 17
        gui.textbox_height = 290
        gui.name_xpos = 80
        gui.dialogue_xpos = 90
        gui.dialogue_width = 1100
        gui.choice_button_width = 1240
        gui.navigation_spacing = 20
        gui.pref_button_spacing = 10
        gui.history_height = 190
        gui.history_text_width = 690
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
        gui.nvl_height = 170
        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325
        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5
        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20
        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20
        gui.quick_button_text_size = 24

## characters.rpy — Personagens e imagens do jogo

init python:
    def textbox_tinted(accent):
        ## Base escura + faixa de 4px na cor do personagem no topo do balão
        return Composite(
            (1280, 185),
            (0, 0), Solid("#0a1a2adf"),
            (0, 0), Solid(accent, xysize=(1280, 4)),
        )

## Narrador (sem nome, itálico)
define narr   = Character(None, what_italic=True, what_color="#dddddd",
                          window_background=Solid("#0a0a0ade"))

## Personagens falantes (cores dos nomes clareadas para legibilidade sobre fundo escuro)
define renato = Character("Renato",
                          color="#9BC5E0",
                          window_background=textbox_tinted("#5C8FB3"))
define tec    = Character("Técnica de Enfermagem",
                          color="#A8D8AE",
                          window_background=textbox_tinted("#7CA982"))
define assist = Character("Assistente Social",
                          color="#D9B080",
                          window_background=textbox_tinted("#B38B59"))
define med    = Character("Médico",
                          color="#D87E7E",
                          window_background=textbox_tinted("#A55858"))

## Imagens de background (subpasta bg/)
image bg titulo           = "bg/titulo.png"
image bg upa_recepcao     = "bg/upa_recepcao.png"
image bg upa_consultorio  = "bg/upa_consultorio.png"
image bg upa_observacao   = "bg/upa_sala_observacao.png"
image bg upa_corredor     = "bg/upa_corredor.png"
image bg upa_saida        = "bg/upa_porta_saida.png"

## Sprites de Renato (subpasta chars/)
image renato normal     = "chars/renato_normal.png"
image renato hesitante  = "chars/renato_hesitante.png"
image renato aberto     = "chars/renato_aberto.png"
image renato emocionado = "chars/renato_emocionado.png"
image renato despedida  = "chars/renato_despedida.png"

## Sprites secundários (subpasta chars/)
image tecnica    = "chars/tecnica.png"
image assistente = "chars/assistente_social.png"
image medico     = "chars/medico.png"

## Objeto especial (subpasta obj/)
image caderno = "obj/caderno_renato.png"

## Fundos de cor sólida (para epílogo e telas de transição)
image bg_escuro   = Solid("#0a1a2a")
image bg_card     = Solid("#0d1f2d")
image bg_positivo = Solid("#0a1a0a")
image bg_negativo = Solid("#1a0a0a")
image bg_preto    = Solid("#080808")

## Transforms para posicionamento de sprites (zoom calibrado para imagens 2816x1536)
## Ajuste o valor de zoom se as imagens forem de tamanho diferente
transform left:
    xalign 0.18
    yalign 1.0
    zoom 0.35

transform center:
    xalign 0.5
    yalign 1.0
    zoom 0.35

transform right:
    xalign 0.82
    yalign 1.0
    zoom 0.35

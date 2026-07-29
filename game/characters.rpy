## characters.rpy — Personagens e imagens do jogo
## História 1 — "Ele não parece morador de rua" (roteiro atualizado, cenas 0–7)

init python:
    def textbox_tinted(accent):
        ## Caixa de diálogo aquarela (gui/textbox.png) com uma pincelada fina
        ## na cor do personagem sob a área do nome.
        return Composite(
            (1280, 170),
            (0, 0), "gui/textbox.png",
            (110, 50), Solid(accent + "cc", xysize=(150, 3)),
        )

## Narrador (sem nome, itálico)
define narr   = Character(None, what_italic=True, what_color="#dddddd",
                          window_background=Image("gui/textbox.png"))

## Paciente central
define renato = Character("Renato",
                          color="#9BC5E0",
                          window_background=textbox_tinted("#5C8FB3"))

## Perspectivas jogáveis — o avatar do jogador muda a cada cena
define recep  = Character("Recepcionista (você)",
                          color="#A9C7E8",
                          window_background=textbox_tinted("#4A7FB5"))
define med    = Character("Médico (você)",
                          color="#D87E7E",
                          window_background=textbox_tinted("#A55858"))
define tec    = Character("Técnica de Enfermagem (você)",
                          color="#A8D8AE",
                          window_background=textbox_tinted("#7CA982"))
define enf    = Character("Enfermeiro (você)",
                          color="#A8D8AE",
                          window_background=textbox_tinted("#5E8C61"))
define prof   = Character("Profissional (você)",
                          color="#C9D4DE",
                          window_background=textbox_tinted("#6E8296"))

## Equipe e NPCs
define assist    = Character("Assistente Social",
                             color="#D9B080",
                             window_background=textbox_tinted("#B38B59"))
define marcos    = Character("Marcos (CNR, ao telefone)",
                             color="#8FD0C6",
                             window_background=textbox_tinted("#4E9A8E"))
define senhora_c = Character("Senhora da sala de espera",
                             color="#D8B8C8",
                             window_background=textbox_tinted("#9A7286"))
define outro_pac = Character("Outro paciente",
                             color="#C8B8A0",
                             window_background=textbox_tinted("#8A7A5E"))

## ── Backgrounds aquarela (padrão visual aprovado em 01/07) ───────────────────
image bg titulo           = "bg/menu_upa.jpg"
image bg aqua_fachada     = "bg/aqua_fachada.jpg"
image bg aqua_recepcao    = "bg/aqua_recepcao.jpg"
image bg aqua_espera      = "bg/aqua_espera.jpg"
image bg aqua_balcao      = "bg/aqua_balcao.jpg"
image bg aqua_consultorio = "bg/aqua_consultorio.jpg"
image bg aqua_box         = "bg/aqua_box.jpg"
image bg aqua_corredor    = "bg/aqua_corredor.jpg"
image bg aqua_saida       = "bg/aqua_saida.jpg"
image bg neutro_cor       = "bg/neutro_cor.png"
image bg neutro_quente    = "bg/neutro_quente.png"
image bg neutro_frio      = "bg/neutro_frio.png"
image bg teste001         = Transform("bg/Teste001.png", size=(1280, 720))
image bg img2             = Transform("bg/Img2.png", size=(1280, 720))

## Overlay do e-SUS (tela de registro)
image esus = "bg/aqua_esus.jpg"

## ── Sprites de Renato (2816x1536, recorte com alpha) ─────────────────────────
image renato normal     = "chars/renato_normal.png"
image renato hesitante  = "chars/renato_hesitante.png"
image renato aberto     = "chars/renato_aberto.png"
image renato emocionado = "chars/renato_emocionado.png"
image renato despedida  = "chars/renato_despedida.png"

## ── Sprites da equipe e NPCs ─────────────────────────────────────────────────
image tecnica        = "chars/tecnica.png"
image assistente     = "chars/assistente_social.png"
image medico         = "chars/medico.png"
image senhora        = "chars/senhora.png"
image senhora_fofoqueira = "chars/SenhoraFofoqueira.png"
image senhor_fofoqueiro  = "chars/SenhorFofoqueiro.png"
image renato_fofocado    = "chars/RenatoFofocado.png"
image recepcionista_chamando_renato = "chars/RecepcionistaChamandoRenato.png"
image outro_paciente = "chars/outro_paciente.png"

## ── Objetos das cenas (recorte com alpha) ────────────────────────────────────
image caderno  = "obj/caderno_renato.png"
image carteira = "obj/obj_carteira_trabalho.png"
image cartao   = "obj/obj_cartao_sus.png"
image receita  = "obj/obj_receita_medica.png"

## ── Fundos de cor sólida (epílogo e transições) ──────────────────────────────
image bg_escuro   = Solid("#0a1a2a")
image bg_card     = Solid("#0d1f2d")
image bg_positivo = Solid("#0a1a0a")
image bg_negativo = Solid("#1a0a0a")
image bg_preto    = Solid("#080808")

## ── Transforms de posicionamento ─────────────────────────────────────────────
## Os sprites 2816x1536 têm margens transparentes largas com a figura no centro
## do canvas — por isso ancoramos pelo CENTRO da imagem (xanchor 0.5) e
## posicionamos com xpos, para a figura cair onde se espera.
## zoom 0.35 → figura com ~505px de altura na tela (referência: Renato).
transform left:
    xanchor 0.5
    xpos 0.16
    yalign 1.0
    zoom 0.35

transform center:
    xanchor 0.5
    xpos 0.5
    yalign 1.0
    zoom 0.35

transform right:
    xanchor 0.5
    xpos 0.82
    yalign 1.0
    zoom 0.35

## Sprites novos 1024x1536 (figura ocupa o canvas inteiro): zoom calibrado para
## ficarem um pouco MENORES que o Renato (504px) — senhora 0.31≈465px,
## outro paciente 0.33≈494px.
transform left_np(z=0.32):
    xanchor 0.5
    xpos 0.16
    yalign 1.0
    zoom z

transform right_np(z=0.32):
    xanchor 0.5
    xpos 0.84
    yalign 1.0
    zoom z

## objetos em destaque (1024x1024)
transform obj_centro:
    xalign 0.5
    yalign 0.42
    zoom 0.45

transform obj_esq:
    xalign 0.32
    yalign 0.42
    zoom 0.42

transform obj_dir:
    xalign 0.68
    yalign 0.45
    zoom 0.36

## overlay e-SUS (1600x900 sobre 1280x720)
transform overlay_esus:
    xalign 0.5
    yalign 0.5
    zoom 0.8
    alpha 0.96

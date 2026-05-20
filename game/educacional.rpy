## educacional.rpy — Cards pedagógicos e Epílogo da Missão 1

## ─────────────────────────────────────────────────────────────────────────────
## Screen: card de reflexão (chamado no fim de cada momento de decisão)
## ─────────────────────────────────────────────────────────────────────────────

screen reflexao_card(linha1, linha2=""):
    zorder 130

    add Solid("#04101a")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 920
        background Solid("#0d1f2de8")
        padding (60, 50, 60, 50)

        has vbox
        spacing 20
        xfit False

        text "REFLEXÃO" size 15 color "#1A6B9A" bold True xalign 0.5 outlines [(1, "#000000", 0, 0)]

        add Solid("#1A6B9A", xysize=(800, 2)) xalign 0.5

        null height 6

        text "[linha1]" size 22 color "#eaeaea" italic True xalign 0.5 textalign 0.5 layout "subtitle"

        if linha2:
            null height 8
            text "[linha2]" size 22 color "#c8d8e8" italic True xalign 0.5 textalign 0.5 layout "subtitle"

        null height 16

        textbutton "Continuar  ›" action Return() xalign 0.5 text_size 16 text_color "#1A6B9A" text_hover_color "#ffffff"


label reflexao_card(linha1, linha2=""):
    call screen reflexao_card(linha1, linha2) with dissolve
    return


## ─────────────────────────────────────────────────────────────────────────────
## Screen: Card de Contexto Real (antes do epílogo)
## ─────────────────────────────────────────────────────────────────────────────

screen contexto_real():
    zorder 130

    add Solid("#04101a")

    viewport:
        xalign 0.5
        yalign 0.5
        xsize 1080
        ysize 680
        mousewheel True
        draggable True

        frame:
            xsize 1080
            background "#00000000"
            padding (60, 40, 60, 40)
            has vbox
            spacing 12

            text "CONTEXTO REAL" size 22 color "#1A6B9A" bold True xalign 0.5
            text "O que os dados dizem" size 16 color "#7a9ab0" italic True xalign 0.5
            null height 4
            add Solid("#1A6B9A", xysize=(960, 2)) xalign 0.5
            null height 8

            text "A população em situação de rua é {b}heterogênea{/b}." size 19 color "#dddddd" layout "subtitle"
            text "Os motivos mais citados para a situação de rua são {b}problemas familiares, desemprego e uso de substâncias{/b}. Não existe um perfil único." size 19 color "#dddddd" layout "subtitle"
            text "A surpresa ao descobrir que alguém {i}\"não parece morador de rua\"{/i} é, ela mesma, um sinal de que o imaginário do profissional precisa ser revisado." size 19 color "#dddddd" layout "subtitle"

            null height 10
            add Solid("#2a3a4a", xysize=(960, 1)) xalign 0.5
            null height 10

            text "{b}Como funciona a rede SUS:{/b}" size 19 color "#dddddd"
            text "• A UPA não atualiza o endereço para 'situação de rua' — esse cuidado pertence ao Consultório na Rua (CNR), acionado pelo Serviço Social após o registro médico no prontuário." size 19 color "#cccccc" layout "subtitle"
            text "• A prioridade do atendimento é dada pela Classificação de Risco Clínica, não pela condição de moradia." size 19 color "#cccccc" layout "subtitle"
            text "• O CIAP-2 permite registrar diagnóstico clínico e fatores psicossociais no e-SUS, criando continuidade de cuidado." size 19 color "#cccccc" layout "subtitle"

            null height 10
            add Solid("#2a3a4a", xysize=(960, 1)) xalign 0.5
            null height 6

            text "Fonte: MDHC — Diagnóstico Federal sobre a Situação de Rua, 2023." size 14 color "#5a7a8a" italic True xalign 1.0

            null height 20
            textbutton "Continuar  ›" action Return() xalign 0.5 text_size 17 text_color "#1A6B9A" text_hover_color "#ffffff"
            null height 20


## ─────────────────────────────────────────────────────────────────────────────
## Screen: Resultado final com revelação do ESTIGMA
## ─────────────────────────────────────────────────────────────────────────────

screen epilogo_medidores(resultado_estigma):
    zorder 120

    frame:
        xalign 0.5
        yalign 0.35
        xsize 820
        background "#000000cc"
        padding (30, 22)

        has vbox
        spacing 14

        text "RESULTADO — MISSÃO 1" size 18 bold True color "#ffffff" xalign 0.5

        null height 4

        hbox:
            spacing 30
            xalign 0.5

            vbox:
                spacing 4
                text "CONFIANÇA" size 12 color "#9BC5E0" bold True
                bar:
                    value VariableValue("confianca", 100)
                    xsize 140
                    ysize 11
                    left_bar Solid("#5C8FB3")
                    right_bar Solid("#222")
                text "[confianca]/100" size 11 color "#9BC5E0"

            vbox:
                spacing 4
                text "SAÚDE" size 12 color "#A8D8AE" bold True
                bar:
                    value VariableValue("saude", 100)
                    xsize 140
                    ysize 11
                    left_bar Solid("#7CA982")
                    right_bar Solid("#222")
                text "[saude]/100" size 11 color "#A8D8AE"

            vbox:
                spacing 4
                text "ACESSO" size 12 color "#D9B080" bold True
                bar:
                    value VariableValue("acesso", 100)
                    xsize 140
                    ysize 11
                    left_bar Solid("#C4A55A")
                    right_bar Solid("#222")
                text "[acesso]/100" size 11 color "#D9B080"

            vbox:
                spacing 4
                text "VÍNCULO" size 12 color "#BB99DD" bold True
                bar:
                    value VariableValue("vinculo", 100)
                    xsize 140
                    ysize 11
                    left_bar Solid("#AA77CC")
                    right_bar Solid("#222")
                text "[vinculo]/100" size 11 color "#BB99DD"

        null height 6
        add Solid("#2a3a4a", xysize=(720, 1)) xalign 0.5

        vbox:
            spacing 5
            xalign 0.5
            text "ESTIGMA" size 15 bold True color "#E05555" xalign 0.5
            text "(Este medidor rodou invisível durante toda a missão)" size 12 color "#888888" xalign 0.5
            bar:
                value VariableValue("estigma", 100)
                xsize 380
                ysize 15
                left_bar Solid("#E05555")
                right_bar Solid("#222")
                xalign 0.5
            text "[estigma]/100  —  [resultado_estigma]" size 12 color "#E05555" xalign 0.5

        null height 6
        textbutton "Continuar" action Hide("epilogo_medidores") xalign 0.5


## ─────────────────────────────────────────────────────────────────────────────
## EPÍLOGO
## ─────────────────────────────────────────────────────────────────────────────

label epilogo:
    play music "audio/music/reflexao.ogg" fadein 2.0

    ## ── Card de Contexto Real ─────────────────────────────────────────────────

    scene bg_preto with fade
    call screen contexto_real with dissolve

    window show

    ## ── Epílogo comparativo ───────────────────────────────────────────────────

    $ pontuacao = confianca + acesso + vinculo + saude

    if pontuacao >= 220:
        scene bg_positivo with fade

        narr "{b}O QUE ACONTECEU COM RENATO — Semana seguinte{/b}"
        narr "O Serviço Social acionou o CNR ainda durante a madrugada."
        narr "A equipe encontrou Renato dois dias depois no ponto combinado. Atualizou o cadastro. Vinculou à UBS do território. Iniciou acompanhamento de saúde mental."
        narr "Renato está medicado, dormindo no abrigo, retomou contato com um dos filhos."
        narr "O caderno de entrevistas continua com nomes riscados — mas a última folha tem um endereço diferente: o do CRAS mais próximo."
        narr "{i}O sistema funcionou porque alguém decidiu que valia a pena fazê-lo funcionar.{/i}"

    else:
        scene bg_negativo with fade

        narr "{b}O QUE ACONTECEU COM RENATO — Semana seguinte{/b}"
        narr "Renato voltou à UPA duas semanas depois, com crise ainda mais intensa."
        narr "Foi atendido por outro profissional. O endereço no sistema ainda era o mesmo de uma década atrás. Sem registro de situação de rua. Sem histórico de depressão."
        narr "Ninguém sabia que ele havia estado aqui antes."
        narr "O cuidado recomeçou do zero."
        narr "{i}O sistema falhou. Mas o sistema somos nós.{/i}"

    ## ── Revelação do ESTIGMA ──────────────────────────────────────────────────

    hide screen medidores
    scene bg_preto with fade

    $ resultado_estigma_texto = ""
    if estigma <= 10:
        $ resultado_estigma_texto = "Baixo — você perguntou antes de assumir"
    elif estigma <= 30:
        $ resultado_estigma_texto = "Moderado — algumas suposições afetaram o cuidado"
    elif estigma <= 60:
        $ resultado_estigma_texto = "Alto — o estigma influenciou decisões clínicas"
    else:
        $ resultado_estigma_texto = "Muito alto — o estigma dominou o atendimento"

    show screen epilogo_medidores(resultado_estigma_texto) with dissolve
    pause

    ## ── Pergunta retórica final ───────────────────────────────────────────────

    hide screen epilogo_medidores
    scene bg_preto with fade

    centered "{color=#dddddd}{size=+8}{i}O que você viu primeiro —{/i}{/size}{/color}"
    pause 0.8
    centered "{color=#dddddd}{size=+8}{i}a pessoa ou a ficha?{/i}{/size}{/color}"
    pause 2.0

    centered "{color=#666666}{size=-2}Missão 1 concluída.{/size}{/color}"
    pause 1.5

    return

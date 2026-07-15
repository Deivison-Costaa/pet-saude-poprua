## educacional.rpy — Cards pedagógicos, Card de Contexto Real e Epílogo
## História 1 — medidores: DIREITO · REDE · EMPATIA (visível) · ACOLHIMENTO

## ─────────────────────────────────────────────────────────────────────────────
## Screen: card de reflexão (fim de cada cena)
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

        text "REFLEXÃO" size 15 color "#3E7CB1" bold True xalign 0.5 outlines [(1, "#000000", 0, 0)]

        add Solid("#3E7CB1", xysize=(800, 2)) xalign 0.5

        null height 6

        text "[linha1]" size 22 color "#eaeaea" italic True xalign 0.5 textalign 0.5 layout "subtitle"

        if linha2:
            null height 8
            text "[linha2]" size 22 color "#c8d8e8" italic True xalign 0.5 textalign 0.5 layout "subtitle"

        null height 16

        textbutton "Continuar  ›" action Return() xalign 0.5 text_size 16 text_color "#3E7CB1" text_hover_color "#ffffff"


label reflexao_card(linha1, linha2=""):
    call screen reflexao_card(linha1, linha2) with dissolve
    return


## ─────────────────────────────────────────────────────────────────────────────
## Screen: Card de Contexto Real (antes do epílogo) — texto do roteiro atualizado
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
        scrollbars "vertical"
        pagekeys True

        frame:
            xsize 1080
            background "#00000000"
            padding (60, 40, 60, 40)
            has vbox
            spacing 12

            text "CONTEXTO REAL" size 22 color "#3E7CB1" bold True xalign 0.5
            text "O que os dados dizem" size 16 color "#7a9ab0" italic True xalign 0.5
            null height 4
            add Solid("#3E7CB1", xysize=(960, 2)) xalign 0.5
            null height 8

            text "A população em situação de rua é {b}heterogênea{/b}. Dados de 2022 apontam como motivos mais citados problemas familiares, desemprego e uso de substâncias. Não existe um perfil único." size 19 color "#dddddd" layout "subtitle"
            text "A surpresa ao descobrir que alguém {i}“não parece morador de rua”{/i} é, ela mesma, um sinal de que o imaginário do profissional precisa ser revisado." size 19 color "#dddddd" layout "subtitle"

            null height 10
            add Solid("#2a3a4a", xysize=(960, 1)) xalign 0.5
            null height 10

            text "{b}Na prática do SUS:{/b}" size 19 color "#dddddd"
            text "• A recepção da UPA não atualiza o endereço para “situação de rua” — esse cuidado pertence ao Consultório na Rua, acionado a partir do Serviço Social, após o registro no prontuário. A prioridade do atendimento é dada pela Classificação de Risco Clínica, não pela condição de moradia." size 19 color "#cccccc" layout "subtitle"
            text "• A {b}Portaria GM/MS 940/2011{/b} garante o cadastro do Cartão SUS para PSR mesmo com dados incompletos ou sem documento. A Defensoria Pública é o caminho legal para a regularização documental, acionada via Serviço Social com ofício curto e anuência do paciente." size 19 color "#cccccc" layout "subtitle"
            text "• O intervalo de observação é onde o profissional consolida o registro e alinha a equipe — ou o desperdiça como tempo morto. A qualidade do registro no e-SUS decide se o caso circula pela rede: a codificação {b}CIAP-2{/b} e o campo de vulnerabilidade social transformam informação em articulação." size 19 color "#cccccc" layout "subtitle"
            text "• A alta não se encerra na prescrição — depende da dispensação na farmácia da UPA, da passagem de caso com contexto ao Serviço Social e da articulação com o CNR. A busca ativa funciona quando tem {b}nome, voz e ponto combinado{/b}, não quando é demanda anônima em relatório de turno." size 19 color "#cccccc" layout "subtitle"

            null height 10
            add Solid("#2a3a4a", xysize=(960, 1)) xalign 0.5
            null height 10

            text "{b}Base conceitual — as quatro dimensões articuladas:{/b}" size 19 color "#dddddd"
            text "• {b}Direito em Saúde{/b} — acesso universal independente de documentação (Portaria GM/MS 940/2011), cidadania civil como condição material do cuidado, PNH/HumanizaSUS como prática técnica, e a estrutura governamental (UPA, UBS, CNR, CRAS, Defensoria, Serviço Social) como rede de garantia de direitos." size 18 color "#cccccc" layout "subtitle"
            text "• {b}Conhecimento da Rede{/b} — articulação institucional exercida, não só conhecida: e-SUS com CIAP-2 e campo de vulnerabilidade como fio de continuidade, Classificação de Risco pelo quadro clínico, CNR como presença territorial com nome e voz, e o caminho UPA → Serviço Social → CNR → UBS → Defensoria." size 18 color "#cccccc" layout "subtitle"
            text "• {b}Empatia / Sensibilidade Social{/b} — reconhecer a pessoa antes do estereótipo, perguntar antes de assumir, identificar fatores sociais sem reduzir a pessoa a eles, posicionar-se diante do preconceito de terceiros e mediar a linguagem técnica na presença do paciente." size 18 color "#cccccc" layout "subtitle"
            text "• {b}Acolhimento{/b} — qualidade do encontro: escuta ativa, presença durante a observação, comunicação humanizada na alta, passagem de caso com contexto e despedida que reconhece a pessoa — não apenas o quadro clínico." size 18 color "#cccccc" layout "subtitle"

            null height 10
            add Solid("#2a3a4a", xysize=(960, 1)) xalign 0.5
            null height 6

            text "Fontes: MDHC, Diagnóstico Federal 2023 · Portaria GM/MS 940/2011 · PNAB 2017 · Política Nacional para PSR (Decreto 7053/2009) · PNH/HumanizaSUS." size 14 color "#5a7a8a" italic True xalign 1.0

            null height 20
            textbutton "Continuar  ›" action Return() xalign 0.5 text_size 17 text_color "#3E7CB1" text_hover_color "#ffffff"
            null height 20


## ─────────────────────────────────────────────────────────────────────────────
## Screen: painel final — 4 medidores + mapa de nós da rede
## ─────────────────────────────────────────────────────────────────────────────

screen epilogo_medidores():
    zorder 120

    frame:
        xalign 0.5
        yalign 0.5
        xsize 980
        background "#000000cc"
        padding (36, 26)

        has vbox
        spacing 14

        text "RESULTADO — DIA 1" size 18 bold True color "#ffffff" xalign 0.5
        text "As quatro dimensões do cuidado, reveladas agora." size 13 color "#8899aa" italic True xalign 0.5

        null height 4

        hbox:
            spacing 26
            xalign 0.5

            vbox:
                spacing 4
                text "DIREITO EM SAÚDE" size 12 color "#E8C97A" bold True
                bar:
                    value VariableValue("direito", 100)
                    xsize 190
                    ysize 12
                    left_bar Solid("#C4A55A")
                    right_bar Solid("#222")
                text "[direito]/100" size 11 color "#E8C97A"

            vbox:
                spacing 4
                text "CONHEC. DA REDE" size 12 color "#8FD0C6" bold True
                bar:
                    value VariableValue("rede", 100)
                    xsize 190
                    ysize 12
                    left_bar Solid("#4E9A8E")
                    right_bar Solid("#222")
                text "[rede]/100" size 11 color "#8FD0C6"

            vbox:
                spacing 4
                text "EMPATIA" size 12 color "#D8A8B8" bold True
                bar:
                    value VariableValue("empatia", 100)
                    xsize 190
                    ysize 12
                    left_bar Solid("#B07286")
                    right_bar Solid("#222")
                text "[empatia]/100" size 11 color "#D8A8B8"

            vbox:
                spacing 4
                text "ACOLHIMENTO" size 12 color "#9BC5E0" bold True
                bar:
                    value VariableValue("acolhimento", 100)
                    xsize 190
                    ysize 12
                    left_bar Solid("#5C8FB3")
                    right_bar Solid("#222")
                text "[acolhimento]/100" size 11 color "#9BC5E0"

        null height 8
        add Solid("#2a3a4a", xysize=(880, 1)) xalign 0.5

        text "MAPA DA REDE — nós que você acendeu" size 14 bold True color "#8FD0C6" xalign 0.5

        hbox:
            xalign 0.5
            spacing 10
            for nome, aceso in nos_rede.items():
                frame:
                    background (Solid("#14524A") if aceso else Solid("#1a2229"))
                    padding (10, 7)
                    text nome size 12 color ("#B8EDE4" if aceso else "#4a555e") bold aceso

        null height 8
        textbutton "Continuar" action Return() xalign 0.5 text_size 16 text_color "#3E7CB1" text_hover_color "#ffffff"


## ─────────────────────────────────────────────────────────────────────────────
## EPÍLOGO — reflexão pós-capítulo e desfechos
## ─────────────────────────────────────────────────────────────────────────────

label epilogo:
    play music "audio/music/reflexao.ogg" fadein 2.0

    ## ── Card de Contexto Real ─────────────────────────────────────────────────
    scene bg neutro_frio with fade
    call screen contexto_real with dissolve

    window show

    ## ── Reflexão pós-capítulo (roteiro) ───────────────────────────────────────
    scene bg neutro_cor with fade
    narr "{b}REFLEXÃO PÓS-CAPÍTULO{/b}"
    narr "O jogo mostra o caminho que as suas escolhas construíram e compara: o que você {b}quis{/b} fazer e o que de fato {b}fez{/b}. A intenção de cuidar é comum a quase todas as escolhas; a diferença está na forma, no tempo e na presença."
    narr "Onde você priorizou o acolhimento — e onde deixou o instrumento (protocolo, prontuário, prescrição, encaminhamento) chegar antes da escuta."
    narr "Onde exerceu o direito como prática — e onde o tratou como princípio abstrato. Saber que o direito existe é diferente de exercê-lo."
    narr "E o que Renato sentiu em cada momento — a hesitação na sala de espera, o pedido de desculpas por “ocupar espaço”, o medo da alta — agora lido pela perspectiva dele."
    narr "A seguir: o que aconteceu com Renato na semana seguinte, dependendo das suas decisões."

    ## ── Painel final: medidores + mapa de nós ─────────────────────────────────
    hide screen medidores
    $ nos_acesos = sum(1 for v in nos_rede.values() if v)
    call screen epilogo_medidores with dissolve

    ## ── Desfecho ──────────────────────────────────────────────────────────────
    $ desfecho_a = (escolha_s51 == "C" and acolhimento >= 60 and rede >= 60)

    if desfecho_a:
        $ persistent.h1_desfecho = "A"
        scene bg neutro_quente with fade

        narr "{b}DESFECHO A — REDE ATIVADA{/b}"
        narr "O Serviço Social acionou Marcos ainda na madrugada. Marcos encontrou Renato dois dias depois no coreto da praça — exatamente onde Renato havia anotado no caderno."
        narr "Atualizou o cadastro no território, vinculou Renato à UBS de referência e iniciou o acompanhamento de saúde mental. A Defensoria agendou a regularização documental para a semana seguinte."
        narr "Renato está medicado, dormindo em abrigo — e retomou contato com um dos filhos."
        narr "{i}Você acendeu [nos_acesos] de 7 nós da rede. O sistema funcionou porque alguém decidiu que valia a pena fazê-lo funcionar.{/i}"

    else:
        $ persistent.h1_desfecho = "B"
        scene bg neutro_frio with fade

        narr "{b}DESFECHO B — RECOMEÇO DO ZERO{/b}"
        narr "Renato voltou ao pronto-socorro em duas semanas, com uma crise pior, atendido por outro profissional."
        narr "O endereço no sistema continua o de uma década atrás. Não há registro da situação de rua no prontuário. Ninguém sabe que ele já tinha estado ali."
        narr "O cuidado recomeça do zero — só que com menos tempo."
        narr "{i}Você acendeu [nos_acesos] de 7 nós da rede. A barra de Conhecimento da Rede é exatamente o que vai (ou não) aparecer como histórico utilizável no início do Dia 2.{/i}"

    ## ── Registro persistente do progresso ─────────────────────────────────────
    $ persistent.h1_concluida = True
    $ persistent.h1_medidores = {"Direito em Saúde": direito, "Conhecimento da Rede": rede, "Empatia": empatia, "Acolhimento": acolhimento}
    $ persistent.h1_nos = dict(nos_rede)

    ## ── Pergunta final ────────────────────────────────────────────────────────
    scene bg_preto with fade

    centered "{color=#dddddd}{size=+8}{i}O perfil dos quatro medidores é o espelho que o jogo devolve —{/i}{/size}{/color}"
    centered "{color=#dddddd}{size=+8}{i}não como julgamento, mas como convite a perceber que cada gesto técnico carrega uma dimensão humana.{/i}{/size}{/color}"
    pause 1.0

    centered "{color=#888888}{size=-2}Dia 1 concluído. Obrigado por jogar esta versão de testes.{/size}{/color}"

    return

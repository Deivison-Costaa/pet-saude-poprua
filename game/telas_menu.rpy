## telas_menu.rpy — Telas de menu: Capítulos, Perfil/Progresso, Materiais,
## Redes de apoio e Sobre o jogo (estrutura de docs/estrutura-telas.md).
## Conteúdo de Materiais/Redes é provisório — validar textos com o grupo.

## ── Progresso persistente ─────────────────────────────────────────────────────
default persistent.h1_concluida = False
default persistent.h1_desfecho = ""
default persistent.h1_medidores = {}
default persistent.h1_nos = {}


## ─────────────────────────────────────────────────────────────────────────────
## CAPÍTULOS
## ─────────────────────────────────────────────────────────────────────────────

screen capitulos():

    tag menu

    use game_menu(_("Capítulos"), scroll="viewport"):

        vbox:
            spacing 18

            ## História 1 — jogável
            frame:
                background "#0d1f2dee"
                padding (24, 18)
                xfill True

                has vbox
                spacing 6

                hbox:
                    spacing 12
                    text "DIA 1" size 15 color "#3E7CB1" bold True
                    if persistent.h1_concluida:
                        text ("concluída — desfecho " + persistent.h1_desfecho) size 13 color "#8FD0C6" italic True yalign 0.5
                    else:
                        text "não iniciada" size 13 color "#8899aa" italic True yalign 0.5

                text "“Ele não parece morador de rua”" size 22 color "#f0f0f0" bold True
                text "Renato, 54 anos, chega à UPA com dor no peito. Quem é essa população — e o que o seu olhar decide antes da ficha?" size 15 color "#b8c4ce"

                null height 6
                textbutton _("Jogar esta história  ›") action Start() text_size 17

            ## Histórias futuras — bloqueadas
            for titulo, tema in [
                ("DIA 2 — Vínculo e rede", "novo paciente, novo recorte do território"),
                ("DIA 3 — Documento e acesso", "a regularização documental como parte do cuidado"),
                ("DIA 4 — Estigma e cuidado", "o enfrentamento do estigma na continuidade")]:

                frame:
                    background "#101820aa"
                    padding (24, 14)
                    xfill True

                    has vbox
                    spacing 3

                    hbox:
                        spacing 10
                        text titulo size 17 color "#5a6773" bold True
                        text "em desenvolvimento" size 12 color "#4a555e" italic True yalign 0.5
                    text tema size 13 color "#4a555e" italic True


## ─────────────────────────────────────────────────────────────────────────────
## PERFIL / PROGRESSO (persistente entre sessões)
## ─────────────────────────────────────────────────────────────────────────────

screen perfil():

    tag menu

    use game_menu(_("Perfil / Progresso"), scroll="viewport"):

        vbox:
            spacing 16

            text "Histórias" size 20 color "#f0f0f0" bold True

            hbox:
                spacing 12
                frame:
                    background ("#14524A" if persistent.h1_concluida else "#1a2229")
                    padding (14, 10)
                    text ("Dia 1  ✓" if persistent.h1_concluida else "Dia 1") size 15 color ("#B8EDE4" if persistent.h1_concluida else "#5a6773") bold True
                for n in ["Dia 2", "Dia 3", "Dia 4"]:
                    frame:
                        background "#1a2229"
                        padding (14, 10)
                        text n size 15 color "#4a555e"

            if persistent.h1_concluida:

                null height 8
                text "Última jogada — Dia 1 (desfecho [persistent.h1_desfecho])" size 17 color "#c8d4de" bold True

                vbox:
                    spacing 8
                    for nome, valor in persistent.h1_medidores.items():
                        hbox:
                            spacing 12
                            text nome size 14 color "#b8c4ce" min_width 260
                            bar:
                                value StaticValue(valor, 100)
                                xsize 300
                                ysize 12
                                yalign 0.5
                                left_bar Solid("#3E7CB1")
                                right_bar Solid("#1a2229")
                            text "[valor]/100" size 13 color "#b8c4ce" yalign 0.5

                null height 6
                text "Nós da rede acesos" size 15 color "#8FD0C6" bold True
                hbox:
                    spacing 8
                    box_wrap True
                    for nome, aceso in persistent.h1_nos.items():
                        frame:
                            background (Solid("#14524A") if aceso else Solid("#1a2229"))
                            padding (8, 6)
                            text nome size 12 color ("#B8EDE4" if aceso else "#4a555e")

                null height 10
                textbutton _("Apagar progresso") action Confirm("Apagar todo o progresso salvo?", yes=[SetField(persistent, "h1_concluida", False), SetField(persistent, "h1_desfecho", ""), SetField(persistent, "h1_medidores", {}), SetField(persistent, "h1_nos", {})]) text_size 14

            else:
                text "Você ainda não concluiu nenhuma história. Os medidores da sua jogada aparecem aqui ao final do Dia 1." size 15 color "#8899aa" italic True


## ─────────────────────────────────────────────────────────────────────────────
## MATERIAIS (conteúdo provisório — validar com o grupo)
## ─────────────────────────────────────────────────────────────────────────────

screen materiais():

    tag menu

    use game_menu(_("Materiais"), scroll="viewport"):

        vbox:
            spacing 14

            text "Conteúdos educativos sobre a população em situação de rua e o atendimento em saúde. {i}(textos provisórios — em validação pelo grupo){/i}" size 15 color "#8899aa"

            frame:
                background "#0d1f2dee"
                padding (22, 16)
                xfill True
                has vbox
                spacing 6
                text "Quem é a população em situação de rua?" size 18 color "#f0f0f0" bold True
                text "É heterogênea: não existe um perfil único. Os motivos mais citados (dados de 2022) são problemas familiares, desemprego e uso de substâncias. A surpresa de que alguém “não parece morador de rua” é, ela mesma, um sinal de que o imaginário precisa ser revisado." size 15 color "#b8c4ce"

            frame:
                background "#0d1f2dee"
                padding (22, 16)
                xfill True
                has vbox
                spacing 6
                text "O direito ao atendimento" size 18 color "#f0f0f0" bold True
                text "O SUS é universal. A Portaria GM/MS 940/2011 garante o cadastro do Cartão SUS mesmo com dados incompletos ou sem documento. Exigir endereço ou documentação para atender é uma barreira ilegal." size 15 color "#b8c4ce"

            frame:
                background "#0d1f2dee"
                padding (22, 16)
                xfill True
                has vbox
                spacing 6
                text "Registro que vira cuidado" size 18 color "#f0f0f0" bold True
                text "A codificação CIAP-2 e o campo de vulnerabilidade social no e-SUS fazem o caso circular pela rede: busca ativa do Consultório na Rua, vinculação à UBS de referência, prioridade nos fluxos. Texto livre é carta que não chega." size 15 color "#b8c4ce"

            frame:
                background "#0d1f2dee"
                padding (22, 16)
                xfill True
                has vbox
                spacing 6
                text "Fontes" size 18 color "#f0f0f0" bold True
                text "MDHC — Diagnóstico Federal 2023 · Portaria GM/MS 940/2011 · PNAB 2017 · Decreto 7053/2009 (Política Nacional para a PSR) · Política Nacional de Humanização (HumanizaSUS)." size 14 color "#8899aa" italic True


## ─────────────────────────────────────────────────────────────────────────────
## REDES DE APOIO (conteúdo provisório)
## ─────────────────────────────────────────────────────────────────────────────

screen redes_apoio():

    tag menu

    use game_menu(_("Redes de apoio"), scroll="viewport"):

        vbox:
            spacing 12

            text "Os principais serviços de atendimento e como eles se conectam. {i}(conteúdo provisório){/i}" size 15 color "#8899aa"

            for nome, desc in [
                ("UPA — Unidade de Pronto Atendimento", "urgência e emergência 24h; a prioridade é dada pela Classificação de Risco Clínica, não pela condição de moradia."),
                ("Serviço Social", "presente na UPA; é a ponte entre o atendimento clínico e o restante da rede — CNR, CRAS, Defensoria."),
                ("CNR — Consultório na Rua", "equipe que atende no território, com busca ativa. Funciona com nome, voz e ponto combinado."),
                ("UBS — Unidade Básica de Saúde", "referência para a continuidade do cuidado: acompanhamento, renovação de receitas, saúde mental."),
                ("CRAS — Centro de Referência de Assistência Social", "documentação, benefícios e programas sociais; recebe encaminhamentos do Serviço Social."),
                ("Farmácia da UPA", "dispensação imediata da medicação na alta — garante que o paciente saia medicado."),
                ("Defensoria Pública", "regularização documental e garantia de direitos; acionada via ofício do Serviço Social com anuência do paciente.")]:

                frame:
                    background "#0d1f2dee"
                    padding (20, 12)
                    xfill True
                    has vbox
                    spacing 3
                    text nome size 16 color "#8FD0C6" bold True
                    text desc size 14 color "#b8c4ce"

            null height 6
            text "Caminho típico do Dia 1:  UPA → Serviço Social → CNR → UBS → CRAS/Defensoria" size 14 color "#3E7CB1" bold True


## ─────────────────────────────────────────────────────────────────────────────
## SOBRE O JOGO
## ─────────────────────────────────────────────────────────────────────────────

screen sobre_jogo():

    tag menu

    use game_menu(_("Sobre o jogo"), scroll="viewport"):

        vbox:
            spacing 14

            text "Caminhos do Cuidado {size=-6}{i}(nome provisório){/i}{/size}" size 24 color "#f0f0f0" bold True
            text "Um jogo sobre acolhimento, direito e empatia." size 16 color "#b8c4ce" italic True

            null height 4

            frame:
                background "#0d1f2dee"
                padding (22, 16)
                xfill True
                has vbox
                spacing 6
                text "Proposta" size 18 color "#3E7CB1" bold True
                text "Sensibilizar e capacitar profissionais de saúde para o cuidado à população em situação de rua (PSR), por meio de histórias interativas baseadas em situações reais de atendimento." size 15 color "#b8c4ce"

            frame:
                background "#0d1f2dee"
                padding (22, 16)
                xfill True
                has vbox
                spacing 6
                text "Como funcionam as missões" size 18 color "#3E7CB1" bold True
                text "Em cada história você troca de perspectiva profissional (recepção, medicina, enfermagem, serviço social) e toma decisões que movem quatro dimensões do cuidado: Direito em Saúde, Conhecimento da Rede, Empatia e Acolhimento. Nenhuma delas aparece durante o jogo — todas são reveladas no epílogo, junto com o mapa da rede." size 15 color "#b8c4ce"
                text "Os pesos das escolhas são provisórios e serão calibrados com profissionais de saúde após os testes." size 13 color "#8899aa" italic True

            frame:
                background "#0d1f2dee"
                padding (22, 16)
                xfill True
                has vbox
                spacing 6
                text "Quem faz" size 18 color "#3E7CB1" bold True
                text "PET-Saúde · Grupo Tutorial 6 — Pop Rua · Universidade Federal da Paraíba (UFPB), em parceria com a rede de saúde do território." size 15 color "#b8c4ce"

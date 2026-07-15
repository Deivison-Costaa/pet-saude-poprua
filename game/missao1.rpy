## missao1.rpy — DIA 1: "ELE NÃO PARECE MORADOR DE RUA"
## Eixo: quem é essa população (afetividade) — desconstrução do estereótipo
## Fonte: ROTEIRO-VISUAL-NOVEL.docx (cenas 0–7) — texto fiel ao documento.
## Pesos provisórios: ▲=+5 · ▲▲=+10 · ▲▲▲=+15 (negativos equivalentes).

init python:
    def ajustar(varname, delta):
        """Ajusta um medidor global, mantendo-o na faixa 0–100."""
        atual = getattr(store, varname)
        setattr(store, varname, max(0, min(100, atual + delta)))

    def no_acende(nome):
        """Acende um nó no mapa da rede."""
        store.nos_rede[nome] = True


## ═════════════════════════════════════════════════════════════════════════════
## CENA 0 — ABERTURA
## Papel: profissional recém-chegado à UPA (visão geral)
## ═════════════════════════════════════════════════════════════════════════════

label missao1:
    play music "audio/music/ambiente_upa.ogg" fadein 2.0

    scene bg aqua_recepcao with fade
    window show

    centered "{color=#f4f1ea}{b}{size=+16}DIA 1{/size}{/b}\n\n{size=+6}“Ele não parece morador de rua”{/size}{/color}"

    narr "{b}Seu papel:{/b} profissional recém-chegado à UPA."

    show renato hesitante at right with dissolve

    narr "É seu primeiro dia na UPA. O pronto-socorro está lotado. Renato chegou há pouco com dor no peito e falta de ar — passou pela Classificação de Risco Clínica e recebeu a cor {b}amarela{/b}: deve ser atendido com prioridade pelo quadro, não pela condição de moradia."

    show esus at overlay_esus with dissolve
    narr "Você abre o prontuário no e-SUS e o sistema puxa um cadastro antigo: um endereço de um bairro do outro lado da cidade, registrado há mais de uma década. A recepção apenas confirmou que o cadastro existe — ninguém atualizou nada."
    narr "No campo de observações da triagem, a técnica anotou em letra apertada: {i}“paciente relata situação de rua há alguns meses”{/i}."
    hide esus with dissolve

    narr "Você olha para a sala de espera. Renato está de cabeça baixa, roupa simples mas limpa, segurando um caderno velho. Ele não se parece com o que você imaginava."
    narr "E, justamente por isso, outros pacientes e até funcionários começam a olhar de um jeito diferente — não por desprezo à condição de rua, mas porque ele não “parece” dessa condição. E isso, em alguns olhares, vira suspeita de outra coisa."
    narr "Esta UPA opera 24 horas e tem Serviço Social com fluxo direto para a equipe do {b}Consultório na Rua{/b} de plantão noturno — o agente comunitário desta noite é {b}Marcos{/b} (ramal 4127), conhecido por andar com um caderno parecido com o de Renato. Você ainda não falou com ele. Pode acionar."

    jump m1_cena1


## ═════════════════════════════════════════════════════════════════════════════
## CENA 1 — MOMENTO DE DECISÃO 0 — "Ele não deveria estar aqui"
## Papel: Recepcionista da UPA
## ═════════════════════════════════════════════════════════════════════════════

label m1_cena1:
    scene bg aqua_espera with dissolve
    narr "{b}Seu papel agora:{/b} Recepcionista da UPA — a primeira pessoa do serviço a perceber o que acontece na sala de espera."

    show renato hesitante at right with dissolve
    show senhora at left_np(0.31) with dissolve

    narr "Você está na recepção registrando outro paciente quando começam os murmúrios na sala de espera. Uma senhora, três cadeiras à frente de Renato, vira para o marido e fala num tom que ela acha discreto, mas não é:"

    senhora_c "Esse homem aí, olha só, tá bem vestido, tá limpo, deve ter plano de saúde. Por que ele tá usando o SUS? Tá tirando lugar de quem precisa."

    hide senhora with dissolve
    show outro_paciente at left_np(0.33) with dissolve

    outro_pac "Se tivesse condição de pagar plano, eu não estaria aqui esperando. Vem gente aqui que não precisa."

    hide outro_paciente with dissolve

    narr "Renato escuta tudo. Aperta o caderno mais forte no colo. Não diz nada."
    narr "Você sabe — porque a anotação da triagem está aberta na sua tela — que ele está em situação de rua há alguns meses. Os outros não sabem."
    narr "O direito ao SUS, universal por princípio constitucional, está sendo questionado em voz alta na sua sala de espera. Você tem alguns segundos para decidir."

    menu:
        narr "Como você age?"

        "Fingir que não ouviu e chamar Renato discretamente ao balcão, sob justificativa administrativa.":
            $ escolha_c1 = "A"
            recep "Renato? Preciso confirmar uma informação no seu cadastro, vem aqui um instante."
            $ ajustar("acolhimento", 5)
            $ ajustar("empatia", -10)
            narr "Você protegeu Renato individualmente — gesto bem-intencionado. Mas a sala de espera continua sendo um lugar onde aquilo pode ser dito sem que ninguém nomeie que é errado."
            narr "Proteger sem educar o espaço é cuidado incompleto: o silêncio diante do estigma público é uma forma de concordância."

        "Levantar a voz da recepção e responder à senhora na frente de todos.":
            $ escolha_c1 = "B"
            recep "Minha senhora, aqui ninguém pergunta se a pessoa tem plano ou não. O SUS é universal e atende todo mundo, ponto final."
            $ ajustar("direito", 10)
            $ ajustar("empatia", 5)
            $ ajustar("acolhimento", -10)
            narr "A intenção é correta — você defendeu o princípio publicamente. Mas a forma transformou Renato em evento público da sala: agora todos olham para ele tentando entender por que foi defendido."
            narr "Defender o direito sem expor a pessoa que ele protege é o desafio do cuidado humanizado."

        "Atravessar a sala com calma, falar firme com a senhora sem alarde — e depois oferecer uma água a Renato.":
            $ escolha_c1 = "C"
            show senhora at left_np(0.31) with dissolve
            recep "Senhora, todo mundo aqui passou pela classificação clínica e foi chamado pela urgência do quadro, não pela aparência. O SUS atende qualquer pessoa, e ninguém aqui tá tirando lugar de ninguém."
            hide senhora with dissolve
            recep "Você vai ser chamado em breve. Aceita uma água?"
            $ ajustar("direito", 10)
            $ ajustar("empatia", 15)
            $ ajustar("acolhimento", 10)
            $ ajustar("rede", 5)
            narr "Você nomeou o princípio (universalidade) sem expor o paciente, restaurou a dignidade da cena em vez de criar nova humilhação, e ainda fez um gesto de acolhimento direto a Renato."
            narr "Direito e empatia operados juntos — não como discurso, como prática cotidiana de recepção."

    call reflexao_card("O estigma contra a PSR nem sempre vem da equipe — vem, com frequência, de outros usuários do mesmo serviço. A aparência de Renato inverte o problema: ele passa a ser suspeito de não pertencer ao SUS.", "Defender o direito é técnica, não opinião pessoal — e a forma como se defende decide se a defesa também acolhe.")

    jump m1_cena2


## ═════════════════════════════════════════════════════════════════════════════
## CENA 2 — MOMENTO DE DECISÃO 1 — A primeira impressão
## Papel: Médico
## ═════════════════════════════════════════════════════════════════════════════

label m1_cena2:
    scene bg aqua_consultorio with dissolve
    narr "{b}Seu papel agora:{/b} Médico — quem recebe Renato para a consulta inicial. A pergunta é: que tipo de profissional eu vou ser nos primeiros 30 segundos?"

    show renato hesitante at center with dissolve

    show esus at overlay_esus with dissolve
    narr "Você chama Renato. Ele entra calado e senta. Na sua tela, três informações entram em conflito antes de você falar: o endereço desatualizado do outro lado da cidade, a observação da triagem ({i}“situação de rua há alguns meses”{/i}) e a classificação amarela (urgência cardiovascular)."
    narr "Antes do paciente, o sistema já te entregou uma narrativa — e ela está incompleta."
    hide esus with dissolve

    menu:
        narr "Como você abre o atendimento?"

        "Ir direto ao protocolo clínico, sem rodeios.":
            $ escolha_c2 = "A"
            med "Onde está a dor? Há quanto tempo? Tem histórico cardíaco?"
            $ ajustar("empatia", -5)
            narr "O protocolo se cumpre, mas o paciente fica invisível atrás da queixa. Quando o instrumento chega antes do encontro, o profissional executa, não cuida."
            narr "Você também aceitou passivamente a narrativa enviesada do sistema. Renato responde o mínimo e a consulta vira triagem repetida."

        "Chamar pelo nome e abrir com pergunta aberta, priorizando a queixa cardiovascular.":
            $ escolha_c2 = "B"
            med "Renato, me conta o que está sentindo. Não só a dor — como você está chegando aqui hoje?"
            $ ajustar("acolhimento", 15)
            $ ajustar("empatia", 15)
            $ ajustar("direito", 5)
            show renato aberto at center
            narr "Você ofereceu vínculo antes do instrumento, respeitou a prioridade clínica que o paciente trouxe e abriu espaço sem forçar."
            narr "Renato hesita, respira fundo e começa a falar do peso no peito que “não é só físico”."

        "Ver a observação “situação de rua” e tentar resolver a moradia primeiro.":
            $ escolha_c2 = "C"
            med "O senhor tem onde dormir hoje? Precisa de encaminhamento para abrigo?"
            $ ajustar("empatia", -10)
            $ ajustar("acolhimento", -10)
            narr "Sua intenção foi cuidar da pessoa inteira, mas você reduziu Renato à condição de moradia antes de escutá-lo."
            narr "Ele veio com dor no peito e medo de infarto, e a primeira coisa que ouve é uma pergunta sobre abrigo. Cuidado social antes da escuta clínica vira mais uma forma de estigma — agora bem-intencionado."

    jump m1_sub11


## ▸ Sub-decisão 1.1 — O campo "endereço" no e-SUS

label m1_sub11:
    narr "{b}Sub-decisão — o campo “endereço” no e-SUS.{/b} Papel: profissional clínico responsável pelo preenchimento da ficha."

    show esus at overlay_esus with dissolve
    narr "Renato responde ao cumprimento. Ao preencher a ficha, você chega ao campo “endereço”. Está em branco — ou desatualizado de uma década. Renato desvia o olhar."
    narr "Há três caminhos no sistema, e cada um materializa uma compreensão diferente do que é direito à saúde."

    menu:
        narr "O que você faz no sistema?"

        "Usar a funcionalidade de vulnerabilidade social do e-SUS: registrar como PSR sem endereço fixo.":
            $ escolha_s11 = "A"
            $ ajustar("direito", 10)
            $ ajustar("rede", 10)
            $ ajustar("acolhimento", 5)
            hide esus with dissolve
            show carteira at obj_esq with dissolve
            show cartao at obj_dir with dissolve
            narr "Procedimento correto e preciso. Renato tira uma {b}carteira de trabalho vencida{/b} do bolso — suficiente para iniciar o registro. O {b}Cartão SUS{/b} é garantido mesmo com dados incompletos."
            narr "Você ativou a base normativa, transformou uma barreira potencial em ponte de cuidado e deixou a carteira vencida sinalizada como pendência documental."
            hide carteira
            hide cartao
            with dissolve

        "Deixar o campo em branco e prosseguir sem explicar — “depois alguém atualiza isso”.":
            $ escolha_s11 = "B"
            $ ajustar("rede", -10)
            hide esus with dissolve
            narr "O atendimento acontece, mas o sistema continua não sabendo onde Renato está. Quando ele voltar (se voltar), outro profissional recomeça do zero."

        "Informar que o sistema “exige” o endereço e orientá-lo a regularizar no CRAS antes de ser atendido.":
            $ escolha_s11 = "C"
            $ ajustar("direito", -10)
            $ ajustar("acolhimento", -10)
            $ ajustar("empatia", -10)
            hide esus with dissolve
            narr "Esta é uma {b}barreira ilegal{/b}. A legislação do SUS garante atendimento independente de documentação, e a Portaria GM/MS 940/2011 prevê expressamente o cadastro em vulnerabilidade social com dados incompletos."

    jump m1_sub12


## ▸ Sub-decisão 1.2 — A espera depois do cadastro

label m1_sub12:
    scene bg aqua_espera with dissolve
    show renato hesitante at right with dissolve

    narr "{b}Sub-decisão — a espera depois do cadastro.{/b} Papel: Técnica de Enfermagem responsável pelo fluxo da sala de espera."
    narr "Renato foi classificado (amarela) e encaminhado à sala de espera. Minutos depois, você percebe que ele está inquieto, olhando repetidamente para a porta de saída."
    narr "A espera estimada é de 20 minutos — o momento crítico em que pacientes da PSR frequentemente desistem e vão embora."

    menu:
        narr "Como você age?"

        "Não fazer nada. É a rotina; mexer com um paciente específico pode parecer favorecimento.":
            $ escolha_s12 = "A"
            $ ajustar("empatia", -5)
            narr "Para alguém acostumado a ser ignorado, o silêncio do serviço é lido como dispensa. A neutralidade aparente do “tratamento igual”, em populações que partem de desvantagens diferentes, reproduz a exclusão."
            narr "Renato considera ir embora."

        "Passar por ele propositalmente, avisar que será chamado em breve e oferecer água.":
            $ escolha_s12 = "B"
            tec "Renato, o médico vai te chamar já já. Aceita uma água enquanto espera?"
            $ ajustar("acolhimento", 10)
            $ ajustar("empatia", 10)
            narr "Humanizar a espera é parte do cuidado, não cortesia opcional. Para alguém acostumado a ser invisível, ser informado e ofertado um copo d’água muda o significado da sala de espera."
            narr "Renato para de olhar para a saída."

        "Comunicar à segurança para “ficar de olho” no Renato, porque ele “parece nervoso e pode querer sair”.":
            $ escolha_s12 = "C"
            $ ajustar("acolhimento", -10)
            $ ajustar("empatia", -15)
            $ ajustar("direito", -15)
            narr "Vigilância não é cuidado. Renato percebe."
            narr "Você confirmou, sem perceber, o estigma que ele temia encontrar do outro lado da mesa."

    jump m1_sub13


## ▸ Sub-decisão 1.3 — A passagem para a consulta médica

label m1_sub13:
    scene bg aqua_corredor with dissolve
    show medico at right with dissolve

    narr "{b}Sub-decisão — a passagem para a consulta médica.{/b} Papel: Técnica de Enfermagem fazendo a entrega do paciente ao médico de plantão."
    narr "Chega a hora de Renato ser atendido. O médico de plantão está cansado e olha para a tela com pressa. Você tem cerca de 40 segundos para entregar o caso — e o que enfatizar vai moldar como o médico vai olhar para Renato."

    menu:
        narr "O que você enfatiza nesses 40 segundos?"

        "Passar apenas os dados técnicos, sem mencionar contexto social.":
            $ escolha_s13 = "A"
            tec "Masculino, 54 anos, dor torácica há 3 horas, PA 180/110, FC 98, classificação amarela."
            narr "Você protegeu o paciente da exposição, o que é legítimo, mas removeu informações que podem ser clínicas — situação de rua afeta adesão, rotina de medicação, possibilidade de retorno."
            narr "A separação rígida entre “social” e “clínico” é uma forma de leitura enviesada. O médico vai descobrir tudo de novo (ou não vai descobrir)."

        "Passar os dados técnicos e acrescentar o contexto com naturalidade profissional, sem rótulo.":
            $ escolha_s13 = "B"
            tec "...e ele está em situação de rua há alguns meses, pelo que relatou na triagem; pode ser relevante para pensar a alta."
            $ ajustar("rede", 10)
            $ ajustar("acolhimento", 10)
            $ ajustar("direito", 10)
            narr "Você integrou contexto social ao caso clínico sem transformá-lo em rótulo. O médico recebe o caso completo e pode pensar a conduta desde o início considerando a realidade do paciente."
            narr "É o registro como fio de continuidade, exercido em tempo real entre profissionais."

        "Começar a passagem mencionando “o morador de rua” e depois ir aos dados técnicos.":
            $ escolha_s13 = "C"
            tec "Esse aqui é o morador de rua... masculino, 54 anos, dor torácica..."
            $ ajustar("empatia", -10)
            $ ajustar("acolhimento", -5)
            narr "Apresentar o paciente pela condição de moradia antes do nome ou do quadro organiza toda a leitura seguinte. Você não fez por mal — fez porque é “assim que o serviço fala”."
            narr "E é exatamente isso que o jogo quer tornar visível. O médico vai entrar procurando o problema social, não o cardiovascular."

    call reflexao_card("O acolhimento da PSR começa antes da ficha clínica — nos olhares da sala de espera, na recepção, na linguagem que a equipe usa para descrever o caso entre si. As quatro dimensões não são etapas separadas: são camadas simultâneas que o profissional opera o tempo todo.", "Defender o direito sem expor a pessoa, registrar com contexto sem rotular, escutar sem julgar, esperar sem desistir — gestos pequenos, técnicos, repetidos.")

    jump m1_cena3


## ═════════════════════════════════════════════════════════════════════════════
## CENA 3 — MOMENTO DE DECISÃO 2 — O que a ficha não diz
## Papel: Médico
## ═════════════════════════════════════════════════════════════════════════════

label m1_cena3:
    scene bg aqua_consultorio with dissolve
    narr "{b}Seu papel agora:{/b} Médico — a emergência cardiovascular já foi afastada, mas o atendimento ainda não terminou de verdade."

    show renato hesitante at center with dissolve

    narr "A pressão começou a ceder depois da medicação; o eletrocardiograma não indica infarto agudo. Mesmo assim Renato continua inquieto: respiração curta, mãos fechadas sobre o caderno, olhar preso na parede atrás de você."
    narr "Você percebe um detalhe que não entrou em nenhum campo: Renato parece pedir desculpas por ocupar espaço ali, mesmo depois de atendido."

    renato "Desculpa... não quero atrapalhar."

    menu:
        narr "Como você conduz a conversa daqui em diante?"

        "Continuar pelo protocolo clínico, evitando abrir o tema emocional.":
            $ escolha_c3 = "A"
            med "A dor piora quando faz esforço? Já teve pressão alta antes?"
            $ ajustar("acolhimento", 5)
            $ ajustar("empatia", -5)
            narr "Você não foi negligente nem incorreto — a consulta seguiu como muitas em serviços sobrecarregados. Mas, quando o profissional permanece só no território seguro do protocolo, o paciente aprende que certos sofrimentos não cabem ali."
            narr "Renato sai com a pressão melhor e a sensação de ter deixado parte de si do lado de fora."

        "Investigar o componente emocional de forma direta, mas no ritmo acelerado da consulta.":
            $ escolha_c3 = "B"
            med "Esses sintomas podem ter relação com ansiedade ou estresse. Você já passou por acompanhamento psicológico ou psiquiátrico?"
            renato "Já tomei remédio há um tempo atrás."
            $ ajustar("empatia", 5)
            $ ajustar("acolhimento", -5)
            narr "A intenção foi correta — você percebeu sofrimento além da pressão e tentou nomeá-lo. Mas a forma manteve Renato na posição de quem é avaliado, não escutado."
            narr "Investigar saúde mental sem construir segurança transforma vulnerabilidade em mais um item do interrogatório clínico."

        "Direcionar a conversa para a vulnerabilidade social, antes de consolidar a escuta clínica.":
            $ escolha_c3 = "C"
            med "Você tá conseguindo ficar em abrigo? Tem alguém te ajudando nesse momento?"
            $ ajustar("empatia", -10)
            $ ajustar("acolhimento", -5)
            $ ajustar("direito", -5)
            narr "Sua intenção foi cuidar além do sintoma — mas, ao antecipar o contexto social, Renato sente que o serviço já decidiu quem ele é antes de entender o que ele veio buscar."
            narr "Quando toda vulnerabilidade vira imediatamente “caso social”, a pessoa desaparece atrás da condição de moradia."

    jump m1_sub21


## ▸ Sub-decisão 2.1 — O registro no prontuário e-SUS

label m1_sub21:
    narr "{b}Sub-decisão — o registro no prontuário.{/b} A consulta terminou, mas o cuidado depende do que vai permanecer registrado."

    show esus at overlay_esus with dissolve
    narr "Você abre o campo de evolução no prontuário. Cabem poucas linhas — e elas vão decidir quanto do atendimento continua existindo para o resto da rede."
    narr "A crise foi controlada, mas a consulta revelou o que não aparece em exames: insegurança, sofrimento emocional, dificuldade de continuidade e meses em situação de rua."

    menu:
        narr "Como você documenta o atendimento?"

        "Registrar apenas os dados clínicos imediatos: “Crise hipertensiva. Medicado. Alta com orientações.”":
            $ escolha_s21 = "A"
            $ ajustar("rede", -10)
            narr "Você registrou só o que o protocolo reconhece com facilidade. Quando o contexto desaparece do prontuário, ele também desaparece da continuidade do cuidado."
            narr "Se Renato retornar, o próximo profissional encontrará apenas uma crise hipertensiva isolada — não a trajetória que a produziu."

        "Registrar o quadro clínico e acrescentar, em termos amplos, o sofrimento emocional recente.":
            $ escolha_s21 = "B"
            $ ajustar("rede", 5)
            $ ajustar("empatia", 5)
            narr "A intenção foi correta — você impediu que o sofrimento sumisse do prontuário. Mas registros muito genéricos têm limites: o próximo profissional saberá que há algo além da pressão, mas talvez não compreenda o contexto."
            narr "Continuidade parcial — abre uma porta, mas talvez não oriente o caminho inteiro."

        "Registrar detalhadamente a situação de rua e as observações sobre vulnerabilidade social.":
            $ escolha_s21 = "C"
            $ ajustar("rede", 10)
            $ ajustar("empatia", -5)
            narr "Sua intenção foi fortalecer a continuidade. Mas, quando o registro enfatiza a vulnerabilidade antes da singularidade clínica, Renato pode passar a circular pela rede primeiro como “o paciente em situação de rua” — e só depois como alguém com dor, medo e sofrimento específicos."
            narr "O prontuário deve ampliar o olhar da equipe, não substituir a pessoa por uma categoria."

    hide esus with dissolve
    jump m1_sub22


## ▸ Sub-decisão 2.2 — A prescrição fora do papel

label m1_sub22:
    narr "{b}Sub-decisão — a prescrição fora do papel.{/b} O tratamento precisa sair da lógica do consultório e entrar na rotina real de Renato."

    show receita at obj_dir with dissolve
    narr "Você prepara a receita do anti-hipertensivo: uso contínuo, um comprimido por dia. Parece simples na tela. Mas a eficácia depende de coisas que o protocolo assume como garantidas: horário estável, local seguro para guardar o remédio, alimentação regular, retorno à UBS."
    narr "Renato segura o caderno contra o peito. Você se pergunta não só “o que prescrever?”, mas “o que dessa prescrição cabe na vida dele?”."
    hide receita with dissolve

    menu:
        narr "Como você conduz a orientação do tratamento?"

        "Explicar a prescrição de forma rápida e padronizada, com orientações gerais de retorno.":
            $ escolha_s22 = "A"
            med "Tomar um comprimido por dia, de preferência pela manhã, e evitar esquecer."
            $ ajustar("acolhimento", 5)
            $ ajustar("empatia", -5)
            narr "A prescrição foi tecnicamente correta, mas o protocolo pressupõe uma rotina estável para existir na prática. Sem investigar como o paciente vive fora do consultório, a adesão passa a depender de condições nunca garantidas."
            narr "Renato sai com a receita, mas sem espaço para dizer se conseguirá segui-la."

        "Incluir o sofrimento emocional na explicação, mas mantendo o ritmo acelerado.":
            $ escolha_s22 = "B"
            med "A pressão melhorou, mas às vezes estresse e ansiedade também dificultam o controle. Você já fez algum acompanhamento?"
            renato "Já tomei uns remédios um tempo atrás."
            $ ajustar("empatia", 5)
            $ ajustar("acolhimento", -5)
            narr "A intenção foi correta — você percebeu que o tratamento não dependia só do comprimido. Mas a conversa seguiu no ritmo do protocolo, não no tempo da escuta."
            narr "Saúde mental como complemento rápido sinaliza que o tema pode ser mencionado, mas não aprofundado. Você abriu uma porta; Renato ainda não sentiu segurança para atravessá-la."

        "Fazer da realidade social o centro da orientação ao entregar a receita.":
            $ escolha_s22 = "C"
            med "Você tá conseguindo ficar em abrigo? Tem algum lugar seguro pra guardar os remédios?"
            renato "Às vezes sim, às vezes não."
            $ ajustar("empatia", -5)
            $ ajustar("acolhimento", -5)
            narr "Adaptar a prescrição à realidade concreta faz parte do cuidado. Mas, quando a vulnerabilidade organiza imediatamente toda a orientação, Renato sente que o serviço já espera menos dele como paciente."
            narr "Reduzir a conversa às limitações vira gestão de vulnerabilidade, não construção compartilhada de autonomia."

    call reflexao_card("Adaptar o cuidado à realidade do paciente é diferente de reduzir o paciente à própria vulnerabilidade. Quando o contexto social ocupa sozinho o centro da consulta, o risco é que a pessoa desapareça atrás da categoria “caso social”.", "O desafio é equilibrar clínica, escuta e contexto sem transformar nenhuma delas na única forma de enxergar quem está sendo atendido.")

    jump m1_cena4


## ═════════════════════════════════════════════════════════════════════════════
## CENA 4 — MOMENTO DE DECISÃO 3 — O intervalo que não é vazio
## Papel: Enfermeiro(a)
## ═════════════════════════════════════════════════════════════════════════════

label m1_cena4:
    scene bg aqua_box with dissolve
    narr "{b}Seu papel agora:{/b} Enfermeiro(a) — responsável pela observação clínica no box de estabilização."

    show renato hesitante at center with dissolve

    narr "Renato tomou a primeira dose do anti-hipertensivo. O monitor multiparâmetro marca {b}PA 168/104, FC 92{/b} — ainda alta, mas cedendo. O protocolo pede ao menos 30 minutos de observação antes de pensar em alta."
    narr "Você tem outros pacientes esperando — mas esta sala também é onde o cuidado se decide."

    menu:
        narr "Como você usa esse intervalo?"

        "Sair da sala e voltar quando o alarme disparar ou a equipe chamar.":
            $ escolha_c4 = "A"
            $ ajustar("acolhimento", -5)
            $ ajustar("empatia", -5)
            narr "O monitor cumpre a função técnica e ninguém deixou de fazer o mínimo. Mas, para alguém que já se sente invisível, ser deixado sozinho com os aparelhos confirma que o cuidado terminou quando a medicação foi administrada."
            narr "A observação virou vigilância eletrônica, não presença profissional."

        "Avisar que volta em 15 minutos, alinhar com a equipe e começar o registro com a história fresca.":
            $ escolha_c4 = "B"
            $ ajustar("rede", 10)
            $ ajustar("acolhimento", 10)
            narr "Você tratou o intervalo como tempo clínico, não como pausa. O alinhamento com a equipe garantiu que a informação não dependa só da sua memória."
            narr "Você retorna com a evolução rascunhada e a equipe ciente do caso. A observação não é desperdício — é onde o cuidado se consolida."

        "Delegar integralmente a observação à enfermagem (“me chama se mudar alguma coisa”).":
            $ escolha_c4 = "C"
            $ ajustar("acolhimento", -10)
            $ ajustar("empatia", -5)
            narr "Delegar não é errado — delegar sem contexto é transferir responsabilidade sem transferir cuidado. A enfermagem monitora os sinais, mas não sabe da insônia, dos bilhetes para os filhos no caderno, do possível componente emocional da pressão."
            narr "Quando você voltar, o caso recomeça pela tela do monitor, não pela história da pessoa."

    jump m1_sub31


## ▸ Sub-decisão 3.1 — A reavaliação clínica

label m1_sub31:
    narr "{b}Sub-decisão — a reavaliação clínica.{/b} Papel: Médico(a) — responsável pela reavaliação antes da decisão de alta."
    narr "35 minutos depois. {b}PA 148/92, FC 84{/b}. Renato está mais corado, respiração tranquila, refere alívio. Clinicamente, cumpre os critérios de alta."
    narr "Mas alta segura não é só pressão controlada — é também ler o que vai acontecer quando ele atravessar a porta."

    menu:
        narr "Como você conduz a reavaliação?"

        "Conferir os sinais vitais, perguntar “tá melhor?” e marcar “estável para alta”.":
            $ escolha_s31 = "A"
            med "Tá melhor?"
            narr "Você confirmou o que o monitor já dizia — e perdeu a chance de captar sinais de alerta que só aparecem quando o paciente fala."
            narr "A reavaliação foi um carimbo, não uma escuta."

        "Sentar ao lado, refazer o exame e perguntar de forma aberta.":
            $ escolha_s31 = "B"
            med "Como tá agora — não só a dor, mas a cabeça, a respiração, o sono?"
            show renato aberto at center
            renato "A dor no peito sumiu... mas o coração acelera quando eu penso em sair daqui."
            $ ajustar("acolhimento", 15)
            $ ajustar("empatia", 10)
            $ renato_medo_alta = True
            narr "A reavaliação capturou um dado que nenhum aparelho mede: Renato tem {b}medo da alta{/b}. Esse dado vai mudar como você conduz os próximos momentos."
            narr "Reavaliar com presença é diferente de reconferir com pressa."

        "Manter Renato em observação por mais 1 hora “por garantia”, sem reavaliar de fato.":
            $ escolha_s31 = "C"
            $ ajustar("acolhimento", -10)
            $ ajustar("direito", -5)
            narr "Mais tempo no box sem reavaliação real é só mais espera para Renato — e atrasa os outros da fila. Cautela sem ação clínica é deslocamento do trabalho, não proteção."
            narr "Renato continua sem saber por que ainda está ali, reforçando que o serviço decide sobre ele, não com ele."

    jump m1_sub32


## ▸ Sub-decisão 3.2 — O prontuário antes da alta

label m1_sub32:
    narr "{b}Sub-decisão — o prontuário antes da alta.{/b} Papel: profissional clínico responsável pela evolução no prontuário eletrônico."

    show esus at overlay_esus with dissolve
    narr "Antes de chamar Renato para a conversa de alta, você abre a evolução no e-SUS. O que se registra agora é o que a UBS de referência, o Consultório na Rua e qualquer profissional que cruzar com Renato vão ler depois."
    narr "O registro é o fio que conecta este atendimento ao próximo — ou que se rompe na porta da UPA."

    menu:
        narr "Como você registra?"

        "Registrar em texto livre, sem codificação nem campo de vulnerabilidade.":
            $ escolha_s32 = "A"
            $ ajustar("rede", -10)
            narr "A informação está lá, mas não circula. A busca ativa do CNR não vai puxar o caso e a UBS não vai filtrar Renato como prioridade."
            narr "Texto livre é como uma carta que nunca chega — existe, mas não alcança quem precisa lê-la."

        "Estruturar com CIAP-2, campo de vulnerabilidade social e sinalização de busca ativa pelo CNR.":
            $ escolha_s32 = "B"
            $ ajustar("rede", 15)
            $ ajustar("direito", 10)
            $ no_acende("UBS de referência")
            narr "O e-SUS agora lista Renato automaticamente na próxima exportação para o CNR e para a UBS de referência. O registro virou ponte, não papel."
            narr "Cada campo preenchido foi uma decisão consciente sobre continuidade."

        "Registrar o quadro clínico, mas omitir o conteúdo emocional “para não expor o paciente”.":
            $ escolha_s32 = "C"
            $ ajustar("rede", 5)
            $ ajustar("empatia", -5)
            narr "A intenção de proteger é legítima, mas a omissão guarda uma intimidade que Renato confiou para que o cuidado seguisse, não para que sumisse no próximo turno."
            narr "Sigilo não é apagar — é registrar com cuidado em campo apropriado. O próximo saberá da hipertensão, mas não entenderá por que ela aconteceu."

    hide esus with dissolve

    call reflexao_card("O intervalo de observação parece tempo morto, mas é o exato lugar onde a alta se constrói. Reavaliar é diferente de reconferir; registrar é diferente de digitar.", "Quando esses dois movimentos acontecem com presença, a alta deixa de ser ato administrativo e passa a ser o início da continuidade do cuidado.")

    jump m1_cena5


## ═════════════════════════════════════════════════════════════════════════════
## CENA 5 — MOMENTO DE DECISÃO 4 — A alta que começa antes da porta
## Papel: Médico(a)
## ═════════════════════════════════════════════════════════════════════════════

label m1_cena5:
    scene bg aqua_box with dissolve
    narr "{b}Seu papel agora:{/b} Médico(a) — responsável pela alta e pela articulação inicial com a rede de cuidado."

    show renato normal at center with dissolve

    narr "Renato melhorou. Você precisa dar a alta. Ele vai precisar de anti-hipertensivo contínuo e acompanhamento de saúde mental."
    narr "O endereço no sistema continua o de uma década atrás — a recepção não atualiza esse campo, e não é função sua corrigi-lo na UPA."
    narr "Mas o que você faz agora define se a rede vai existir para Renato ou se ele sai apenas com um papel na mão."

    if renato_medo_alta:
        narr "Você se lembra do que ele disse na reavaliação: {i}“o coração acelera quando eu penso em sair daqui”{/i}. A alta, para Renato, não é alívio — é ameaça."

    menu:
        narr "Como você conduz a alta?"

        "Prescrever, explicar a posologia e liberar.":
            $ escolha_c5 = "A"
            $ ajustar("direito", -10)
            $ ajustar("acolhimento", -10)
            narr "A prescrição foi correta — mas uma receita sem caminho é um papel. Renato sai com orientações que pressupõem farmácia acessível, endereço que funcione e retorno por iniciativa própria."
            narr "Para quem vive na rua, cada uma é uma barreira concreta. A alta que não articula rede é alta que abandona."

        "Prescrever, registrar a situação de rua e perguntar sobre o acesso ao remédio — sem acionar a rede.":
            $ escolha_c5 = "B"
            med "Você consegue comprar esse remédio? Tem acesso a alguma farmácia do SUS?"
            renato "Não tenho Cartão SUS ativo."
            $ ajustar("rede", 5)
            $ ajustar("empatia", 5)
            $ ajustar("acolhimento", 5)
            narr "Você identificou a barreira — mais do que muitos atendimentos alcançam. Mas identificar sem acionar deixa o problema nomeado e sem solução."
            narr "A farmácia da UPA aparece como possibilidade e o registro garante o histórico; falta o passo que conecta a informação ao movimento concreto."

        "Fazer o fluxo completo: registro codificado, Serviço Social, ponte com o CNR, medicação na farmácia da UPA e plano construído com Renato.":
            $ escolha_c5 = "C"
            $ ajustar("direito", 10)
            $ ajustar("rede", 10)
            $ ajustar("acolhimento", 10)
            $ ajustar("empatia", 10)
            $ no_acende("Serviço Social")
            $ no_acende("Farmácia da UPA")
            narr "Você transformou a alta num ato de articulação, não de encerramento. Cada serviço acionado é um nó que acende na rede — e cada nó aceso reduz a chance de Renato sumir depois da porta."
            narr "A dispensação garante que ele saia já medicado; o Serviço Social faz a ponte que o prontuário sozinho não faz. A alta deixou de ser ponto final e virou vírgula."

    jump m1_sub41


## ▸ Sub-decisão 4.1 — Comunicando os próximos passos

label m1_sub41:
    narr "{b}Sub-decisão — comunicando os próximos passos.{/b} Papel: profissional responsável pela orientação de alta."
    narr "O plano de alta está definido. Renato está sentado na cama, caderno no colo, esperando. Você tem alguns minutos antes do próximo paciente."

    menu:
        narr "Como você comunica o que vem depois?"

        "Explicar rapidamente os próximos passos, em pé, enquanto organiza a ficha para sair.":
            $ escolha_s41 = "A"
            $ ajustar("empatia", -5)
            narr "Comunicar em pé, com pressa, comunica que o momento não é importante. Sem confirmar o que foi entendido, detalhes como o endereço do CNR e os dias de atendimento se perdem."
            narr "Não por falha de Renato — mas porque a forma apressada não garantiu que a orientação chegasse."

        "Sentar ao lado e entregar o plano em partes, confirmando cada passo e perguntando sobre barreiras.":
            $ escolha_s41 = "B"
            prof "O que pode dificultar você chegar lá?"
            prof "A assistente social vai te ajudar com documentação, abrigo e a ponte com o Consultório na Rua."
            $ ajustar("acolhimento", 15)
            $ ajustar("empatia", 10)
            $ ajustar("direito", 5)
            narr "Você não apenas informou — perguntou sobre as barreiras. Essa inversão muda o significado do plano: de imposto para construído."
            narr "Renato sabe o que fazer e sente que alguém se importou com o que vem depois. A pergunta sobre dificuldades é, ela mesma, uma forma de cuidado."

        "Delegar o encerramento à assistente social e sair antes de terminar a conversa.":
            $ escolha_s41 = "C"
            $ ajustar("acolhimento", -10)
            $ ajustar("empatia", -5)
            narr "A assistente social vai conduzir bem — mas quem começou o atendimento não terminou. Para Renato, isso confirma um padrão: as pessoas entram na vida dele e saem quando aparece algo mais urgente."
            narr "Às vezes, os últimos dois minutos são os mais importantes do atendimento."

    jump m1_sub42


## ▸ Sub-decisão 4.2 — A passagem para o Serviço Social

label m1_sub42:
    show assistente at left with dissolve

    narr "{b}Sub-decisão — a passagem para o Serviço Social.{/b} Você acionou o Serviço Social. A assistente social aparece na porta com expressão de sobrecarga."

    assist "Posso te ajudar em 5 minutos — tem uma fila hoje."

    menu:
        narr "Como você conduz a passagem?"

        "Agradecer e deixar que ela conduza como puder no tempo que tem.":
            $ escolha_s42 = "A"
            $ ajustar("rede", 5)
            $ no_acende("Serviço Social")
            narr "A assistente social fez o possível — mas sem o contexto do atendimento, os 5 minutos viraram um encaminhamento genérico."
            narr "O papel do CRAS, sem explicação de como chegar, a quem procurar e em que horário, é mais um papel na mochila de Renato."

        "Fazer uma rápida apresentação de Renato — contexto, o que foi observado, o que foi combinado.":
            $ escolha_s42 = "B"
            $ ajustar("rede", 10)
            $ ajustar("acolhimento", 10)
            $ ajustar("direito", 5)
            $ no_acende("Serviço Social")
            narr "A assistente social vai direto ao ponto, porque alguém fez a ponte entre os saberes. Cinco minutos bem preparados valem mais que trinta do zero."
            narr "A passagem de caso entre profissionais é, ela mesma, uma forma de cuidado — e sua qualidade decide se o próximo elo vai funcionar ou apenas existir."

        "Pedir para a assistente social remarcar para outro dia — Renato “pode voltar para conversar com ela”.":
            $ escolha_s42 = "C"
            $ ajustar("rede", -10)
            $ ajustar("acolhimento", -10)
            $ ajustar("direito", -5)
            narr "“Pode voltar” é o tipo de encaminhamento que raramente se concretiza para a PSR. Sem data, sem nome, sem compromisso, é uma porta que parece aberta mas que ninguém segura."
            narr "Remarcar é, muitas vezes, desmarcar sem assumir."

    call reflexao_card("A alta segura não se constrói só com pressão controlada e receita na mão. Ela exige que o profissional se pergunte: “o que vai acontecer com essa pessoa depois que ela cruzar a porta?”", "Quando essa pergunta organiza a conduta, a alta deixa de ser encerramento e passa a ser início.")

    jump m1_cena6


## ═════════════════════════════════════════════════════════════════════════════
## CENA 6 — MOMENTO DE DECISÃO 5 — A rede que se constrói com nome e voz
## Papel: equipe multiprofissional (+ Renato como participante ativo)
## ═════════════════════════════════════════════════════════════════════════════

label m1_cena6:
    scene bg aqua_box with dissolve
    show renato normal at center
    show assistente at left
    with dissolve

    narr "{b}Agora é a equipe:{/b} você, a assistente social — e Renato, como participante ativo."
    narr "Com o plano de alta definido, a assistente social lembra que ainda é preciso fechar quem do CNR vai fazer a busca ativa. Marcos, agente comunitário de plantão noturno, está em ronda no território — ramal 4127, atende o telefone do plantão pela enfermagem."
    narr "Renato está sentado na cama, atento, ouvindo."

    menu:
        narr "Como você conduz a articulação com o Consultório na Rua?"

        "Pedir que a assistente social ligue depois para o CNR — você precisa atender o próximo paciente.":
            $ escolha_c6 = "A"
            $ ajustar("rede", 5)
            narr "O acionamento aconteceu — mas à distância, sem voz, sem nome, sem horário. O CNR vira caixa-preta institucional: foi acionada, mas ninguém sabe se vai funcionar."
            narr "Para Renato, “vão entrar em contato” soa como todas as promessas que não se cumpriram."

        "Ligar você mesmo, no viva-voz, e apresentar o caso a Marcos em linguagem técnica.":
            $ escolha_c6 = "B"
            prof "PSR masculino, 54 anos, crise hipertensiva com componente ansioso, depressão prévia, busca ativa para vinculação à UBS de referência."
            $ ajustar("rede", 10)
            $ ajustar("empatia", -10)
            $ ajustar("acolhimento", -5)
            $ no_acende("CNR (Marcos)")
            show renato hesitante at center
            narr "A articulação foi feita com qualidade institucional — Marcos recebeu informações suficientes para agir. Mas Renato ouviu a si mesmo virar “PSR masculino, 54 anos” na frente dele."
            narr "O vínculo já nasce contaminado: ele foi apresentado como demanda, não como pessoa. A linguagem técnica é necessária entre profissionais — mas, na presença do paciente, precisa ser mediada."

        "Ligar, apresentar o contexto — e, em vez de falar sobre Renato, falar com ele: incluí-lo na conversa.":
            $ escolha_c6 = "C"
            marcos "Renato, onde você costuma passar a noite?"
            show renato aberto at center
            renato "Tenho ficado num abrigo nas últimas semanas... e de tarde costumo ficar no coreto da praça do bairro."
            marcos "Então combinamos: sexta-feira, 16h, no coreto. Eu vou estar lá."
            $ ajustar("rede", 15)
            $ ajustar("acolhimento", 10)
            $ ajustar("empatia", 10)
            $ ajustar("direito", 10)
            $ no_acende("CNR (Marcos)")
            $ no_acende("UBS de referência")
            narr "Renato vai ao encontro na sexta porque alguém chamado {b}Marcos{/b} vai estar lá — não porque “a equipe do CNR vai passar”. A rede se ativou com nome, voz e ponto combinado."
            narr "Incluir Renato na conversa fez o que nenhum encaminhamento por escrito consegue: transformou-o de objeto do cuidado em participante do próprio plano. A busca ativa começa aqui — com um acordo entre duas pessoas."
            show caderno at obj_dir with dissolve
            narr "Renato anota o nome de Marcos no caderno."
            hide caderno with dissolve

    jump m1_sub51


## ▸ Sub-decisão 5.1 — A carteira vencida e a cidadania

label m1_sub51:
    narr "{b}Sub-decisão — a carteira vencida e a cidadania.{/b} Papel: Assistente Social + profissional clínico — decisão compartilhada sobre o que está além da ficha clínica."

    show carteira at obj_dir with dissolve
    narr "Você se lembra da carteira de trabalho vencida que Renato tirou do bolso na recepção. É a única identificação ativa que ele tem, e o registro civil está fragmentado — sem CPF regularizado, sem RG recente."
    narr "Sem isso, o Cartão SUS pleno não se completa, e o acesso a transferência de renda ou abrigamento de longa permanência fica travado."
    hide carteira with dissolve
    narr "A assistente social ainda está na sala. Você tem 2 minutos antes do próximo paciente."

    menu:
        narr "O que você faz com a questão documental?"

        "Tratar como fora do escopo — “documento não é problema da saúde”.":
            $ escolha_s51 = "A"
            prof "Documento não é problema da saúde. Foco no que é meu."
            $ ajustar("direito", -10)
            $ ajustar("empatia", -5)
            narr "A frase “não é problema da saúde” define uma fronteira que parece profissional, mas abandona a pessoa na lacuna entre serviços."
            narr "A saúde não precisa resolver a documentação — mas precisa reconhecer que, sem ela, o cuidado recém-construído não se sustenta."

        "Entregar o folheto do CRAS e orientar verbalmente.":
            $ escolha_s51 = "B"
            prof "Procura o CRAS do bairro, eles te ajudam com a documentação."
            $ ajustar("rede", 5)
            $ no_acende("CRAS")
            narr "A orientação é correta, mas genérica. Para a PSR, um folheto sem nome de referência, sem data e sem ponte construída é papel — não caminho."
            narr "A diferença entre informação e acesso está na ponte que o profissional constrói (ou não)."

        "Registrar a pendência, pedir ofício curto à Defensoria Pública e obter a anuência de Renato por digital.":
            $ escolha_s51 = "C"
            $ ajustar("direito", 10)
            $ ajustar("rede", 10)
            $ ajustar("acolhimento", 10)
            $ ajustar("empatia", 10)
            $ no_acende("CRAS")
            $ no_acende("Defensoria Pública")
            narr "A saúde reconheceu que a pessoa inteira não cabe só na ficha clínica. O ofício à Defensoria é um gesto de 2 minutos que pode mudar meses de travamento burocrático."
            narr "O registro garante que o próximo profissional saiba que a documentação é parte do plano, e a anuência por digital respeita a autonomia de Renato — ele não foi inscrito em nada sem saber."
            narr "Marcos leva a cópia do encaminhamento do CRAS na visita de sexta."

    call reflexao_card("Ativar a rede com nome, voz e ponto combinado é diferente de acionar uma caixa-preta à distância. Incluir o paciente na construção do próprio plano não é cortesia — é princípio da Política Nacional de Humanização.", "Reconhecer que a documentação é parte do cuidado em saúde é o gesto que separa o atendimento da pessoa inteira do atendimento do sintoma isolado.")

    jump m1_cena7


## ═════════════════════════════════════════════════════════════════════════════
## CENA 7 — MOMENTO DE DECISÃO 6 — A despedida que fica
## Papel: o profissional que estiver presente na porta
## ═════════════════════════════════════════════════════════════════════════════

label m1_cena7:
    scene bg aqua_saida with dissolve
    narr "{b}Seu papel agora:{/b} o profissional que estiver na porta — qualquer membro da equipe que conduziu o atendimento."

    show renato despedida at center with dissolve

    narr "Renato pega suas coisas para ir embora. Na porta, ele para. Vira para você com o caderno na mão."

    renato "E se eu não conseguir encontrar o Marcos na sexta?"

    narr "Ele não está falando de transporte. Está falando de {b}medo{/b} — de não acreditar que vai dar certo."

    menu:
        narr "Como você responde?"

        "Explicar que o Consultório na Rua atende em outros dias também.":
            $ escolha_c7 = "A"
            prof "O Consultório na Rua atende em outros dias também. É só tentar."
            $ ajustar("acolhimento", -5)
            narr "A informação está correta — mas não respondeu o que Renato realmente perguntava. Ele não queria saber o horário; queria saber se alguém acredita que ele é capaz de dar o próximo passo."
            narr "Responder logística a uma pergunta sobre confiança é perder o momento em que o vínculo se consolidaria."

        "Parar, olhar para ele e reconhecer o que ele já fez — sem prometer resultado.":
            $ escolha_c7 = "B"
            prof "Renato, você chegou aqui hoje com dor no peito, sozinho. Isso já foi difícil. O próximo passo não precisa ser perfeito — só precisa existir."
            $ ajustar("acolhimento", 15)
            $ ajustar("empatia", 15)
            $ ajustar("direito", 5)
            show renato emocionado at center
            narr "É o tipo de frase que não está em nenhum protocolo — e que às vezes muda uma trajetória. Você não prometeu resultado; reconheceu esforço. Não deu orientação; devolveu dignidade."
            narr "A despedida que nomeia o que o paciente já fez diz a ele que alguém viu quem ele é — não só o que ele precisa."

        "Dizer que entende, mas que o importante é tentar — “a gente torce por você”.":
            $ escolha_c7 = "C"
            prof "Entendo. Mas o importante é tentar. A gente torce por você."
            $ ajustar("acolhimento", 5)
            narr "A intenção é boa, mas “a gente torce” soa distante — uma despedida educada que não cria compromisso. Torcer é o que se faz por quem está longe; cuidar é o que se faz por quem está na frente."
            narr "Renato sente que o serviço foi gentil — mas gentileza sem vínculo é cortesia, não cuidado."

    call reflexao_card("A despedida não está em nenhum fluxograma e não aparece em nenhum indicador de desempenho.", "Mas é o último registro que o paciente leva do serviço — e, para alguém que aprendeu a esperar rejeição, pode ser o primeiro motivo para voltar.")

    narr "Renato ajeita o caderno debaixo do braço e atravessa a porta. O entardecer alonga a sombra dele na calçada."

    stop music fadeout 3.0
    jump epilogo

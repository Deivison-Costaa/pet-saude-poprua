## missao1.rpy — Missão 1: "Ele não parece morador de rua"
## GT6 – Pop Rua | Frente TI | PET-Saúde
##
## Paciente: Renato, 54 anos.
## Eixo temático: Quem é essa população (afetividade)

init python:
    def ajustar(varname, delta):
        """Ajusta medidor dentro do intervalo 0-100."""
        val = getattr(renpy.store, varname, 0)
        setattr(renpy.store, varname, max(0, min(100, val + delta)))


## ─────────────────────────────────────────────────────────────────────────────
## ENTRADA
## ─────────────────────────────────────────────────────────────────────────────

label missao1:
    play music "audio/music/ambiente_upa.ogg" fadein 2.0
    jump m1_abertura


## ─────────────────────────────────────────────────────────────────────────────
## ABERTURA — A chegada de Renato
## ─────────────────────────────────────────────────────────────────────────────

label m1_abertura:
    scene bg upa_recepcao with fade

    narr "É seu primeiro dia na UPA. O pronto-socorro está lotado."
    narr "Renato chegou há pouco com dor no peito e falta de ar. Passou pela Classificação de Risco Clínica e recebeu cor {b}amarela{/b} — deve ser atendido pelo quadro clínico, não pela condição de moradia."
    narr "Você abre o prontuário no e-SUS. Um cadastro antigo registra um endereço de outro bairro, de mais de uma década atrás. No campo de observações da triagem, a técnica anotou em letra apertada:"
    narr "{i}\"Paciente relata situação de rua há alguns meses.\"{/i}"
    narr "Você olha para a sala de espera."

    show renato normal at center with dissolve

    narr "Renato está sentado no canto, de cabeça baixa, com roupa simples mas limpa, segurando um caderno velho."
    narr "Ele não se parece com o que você imaginava."

    jump m1_momento1


## ─────────────────────────────────────────────────────────────────────────────
## MOMENTO 1 — "A primeira impressão"
## ─────────────────────────────────────────────────────────────────────────────

label m1_momento1:
    show renato normal at center
    show tecnica at right with dissolve

    tec "Renato? Pode vir."

    narr "Ele entra calado. Senta. Endereço desatualizado no sistema, observação da triagem à vista. Como você abre o atendimento?"

    menu:

        "Protocolo clínico — {i}\"Onde está a dor? Há quanto tempo? Tem histórico cardíaco?\"{/i}":
            $ ajustar("saude", 5)
            $ escolha_m1 = "A"
            narr "Você vai direto ao protocolo. Renato lê a pressa e responde o mínimo — pressão alta, dor no peito há três horas. Mantém o caderno fechado."
            jump m1_sub11

        "Pausa e pergunta aberta — {i}\"Renato, me conta o que está sentindo. Não só a dor — como você está?\"{/i}":
            $ ajustar("confianca", 15)
            $ escolha_m1 = "B"
            show renato aberto with dissolve
            renato "Eu... tô com uma dor aqui. {i}(aponta para o peito){/i} E uma falta de ar que não passa."
            narr "Ele hesita, respira fundo."
            renato "Na verdade... não tô dormindo direito. Faz semanas. Tem um peso aqui que não é só físico."
            jump m1_sub11

        "Pergunta sobre moradia — {i}\"Você tem onde dormir hoje? Precisa de encaminhamento para abrigo?\"{/i}":
            $ ajustar("confianca", -15)
            $ ajustar("estigma", 10)
            $ escolha_m1 = "C"
            show renato hesitante with dissolve
            renato "Eu vim com dor no peito."
            narr "Renato se fecha. Veio com medo de infarto, não pedindo abrigo. A pergunta chegou antes do olhar."
            jump m1_sub11


## Sub-decisão 1.1 — O campo endereço no e-SUS

label m1_sub11:
    narr "O campo de endereço no e-SUS está desatualizado — o sistema pede atualização. Renato apresenta uma carteira de trabalho vencida como único documento."

    menu:

        "Usar o campo de vulnerabilidade social do e-SUS; aceitar o documento que ele tem":
            $ ajustar("acesso", 15)
            tec "Tudo certo. O sistema aceita outros documentos para quem está em situação de rua."
            narr "A situação de rua é registrada no campo correto. O atendimento avança sem barreira."
            jump m1_sub12

        "Deixar o campo em branco por enquanto — resolver depois":
            narr "O registro fica fragmentado. O próximo profissional começa sem saber que Renato esteve aqui."
            jump m1_sub12

        "Exigir endereço atualizado — {i}\"Precisa regularizar no CRAS antes de continuar\"{/i}":
            $ ajustar("acesso", -20)
            $ ajustar("confianca", -10)
            $ ajustar("estigma", 10)
            show renato hesitante with dissolve
            narr "Renato olha para você sem entender."
            narr "{b}O SUS garante atendimento independente de documentação.{/b} Essa exigência é uma barreira ilegal."
            jump m1_sub12


## Sub-decisão 1.2 — Classificação de risco

label m1_sub12:
    tec "PA 180/110. FC 98. Sudorese leve e palidez."

    narr "Os sinais vitais estão alterados. A Classificação de Risco pelo Protocolo de Manchester prioriza pelo {b}quadro clínico{/b}, não pela condição social."

    menu:

        "{b}LARANJA{/b} — urgente, atendimento em até 10 minutos":
            $ ajustar("saude", 5)
            narr "Classificação correta para o quadro clínico de Renato."
            jump m1_sub13

        "{b}AMARELO{/b} — pouco urgente, até 60 minutos — {i}\"deve ser ansiedade\"{/i}":
            $ ajustar("saude", -10)
            $ ajustar("estigma", 5)
            narr "A pressão e a frequência cardíaca não apontam para ansiedade simples. A condição de moradia pode ter influenciado a leitura clínica."
            jump m1_sub13

        "{b}VERDE{/b} — não urgente — {i}\"mais emocional do que físico\"{/i}":
            $ ajustar("saude", -20)
            $ ajustar("estigma", 15)
            narr "Classificação incorreta. O médico vai receber Renato mais comprometido do que deveria estar."
            narr "{b}[[Efeito Atrasado registrado]]{/b}"
            jump m1_sub13


## Sub-decisão 1.3 — A sala de espera

label m1_sub13:
    show renato hesitante at center
    narr "Vinte minutos de espera. Renato olha para a porta, inquieto. A qualquer momento pode se levantar e ir embora."

    menu:

        "Não fazer nada — ele foi avisado que haveria espera":
            narr "Renato continua olhando para a porta. Sem referência."
            jump m1_reflexao1

        "Avisar sobre o tempo de espera e oferecer um copo d'água":
            $ ajustar("confianca", 10)
            $ ajustar("vinculo", 5)
            tec "Renato, mais uns 15 minutinhos. Quer água?"
            show renato aberto with dissolve
            renato "Tá bom. Obrigado."
            narr "Pequeno gesto. Renato para de olhar para a porta."
            jump m1_reflexao1

        "Pedir à segurança que {i}\"fique de olho\"{/i} — ele parece agitado":
            $ ajustar("confianca", -5)
            $ ajustar("estigma", 15)
            narr "O segurança se posiciona perto. Renato percebe. Aperta o caderno contra o peito e baixa a cabeça."
            show renato hesitante with dissolve
            jump m1_reflexao1


## Reflexão intermediária — Momento 1

label m1_reflexao1:
    scene bg_escuro with fade
    call reflexao_card("A surpresa ao constatar que Renato não se encaixa na imagem mental de 'morador de rua' revela como o estigma opera na prática.", "O acolhimento não começa no preenchimento da ficha. Começa no olhar.")
    jump m1_momento2


## ─────────────────────────────────────────────────────────────────────────────
## MOMENTO 2 — "O que a ficha não diz"
## ─────────────────────────────────────────────────────────────────────────────

label m1_momento2:
    scene bg upa_consultorio with fade
    show renato normal at center with dissolve
    show medico at right with dissolve

    narr "O diagnóstico revela crise hipertensiva com forte componente ansioso. Renato não mencionou depressão. O estado dele agora reflete as escolhas anteriores."

    menu:

        "Checklist direto — {i}\"Você tem diagnóstico de depressão ou ansiedade?\"{/i}":
            $ ajustar("saude", 5)
            $ escolha_m2 = "A"
            if confianca >= 35:
                renato "Tenho. Depressão severa. Estava tomando medicação, mas perdi o plano quando fui demitido."
                narr "A confiança construída antes abriu essa porta."
            else:
                renato "Não."
                narr "A confiança baixa fechou essa porta."
            jump m1_sub21

        "Focar só na hipertensão — a saúde mental não é prioridade agora":
            $ ajustar("saude", 5)
            $ ajustar("estigma", 5)
            $ escolha_m2 = "B"
            narr "A hipertensão é tratada. O componente ansioso fica sem resposta."
            narr "{b}[[Efeito Atrasado]]{/b}: Renato volta em duas semanas com quadro pior, sem registro de saúde mental no prontuário."
            jump m1_sub21

        "Reduzir o ritmo — {i}\"Às vezes o corpo mostra o que a gente não consegue falar. Você está passando por algo difícil além da saúde?\"{/i}":
            $ ajustar("confianca", 20)
            $ escolha_m2 = "C"
            show renato emocionado with dissolve
            narr "Silêncio longo."
            renato "Faz 8 meses que eu durmo na rua."
            narr "Ele para. Parece não acreditar que disse isso em voz alta."
            renato "Nunca pensei que ia chegar nisso."
            narr "Ele abre o caderno devagar."
            jump m1_sub22_direto


## Sub-decisão 2.1 — Registro no prontuário

label m1_sub21:
    narr "Como você registra o atendimento no prontuário do e-SUS?"

    menu:

        "Só diagnóstico e conduta clínica":
            narr "O próximo profissional começa do zero — sem histórico de depressão, sem contexto de rua."
            jump m1_sub22

        "Diagnóstico + depressão + contexto de rua + encaminhamento para saúde mental e serviço social":
            $ ajustar("acesso", 20)
            $ ajustar("vinculo", 10)
            narr "Registro completo. Cria continuidade de cuidado. O próximo profissional sabe com quem está falando."
            jump m1_sub22

        "Registrar o clínico, omitir o contexto emocional {i}\"para não expor\"{/i}":
            $ ajustar("acesso", 5)
            narr "Sigilo não é apagar — é proteger. Um prontuário sem contexto fragmenta o cuidado."
            jump m1_sub22


## Sub-decisão 2.2 — O caderno de Renato

label m1_sub22:
    show renato aberto at center
    narr "Renato pega o caderno, parece quase mostrar algo. Recua."
    renato "Desculpa. Não sei por que mostrei isso."
    jump m1_sub22_escolha

label m1_sub22_direto:
    show renato emocionado at center
    show caderno at center with dissolve
    narr "No caderno: uma coluna de 'ENTREVISTAS' com nomes riscados. Na outra página, o começo de uma carta para os filhos que nunca foi enviada."
    hide caderno with dissolve
    renato "Desculpa. Não sei por que mostrei isso."
    jump m1_sub22_escolha

label m1_sub22_escolha:
    menu:

        "{i}\"Entendo.\"{/i} — e volta ao exame":
            $ ajustar("confianca", -5)
            show renato hesitante with dissolve
            narr "Renato guarda o caderno. Fecha-se de novo."
            jump m1_sub23

        "Para. Olha para ele. {i}\"Não precisa pedir desculpa. Fico feliz que você mostrou.\"{/i}":
            $ ajustar("confianca", 20)
            $ ajustar("estigma", -5)
            show renato aberto with dissolve
            narr "Renato fica em silêncio. Mas não guarda o caderno."
            narr "É a primeira vez em meses que alguém o trata como uma pessoa com uma história — não com um problema a resolver."
            jump m1_sub23

        "Pede para ler o bilhete para os filhos":
            $ ajustar("confianca", -15)
            show renato hesitante with dissolve
            renato "Não. Isso é meu."
            narr "A invasão fechou o que tinha começado a se abrir."
            jump m1_sub23


## Sub-decisão 2.3 — Prescrição ancorada na rotina

label m1_sub23:
    narr "Anti-hipertensivo de uso diário. Preferencialmente pela manhã, antes de comer."

    menu:

        "Posologia padrão — {i}\"tome em jejum pela manhã\"{/i}":
            $ ajustar("saude", 5)
            narr "Posologia padrão. Mas a rotina de Renato não é padrão. A adesão ao tratamento depende de conhecer essa rotina."
            jump m1_reflexao2

        "Perguntar sobre a rotina real de Renato antes de prescrever":
            $ ajustar("saude", 15)
            $ ajustar("confianca", 5)
            narr "Você pergunta como é o dia a dia dele."
            renato "Eu fico num abrigo. Acordo cedo, antes das 7. Café eles dão."
            narr "Você ancora a posologia nessa rotina. A prescrição agora é viável."
            jump m1_reflexao2

        "Perguntar só sobre armazenamento do medicamento":
            $ ajustar("saude", 8)
            narr "Armazenamento resolvido. Mas o horário e os hábitos do paciente continuam desconhecidos."
            jump m1_reflexao2


## Reflexão intermediária — Momento 2

label m1_reflexao2:
    scene bg_escuro with fade
    call reflexao_card("Separar saúde física da mental em populações vulneráveis gera retornos precoces e agravados.", "O prontuário é uma ferramenta de cuidado — não apenas um registro.")
    jump m1_momento3


## ─────────────────────────────────────────────────────────────────────────────
## MOMENTO 3 — "O intervalo de observação"
## ─────────────────────────────────────────────────────────────────────────────

label m1_momento3:
    scene bg upa_observacao with fade
    show renato hesitante at center with dissolve
    show tecnica at right with dissolve

    narr "Renato tomou a primeira dose. PA 168/104, FC 92. O protocolo exige pelo menos 30 minutos de observação."
    narr "A sala de espera está cheia. Há outros pacientes para atender."

    menu:

        "Sair e atender o próximo — voltar quando o monitor alarmar":
            $ ajustar("confianca", -5)
            narr "Renato aperta o caderno. Olha para a porta. Sem referência, sem saber o que esperar."
            jump m1_sub31

        "Avisar a enfermagem para checar em 15 min; iniciar o rascunho do registro":
            $ ajustar("confianca", 5)
            $ ajustar("acesso", 5)
            tec "Pode contar comigo. Volto em 15."
            show renato aberto with dissolve
            narr "Renato vê que alguém vai continuar presente. Solta levemente os ombros."
            jump m1_sub31

        "Delegar integralmente à enfermagem — {i}\"pode liberar quando estabilizar\"{/i}":
            $ ajustar("vinculo", -10)
            narr "O caso vira 'leito monitorado'. Renato percebe quando se torna um número."
            jump m1_sub31


## Sub-decisão 3.1 — Reavaliação clínica

label m1_sub31:
    narr "35 minutos depois. PA 148/92, FC 84. Critérios clínicos dentro do limite para alta."

    menu:

        "Conferir sinais vitais, perguntar 'tá melhor?', registrar 'estável para alta'":
            narr "Clinicamente em ordem. Mas há sinais que só aparecem na fala — e você não perguntou."
            jump m1_sub32

        "Sentar, refazer o exame, perguntar abertamente sobre dor, falta de ar e sono":
            $ ajustar("confianca", 10)
            $ renato_medo_alta = True
            show renato hesitante at center
            renato "Tá... mas ainda sinto o coração acelerado quando penso em sair."
            narr "Ele não está com medo dos sintomas. Está com medo da alta."
            narr "Esse dado vai mudar o Momento 4."
            jump m1_sub32

        "Manter em observação 'por garantia', sem reavaliar clinicamente":
            $ ajustar("vinculo", -5)
            narr "A observação se estende sem finalidade clínica. Para Renato, é mais tempo de incerteza."
            jump m1_sub32


## Sub-decisão 3.2 — Consolidação do prontuário

label m1_sub32:
    narr "Antes da alta, como você registra o atendimento no e-SUS?"

    menu:

        "Texto livre básico — diagnóstico e conduta":
            narr "O registro existe, mas é ilegível para o sistema. O CNR não encontra Renato automaticamente."
            jump m1_reflexao3

        "CIAP-2 (K86 + P03) + vulnerabilidade social + sinalização para busca ativa pelo CNR":
            $ ajustar("acesso", 20)
            narr "Registro completo. O e-SUS lista Renato para busca ativa pelo Consultório na Rua."
            narr "{i}\"Cinco minutos bem feitos podem valer meses de acesso.\"{/i}"
            jump m1_reflexao3

        "Registrar só o clínico — omitir contexto emocional 'para não comprometer a alta'":
            $ ajustar("acesso", 5)
            narr "O registro clínico está feito. Mas o contexto que mais define se Renato vai conseguir continuar o tratamento ficou de fora."
            jump m1_reflexao3


## Reflexão intermediária — Momento 3

label m1_reflexao3:
    scene bg_escuro with fade
    call reflexao_card("O intervalo de observação parece tempo morto. Mas é o exato lugar onde a alta se constrói.", "Reavaliar é diferente de reconferir. Registrar é diferente de digitar.")
    jump m1_momento4


## ─────────────────────────────────────────────────────────────────────────────
## MOMENTO 4 — "A alta"
## ─────────────────────────────────────────────────────────────────────────────

label m1_momento4:
    scene bg upa_corredor with fade
    show assistente at right with dissolve
    show renato normal at left with dissolve

    narr "Hora da alta. Renato não tem dinheiro. Não tem Cartão SUS ativo. Não tem endereço no sistema."

    if renato_medo_alta:
        narr "E você sabe que ele está com medo de sair."

    menu:

        "Dar a receita e liberar — {i}\"tome conforme indicado\"{/i}":
            $ ajustar("acesso", -20)
            $ ajustar("vinculo", -15)
            hide assistente
            narr "Renato olha para a receita. Não tem como comprar o remédio. Não tem Cartão SUS ativo. Não volta."
            jump m1_sub41

        "Dar a receita, registrar situação de rua, orientar sobre a farmácia popular":
            $ ajustar("acesso", 10)
            $ ajustar("vinculo", 5)
            narr "Orientação parcial. Mas o CNR não foi acionado e o Cartão SUS ainda está inativo."
            jump m1_sub41

        "Fluxo completo: acionar Serviço Social, dispensar medicação da farmácia da UPA, combinar encontro com o CNR":
            $ ajustar("acesso", 25)
            $ ajustar("vinculo", 20)
            assist "Me passa o resumo do caso?"
            narr "Renato vai sair com a primeira dose tomada, o medicamento na mochila e o nome da assistente social escrito no caderno."
            jump m1_sub41


## Sub-decisão 4.1 — Comunicando os próximos passos

label m1_sub41:
    hide assistente
    show renato normal at center

    narr "Você vai explicar os próximos passos."

    menu:

        "Explicar rapidamente em pé enquanto organiza a ficha":
            narr "Renato absorve o que consegue. O endereço do CNR vai errar — não por descuido, mas porque a informação chegou rápido demais."
            jump m1_sub42

        "Sentar. Revisar passo a passo. Perguntar: {i}\"Tem algo que pode dificultar você ir lá na quarta?\"{/i}":
            $ ajustar("confianca", 10)
            $ ajustar("vinculo", 15)
            show renato aberto with dissolve
            renato "Nunca ninguém me perguntou isso."
            narr "A pergunta não é sobre logística. É sobre reconhecer que o caminho entre a UPA e o CNR pode ter obstáculos que você não enxerga do consultório."
            jump m1_sub42

        "Delegar o encerramento à assistente social e seguir para o próximo paciente":
            $ ajustar("vinculo", -5)
            narr "Ela faz o que pode. Mas a transição sem apresentação perde contexto essencial."
            jump m1_sub42


## Sub-decisão 4.2 — Passagem para a assistente social

label m1_sub42:
    show assistente at right with dissolve

    assist "Posso ajudar em 5 minutos."

    menu:

        "Agradecer e deixar que ela conduza como puder":
            $ ajustar("acesso", 5)
            narr "Ela faz o que consegue. Mas começa do zero."
            jump m1_sub43

        "Fazer uma apresentação rápida do caso — diagnóstico, contexto, o que já foi combinado":
            $ ajustar("acesso", 15)
            assist "Entendido. Conheço o fluxo com o CNR. Já aciono."
            narr "{i}\"Cinco minutos bem preparados valem mais que trinta minutos do zero.\"{/i}"
            jump m1_sub43

        "Sugerir que ele volte em outro dia para conversar com ela":
            $ ajustar("vinculo", -10)
            $ ajustar("acesso", -5)
            narr "'Pode voltar' raramente se concretiza para quem não tem endereço fixo."
            jump m1_sub43


## Sub-decisão 4.3 — A despedida na porta

label m1_sub43:
    scene bg upa_saida with fade
    hide assistente
    show renato despedida at center with dissolve

    narr "Renato para na porta."
    renato "E se eu não conseguir ir lá na quarta?"

    narr "Não é sobre transporte. É sobre medo."

    menu:

        "{i}\"O CNR atende em outros dias também.\"{/i}":
            narr "A resposta está correta. Mas não respondeu o que ele perguntou."
            jump m1_reflexao4

        "Para. Olha para ele. {i}\"Renato, você chegou aqui hoje com dor no peito, sozinho. Isso já foi difícil. O próximo passo não precisa ser perfeito — só precisa existir.\"{/i}":
            $ ajustar("confianca", 15)
            $ ajustar("vinculo", 20)
            show renato aberto with dissolve
            narr "Renato fica parado por um segundo. Segura o caderno com as duas mãos."
            narr "Essa frase não está em nenhum protocolo."
            jump m1_reflexao4

        "{i}\"A gente torce por você.\"{/i}":
            $ ajustar("vinculo", 5)
            narr "Bondade genuína. Mas distante."
            jump m1_reflexao4


## Reflexão intermediária — Momento 4

label m1_reflexao4:
    scene bg_escuro with fade
    call reflexao_card("Entregar uma receita para alguém sem dinheiro nem Cartão SUS ativo não resolve o problema.", "A alta é um ato de continuidade — não de encerramento.")
    jump m1_fim


## ─────────────────────────────────────────────────────────────────────────────
## FIM DA MISSÃO 1
## ─────────────────────────────────────────────────────────────────────────────

label m1_fim:
    stop music fadeout 3.0
    scene bg_escuro with fade
    jump epilogo

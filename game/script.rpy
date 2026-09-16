## script.rpy — Caminhos do Cuidado (nome provisório) · PET-Saúde Pop Rua GT6
## Ponto de entrada e variáveis globais
## História 1 — "Ele não parece morador de rua" (roteiro atualizado)

## ── Medidores (0–100; revelados apenas no Epílogo — regra do roteiro) ────────
default direito     = 40   # [DIREITO] Direito em Saúde — cuidado como direito
default rede        = 40   # [REDE] Conhecimento da Rede — articulação dos serviços
default empatia     = 40   # [EMPATIA] Empatia / Sensibilidade Social
default acolhimento = 40   # [ACOLHIMENTO] — qualidade do encontro

## O roteiro determina que NENHUM medidor aparece em tempo real (todos só no
## Epílogo). O documento de design anterior previa a Empatia visível — se o
## grupo decidir reativá-la, basta mudar para True.
default hud_empatia = False

## Convenção de pesos (provisória — calibrar com profissionais de saúde):
## ▲ = +5 · ▲▲ = +10 · ▲▲▲ = +15 · ▼ = -5 · ▼▼ = -10 · ▼▼▼ = -15

## ── Nós da rede (mapa do medidor REDE — acendem conforme as escolhas) ────────
default nos_rede = {
    "UPA": True,              # o atendimento aconteceu
    "Serviço Social": False,
    "CNR (Marcos)": False,
    "Farmácia da UPA": False,
    "UBS de referência": False,
    "CRAS": False,
    "Defensoria Pública": False,
}

## ── Registros de escolha (efeitos atrasados e desfecho) ──────────────────────
default escolha_c1  = ""   # Cena 1 — "Ele não deveria estar aqui"
default escolha_c2  = ""   # Cena 2 — A primeira impressão
default escolha_s11 = ""   # Sub 1.1 — endereço no e-SUS
default escolha_s12 = ""   # Sub 1.2 — a espera
default escolha_s13 = ""   # Sub 1.3 — passagem de caso
default escolha_c3  = ""   # Cena 3 — O que a ficha não diz
default escolha_s21 = ""   # Sub 2.1 — registro no e-SUS
default escolha_s22 = ""   # Sub 2.2 — a prescrição
default escolha_c4  = ""   # Cena 4 — O intervalo
default escolha_s31 = ""   # Sub 3.1 — reavaliação
default escolha_s32 = ""   # Sub 3.2 — prontuário antes da alta
default escolha_c5  = ""   # Cena 5 — A alta
default escolha_s41 = ""   # Sub 4.1 — comunicando os próximos passos
default escolha_s42 = ""   # Sub 4.2 — passagem ao Serviço Social
default escolha_c6  = ""   # Cena 6 — A rede com nome e voz
default escolha_s51 = ""   # Sub 5.1 — a carteira vencida e a cidadania
default escolha_c7  = ""   # Cena 7 — A despedida
default renato_medo_alta = False   # revelado na sub-decisão 3.1 [B]
default nos_acesos = 0             # calculado no epílogo

## ── Início ───────────────────────────────────────────────────────────────────
label start:
    ## Tela conceitual sobre PSR (uma vez, antes da 1ª história)
    call tela_conceitual_psr

    if hud_empatia:
        show screen medidores
    jump missao1

## ── Tela conceitual sobre PSR ────────────────────────────────────────────────
label tela_conceitual_psr:
    scene bg neutro_cor with fade
    window show

    narr "{b}Antes de começar.{/b}"
    narr "A população em situação de rua é heterogênea: não existe um perfil único. Os motivos mais citados são problemas familiares, desemprego e uso de substâncias."
    narr "Neste jogo, você é quem faz o serviço funcionar. A cada cena, sua perspectiva muda — recepção, medicina, enfermagem, serviço social."
    narr "Suas escolhas movem quatro dimensões do cuidado: {b}Direito em Saúde{/b}, {b}Conhecimento da Rede{/b}, {b}Empatia{/b} e {b}Acolhimento{/b}. Nenhuma delas aparece durante o jogo — você descobre no fim, olhando para o que fez."
    narr "{i}Não há pontuação a vencer. Há uma pessoa a encontrar.{/i}"

    window hide
    return

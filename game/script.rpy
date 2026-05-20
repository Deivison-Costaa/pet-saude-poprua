## script.rpy — PET-Saúde: Pop Rua
## Ponto de entrada e variáveis globais

## ── Medidores ────────────────────────────────────────────────────────────────
default confianca = 30   # Confiança do paciente no profissional (0–100)
default vinculo   = 10   # Vínculo do paciente com o serviço (0–100)
default saude     = 50   # Estado clínico (0–100; começa comprometido)
default acesso    = 10   # Capacidade de seguir o plano terapêutico (0–100)
default estigma   = 0    # INVISÍVEL ao jogador — revelado apenas no epílogo

## ── Registros de escolha (para efeitos atrasados) ────────────────────────────
default escolha_m1 = ""
default escolha_m2 = ""
default escolha_m3 = ""
default escolha_m4 = ""
default renato_medo_alta = False  # revelado na sub-decisão 3.1

## ── Tela de título ───────────────────────────────────────────────────────────
label start:
    scene bg titulo with fade
    pause 1.5
    centered "{color=#ffffff}{b}{size=+22}PET-Saúde: Pop Rua{/size}{/b}\n\n{size=+4}Missão 1 — Ele não parece morador de rua{/size}{/color}"
    pause 2.0
    show screen medidores
    jump missao1

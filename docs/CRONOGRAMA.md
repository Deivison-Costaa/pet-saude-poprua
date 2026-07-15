# Cronograma de Desenvolvimento — Protótipo da 1ª História (Renato)

**Projeto:** Visual novel educacional PET-Saúde Pop Rua (GT6) · **Frente:** TI
**Meta:** protótipo funcional da 1ª história ("Ele não parece morador de rua") **pronto para testes até 05/08/2026**
**Elaborado em:** 14/07/2026 · Reuniões do grupo: quartas-feiras

---

## Visão geral

| Semana | Período | Foco | Marco (critério de pronto) |
|---|---|---|---|
| **S0** | até 15/07 | Planejamento e padrões | Cronograma + fluxograma de telas + estrutura de menus + padrões visuais apresentados na reunião de **15/07** |
| **S1** | 16/07 – 22/07 | Telas e assets | Menus navegáveis no Ren'Py (conteúdo provisório ok) + assets da história 1 completos (cenários, sprites, objetos) |
| **S2** | 23/07 – 29/07 | História 1 jogável | Cenas 0–7 implementadas com decisões, medidores e os 2 desfechos; áudio básico |
| **S3** | 30/07 – 04/08 | Testes internos e build | APK Android + versão Windows; rodada de teste do GT; correções |
| **Entrega** | **05/08** | Protótipo para testes | Build estável nas mãos do grupo para iniciar testes com profissionais de saúde |

---

## Detalhamento

### S0 — até a reunião de 15/07 (esta entrega)
- [x] Cronograma de desenvolvimento (este documento)
- [x] Fluxograma de navegação de telas (`fluxograma-navegacao.md` — portar ao Cacoo, ver riscos)
- [x] Proposta de estrutura de menus e telas (`estrutura-telas.md`)
- [x] Padrões visuais consolidados + novas imagens no estilo aquarela (`padroes-visuais.md`)
- [x] Mockups do caminho de criação das telas da história do Renato

### S1 — 16/07 a 22/07 · Telas e assets
- Incorporar feedback da reunião de 15/07 (estrutura de telas e visual).
- Implementar no Ren'Py: menu principal, capítulos, perfil/progresso (com persistência), materiais, redes de apoio, sobre o jogo, créditos, configurações — conteúdo provisório onde faltar.
- Fatiar os sprites por pose/expressão a partir das fichas de personagens; recortes com transparência.
- Gerar objetos restantes e variações de cenário que a implementação revelar necessárias.
- **Pronto quando:** dá para navegar por todas as telas do fluxograma no aparelho, mesmo sem a história.

### S2 — 23/07 a 29/07 · História 1 jogável
- Implementar as cenas 0–7 do roteiro com todas as decisões e sub-decisões (A/B/C).
- Medidores: Direito em Saúde, Conhecimento da Rede, Empatia (visível em tempo real), Acolhimento; mapa de nós da rede; card de contexto real; epílogo com desfechos A ("Rede ativada") e B ("Recomeço do zero").
- Pesos provisórios das escolhas (▲=+5 · ▲▲=+10 · ▲▲▲=+15; ▼ equivalentes negativos) — calibração final com os profissionais de saúde após os testes.
- Áudio: ambiência da UPA, toque de telefone (cena da ligação ao CNR), bipe de monitor (box).
- **Pronto quando:** a história fecha de ponta a ponta nos dois desfechos, sem erro de lint.

### S3 — 30/07 a 04/08 · Testes internos e build
- Build Android (APK) e Windows; instalação nos aparelhos do grupo.
- Rodada de testes internos do GT (roteiro de teste: 1 jogada visando desfecho A, 1 visando desfecho B, navegação por todas as telas).
- Correção dos problemas encontrados; ajuste de textos.
- Preparar o roteiro de teste para os profissionais de saúde (o que observar, o que perguntar).
- **Pronto quando:** build estável instalado e roteiro de teste definido.

### 05/08 — Entrega
- Protótipo funcional da 1ª história distribuído ao grupo para iniciar os testes com profissionais de saúde.

---

## O que já está pronto hoje (14/07)

- Roteiro da história 1 finalizado e atualizado (`ROTEIRO-VISUAL-NOVEL.docx`, cenas 0–7).
- 9 cenários aquarela da missão + 8 fundos neutros + caderno do Renato (padrão visual aprovado em 01/07).
- Fichas de referência dos 6 personagens (Renato, Marcos, médico, assistente social, recepcionista, técnica de enfermagem).
- Base técnica Ren'Py funcionando (motor de medidores, cards de reflexão, epílogo) — será atualizada ao roteiro novo.
- Novas imagens desta entrega: fundo do menu em aquarela, objetos das cenas (carteira de trabalho, Cartão SUS, receita) e personagens da sala de espera.

## Riscos e pendências

| Risco / pendência | Mitigação |
|---|---|
| Pesos da pontuação ainda não validados com profissionais de saúde (decisão da ata de 01/07) | Usar pesos provisórios documentados; calibrar após a rodada de testes |
| Fluxograma pedido "preferencialmente no Cacoo" | Entregue em Mermaid (texto versionável + imagem); portar ao Cacoo é transcrição direta — 1h de trabalho, fazer na S1 |
| Fichas de personagens precisam ser fatiadas em sprites individuais | Tarefa da S1; se alguma pose faltar, gerar no mesmo estilo |
| Diversidade corporal apontada na ata | Novos personagens gerados já contemplam; revisar elenco existente na S1 |
| Nome do jogo em aberto ("Caminhos do Cuidado" é o candidato usado nos materiais) | Decidir até o fim da 2ª história (ata); protótipo usa nome provisório |
| Testes em aparelhos Android variados | Priorizar 2–3 aparelhos do próprio grupo na S3 |

# Prompts das imagens geradas — entrega de 14/07/2026

Modelo: **gpt-image-1** (OpenAI) · qualidade alta · PNG
Blocos de estilo reutilizados dos documentos `01-07/PROMPTS-CENARIOS-MISSAO1.md` e `PROMPTS-OBJETOS-MISSAO1.md`.

---

## Blocos de estilo usados

**CENÁRIO (aquarela):**
```
digital watercolor illustration, soft loose washes, muted faded pastel palette,
simplified almost cartoonish shapes, minimal fine detail, gentle soft edges,
light paper texture, slightly desaturated, calm subdued mood, soft background blur,
mobile visual novel background, clean uncluttered composition, eye-level view,
no text, no letters, no logos
```

**OBJETO (aquarela, fundo transparente):**
```
digital watercolor illustration, single object study, soft loose washes, muted faded pastel palette,
simplified but clearly readable shapes, gentle soft edges, light paper texture, slightly desaturated,
calm mood, centered close-up prop, transparent background, subtle soft shadow beneath,
mobile game item art, clean and uncluttered, no people, no hands, no readable text, no letters, no numbers
```

**PERSONAGEM (sprite, fundo transparente):**
```
clean semi-realistic comic illustration style, soft cel shading, natural proportions,
warm approachable rendering, full body standing character for a visual novel sprite,
facing slightly toward viewer, transparent background, no text, no watermark,
consistent with a Brazilian public health (SUS) educational game cast
```

---

## Imagens

### menu_upa_entardecer.png — 1536x1024, opaco
Fundo do menu principal (ilustração de capa — única exceção à regra "sem pessoas no fundo").
> Wide establishing scene for a game main menu: a Brazilian UPA 24h emergency health unit at dusk, warm golden-orange sky fading to deep blue, soft warm light spilling from the entrance. In the middle distance, small soft-edged figures: health professionals in white and teal warmly welcoming a few homeless people of diverse body types near the entrance ramp — figures loose and painterly, no facial detail, integrated into the wash. Foreground street with long soft shadows. Left third of the composition calmer and emptier to hold menu buttons. Blank sign shapes only. + BLOCO CENÁRIO

Observação: o letreiro "UPA 24h" saiu legível e grafado corretamente — mantido por ser arte de capa.

### obj_carteira_trabalho.png — 1024x1024, transparente ✅
Sub-decisão 1.1 (documentos de Renato).
> An old worn Brazilian work document booklet (carteira de trabalho), closed, deep blue cover faded and scuffed, dog-eared corners, slightly bent spine, its cover markings suggested only as soft illegible golden smudges. + BLOCO OBJETO

### obj_cartao_sus.png — 1024x1024, transparente ✅
Sub-decisão 1.1 (Cartão SUS garantido por lei).
> A Brazilian public health plastic card (SUS card): white card with soft blue and green horizontal accents, gentle rounded corners, slightly worn, lying flat at a small angle; any lettering rendered only as blurred illegible strokes. + BLOCO OBJETO

### obj_receita_medica.png — 1024x1024, transparente ✅
Sub-decisão 2.2 (a prescrição fora do papel).
> A medical prescription: single sheet of slightly creased white paper with soft illegible handwritten scribble lines in blue-gray, a faint stamp shape as a smudge, one folded corner. + BLOCO OBJETO

### sprite_senhora.png — 1024x1536 (NPC Cena 1)
> A Brazilian woman in her early 60s waiting in a public emergency room: fuller plus-size body type, light-brown skin, gray-streaked hair in a low bun, simple floral blouse and long skirt, small purse held tight, arms crossed, disapproving judgmental expression with raised eyebrow. + BLOCO PERSONAGEM

### sprite_outro_paciente.png — 1024x1536 (NPC Cena 1)
> A Brazilian man around 45 waiting in a public emergency room: stocky broad build, dark skin, short curly hair, polo shirt and jeans, holding a numbered-ticket-like blank slip, slightly annoyed skeptical expression, weight shifted to one leg. + BLOCO PERSONAGEM

---

## Aprendizados de pipeline
- `background: "transparent"` funciona de forma confiável para **objetos**; para **personagens de corpo inteiro**, o modelo tende a pintar um ambiente atrás — pedir explicitamente "isolated character cutout, plain empty transparent background, no environment, no floor, no wall" (as versões finais dos sprites usam essa formulação).
- Verificar sempre o canal alpha com PIL (`getchannel('A').getextrema()`), não a olho.

---

## Peças de interface em aquarela — 15/07/2026 (`assets-gerados/ui/`)

Geradas para os mockups v2 (`docs/mockups/mockup_*_aquarela.png`) e reutilizáveis como GUI do jogo.
Bloco base comum:
```
digital watercolor illustration, soft loose washes, gentle soft edges, light paper texture,
slightly desaturated, hand-painted game UI element, single element centered,
transparent background, nothing else in frame, no text, no letters, no numbers, no logos
```

- **ui_botao_azul.png** — placa de botão em lavagem azul-marinho (#1d3d5c), bordas empoçadas, miolo com bloom claro.
- **ui_botao_claro.png** — placa de botão em papel branco-gelo com contorno azul irregular pintado à mão.
- **ui_painel_papel.png** — painel vertical de papel aquarela branco-gelo, bordas suaves (painel do menu).
- **ui_caixa_dialogo.png** — placa larga e baixa em tinta azul-escura para caixa de diálogo.
- **ui_faixa_titulo.png** — pincelada horizontal âmbar-dourado (sublinhado de título).

Técnica de composição: recorte pelo alpha + escala uniforme até a altura desejada + **3 fatias**
(esticar apenas o miolo horizontal) para não distorcer as bordas pintadas — ver
`compor_mockups_aquarela.py` (scratchpad da sessão) ou reproduzir com PIL.

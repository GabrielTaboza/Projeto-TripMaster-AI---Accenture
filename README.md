# TripMaster AI – Planejador de Viagens Inteligente

##  Objetivo do Projeto
O **TripMaster AI** é um sistema multiagente desenvolvido com a ferramenta **Microsoft AutoGen**, projetado para criar roteiros de viagem personalizados a partir de um único input do cliente.  
O sistema simula uma equipe de agentes autônomos que cooperam para montar uma proposta completa de viagem, incluindo destino, transporte, hospedagem, experiências locais e custos estimados.

---

## Equipe de Desenvolvimento
| Integrante | Agente | Personalidade / Estilo de Fala |
|-------------|---------|--------------------------------|
| **Gabriel** | Orquestrador | Líder calmo, racional, direto e formal |
| **Maisa** | Perfil do Usuário | Empática, amigável e gosta de ouvir |
| **Miguel** | Agente Destinos | Criativo, entusiasmado e descritivo |
| **Ygor** | Agente Transporte | Técnico, detalhista e objetivo |
| **Alexis** | Agente Hospedagem | Organizado, Educado e pouco formal |
| **João** | Agente Financeiro | Rigoroso, racional e técnico |
| **Brenno** | Agente Experiências Locais | Animado, criativo e inspirador |
| **Levi** | Apresentação | Comunicativo, empolgado e criativo |

---

## Input Inicial do Cliente
> “Quero viajar com minha namorada em dezembro por uns 10 dias. Buscamos um lugar tranquilo, com natureza, boa comida e clima ameno. Nosso orçamento é de até R$ 7.000 e preferimos evitar voos longos.”

---

## Fluxo de Interação Entre os Agentes
```
Cliente 
   ↓
Orquestrador  
   ↓
Orquestrador → Perfil do Usuário  
   ↓
Perfil do Usuário → Orquestrador → Destinos  
   ↓
Destinos → Orquestrador → Transporte e Hospedagem  
   ↓
Orquestrador → Financeiro → Experiências Locais  
   ↓
Orquestrador → Apresentação  
   ↓
Resultado Final (Proposta de Viagem)

```

---

## Estrutura do Repositório
```
TripMaster-AI/
│
├── README.md
├── /agents/
│   ├── orquestrador.md
│   ├── perfil_usuario.md
│   ├── agente_destinos.md
│   ├── agente_transporte.md
│   ├── agente_hospedagem.md
│   ├── agente_financeiro.md
│   ├── experiencias_locais.md
│   └── apresentacao.md
├── /inputs/
│   └── cliente.txt
└── /docs/
    └── fluxograma_interacao.png
```

---

##  Andamento do Projeto (Sprints)

###  Sprint 1 – Organização Inicial (até 13/11)
- [x] Definição dos papéis dos 8 agentes  
- [x] Criação do input inicial do cliente  
- [x] Esboço do fluxo de interação  
- [x] Criação do repositório e estrutura base  

###  Sprint 2 – Desenvolvimento no AutoGen (14/11 a 20/11)
- [x] Configuração de 3 agentes no AutoGen  
- [x] Criação dos prompts personalizados  
- [x] Simulação curta entre os 3 agentes
- [x] Registro de logs e prints das conversas  
- [x] Análise de conflitos entre agentes  

###  Sprint 3 – Finalização e Apresentação (21/11 a 25/11)
- [ ] Organização da documentação final no GitHub  
- [ ] Montagem dos slides de apresentação  
- [ ] Simulação completa e ajustes finais  

---

##  Evidências (a serem adicionadas)
- [ ] Capturas de tela do AutoGen  
- [ ] Logs de conversas entre agentes  
- [ ] Gráfico ou diagrama do fluxo de comunicação  

---

##  Curiosidades
- Como o papel e a personalidade do seu agente influenciaram as decisões finais?
- Houve conflitos entre os agentes? Como o orquestrador poderia resolvê-los?
- Quais seriam riscos se um agente estivesse mal configurado (prompt mal
escrito)? Responda para cada agente.
Que melhorias você faria ou fez para aprimorar a coordenação multiagente?

---

##  Professor Orientador
**Vieira** – Engenharia de Prompt
Curso: *Inteligência Artificial – 2025.2*  
Instituição: *Residência Tecnológica – Accenture - Turma 2*

---

> Projeto desenvolvido por estudantes como parte da disciplina de Engenharia de Prompt e Agentes Autônomos.  
> Uso exclusivo educacional.

import os
import google.generativeai as genai

# ======================================================
# CONFIGURAÇÃO DA API GEMINI
# ======================================================

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


# ======================================================
# FUNÇÃO AUXILIAR PARA CARREGAR AGENTES
# ======================================================

def carregar_agente(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()


# ======================================================
# CARREGAR AGENTES DA PASTA agents/
# ======================================================

ag_orq = carregar_agente("agents/orquestrador.md")
ag_perfil = carregar_agente("agents/perfil.md")
ag_destinos = carregar_agente("agents/destinos.md")

print("Agentes carregados com sucesso!")
print("- Orquestrador")
print("- Perfil do Usuário")
print("- Destinos\n")


# ======================================================
# CARREGAR BRIEFING DO USUÁRIO
# ======================================================

with open("inputs/briefing.txt", "r", encoding="utf-8") as f:
    briefing = f.read()

print("Briefing carregado:\n", briefing, "\n")


# ======================================================
# ETAPA 1 → PERFIL ANALISA O BRIEFING
# ======================================================

prompt_perfil = f"""
Você é o agente PERFIL DO USUÁRIO.
Aqui está sua descrição oficial:

{ag_perfil}

Agora analise o briefing abaixo e gere:
- Um perfil do viajante
- Preferências
- Restrições
- Objetivos

Briefing do cliente:
{briefing}
"""

resp_perfil = model.generate_content(prompt_perfil)
print("===== PERFIL DO USUÁRIO =====\n")
print(resp_perfil.text, "\n")


# ======================================================
# ETAPA 2 → DESTINOS USA O PERFIL PARA RECOMENDAR LUGARES
# ======================================================

prompt_destinos = f"""
Você é o agente DESTINOS.
Aqui está sua descrição oficial:

{ag_destinos}

Use o seguinte perfil do cliente para sugerir 3 destinos ideais:

{resp_perfil.text}

Responda de forma clara.
"""

resp_destinos = model.generate_content(prompt_destinos)
print("===== RECOMENDAÇÕES DE DESTINOS =====\n")
print(resp_destinos.text, "\n")


# ======================================================
# ETAPA 3 → ORQUESTRADOR RESUME E FINALIZA
# ======================================================

prompt_orq = f"""
Você é o agente ORQUESTRADOR.

Sua descrição:

{ag_orq}

Seu trabalho é:
- Ler o briefing
- Ler o perfil gerado pelo agente Perfil
- Ler as recomendações do agente Destinos
- Criar um resumo final para apresentar à equipe

Briefing:
{briefing}

Perfil do cliente:
{resp_perfil.text}

Destinos recomendados:
{resp_destinos.text}

Gere um resumo final organizado.
"""

resp_final = model.generate_content(prompt_orq)

print("===== RESUMO FINAL DO ORQUESTRADOR =====\n")
print(resp_final.text)

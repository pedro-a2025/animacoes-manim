# Visualização de Física e Matemática com Python (Manim)

<div align="center">
  <img src="assets/MaquinaComContradominioCompleta_ManimCE_v0.20.1.gif" width="600" alt="Animação da Máquina">
</div>

Este repositório contém scripts desenvolvidos em Python utilizando a biblioteca Manim. O foco principal é a criação de animações automatizadas para traduzir demonstrações e deduções analíticas complexas em visualizações didáticas passo a passo.

## 🎯 Objetivos do Projeto
- Automatizar a geração de material didático em vídeo.
- Aplicar estruturas de repetição e manipulação de listas em Python para refatorar e otimizar animações matemáticas.
- Integrar renderização tipográfica de alta qualidade com programação orientada a objetos.

## 📂 Estrutura do Repositório

* **`decomposicao_helmholtz.py`**: Script completo que renderiza a demonstração matemática da Decomposição de Helmholtz. O código destaca a aplicação de identidades vetoriais (6.b e 6.c) e a substituição da delta de Dirac, utilizando laços `for` para mapear transformações algébricas paralelas e manter a legibilidade do código.

## 🛠️ Tecnologias Utilizadas
- **Python:** Lógica de animação, refatoração e estruturação de cenas.
- **Manim Community:** Engine de renderização de vídeos matemáticos.
- **LaTeX:** Tipografia e formatação rigorosa das equações físicas e vetoriais.

## 🚀 Como executar
Para renderizar o vídeo do Teorema de Helmholtz em qualidade de teste, clone este repositório e execute o comando abaixo no terminal:

(Obs: pql resultará em um vídeo de baixa qualidade, caso queira uma qualidade melhor, use pqh)


```bash
manim -pql decomposicao_helmholtz.py Teorema_H_final3



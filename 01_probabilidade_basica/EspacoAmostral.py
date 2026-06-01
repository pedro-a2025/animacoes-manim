from manim import *

class EspacoAmostral(Scene):
    def construct(self):
        # ==========================================
        # ATO 1: A "Historinha" (Definição de Probabilidade)
        # ==========================================
        titulo_prob = Text("O que é Probabilidade?", font_size=40, color=YELLOW).to_edge(UP)
        
        formula = MathTex(
            "P = \\frac{\\text{Casos Favoráveis (o que eu quero)}}{\\text{Casos Possíveis (tudo que pode acontecer)}}",
            font_size=36
        )
        
        self.play(Write(titulo_prob))
        self.wait(0.5)
        self.play(FadeIn(formula, shift=UP))
        self.wait(3)
        self.play(FadeOut(titulo_prob), FadeOut(formula))

        # ==========================================
        # ATO 2: O Gancho (A Pergunta)
        # ==========================================
        pergunta = Paragraph(
            "Se jogarmos 2 dados e somarmos os resultados,\nqual soma tem a maior probabilidade de sair?", 
            font_size=28, 
            alignment="center"
        ).move_to(ORIGIN)
        
        self.play(Write(pergunta), run_time=2)
        self.wait(2)
        self.play(FadeOut(pergunta))

        # ==========================================
        # ATO 3: Construindo a Tabela Retangular (7x7)
        # ==========================================
        titulo_tabela = Text("Espaço Amostral (Todos os Casos Possíveis)", font_size=32).to_edge(UP)
        self.play(FadeIn(titulo_tabela))

        grade = VGroup()
        celulas_soma_7 = VGroup()
        
        # Novas dimensões: mais largo para caber o texto
        largura = 1.2
        altura = 0.8 

        for i in range(7): 
            linha = VGroup()
            for j in range(7): 
                # Trocamos Square por Rectangle
                retangulo = Rectangle(width=largura, height=altura)
                
                # Célula [0,0]: A divisão diagonal com os nomes dos dados
                if i == 0 and j == 0:
                    linha_diag = Line(retangulo.get_corner(UL), retangulo.get_corner(DR), color=WHITE)
                    # Ajustei as posições para caber no novo formato retangular
                    txt_d1 = Text("Dado 1", font_size=14, color=RED).move_to(retangulo).shift(DOWN*0.2 + LEFT*0.25)
                    txt_d2 = Text("Dado 2", font_size=14, color=BLUE).move_to(retangulo).shift(UP*0.2 + RIGHT*0.25)
                    celula = VGroup(retangulo, linha_diag, txt_d1, txt_d2)
                
                # Primeira Linha: Cabeçalho do Dado 2
                elif i == 0:
                    txt = Text(str(j), font_size=20, color=BLUE)
                    celula = VGroup(retangulo, txt)
                
                # Primeira Coluna: Cabeçalho do Dado 1
                elif j == 0:
                    txt = Text(str(i), font_size=20, color=RED)
                    celula = VGroup(retangulo, txt)
                
                # Miolo da Tabela: As Somas
                else:
                    soma = i + j
                    txt = Text(str(soma), font_size=20)
                    celula = VGroup(retangulo, txt)
                    
                    if soma == 7:
                        celulas_soma_7.add(celula)
                        
                linha.add(celula)
                
            linha.arrange(RIGHT, buff=0) 
            grade.add(linha)
        
        grade.arrange(DOWN, buff=0)
        grade.next_to(titulo_tabela, DOWN, buff=0.5)

        self.play(Create(grade), run_time=4)
        self.wait(1)

        # ==========================================
        # ATO 4: O Suspense e a Contagem
        # ==========================================
        titulo_investigacao = Text("Vamos contar qual soma aparece mais vezes?", font_size=32, color=YELLOW).to_edge(UP)
        self.play(Transform(titulo_tabela, titulo_investigacao))
        self.wait(2)

        titulo_revelacao = Text("A soma 7 é a campeã!", font_size=32, color=YELLOW).to_edge(UP)
        self.play(Transform(titulo_tabela, titulo_revelacao))

        # Colore a diagonal do 7
        for celula in celulas_soma_7:
            retangulo_interno = celula[0]
            self.play(
                retangulo_interno.animate.set_fill(YELLOW, opacity=0.4).set_color(YELLOW),
                run_time=0.15
            )
        self.wait(1)

        # ==========================================
        # ATO 5: A Matemática Final
        # ==========================================
        # Desliza a tabela um pouco menos para a esquerda por ela estar mais larga
        self.play(grade.animate.shift(LEFT * 2.0))

        texto_possiveis = Text("Casos Possíveis: 36", font_size=24)
        texto_favoraveis = Text("Casos Favoráveis (7): 6", font_size=24, color=YELLOW)
        
        probabilidade = MathTex("P(Soma=7) = \\frac{6}{36} = \\frac{1}{6}", font_size=32)
        
        conclusao = VGroup(texto_possiveis, texto_favoraveis, probabilidade).arrange(DOWN, buff=0.5)
        conclusao.next_to(grade, RIGHT, buff=0.8)

        self.play(Write(texto_possiveis))
        self.play(Write(texto_favoraveis))
        self.wait(0.5)
        self.play(Write(probabilidade))
        
        self.wait(3)
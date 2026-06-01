from manim import *

class ProbabilidadeCondicional(Scene):
    def construct(self):
        # ==========================================
        # ATO 1: O que é Probabilidade Condicional?
        # ==========================================
        titulo_cond = Text("O que é Probabilidade Condicional?", font_size=40, color=YELLOW).to_edge(UP)
        
        # Quebrando a explicação em partes para a leitura ficar mais suave
        explicacao_1 = Text("É quando recebemos uma", font_size=28)
        explicacao_2 = Text("NOVA INFORMAÇÃO (uma pista)", font_size=32, color=BLUE)
        explicacao_3 = Text("antes de calcular as nossas chances.", font_size=28)
        
        bloco_explicacao = VGroup(explicacao_1, explicacao_2, explicacao_3).arrange(DOWN, buff=0.2)
        bloco_explicacao.next_to(titulo_cond, DOWN, buff=0.8)

        # A fórmula didática adaptada para a historinha
        formula = MathTex(
            "P(\\text{Evento} \\mid \\text{Pista}) = \\frac{\\text{Casos Favoráveis DENTRO da Pista}}{\\text{Total de Casos da Pista (Novo Universo)}}",
            font_size=30
        ).next_to(bloco_explicacao, DOWN, buff=1)
        
        self.play(Write(titulo_cond))
        self.wait(0.5)
        self.play(FadeIn(bloco_explicacao, shift=UP))
        self.wait(1.5)
        self.play(Write(formula))
        self.wait(4)
        
        # Limpa a tela para o gancho
        self.play(FadeOut(titulo_cond), FadeOut(bloco_explicacao), FadeOut(formula))

        # ==========================================
        # ATO 2: O Gancho (A Pergunta)
        # ==========================================
        pergunta = Paragraph(
            "Exemplo Prático:\n"
            "Sabendo que o Dado 1 caiu no número 4 (Nossa Pista),\n"
            "qual a chance da soma ser maior que 7?", 
            font_size=28, 
            alignment="center",
            t2c={"Sabendo que o Dado 1 caiu no número 4 (Nossa Pista),": BLUE} # Colore a pista de azul
        ).move_to(ORIGIN)
        
        self.play(Write(pergunta), run_time=2.5)
        self.wait(3)
        self.play(FadeOut(pergunta))

        # ==========================================
        # ATO 3: Construindo a Tabela do Zero (36 Casos)
        # ==========================================
        titulo_tabela = Text("Nosso universo inicial (36 Casos Possíveis)", font_size=32).to_edge(UP)
        self.play(FadeIn(titulo_tabela))

        grade = VGroup()
        
        celulas_descartadas = VGroup()
        celulas_favoraveis = VGroup()
        linha_do_dado_4 = VGroup() 
        
        largura = 1.1
        altura = 0.7 

        for i in range(7): 
            linha = VGroup()
            for j in range(7): 
                retangulo = Rectangle(width=largura, height=altura)
                
                # Célula [0,0]: Cabeçalho dividido
                if i == 0 and j == 0:
                    linha_diag = Line(retangulo.get_corner(UL), retangulo.get_corner(DR), color=WHITE)
                    txt_d1 = Text("Dado 1", font_size=12, color=RED).move_to(retangulo).shift(DOWN*0.18 + LEFT*0.22)
                    txt_d2 = Text("Dado 2", font_size=12, color=BLUE).move_to(retangulo).shift(UP*0.18 + RIGHT*0.22)
                    celula = VGroup(retangulo, linha_diag, txt_d1, txt_d2)
                    celulas_descartadas.add(celula)
                
                # Cabeçalho do Dado 2 (Colunas)
                elif i == 0:
                    txt = Text(str(j), font_size=20, color=BLUE)
                    celula = VGroup(retangulo, txt)
                    celulas_descartadas.add(celula)
                
                # Cabeçalho do Dado 1 (Linhas)
                elif j == 0:
                    txt = Text(str(i), font_size=20, color=RED)
                    celula = VGroup(retangulo, txt)
                    if i != 4:
                        celulas_descartadas.add(celula)
                
                # Miolo da Tabela: As Somas reais
                else:
                    soma = i + j
                    txt = Text(str(soma), font_size=20)
                    celula = VGroup(retangulo, txt)
                    
                    # Filtro da Condição: Dado 1 precisa ser igual a 4
                    if i == 4:
                        linha_do_dado_4.add(celula)
                        # Dentro da condição, filtramos o evento desejado (> 7)
                        if soma > 7:
                            celulas_favoraveis.add(celula)
                    else:
                        celulas_descartadas.add(celula)
                        
                linha.add(celula)
                
            linha.arrange(RIGHT, buff=0) 
            grade.add(linha)
        
        grade.arrange(DOWN, buff=0)
        grade.next_to(titulo_tabela, DOWN, buff=0.5)

        self.play(Create(grade), run_time=3.5)
        self.wait(1)

        # ==========================================
        # ATO 4: Encolhendo o Universo (A Pista)
        # ==========================================
        titulo_pista = Text("Pista: O Dado 1 é 4. O Universo encolheu!", font_size=32, color=BLUE).to_edge(UP)
        self.play(Transform(titulo_tabela, titulo_pista))
        
        # Esmaece tudo o que não pertence à linha do Dado 1 = 4
        self.play(celulas_descartadas.animate.set_opacity(0.15), run_time=1.5)
        
        # Destaca a borda da nossa linha de interesse em Azul
        for celula in linha_do_dado_4:
            borda = celula[0]
            self.play(borda.animate.set_color(BLUE), run_time=0.1)
            
        self.wait(1)

        # ==========================================
        # ATO 5: Contando os Casos Favoráveis
        # ==========================================
        titulo_pergunta = Text("Destes 6 casos, quais são maiores que 7?", font_size=32, color=GREEN).to_edge(UP)
        self.play(Transform(titulo_tabela, titulo_pergunta))

        # Acende as respostas corretas em Verde (8, 9 e 10)
        for celula in celulas_favoraveis:
            retangulo_interno = celula[0]
            self.play(
                retangulo_interno.animate.set_fill(GREEN, opacity=0.4).set_color(GREEN),
                run_time=0.2
            )
        self.wait(1)

        # ==========================================
        # ATO 6: A Matemática na Lateral
        # ==========================================
        self.play(grade.animate.shift(LEFT * 2.6))

        texto_possiveis = Text("Novos Casos Possíveis: 6", font_size=20)
        texto_favoraveis = Text("Casos Favoráveis (>7): 3", font_size=20, color=GREEN)
        
        probabilidade = MathTex(
            "P(\\text{Soma}>7 \\mid \\text{D1}=4) = \\frac{3}{6} = 50\\%", 
            font_size=26
        )
        
        conclusao = VGroup(texto_possiveis, texto_favoraveis, probabilidade).arrange(DOWN, buff=0.4)
        conclusao.next_to(grade, RIGHT, buff=0.5)

        self.play(Write(texto_possiveis))
        self.play(Write(texto_favoraveis))
        self.wait(0.5)
        self.play(Write(probabilidade))
        
        self.wait(3)
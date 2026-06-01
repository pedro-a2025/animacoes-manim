from manim import *

class TesteMedico(Scene):
    def construct(self):
        # ==========================================
        # ATO 1: O Cenário
        # ==========================================
        titulo = Text("Teorema de Bayes: O Teste Médico", font_size=36, color=YELLOW).to_edge(UP)
        
        contexto = VGroup(
            Text("Imagine uma doença que afeta 1 em cada 100 pessoas.", font_size=24),
            Text("Você faz um exame e o resultado dá POSITIVO.", font_size=24, color=RED),
            Text("O teste tem 90% de precisão. Qual a chance de você estar doente?", font_size=24)
        ).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        self.play(Write(titulo))
        self.play(Write(contexto), run_time=3)
        self.wait(3)
        self.play(FadeOut(contexto))

        # ==========================================
        # ATO 2: Construindo a População (Waffle Chart)
        # ==========================================
        # Cria 100 quadrados cinzas (População Saudável)
        quadrados = [Square(side_length=0.4, fill_opacity=0.8, color=GRAY, stroke_width=2) for _ in range(100)]
        populacao = VGroup(*quadrados).arrange_in_grid(rows=10, cols=10, buff=0.1)
        populacao.scale(0.9).move_to(LEFT * 2.5 + DOWN * 0.5)

        legenda_pop = Text("População: 100 pessoas", font_size=24).next_to(populacao, UP)
        
        self.play(FadeIn(populacao, shift=UP), Write(legenda_pop))
        self.wait(1)

        # ==========================================
        # ATO 3: A Realidade (Quem está doente?)
        # ==========================================
        doente = quadrados[0] # O primeiro quadrado é o doente (1%)
        
        legenda_doente = Text("1 doente real", font_size=24, color=RED).move_to(RIGHT * 3 + UP * 1.5)
        seta_doente = Arrow(legenda_doente.get_left(), doente.get_right(), color=RED)

        self.play(doente.animate.set_color(RED))
        self.play(Write(legenda_doente), Create(seta_doente))
        self.wait(2)

        # ==========================================
        # ATO 4: Aplicando o Teste Médico (Falsos Positivos)
        # ==========================================
        # O teste erra em 10% dos saudáveis (aproximadamente 9 pessoas das 99)
        falsos_positivos = quadrados[1:10] # Do segundo ao décimo quadrado
        
        legenda_falsos = Text("9 falsos positivos\n(pessoas saudáveis)", font_size=24, color=YELLOW).next_to(legenda_doente, DOWN, buff=1)
        
        # Animando a mudança de cor simultaneamente
        self.play(
            *[q.animate.set_color(YELLOW) for q in falsos_positivos],
            Write(legenda_falsos)
        )
        self.wait(2)

        # ==========================================
        # ATO 5: O Filtro do Bayes (A Pista)
        # ==========================================
        # Se você testou positivo, você NÃO está na parte cinza.
        # Vamos esmaecer os negativos (quadrados do 10 ao 99)
        negativos = quadrados[10:100]
        
        self.play(FadeOut(legenda_doente), FadeOut(seta_doente), FadeOut(legenda_falsos))
        
        conclusao_texto = Text("O seu teste deu Positivo.\nVocê só pode ser um dos coloridos!", font_size=28, color=WHITE).to_edge(RIGHT).shift(LEFT * 0.5)
        
        self.play(
            *[q.animate.set_opacity(0.1) for q in negativos],
            Write(conclusao_texto)
        )
        self.wait(2)

        # ==========================================
        # ATO 6: A Matemática Revelada
        # ==========================================
        self.play(FadeOut(conclusao_texto))

        # Agrupando a conta final
        conta_final = VGroup()
        passo1 = Text("Total de testes positivos: 10", font_size=24)
        passo2 = Text("Doentes reais nos positivos: 1", font_size=24, color=RED)
        
        bayes_calc = MathTex(
            "P(\\text{Doente} \\mid \\text{Positivo}) = \\frac{1}{10} = 10\\%", 
            font_size=36, 
            color=YELLOW
        )
        
        conta_final.add(passo1, passo2, bayes_calc).arrange(DOWN, buff=0.5).move_to(RIGHT * 3)

        self.play(Write(passo1))
        self.play(Write(passo2))
        self.wait(1)
        self.play(Write(bayes_calc))
        
        destaque = SurroundingRectangle(bayes_calc, color=RED, buff=0.2)
        self.play(Create(destaque))
        self.wait(4)
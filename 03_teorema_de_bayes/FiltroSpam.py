from manim import *

class FiltroSpam(Scene):
    def construct(self):
        # ==========================================
        # ATO 1: O Problema
        # ==========================================
        titulo = Text("Teorema de Bayes na Prática", font_size=40, color=YELLOW).to_edge(UP)
        pergunta = Paragraph(
            "Você recebeu um e-mail com a palavra 'GRÁTIS'.\n"
            "Qual é a probabilidade real de ser um Spam?",
            alignment="center",
            font_size=28
        ).move_to(ORIGIN)

        self.play(Write(titulo))
        self.play(Write(pergunta), run_time=2)
        self.wait(2)
        
        # Limpamos a tela cedo para dar espaço à árvore
        self.play(FadeOut(pergunta), FadeOut(titulo))

        # ==========================================
        # ATO 2: A Árvore de Decisão
        # ==========================================
        raiz = Text("Novo\nE-mail", font_size=24).move_to(LEFT * 5)
        
        # Nível 1
        spam = Text("Spam\n(30%)", font_size=20, color=RED).move_to(LEFT * 1 + UP * 2)
        legitimo = Text("Legítimo\n(70%)", font_size=20, color=GREEN).move_to(LEFT * 1 + DOWN * 2)
        
        linha_raiz_spam = Line(raiz.get_right(), spam.get_left(), color=WHITE)
        linha_raiz_legitimo = Line(raiz.get_right(), legitimo.get_left(), color=WHITE)

        self.play(Write(raiz))
        self.play(
            Create(linha_raiz_spam), Write(spam),
            Create(linha_raiz_legitimo), Write(legitimo)
        )

        # Nível 2
        spam_gratis = Text("Tem 'Grátis'\n(80%)", font_size=18, color=YELLOW).move_to(RIGHT * 3 + UP * 3)
        spam_sem_gratis = Text("Sem 'Grátis'\n(20%)", font_size=18, color=GRAY).move_to(RIGHT * 3 + UP * 1)
        linha_s_g = Line(spam.get_right(), spam_gratis.get_left(), color=RED)
        linha_s_sg = Line(spam.get_right(), spam_sem_gratis.get_left(), color=RED).set_opacity(0.3)

        legitimo_gratis = Text("Tem 'Grátis'\n(5%)", font_size=18, color=YELLOW).move_to(RIGHT * 3 + DOWN * 1)
        legitimo_sem_gratis = Text("Sem 'Grátis'\n(95%)", font_size=18, color=GRAY).move_to(RIGHT * 3 + DOWN * 3)
        linha_l_g = Line(legitimo.get_right(), legitimo_gratis.get_left(), color=GREEN)
        linha_l_sg = Line(legitimo.get_right(), legitimo_sem_gratis.get_left(), color=GREEN).set_opacity(0.3)

        self.play(
            Create(linha_s_g), Write(spam_gratis),
            Create(linha_s_sg), Write(spam_sem_gratis),
            Create(linha_l_g), Write(legitimo_gratis),
            Create(linha_l_sg), Write(legitimo_sem_gratis)
        )
        self.wait(1)

        # ==========================================
        # ATO 3: Calculando e Filtrando a Evidência
        # ==========================================
        # Esmaece o que não importa
        self.play(
            spam_sem_gratis.animate.set_opacity(0.1),
            legitimo_sem_gratis.animate.set_opacity(0.1),
            linha_s_sg.animate.set_opacity(0.1),
            linha_l_sg.animate.set_opacity(0.1)
        )

        # Mostra de onde vêm os valores direto nos galhos
        calc_spam = MathTex("30\\% \\times 80\\% = 24\\%", font_size=24, color=RED).next_to(spam_gratis, DOWN, buff=0.2)
        calc_legit = MathTex("70\\% \\times 5\\% = 3,5\\%", font_size=24, color=GREEN).next_to(legitimo_gratis, DOWN, buff=0.2)

        self.play(Write(calc_spam))
        self.play(Write(calc_legit))
        self.wait(2)

        # ==========================================
        # ATO 4: Limpeza de Tela e Foco nos Resultados
        # ==========================================
        elementos_arvore = VGroup(
            raiz, spam, legitimo, linha_raiz_spam, linha_raiz_legitimo,
            spam_gratis, spam_sem_gratis, legitimo_gratis, legitimo_sem_gratis,
            linha_s_g, linha_s_sg, linha_l_g, linha_l_sg,
            calc_spam, calc_legit
        )
        
        resumo_spam = Text("Cenário A (Spam com 'Grátis') = 24%", font_size=28, color=RED)
        resumo_legit = Text("Cenário B (Legítimo com 'Grátis') = 3,5%", font_size=28, color=GREEN)
        grupo_resumo = VGroup(resumo_spam, resumo_legit).arrange(DOWN, buff=0.5).to_edge(UP, buff=1)

        # A mágica da transição: sai a árvore, entram os dados limpos
        self.play(FadeOut(elementos_arvore))
        self.play(FadeIn(grupo_resumo))
        self.wait(1)

        # ==========================================
        # ATO 5: Probabilidade Condicional Passo a Passo
        # ==========================================
        passo1 = Text("1. Total de e-mails com 'Grátis' (Nosso Novo Universo):", font_size=24)
        conta1 = MathTex("24\\% + 3,5\\% = 27,5\\%", font_size=28, color=YELLOW)
        grupo_passo1 = VGroup(passo1, conta1).arrange(DOWN, buff=0.2).next_to(grupo_resumo, DOWN, buff=0.8)

        passo2 = Text("2. Qual a chance de ser Spam dentro desse universo?", font_size=24)
        conta2 = MathTex(
            "P(\\text{Spam} \\mid \\text{Grátis}) = \\frac{24\\%}{27,5\\%} \\approx 87,2\\%", 
            font_size=32, 
            color=YELLOW
        )
        grupo_passo2 = VGroup(passo2, conta2).arrange(DOWN, buff=0.2).next_to(grupo_passo1, DOWN, buff=0.8)

        # Exibe a soma total
        self.play(Write(passo1))
        self.play(Write(conta1))
        self.wait(1.5)
        
        # Exibe o cálculo final de Bayes
        self.play(Write(passo2))
        self.play(Write(conta2))
        self.wait(3)
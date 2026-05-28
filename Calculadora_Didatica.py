from manim import *

class MaquinaComContradominioCompleta(Scene):
    def construct(self):
        # ---------------------------------------------------------
        # 1. CONFIGURAÇÃO INICIAL DOS CONJUNTOS
        # ---------------------------------------------------------
        box_dominio = Ellipse(width=2.5, height=4.5, color=PURPLE).shift(LEFT * 5)
        txt_dominio = Text("DOMÍNIO (X)", font_size=16, color=PURPLE).next_to(box_dominio, UP)
        
        box_contradominio = Ellipse(width=3.5, height=4.5, color=ORANGE).shift(RIGHT * 4.5)
        txt_contradominio = Text("CONTRADOMÍNIO (Y)", font_size=16, color=ORANGE).next_to(box_contradominio, UP)
        
        self.play(
            Create(box_dominio), Write(txt_dominio),
            Create(box_contradominio), Write(txt_contradominio)
        )

        valores_x = [1, 2, 3]
        posicoes_y_dominio = [1.2, 0, -1.2]
        elementos_dominio = []
        
        for i in range(3):
            num = MathTex(str(valores_x[i])).move_to(box_dominio.get_center() + UP * posicoes_y_dominio[i])
            elementos_dominio.append(num)
        
        self.play(*[FadeIn(n) for n in elementos_dominio])
        self.wait(0.5)

        # =========================================================
        # EXEMPLO 1: f(x) = x^2
        # =========================================================
        caixa_f = RoundedRectangle(corner_radius=0.2, height=2.5, width=3.5, color=BLUE)
        txt_f = MathTex("f(x) = x^2").scale(1.2)
        maquina_f = VGroup(caixa_f, txt_f)
        
        self.play(FadeIn(maquina_f))

        dados_cd_f = {
            "1": UP * 1.2 + LEFT * 0.4,
            "2": UP * 0.6 + RIGHT * 0.6,   
            "4": ORIGIN,
            "6": DOWN * 0.6 + RIGHT * 0.7, 
            "9": DOWN * 1.2 + LEFT * 0.4
        }
        
        objetos_cd_f = {}
        for texto, pos in dados_cd_f.items():
            objetos_cd_f[texto] = MathTex(texto).move_to(box_contradominio.get_center() + pos).set_opacity(0.4)

        self.play(*[FadeIn(obj) for obj in objetos_cd_f.values()])
        self.wait(0.5)

        # Processamento M1
        outputs_f = ["1", "4", "9"]
        for i in range(3):
            num_x = elementos_dominio[i]
            num_voador = num_x.copy()
            alvo_cd = objetos_cd_f[outputs_f[i]]
            
            self.play(
                num_x.animate.set_color(PURPLE).scale(1.2),
                num_voador.animate.move_to(ORIGIN).scale(0.3).set_opacity(0),
                run_time=0.6
            )
            
            self.play(
                caixa_f.animate.set_color(YELLOW),
                alvo_cd.animate.set_color(ORANGE).set_opacity(1).scale(1.3),
                run_time=0.3
            )
            
            self.play(
                caixa_f.animate.set_color(BLUE),
                alvo_cd.animate.scale(1/1.3),
                num_x.animate.set_color(WHITE).scale(1/1.2),
                run_time=0.3
            )
            self.wait(0.2)

        # Revelando Imagem 1 (Texto reposicionado para o topo externo da elipse verde)
        box_imagem_f = Ellipse(width=1.6, height=3.6, color=GREEN).move_to(box_contradominio.get_center() + LEFT * 0.4)
        txt_imagem_f = Text("IMAGEM", font_size=16, weight=BOLD, color=GREEN).next_to(box_imagem_f, UP, buff=0.1)
        
        self.play(Create(box_imagem_f), Write(txt_imagem_f))
        self.wait(1.5)

        # =========================================================
        # TRANSIÇÃO PARA O EXEMPLO 2
        # =========================================================
        self.play(
            FadeOut(box_imagem_f),
            FadeOut(txt_imagem_f),
            *[FadeOut(obj) for obj in objetos_cd_f.values()]
        )

        # Hexágono com escala aumentada para 1.9
        caixa_g = RegularPolygon(n=6, color=GREEN).scale(1.9)
        txt_g = MathTex("g(x) = 2x").scale(1.2)
        maquina_g = VGroup(caixa_g, txt_g)

        self.play(ReplacementTransform(maquina_f, maquina_g))
        self.wait(0.5)

        # =========================================================
        # EXEMPLO 2: g(x) = 2x
        # =========================================================
        dados_cd_g = {
            "2": UP * 1.2 + LEFT * 0.4,
            "3": UP * 0.6 + RIGHT * 0.6,   
            "4": ORIGIN,
            "5": DOWN * 0.6 + RIGHT * 0.7, 
            "6": DOWN * 1.2 + LEFT * 0.4,
            "8": DOWN * 1.6 + RIGHT * 0.1  
        }

        objetos_cd_g = {}
        for texto, pos in dados_cd_g.items():
            objetos_cd_g[texto] = MathTex(texto).move_to(box_contradominio.get_center() + pos).set_opacity(0.4)

        self.play(*[FadeIn(obj) for obj in objetos_cd_g.values()])
        self.wait(0.5)

        # Processamento M2
        outputs_g = ["2", "4", "6"]
        for i in range(3):
            num_x = elementos_dominio[i]
            num_voador = num_x.copy()
            alvo_cd = objetos_cd_g[outputs_g[i]]
            
            self.play(
                num_x.animate.set_color(PURPLE).scale(1.2),
                num_voador.animate.move_to(ORIGIN).scale(0.3).set_opacity(0),
                run_time=0.6
            )
            
            self.play(
                caixa_g.animate.set_color(YELLOW),
                alvo_cd.animate.set_color(ORANGE).set_opacity(1).scale(1.3),
                run_time=0.3
            )
            
            self.play(
                caixa_g.animate.set_color(GREEN),
                alvo_cd.animate.scale(1/1.3),
                num_x.animate.set_color(WHITE).scale(1/1.2),
                run_time=0.3
            )
            self.wait(0.2)

        # Revelando Imagem 2 (Texto reposicionado para o topo externo da elipse verde)
        box_imagem_g = Ellipse(width=1.6, height=3.6, color=GREEN).move_to(box_contradominio.get_center() + LEFT * 0.4)
        txt_imagem_g = Text("IMAGEM", font_size=16, weight=BOLD, color=GREEN).next_to(box_imagem_g, UP, buff=0.1)
        
        self.play(Create(box_imagem_g), Write(txt_imagem_g))
        self.wait(2)
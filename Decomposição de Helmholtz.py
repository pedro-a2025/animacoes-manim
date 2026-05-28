#Decomposição de Helmholtz
from manim import *
import numpy as np

class Teorema_H_final3(Scene):
    def construct(self):
        escala = 0.5
        duracao = 2
        tempo_de_espera_entre_equacoes = 1.2

        # --- Definição das Mobjects (Textos e Equações) ---
        # Textos introdutórios e equações iniciais
        t1 = Text('Seja F(x) uma função vetorial dada por: ').scale(escala).to_edge(UP)
        t2 = MathTex(r"\mathbf{F(x)} = \int \limits_V \mathbf{F(x')} \delta(\mathbf{x} - \mathbf{x'})d^3x'").scale(escala)
        t3 = Text('Sabendo que:').scale(escala).to_edge(UP)
        t4 = MathTex(r" \delta(\mathbf{x} - \mathbf{x'}) = -\dfrac{1}{4\pi} \nabla ^{2} \left(\dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert}\right) ").scale(escala)
        t5 = Text('Então temos: ').scale(escala).to_edge(UP)
        t6 = MathTex(r"\mathbf{F(x)} =  -\dfrac{1}{4\pi} \int \limits_V \mathbf{F(x')} \nabla ^{2} \left(\dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert}\right) d^3x' ").scale(escala)

        # Texto e equação após mover o Laplaciano
        t7 = Text( 'Retirando o laplaciano para fora da integral, temos:').scale(escala).to_edge(UP)
        t8 = MathTex(r"\mathbf{F(x)} =  -\dfrac{1}{4\pi}  \nabla ^{2} \int \limits_V \dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} d^3x'" ).scale(escala)

        # Texto e identidade vetorial
        t9 = Text('Sabendo da identidade vetorial (6.j): ').scale(escala).to_edge(UP)
        t10 = MathTex(r"  \nabla^2\mathbf{a} = \nabla \left( \nabla \cdot \mathbf{a}     \right)   - \nabla \times \left(   \nabla \times \mathbf{a}   \right) ").scale(escala)
        t11 = Text('Temos assim que: ').scale(escala).to_edge(UP)
        t12 = MathTex(r"\mathbf{F(x)} = -\dfrac{1}{4\pi} \nabla \left( \nabla \cdot \int \limits_V \dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} d^3x' \right)  + \dfrac{1}{4\pi} \nabla \times \left( \nabla \times   \int \limits_V \dfrac{\mathbf{F(x')}}{\left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} d^3x' \right) ").scale(escala)

        # Continuação das definições de Mobjects
        t13 = Text('Para facilitar a explicação, temos que: ').scale(escala).to_edge(UP)
        t14 = MathTex(r"\mathbf{F(x)} = -\dfrac{1}{4\pi} \nabla \overbrace{\left( \nabla \cdot \int \limits_V \dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} d^3x' \right)}^{\nabla \cdot \left( \phi \overrightarrow{a} \right)} + \dfrac{1}{4\pi} \nabla \times \overbrace{ \left( \nabla \times  \int \limits_V \dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} d^3x' \right) }^{\nabla \times \left( \phi \overrightarrow{a} \right)}").scale(escala)
        t15 = MathTex(r" \text{Onde, } \phi = \dfrac{1}{\left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \text{ e } \overrightarrow{a} =   \mathbf{F(x')} ").scale(escala)
        t16 = Text('Aplicando 6.b: ').scale(escala).to_edge(UP)
        t17 = MathTex(r" \nabla \cdot \left( \phi  \, \overrightarrow{a} \right) = \phi \left ( \nabla \cdot \overrightarrow{a}   \right) + \overrightarrow{a} \, \cdot \, \left( \nabla \phi \right)").scale(escala)
        t18 = MathTex(
            r" \text{Como } \overrightarrow{a} =   \mathbf{F(x')} \text{ o } \nabla \cdot \mathbf{F(x')} = 0 \text{ visto em (10.1) e (8.35),} \\ \text{pois o } \nabla \text{ não está sendo aplicado em x, mas em x', logo como a variável é diferente, o divergente resulta em zero.} "
        ).scale(escala * 0.9)
        t19 = Text('Aplicando isso em 6.b temos:').scale(escala).to_edge(UP)
        t20 = MathTex(r"\nabla \cdot \left( \phi  \, \overrightarrow{a} \right) = \overrightarrow{a} \, \cdot \, \left( \nabla \phi \right) ").scale(escala)
        t21 = MathTex(r"\nabla \cdot \left(\dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right) = \mathbf{F(x')} \, \cdot \, \nabla \left(   \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right)").scale(escala)
        t22 = Text('Então, temos até agora que: ').scale(escala).to_edge(UP)
        t23 = MathTex(r" \mathbf{F(x)} = -\dfrac{1}{4\pi} \nabla \left( \int \limits_V \mathbf{F(x')} \, \cdot \, \nabla \left(   \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right)  d^3x' \right) + \dfrac{1}{4\pi} \nabla \times \overbrace{\left( \nabla \times   \int \limits_V \dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} d^3x' \right) }^{\nabla \times \left( \phi \overrightarrow{a} \right)}").scale(escala)
        t24 = Text('Fazendo um processo parecido para a outra integral, temos uma aplicação 6.c:').scale(escala).to_edge(UP)
        t25 = MathTex(r"\nabla \times (\phi \, \overrightarrow{a} ) = \phi \left (\nabla \times \overrightarrow{a} \right) + \left( \nabla \phi \right) \times \overrightarrow{a}").scale(escala)

        t26 = MathTex(r" \text{Analogamente, sabendo que } \nabla \times \overrightarrow{a} = \nabla \times \mathbf{F(x')} = 0 \text{ temos que:} ").scale(escala).to_edge(UP)
        t27 = MathTex(r"\nabla \times (\phi \, \overrightarrow{a} ) = \left( \nabla \phi \right) \times \overrightarrow{a}").scale(escala)
        t28 = MathTex(r" \nabla \times (\phi \, \overrightarrow{a} ) = - \overrightarrow{a} \times \left( \nabla \phi \right)").scale(escala).to_edge(UP)
        t29 = MathTex(r"\nabla \times \left(\dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right) = - \mathbf{F(x')} \times   \nabla \left( \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right)").scale(escala)
        t30 = MathTex(r"\text{E como } \nabla \left( \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right)  = -\nabla^{\prime} \left( \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right) ").scale(escala)
        t31 = Text('Sendo assim, temos: ').scale(escala).to_edge(UP)
        t32 = MathTex(r" \nabla \times \left(\dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right) = - \mathbf{F(x')} \times   \nabla \left( \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right)").scale(escala).to_edge(UP)
        t33 = MathTex(r" \nabla \times \left(\dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right) = \mathbf{F(x')} \times   \nabla^{\prime} \left( \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right)").scale(escala)
        t34 = MathTex(r" \text{Mudando a aplicação de } \nabla \text{ de } \mathbf{x} \text{ para }   \mathbf{x'} \text{ temos que mudar o sinal, onde chegamos em: }").scale(escala).to_edge(UP)
        t35 = MathTex(r"\mathbf{F(x)} = \dfrac{1}{4\pi} \nabla \left(   \int \limits_V \mathbf{F(x')} \cdot \nabla^{\prime}   \left( \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right) d^3x' \right)   + \dfrac{1}{4\pi} \nabla \times \left(    \int \limits_V \mathbf{F(x')} \times \nabla'   \left( \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right) d^3x' \right) ").scale(escala)
        # Retirei o 'r' do começo e troquei '\\' por '\n'
        t36 = Text(
            "Ainda assim, necessitamos de mais manipulações matemáticas, com isso,\nchamaremos as partes utilizadas da seguinte forma: "
        ).scale(escala).to_edge(UP)
        # Definindo os marcadores de forma mais robusta e reutilizável
        t37_I = MathTex(r"\mathbf{F(x')} \cdot \nabla^{\prime}   \left( \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right)").scale(escala)
        t37_II = MathTex(r"\mathbf{F(x')} \times \nabla'   \left( \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right)").scale(escala)

        # Para simplificar, vou recriar t37 com o overbrace no próprio MathTex
        t37 = MathTex(r"\mathbf{F(x)} = \dfrac{1}{4\pi} \nabla \left(   \int \limits_V \underbrace {\mathbf{F(x')} \cdot \nabla^{\prime}   \left( \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right)}_{\text{I}} d^3x' \right)   + \dfrac{1}{4\pi} \nabla \times \left(    \int \limits_V \underbrace {\mathbf{F(x')} \times \nabla'   \left( \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right)}_{\text{II}} d^3x' \right) ").scale(escala)
        t38 = Tex(r"Usando as identidades vetoriais 6.b para \textsc{I}:").scale(escala).to_edge(UP)
        t39 = MathTex(r" \nabla \cdot \left( \phi  \, \overrightarrow{a} \right) = \phi \left ( \nabla \cdot \overrightarrow{a}   \right) + \overrightarrow{a} \, \cdot \, \left( \nabla \phi \right)").scale(escala)
        t40 = MathTex(r"\nabla \cdot \left( \phi  \, \overrightarrow{a} \right) - \phi \left ( \nabla \cdot \overrightarrow{a}   \right) = \overrightarrow{a} \, \cdot \, \left( \nabla \phi \right) ").scale(escala)
        t41 = MathTex(r"\overrightarrow{a} \, \cdot \, \left( \nabla \phi \right) = \nabla \cdot \left( \phi  \, \overrightarrow{a} \right) - \phi \left ( \nabla \cdot \overrightarrow{a}   \right)   ").scale(escala)
        t42 = MathTex(r"\overrightarrow{a} \, \cdot \, \left( \nabla \phi \right) = - \left(-\nabla \cdot \left( \phi   \, \overrightarrow{a} \right) + \phi \left ( \nabla \cdot \overrightarrow{a}   \right) \right)").scale(escala)
        t43 = MathTex(r"\overrightarrow{a} \, \cdot     \left( \nabla \phi \right) = - \left( \phi \left ( \nabla \cdot \overrightarrow{a}   \right)-\nabla \cdot \left( \phi   \, \overrightarrow{a} \right) \right)").scale(escala)
        t44 = Text('Aplicando no nosso caso, temos: ').scale(escala)
        t45 = MathTex(r"\mathbf{F(x')} \cdot   \nabla \left( \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right) = - \left( \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \left( \nabla \cdot \mathbf{F(x')} \right) - \nabla \cdot \left( \dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right) \right) ").scale(escala)
        t46 = MathTex(r" \mathbf{F(x')} \cdot   \nabla \left( \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right) = - \left( \dfrac{\nabla \cdot \mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \  - \nabla \cdot \left( \dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right) \right) ").scale(escala)
        t47 = Tex(r"Usando as identidades vetoriais 6.c para \textsc{II}: ").scale(escala).to_edge(UP)
        t48 = MathTex(r"\nabla \times (\phi \, \overrightarrow{a} ) = \phi \left (\nabla \times \overrightarrow{a} \right) + \left( \nabla \phi \right) \times \overrightarrow{a}").scale(escala)
        t49 = MathTex(r"\nabla \times (\phi \, \overrightarrow{a} ) - \phi \left (\nabla \times \overrightarrow{a} \right) = \left( \nabla \phi \right) \times \overrightarrow{a}").scale(escala)
        t50 = MathTex(r" - \left[\nabla \times (\phi \, \overrightarrow{a} ) - \phi \left (\nabla \times \overrightarrow{a} \right) \right] = - \left( \nabla \phi \right) \times \overrightarrow{a}").scale(escala)
        t51 = MathTex(r" - \nabla \times (\phi \, \overrightarrow{a} ) + \phi \left (\nabla \times \overrightarrow{a} \right)  =  \overrightarrow{a} \times \left( \nabla \phi \right)").scale(escala)
        t52 = Text('Aplicando no nosso caso, temos:').scale(escala)
        t53 = MathTex(r"- \nabla \times \left(\dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert}   \right ) + \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert}   \left (\nabla \times \mathbf{F(x')} \right)   =   \mathbf{F(x')} \times \left( \nabla \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert}   \right)").scale(escala)
        t54 = MathTex(r"- \nabla \times \left(\dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert}   \right ) + \dfrac{\nabla \times \mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert}    =   \mathbf{F(x')} \times \left( \nabla \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert}   \right)").scale(escala)
        t55 = Text('Com isso, temos:').scale(escala).to_edge(UP)
        t56 = MathTex(r"\mathbf{F(x)} = \dfrac{1}{4\pi} \nabla \left(   \int \limits_V \underbrace {\mathbf{F(x')} \cdot \nabla^{\prime}   \left( \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right)}_{- \left( \dfrac{\nabla \cdot \mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \ - \nabla \cdot \left( \dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right) \right)} d^3x' \right)   + \dfrac{1}{4\pi} \nabla \times \left(    \int \limits_V \underbrace {\mathbf{F(x')} \times \nabla'   \left( \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right)}_{   - \nabla \times \left(\dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert}   \right ) + \dfrac{\nabla \times \mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} } d^3x' \right) ").scale(escala)
        t57 = MathTex(r"\mathbf{F(x)} = \dfrac{1}{4\pi} \nabla \left(   \int \limits_V - \left( \dfrac{\nabla \cdot \mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \ - \nabla \cdot \left( \dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right) \right) d^3x' \right)   + \dfrac{1}{4\pi} \nabla \times \left(    \int \limits_V - \nabla \times \left(\dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert}   \right ) + \dfrac{\nabla \times \mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} d^3x' \right)").scale(escala)
        t58 = MathTex(r"\mathbf{F(x)} = \dfrac{1}{4\pi} \nabla \left(   \int \limits_V \underbrace {\mathbf{F(x')} \cdot \nabla^{\prime}   \left( \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right)}_{- \left( \dfrac{\nabla^{\prime} \cdot \mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \ - \nabla^{\prime} \cdot \left( \dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right) \right)} d^3x' \right)   + \dfrac{1}{4\pi} \nabla \times \left(    \int \limits_V \underbrace {\mathbf{F(x')} \times \nabla^{\prime}   \left( \dfrac{1}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right)}_{   - \nabla^{\prime} \times \left(\dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert}   \right ) + \dfrac{\nabla^{\prime} \times \mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} } d^3x' \right)").scale(escala)
        t59 = MathTex(r"\mathbf{F(x)} = \dfrac{1}{4\pi} \nabla \left(   \int \limits_V - \left( \dfrac{\nabla^{\prime} \cdot \mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \ - \nabla^{\prime} \cdot \left( \dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right) \right) d^3x' \right)   + \dfrac{1}{4\pi} \nabla \times \left(    \int \limits_V - \nabla^{\prime} \times \left(\dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert}   \right ) + \dfrac{\nabla^{\prime} \times \mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} d^3x' \right) ").scale(escala)
        t60 = MathTex(r" \mathbf{F(x)} = -\dfrac{1}{4\pi} \nabla \left(   \int \limits_V    \dfrac{\nabla^{\prime} \cdot \mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} d^3x'    - \underbrace{\int \limits_V    \nabla^{\prime} \cdot \left( \dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right)}_{\text{III}}    d^3x' \right)    + \dfrac{1}{4\pi} \nabla \times \left(    \int \limits_V    \dfrac{\nabla^{\prime} \times \mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} d^3x' - \underbrace{\int \limits_V \nabla^{\prime} \times \left(\dfrac{\mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert}    \right ) d^3x'}_{\text{IV}} \right) ").scale(escala)   
        t61 = Tex(r" Em \textsc{III} aplicamos o teorema da divergência de Gauss e, \\ em \textsc{IV} aplicamos o teorema de Stokes (mais precisamente a eq 7b), \\ sendo assim, temos:").scale(escala*0.7).to_edge(UP)
        t62 = MathTex(r"\mathbf{F(x)} = -\dfrac{1}{4\pi} \nabla \left( \int \limits_V \dfrac{\nabla^{\prime} \cdot \mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} d^3x' - \oint \limits_S \dfrac{\mathbf{F(x')}}{\left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \cdot \hat{\mathbf{n}}^{\prime} dS^{\prime} \right) + \dfrac{1}{4\pi} \nabla \times \left(\int \limits_V \dfrac{\nabla^{\prime} \times \mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} d^3x' - \oint \limits_S \hat{\mathbf{n}}^{\prime} \times \left( \dfrac{\mathbf{F(x')}}{\left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right) dS^{\prime} \right) ").scale(escala * 0.7)
        t63 = MathTex(r"\mathbf{F(x)} = - \nabla \left( \underbrace{\dfrac{1}{4\pi} \int \limits_V \dfrac{\nabla^{\prime} \cdot \mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} d^3x' - \dfrac{1}{4\pi} \oint \limits_S \dfrac{\mathbf{F(x')}}{\left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \cdot \hat{\mathbf{n}}^{\prime} dS^{\prime} }_{\Phi} \right) + \nabla \times \left(\underbrace{\dfrac{1}{4\pi} \int \limits_V \dfrac{\nabla^{\prime} \times \mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} d^3x' - \dfrac{1}{4\pi} \oint \limits_S \hat{\mathbf{n}}^{\prime} \times \left( \dfrac{\mathbf{F(x')}}{\left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right) dS^{\prime}}_{\mathbf{A}} \right)").scale(escala)
        t64 = MathTex(r"\Phi = \dfrac{1}{4\pi} \int \limits_V \dfrac{\nabla^{\prime} \cdot \mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} d^3x' - \dfrac{1}{4\pi} \oint \limits_S \dfrac{\mathbf{F(x')}}{\left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \cdot \hat{\mathbf{n}}^{\prime} dS^{\prime}").scale(escala)
        t65 = MathTex(r"\mathbf{A} = \dfrac{1}{4\pi} \int \limits_V \dfrac{\nabla^{\prime} \times \mathbf{F(x')}}{ \left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} d^3x' - \dfrac{1}{4\pi} \oint \limits_S \hat{\mathbf{n}}^{\prime} \times \left( \dfrac{\mathbf{F(x')}}{\left\lVert \mathbf{x} - \mathbf{x'} \right\rVert} \right) dS^{\prime}").scale(escala)
        t66 = MathTex(r" \text{Se } \mathbf{F} \to 0 \text{ mais rápido do que } \dfrac{1}{r}").scale(escala)
        # --- Animação (Sequência de exibições e transformações) ---


















        # Seção 1: Introdução
        self.play(Write(t1), Write(t2))
        self.wait(tempo_de_espera_entre_equacoes)

        # Mapeando transformações duplas (Texto e Equação mudando juntos)
        transicoes_paralelas_parte1 = [
            ((t1, t3), (t2, t4)),
            ((t3, t5), (t4, t6)),
            ((t5, t7), (t6, t8)),  # Seção 2 começa aqui
            ((t7, t9), (t8, t10)),
            ((t9, t11), (t10, t12)),
            ((t11, t13), (t12, t14))
        ]

        for (txt_velho, txt_novo), (eq_velha, eq_nova) in transicoes_paralelas_parte1:
            self.play(ReplacementTransform(txt_velho, txt_novo), ReplacementTransform(eq_velha, eq_nova))
            self.wait(tempo_de_espera_entre_equacoes)

        # Seção 3 e 4: Trecho customizado (mantido explícito por causa dos FadeOuts e tempos diferentes)
        self.play(Write(t15.next_to(t14, DOWN)))
        self.wait(tempo_de_espera_entre_equacoes)
        self.play(FadeOut(t15), ReplacementTransform(t13, t16), ReplacementTransform(t14, t17))
        self.wait(tempo_de_espera_entre_equacoes)
  
        self.play(Write(t18.next_to(t17, DOWN)), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes * 1.5)
        self.play(FadeOut(t18), ReplacementTransform(t16, t19), ReplacementTransform(t17, t20), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)
        self.play(ReplacementTransform(t20, t21), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)
        
        self.play(ReplacementTransform(t19, t22), ReplacementTransform(t21, t23), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)
        self.play(FadeOut(t23), ReplacementTransform(t22, t24), t25.animate.next_to(t24, DOWN), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)

        # Seção 5 e início da 6: Novo loop de transformações duplas (com run_time=duracao)
        transicoes_paralelas_parte2 = [
            ((t24, t26), (t25, t27)),
            ((t26, t28), (t27, t29)),
            ((t28, t30), (t29, t31)),
            ((t31, t32), (t30, t33)),
            ((t32, t34), (t33, t35)),
            ((t34, t36), (t35, t37))
        ]

        for (obj1_velho, obj1_novo), (obj2_velho, obj2_novo) in transicoes_paralelas_parte2:
            self.play(ReplacementTransform(obj1_velho, obj1_novo), ReplacementTransform(obj2_velho, obj2_novo), run_time=duracao)
            self.wait(tempo_de_espera_entre_equacoes)

        # O restante da Seção 6 também fica explícito pois altera FadeOuts e Writes sozinhos
        self.play(ReplacementTransform(t36, t38), FadeOut(t37), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)
        # ... (segue o resto do seu código até conectar com a lista do t54)



        # Trazendo o título do primeiro bloco (conecta com o final da seção anterior)
        self.play(ReplacementTransform(t36, t38), FadeOut(t37), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)

        # Escrevendo a primeira equação base da identidade
        self.play(Write(t39), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)

        # Loop da primeira dedução algébrica (passo a passo de t39 até t43)
        deducao_I = [
            (t39, t40),
            (t40, t41),
            (t41, t42),
            (t42, t43)
        ]
        for antigo, novo in deducao_I:
            self.play(ReplacementTransform(antigo, novo), run_time=duracao)
            self.wait(tempo_de_espera_entre_equacoes)

        # QUEBRA DIDÁTICA: Sai a regra geral, entra a aplicação no nosso caso
        self.play(FadeOut(t43), Write(t44), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)
        self.play(ReplacementTransform(t44, t45), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)
        self.play(ReplacementTransform(t45, t46), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)

        # Trocando o título superior para o segundo bloco
        self.play(FadeOut(t46), ReplacementTransform(t38, t47), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)

        # Escrevendo a equação base da segunda identidade
        self.play(Write(t48), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)

        # Loop da segunda dedução algébrica (passo a passo de t48 até t51)
        deducao_II = [
            (t48, t49),
            (t49, t50),
            (t50, t51)
        ]
        for antigo, novo in deducao_II:
            self.play(ReplacementTransform(antigo, novo), run_time=duracao)
            self.wait(tempo_de_espera_entre_equacoes)

        # QUEBRA DIDÁTICA: Sai a regra geral, entra a aplicação
        self.play(FadeOut(t51), Write(t52), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)
        self.play(ReplacementTransform(t52, t53), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)
        self.play(ReplacementTransform(t53, t54), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)

        # Conectando com a reta final do seu código (transição para t55)
        self.play(ReplacementTransform(t54, t55), FadeOut(t47), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)



        '''


     

        self.play(Write(t44), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)
        self.play(ReplacementTransform(t44, t45), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)
        # Identidade vetorial para II
        self.play(FadeOut(t45), ReplacementTransform(t38, t47), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)
        self.play(Write(t52), run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)
        self.play(ReplacementTransform(t52, t53), run_time=duracao)

        self.wait(tempo_de_espera_entre_equacoes) 
        self.play(ReplacementTransform(t53, t54), FadeOut(t47),run_time=duracao)
        self.wait(tempo_de_espera_entre_equacoes)
        '''
        # Mapeando apenas as transformações que são sequenciais e diretas
        transicoes_diretas = [
            (t54, t55),
            (t55, t56),
            (t56, t57),
            (t57, t58),
            (t58, t59),
            (t59, t60),
            (t60, t61),
            (t61, t62),
            (t62, t63),
            (t63, t64),
            (t64, t65),
            (t65, t66)
            ]

        for antigo, novo in transicoes_diretas:
            self.play(ReplacementTransform(antigo, novo), run_time=duracao)
            # Tratando a exceção do tempo de espera do t61
            if novo == t61:
                self.wait(tempo_de_espera_entre_equacoes * 1.5)
            else:
                self.wait(tempo_de_espera_entre_equacoes)

        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)
from manim import *
import os


class FundamentalTheoremOfCalculus(Scene):
    def construct(self):
        greeting = Tex(r"Der Fundamentalsatz der Analysis", font_size=86)
        greetingUp = Tex(r"Der Fundamentalsatz der Analysis", font_size=86).move_to([0, 1, 0])
        name = Tex(r"von Benno Schörmann", font_size=86).move_to([0, -1, 0])

        self.play(Write(greeting))
        self.wait(1)
        self.play(Transform(greeting, greetingUp))
        self.wait(0.5)
        self.play(Write(name))
        self.wait(2)
        self.play(Unwrite(greeting), Unwrite(name))

        title = Tex(r"I. Geschichte", font_size=86)
        upperCorner = Tex(r"I.").move_to([-6.5, 3.5, 0])
        self.wait(1)
        self.play(Write(title))
        self.wait(1)
        self.play(Transform(title, upperCorner))
        self.wait(1)
        nl = ImageMobject(os.path.normpath("assets/Newton+Leibnitz.png"))
        nl.scale(1.2)
        nl.to_edge(RIGHT, buff=1)
        self.play(FadeIn(nl))
        self.wait(1)
        self.play(FadeOut(nl))
        fact = Tex(r"\huge Anfang:\normalsize\\Um 1600-1700 mit Gottfried Leibniz und Isaac Newton").move_to(
            [0, 2.5, 0])
        self.play(Write(fact))
        self.wait(1)
        self.play(Unwrite(fact))

        self.play(Unwrite(title))
        title = Tex(r"II. Riemann-Integral", font_size=86)
        upperCorner = Tex(r"II.").move_to([-6.5, 3.5, 0])
        self.play(Write(title))
        self.wait(1)
        self.play(Transform(title, upperCorner))
        ax = Axes(
            x_range=[0, 3],
            y_range=[0, 6],
            x_axis_config={"numbers_to_include": [1, 3]},
            tips=False,
        )
        labels = ax.get_axis_labels()
        f = ax.plot(lambda x: (x - 2) ** 3 + 2 * (x - 2) ** 2 + 1, x_range=[0, 3], color=BLUE_C)
        fa = ax.plot(lambda x: (1 / 4) * x ** 4 + (-4 / 3) * x ** 3 + 2 * x ** 2 + x, x_range=[0, 3], color=RED_C)
        riemann_5 = ax.get_riemann_rectangles(f, x_range=[0, 3], dx=0.5, color=BLUE, fill_opacity=0.5)
        riemann_1 = ax.get_riemann_rectangles(f, x_range=[0, 3], dx=0.1, color=BLUE, fill_opacity=0.5)
        riemann_02 = ax.get_riemann_rectangles(f, x_range=[0, 3], dx=0.02, color=BLUE, fill_opacity=0.5)
        riemann_inf = ax.get_area(f, [0, 3], color=BLUE, fill_opacity=0.5)
        dx_5 = Tex(r"dx = 0.5")
        dx_1 = Tex(r"dx = 0.1")
        dx_02 = Tex(r"dx = 0.02")
        dx_inf = Tex(r"dx $\to$ 0")
        self.play(Write(ax), Write(labels))
        self.wait(1)
        self.play(Create(f))
        self.wait(1)
        self.play(Write(riemann_5), Write(dx_5))
        self.wait(1)
        self.play(Transform(riemann_5, riemann_1), Transform(dx_5, dx_1))
        self.wait(1)
        self.play(Transform(riemann_5, riemann_02), Transform(dx_5, dx_02))
        self.wait(1)
        self.play(Unwrite(riemann_5), Write(riemann_inf), Transform(dx_5, dx_inf))
        self.wait(1)
        self.play(Create(fa))
        self.wait(2)
        self.play(Unwrite(fa), Unwrite(f), Unwrite(ax), Unwrite(labels), Unwrite(riemann_5), Unwrite(dx_5), Unwrite(riemann_inf))

        self.play(Unwrite(title))
        title = Tex(r"III. Mittelwertsatz der\\Integralrechnung", font_size=86)
        upperCorner = Tex(r"III.").move_to([-6.5, 3.5, 0])
        self.play(Write(title))
        self.wait(1)
        self.play(Transform(title, upperCorner))

        self.play(Unwrite(title))
        title = Tex(r"IV. Hauptsatz der Differential-\\und Integralrechnung", font_size=86)
        upperCorner = Tex(r"IV.").move_to([-6.5, 3.5, 0])
        self.play(Write(title))
        self.wait(1)
        self.play(Transform(title, upperCorner))

        Theorie = Tex(r'''Gegeben ist die in $\mathbb{R}$ definierte Funktion $f$ in einem geschlossenen Intervall $[a, b]$. Sei $F$ definiert für alle $x$ im Intervall $[a, b]$ durch \\
        \begin{equation*}
        F(x)=\int_{a}^{x}f(t) dt
        \end{equation*}
        Dann ist $F$ gleichmäßig stetig auf dem Intervall $[a, b]$ und differenzierbar auf dem offenen Intervall $(a, b)$, und 
        \begin{equation*}
        F'(x)=f(x)
        \end{equation*}
        Für alle $x$ in $(a, b)$, sodass $F$ eine Stammfunktion von $f$ ist.''')
        self.play(Write(Theorie))

        self.wait(5)

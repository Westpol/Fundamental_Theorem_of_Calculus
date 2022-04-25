from manim import *


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

        self.play(Unwrite(title))
        title = Tex(r"II. Riemann-Integral", font_size=86)
        upperCorner = Tex(r"II.").move_to([-6.5, 3.5, 0])
        self.play(Write(title))
        self.wait(1)
        self.play(Transform(title, upperCorner))

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

        self.wait(5)

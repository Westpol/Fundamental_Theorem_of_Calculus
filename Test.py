from manim import *

class PlotTwoGraphsAtOnce(Scene):

    def get_rectangle_corners(self, bottom_left, top_right):
        return [
            (top_right[0], top_right[1]),
            (bottom_left[0], top_right[1]),
            (bottom_left[0], bottom_left[1]),
            (top_right[0], bottom_left[1]),
        ]

    def construct(self):
        ax1 = Axes(
            x_range=[0, 3],
            y_range=[0, 3],
            tips=True,
        ).scale(0.45).move_to([0, 1.6, 0])
        ax2 = Axes(
            x_range=[0, 3],
            y_range=[0, 3],
            tips=True,
        ).scale(0.45).move_to([0, -1.6, 0])
        func1 = ax1.plot(lambda x: (x / 2) ** 2 + 1)
        func2 = ax2.plot(lambda x: (x / 2) ** 2 + 1)
        self.play(Write(ax1), Write(ax2))
        self.play(Write(func1), Write(func2))
        e1 = MathTex(r"\int_{a}^{x_1}f(f)dt").scale(0.75).move_to([-0.8, 0.8, 0])
        e2 = MathTex(r"\int_{a}^{x_1+\Delta x}f(t)dt").scale(0.75).move_to([-0.3, -2.35, 0])
        t_label_1 = ax1.get_T_label(x_val=2, graph=func1, label=MathTex(r"x_1"))
        t_label_2 = ax2.get_T_label(x_val=2.5, graph=func2, label=MathTex(r"x_1+\Delta x"))
        self.play(Write(t_label_1))
        self.play(Write(t_label_2))
        ar1 = ax1.get_area(func1, [0, 2], color=RED_C, fill_opacity=0.5)
        ar2 = ax2.get_area(func2, [0, 2.5], color=BLUE_C, fill_opacity=0.5)
        ar3 = ax2.get_area(func2, [2, 2.5], color=BLUE_C, fill_opacity=0.5)
        self.play(Write(ar1), Write(ar2))
        self.play(Write(e1), Write(e2))
        everything = VGroup(e1, e2, t_label_1, t_label_2, ax1, ax2, ar1, ar2, func1, func2)
        graph1 = VGroup(e1, t_label_1, ax1, ar1, func1)
        graph2 = VGroup(e2, t_label_2, ax2, ar2, func2)
        # noinspection PyTypeChecker
        prevBox = Rectangle(width=3, height=2.5, color=ORANGE).move_to([6.5, -3.3, 0])
        self.play(everything.animate.scale(0.2).move_to([6, -3, 0]), Write(prevBox))
        self.wait(1)

        p3 = Tex(r'''Wenn diese beiden Gleichungen nun subtrahiert werden, dann ergibt sich
                \begin{equation*}
                    F(x_1+\Delta x)-F(x_1)=\int_{a}^{x_1+\Delta x}f(t)dt-\int_{a}^{x_1}f(t)dt
                \end{equation*}''').scale(0.8)
        self.play(Write(p3))
        self.wait(1)

        self.play(Unwrite(p3), Unwrite(prevBox))
        self.play(Unwrite(e1), Unwrite(e2))
        self.play(graph1.animate.scale(5).move_to([0, 1.6, 0]), graph2.animate.scale(5).move_to([0, -1.9, 0]))
        self.play(ar1.animate.move_to([[-0.85, -2, 0]]))
        num = DecimalNumber(0, show_ellipsis=True, num_decimal_places=2, include_sign=False)
        vt = ValueTracker(10)
        num.add_updater(lambda m: m.set_value(vt.get_value() / 10))
        ar1.add_updater(lambda m: m.set_opacity(vt.get_value() / 10))
        for k in range(2):
            self.play(vt.animate.set_value(5), run_time=0.5, rate_func=there_and_back)
        self.wait(1)
        self.play(FadeIn(ar3), FadeOut(ar1), FadeOut(ar2))
        self.wait(2)
        graph1 = VGroup(e1, t_label_1, ax1, func1)
        self.play(Unwrite(ax2), Unwrite(ar3), Unwrite(t_label_2), Unwrite(func2), Unwrite(graph1))
        ax = Axes(
            x_range=[0, 3],
            y_range=[0, 3],
            tips=True,
        )
        func = ax.plot(lambda x: (x / 2) ** 2 + 1)
        ar = ax.get_area(func, [2, 2.5], color=BLUE_C, fill_opacity=0.5)
        t_label_left = ax.get_T_label(x_val=2, graph=func, label=MathTex(r"x_1"))
        t_label_right = ax.get_T_label(x_val=2.5, graph=func, label=MathTex(r"x_1+\Delta x"))
        allNew = VGroup(ax, func, ar, t_label_left, t_label_right)
        self.play(Write(allNew))
        e = MathTex(r"\int_{x_1}^{x_1+\Delta x}f(t)dt").scale(0.6).move_to([3, -1, 0])
        self.wait(1)
        self.play(Write(e))
        self.wait(1)
        self.play(Unwrite(e), Unwrite(allNew))
        self.wait(1)

        p4 = Tex(r'''Zusammenfassend ergibt:
        \begin{equation*}
            F(x_1+\Delta x)-F(x_1)=\int_{a}^{x_1+\Delta x}f(t)dt-\int_{a}^{x_1}f(t)dt
        \end{equation*}
        Und
        \begin{equation*}
            \int_{a}^{x_1+\Delta x}f(t)dt-\int_{a}^{x_1}f(t)dt=\int_{x_1}^{x_1+\Delta x}f(t)dt
        \end{equation*}
        und somit
        \begin{equation*}
            F(x_1+\Delta x)-F(x_1)=\int_{x_1}^{x_1+\Delta x}f(t)dt
        \end{equation*}''').scale(0.8)
        p4[0][22:36].set_color(YELLOW)
        p4[0][111:125].set_color(YELLOW)
        p4[0][37:61].set_color(BLUE)
        p4[0][64:88].set_color(BLUE)
        p4[0][89:103].set_color(RED)
        p4[0][126:140].set_color(RED)
        self.play(Write(p4))
        self.wait(1)
        self.play(Unwrite(p4))
        self.wait(1)

        p5 = Tex(r'''Laut dem Mittelwertsatz der Integralrechnung gibt es eine Zahl c in $[x_1, x_1+\Delta x]$, sodass
        \begin{equation*}
            \int_{x_1}^{x_1+\Delta x}f(t)dt=f(c)*\Delta x
        \end{equation*}''').scale(0.8)
        self.play(Write(p5))
        self.wait(1)
        self.play(Unwrite(p5))
        self.wait(1)

        ax = Axes(
            x_range=[0, 3],
            y_range=[0, 3],
            tips=True
        )
        func = ax.plot(lambda x: (x / 2) ** 2 + 1)
        # noinspection PyTypeChecker
        ar = ax.get_area(func, [2, 2.5], color=BLUE_C, fill_opacity=0.5)

        def funcc(x):
            return (x / 2) ** 2 + 1

        t = ValueTracker(2.05)
        # noinspection PyTypeChecker
        initial_point = [ax.coords_to_point(t.get_value(), funcc(t.get_value()))]
        dot = Dot(point=initial_point)
        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), funcc(t.get_value()))))

        def get_rectangle():
            polygon = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (2, 0), (2.5, funcc(t.get_value()))
                    )
                ]
            )
            polygon.stroke_width = 1
            polygon.set_fill(YELLOW, opacity=0.5)
            return polygon

        polygon = always_redraw(get_rectangle)
        self.play(Write(ax), Write(func), Write(ar), Write(dot), Write(polygon))
        self.play(t.animate.set_value(2.45))
        self.wait(1)
        self.play(t.animate.set_value(2.05))
        self.wait(1)
        self.play(t.animate.set_value(2.2546))
        self.wait(1)
        self.play(Unwrite(VGroup(ax, func, ar, dot, polygon)))
        self.wait(1)

        p6 = Tex(r'''Zusammenfassend ergibt:
                \begin{equation*}
                    F(x_1+\Delta x)-F(x_1)=\int_{x_1}^{x_1+\Delta x}f(t)dt
                \end{equation*}
                Und
                \begin{equation*}
                    \int_{x_1}^{x_1+\Delta x}f(t)dt=f(c)*\Delta x
                \end{equation*}
                und somit
                \begin{equation*}
                    F(x_1+\Delta x)-F(x_1)=f(c)*\Delta x
                \end{equation*}''').scale(0.8)
        p6[0][22:36].set_color(YELLOW)
        p6[0][84:98].set_color(YELLOW)
        p6[0][37:51].set_color(BLUE)
        p6[0][54:68].set_color(BLUE)
        p6[0][69:76].set_color(RED)
        p6[0][99:106].set_color(RED)
        self.play(Write(p6))
        self.wait(1)
        self.play(Unwrite(p6))
        self.wait(1)

        p7 = Tex(r'''Nun wird die Gleichung durch $\Delta x$ geteilt und man erhält:
        \begin{equation*}
            \frac{F(x_1+\Delta x)-F(x_1)}{\Delta x}=f(c)
        \end{equation*}
        ''')

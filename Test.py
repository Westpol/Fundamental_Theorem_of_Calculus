from manim import *

class PlotTwoGraphsAtOnce(Scene):
    CONFIG = {
        "y_max" : 40,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 10,
        "x_tick_frequency" : 1,
        "x_axis_width": 6,
        "y_axis_height": 3,
        "axes_color" : GRAY,
    }
    def construct(self):
        self.graph_origin = -0.5 * DOWN + 3 * LEFT
        self.setup_axes(animate=True)
        graph_up = self.get_graph(lambda x : x**2,
                                    color = GOLD_A,
                                    x_min = 0,
                                    x_max = 3
                                    )
        f1 = Tex(r"f(x) = {x}^2", color = GOLD_A)
        f1.scale(0.7)
        label_coord1 = self.input_to_graph_point(3,graph_up)
        f1.next_to(label_coord1,RIGHT+UP)
        self.graph_origin = 3.5 * DOWN + 3 * LEFT
        self.setup_axes(animate=True)
        graph_down = self.get_graph(lambda x : x**3,
                                    color = BLUE_D,
                                    x_min = 0,
                                    x_max = 3
                                    )
        graphs=VGroup(graph_up,graph_down)
        f2 = Tex(r"f(x) = {x}^3", color = BLUE_D)
        f2.scale(0.7)
        label_coord2 = self.input_to_graph_point(3,graph_up)
        f2.next_to(label_coord2,RIGHT+UP)
        self.play(
            Write(graphs),
            run_time = 2,
        )
        self.play(Write(f1), Write(f2))
        self.wait(3)
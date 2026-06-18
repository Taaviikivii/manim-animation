from manim import *
import numpy as np

class GraphAnimation(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-2, 10, 2],
            x_length=10,
            y_length=6,
            axis_config={"include_numbers": True},
        )

        labels = axes.get_axis_labels("x", "y")

        graph = axes.plot(
            lambda x: x**2,
            color=BLUE,
        )

        graph_label = MathTex("y=x^2")
        graph_label.to_corner(UR)

        self.play(Create(axes))
        self.play(Write(labels))

        self.play(
            Create(graph),
            Write(graph_label),
            run_time=3
        )

        dot = Dot(color=YELLOW)
        dot.move_to(axes.c2p(-2, 4))

        self.play(FadeIn(dot))

        self.play(
            dot.animate.move_to(axes.c2p(2, 4)),
            run_time=2
        )

        self.wait(2)

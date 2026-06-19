from manim import *
import numpy as np

class ManimEvolution(Scene):
    def construct(self):

        # =====================================================
        # MANIM
        # =====================================================

        title = Text("MANIM", font_size=120, weight=BOLD)

        self.play(Write(title), run_time=2)
        self.wait()

        # =====================================================
        # TEXT -> PARTICLES
        # =====================================================

        particles = VGroup()

        for letter in title:
            for _ in range(100):
                try:
                    point = letter.point_from_proportion(
                        np.random.random()
                    )
                except:
                    point = letter.get_center()

                dot = Dot(
                    point=point,
                    radius=0.02,
                    color=BLUE
                )

                particles.add(dot)

        self.play(
            ReplacementTransform(
                title.copy(),
                particles
            ),
            FadeOut(title),
            run_time=2
        )

        self.wait(0.5)

        # =====================================================
        # PARTICLE EXPLOSION
        # =====================================================

        self.play(
            *[
                particle.animate.shift(
                    np.array([
                        np.random.uniform(-4, 4),
                        np.random.uniform(-2.5, 2.5),
                        0
                    ])
                )
                for particle in particles
            ],
            run_time=2
        )

        self.wait()

        # =====================================================
        # PARTICLE SWIRL
        # =====================================================

        self.play(
            Rotate(
                particles,
                angle=2 * PI,
                about_point=ORIGIN
            ),
            run_time=3
        )

        self.wait()

        # =====================================================
        # PARTICLES -> AXES
        # =====================================================

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            x_length=10,
            y_length=6
        )

        targets = []

        for i in range(len(particles)):

            if i % 2 == 0:
                targets.append(
                    axes.x_axis.point_from_proportion(
                        np.random.random()
                    )
                )
            else:
                targets.append(
                    axes.y_axis.point_from_proportion(
                        np.random.random()
                    )
                )

        self.play(
            *[
                particles[i].animate.move_to(targets[i])
                for i in range(len(particles))
            ],
            run_time=3
        )

        self.play(Create(axes), run_time=2)

        self.play(FadeOut(particles))

        self.wait()

        # =====================================================
        # SINE
        # =====================================================

        graph = axes.plot(
            lambda x: np.sin(x),
            color=BLUE
        )

        label = Text(
            "Sine Wave",
            font_size=30
        ).to_corner(UR)

        self.play(
            Create(graph),
            Write(label),
            run_time=3
        )

        self.wait()

        # =====================================================
        # PARABOLA
        # =====================================================

        parabola = axes.plot(
            lambda x: x**2 / 4,
            color=GREEN
        )

        self.play(
            Transform(graph, parabola),
            run_time=2
        )

        label2 = Text(
            "Parabola",
            font_size=30
        ).to_corner(UR)

        self.play(
            Transform(label, label2)
        )

        self.wait()

        # =====================================================
        # EXPONENTIAL
        # =====================================================

        expo = axes.plot(
            lambda x: np.exp(x / 3),
            x_range=[-5, 3.5],
            color=YELLOW
        )

        self.play(
            Transform(graph, expo),
            run_time=2
        )

        label3 = Text(
            "Exponential",
            font_size=30
        ).to_corner(UR)

        self.play(
            Transform(label, label3)
        )

        self.wait()

        # =====================================================
        # SPIRAL
        # =====================================================

        spiral = ParametricFunction(
            lambda t: np.array([
                0.12 * t * np.cos(t),
                0.12 * t * np.sin(t),
                0
            ]),
            t_range=[0, 8 * PI],
            color=PURPLE
        )

        self.play(
            Transform(graph, spiral),
            run_time=3
        )

        label4 = Text(
            "Infinite Patterns",
            font_size=30
        ).to_corner(UR)

        self.play(
            Transform(label, label4)
        )

        self.wait()

        # =====================================================
        # SPIRAL -> CIRCLE
        # =====================================================

        circle = Circle(
            radius=2,
            color=BLUE
        )

        self.play(
            Transform(graph, circle),
            FadeOut(label),
            run_time=3
        )

        self.wait()

        # =====================================================
        # SPINNING CIRCLE
        # =====================================================

        self.play(
            Rotate(
                graph,
                angle=4 * PI
            ),
            run_time=3
        )

        # =====================================================
        # ENERGY SPHERE
        # =====================================================

        sphere = Circle(
            radius=2,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.35
        )

        self.play(
            Transform(graph, sphere),
            run_time=2
        )

        # Pulse

        self.play(graph.animate.scale(1.2), run_time=0.4)
        self.play(graph.animate.scale(0.85), run_time=0.4)
        self.play(graph.animate.scale(1.25), run_time=0.4)

        self.wait()

        # =====================================================
        # SCREEN FILL
        # =====================================================

        self.play(
            graph.animate.scale(30),
            run_time=4
        )

        self.wait()

        # =====================================================
        # FINAL TEXT
        # =====================================================

        final_text = Text(
            "MATHEMATICS IS BEAUTIFUL",
            font_size=60,
            color=WHITE
        )

        self.play(
            FadeIn(final_text),
            run_time=2
        )

        self.wait(3)
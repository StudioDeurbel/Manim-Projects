from manim import *


class intro(Scene):
    def construct(self):
        c = Circle(radius=2, color=RED, fill_opacity=0.1)
        self.play(DrawBorderThenFill(c), run_time=0.5)
        s = Square(side_length=2, color=BLUE, fill_opacity=0.1)
        self.play(ReplacementTransform(c,s), run_time=0.5)
        t = Triangle(color=GREEN, fill_opacity=0.1).scale(2)
        self.play(ReplacementTransform(s,t), run_time=0.5)
        title1 = Text("Thanks for watching!", slant=ITALIC, font_size=48, color=WHITE)
        self.play(ReplacementTransform(t,title1), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(title1), run_time=1)

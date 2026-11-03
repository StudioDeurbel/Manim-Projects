from manim import *


class outro(Scene):
    def construct(self):
        c = Circle(radius=2, color=RED, fill_opacity=0.1)
        self.play(DrawBorderThenFill(c), run_time=0.5)
        s = Square(side_length=2, color=BLUE, fill_opacity=0.1)
        self.play(ReplacementTransform(c,s), run_time=0.5)
        t = Triangle(color=GREEN, fill_opacity=0.1).scale(2)
        self.play(ReplacementTransform(s,t), run_time=0.5)
        title = Text("Thanks for watching!", font_size=48, slant=ITALIC, color=WHITE)
        self.play(ReplacementTransform(t,title), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(title), run_time=1) 

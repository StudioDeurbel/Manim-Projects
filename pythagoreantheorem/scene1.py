from manim import *


class scene1(Scene):
    def construct(self):
        title = Text("Pythagorean Theorem", font_size=48, color=WHITE).shift(UP * 2.5)
        formula = Text("a² × b² = c²", font_size=48, color=YELLOW, slant=ITALIC).next_to(title, DOWN)
        raw_statement = (
            "In a right triangle, the square of the hypotenuse is equal\n"
            "to the sum of the squares of the other two sides."
        )
        statement = Text(raw_statement, font_size=36, color=WHITE)
        self.play(Write(title), run_time=1.5)
        self.play(Write(formula), run_time=1.5)
        self.play(Write(statement), run_time=2)
        self.wait(2)
        self.play(Unwrite(statement), run_time=1.5)
        historyraw = (
            "First recorded by an Egyptian philosopher in 1800BC\n"
            "in Berlin Papyrus 6619."
            )
        historystate = Text(historyraw, font_size=36, color=WHITE)
        self.play(Write(historystate), run_time=2)
        self.wait(2)
        self.play(Unwrite(historystate), run_time=1.5)
        historyraw2 = (
            "Popularized and usually attributed to the Greek philosopher\n"
            "Pythagoras of Samos (570BC - 495BC)"
            )
        historystate2 = Text(historyraw2, font_size=36, color=WHITE)
        self.play(Write(historystate2), run_time=2)
        self.wait(2)
        self.play(Unwrite(historystate2), run_time=1.5)
        self.play(Unwrite(title), run_time=1.5)
        self.play(Unwrite(formula), run_time=1.5)
        self.wait(0.5)
        

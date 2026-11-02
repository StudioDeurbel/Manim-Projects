from manim import *


class scene1(Scene):
    def construct(self):
        flag_bg = Rectangle(
            width=8, 
            height=5.33, # Behoudt de klassieke verhouding
            stroke_color=GRAY_B, 
            stroke_width=1, 
            fill_color=WHITE, 
            fill_opacity=1
        )
        
        # 2. Het Bourgondische Kruis (Dikte is verhoogd voor de grotere vlag)
        burgundy_red = "#C8102E" 
        cross_thickness = 0.65
        
        # Diagonale lijn van linksboven naar rechtsonder
        line1 = Line(
            start=flag_bg.get_corner(UL), 
            end=flag_bg.get_corner(DR), 
            color=burgundy_red, 
            stroke_width=cross_thickness * 100
        )
        
        # Diagonale lijn van linksonder naar rechtsboven
        line2 = Line(
            start=flag_bg.get_corner(DL), 
            end=flag_bg.get_corner(UR), 
            color=burgundy_red, 
            stroke_width=cross_thickness * 100
        )
        
        cross = VGroup(line1, line2)
        
        # 3. Animatie Sequence
        # Laat de grote witte achtergrond verschijnen
        self.play(FadeIn(flag_bg, scale=0.95), run_time=1.5)
        self.wait(0.5)
        
        # Teken het rode kruis over de hele vlag
        self.play(
            Create(line1),
            Create(line2),
            run_time=2.5,
            rate_func=linear
        )
        
        # Subtiele eindanimatie (zonder rotatie zodat hij mooi strak op het scherm blijft)
        text = Text("Bourgondische Nederlanden", font_size=32, color=WHITE, slant=ITALIC).next_to(flag_bg, DOWN)
        subtitle = Text("1384 - 1482", font_size=28, color=WHITE, slant=ITALIC).next_to(text, DOWN)
        self.play(Write(text), run_time=1)
        self.play(Write(subtitle), run_time=1)
        self.wait(2)
        self.play(FadeOut(flag_bg, line1, line2), run_time=1)
        self.play(Unwrite(text), run_time=1)
        self.play(Unwrite(subtitle), run_time=1)
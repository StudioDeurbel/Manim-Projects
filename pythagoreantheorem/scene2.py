from manim import *


class scene2(Scene):
    def construct(self):
        title = Text("Example", font_size=48, color=WHITE).shift(UP * 3)
        self.play(Write(title), run_time=1.5)
        self.wait(1)
        self.play(Unwrite(title), run_time=1.5)
        A = np.array([-1.5, -1, 0])  # Linksonder (rechte hoek)
        B = np.array([1.5, -1, 0])   # Rechtsonder
        C = np.array([-1.5, 2, 0])   # Linksboven
        
        # Teken de driehoek
        triangle = Polygon(A, B, C, color=WHITE, stroke_width=4)
        
        # Zijde labels met normale tekst
        label_a = Text("a = 3", font_size=24).next_to(Line(A, B), DOWN, buff=0.2)
        label_b = Text("b = 4", font_size=24).next_to(Line(A, C), LEFT, buff=0.2)
        
        # Voor de schuine zijde berekenen we het midden en schuiven het label iets op
        center_c = Line(B, C).get_center()
        label_c = Text("c = 5", font_size=24).move_to(center_c + np.array([0.4, 0.4, 0]))

        self.play(Create(triangle))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(0.5)

        # 3. Vierkant op zijde a (onderkant)
        square_a = Square(side_length=3, color=RED, fill_opacity=0.4)
        square_a.next_to(triangle, DOWN, buff=0)
        square_a.align_to(triangle, LEFT) 
        label_sq_a = Text("a² = 9", font_size=24).move_to(square_a.get_center())

        # 4. Vierkant op zijde b (linkerkant)
        square_b = Square(side_length=3, color=BLUE, fill_opacity=0.4)
        square_b.next_to(triangle, LEFT, buff=0)
        square_b.align_to(triangle, DOWN)
        label_sq_b = Text("b² = 16", font_size=24).move_to(square_b.get_center())

        # Animeer de eerste twee vierkanten
        self.play(Create(square_a), Write(label_sq_a))
        self.play(Create(square_b), Write(label_sq_b))
        self.wait(0.5)

        # 5. RECHTGEZET: Geometrisch vierkant op de schuine zijde (hypotenusa c) naar BUITEN
        # Loodrechte vector berekend voor een rotatie naar de buitenzijde
        v_perp = np.array([3, 3, 0]) 
        
        D = C + v_perp
        E = B + v_perp
        
        # We tekenen het vierkant door de hoekpunten in de juiste volgorde te verbinden
        square_c = Polygon(B, C, D, E, color=GREEN, fill_opacity=0.4, stroke_width=4)
        label_sq_c = Text("c² = 25", font_size=24).move_to(square_c.get_center())

        self.play(Create(square_c), Write(label_sq_c))
        self.wait(1)

        # 6. Conclusie onderaan het scherm
        conclusion = Text("9 + 16 = 25  →  a² + b² = c²", font_size=32)
        conclusion.to_edge(DOWN, buff=0.5)
        
        self.play(Write(conclusion))
        self.wait(2)
        self.play(
            Unwrite(conclusion),
            Unwrite(label_sq_a),
            Unwrite(label_sq_b),
            Unwrite(label_sq_c),
            Uncreate(square_a),
            Uncreate(square_b),
            Uncreate(square_c),
            Uncreate(triangle),
            Unwrite(label_a),
            Unwrite(label_b),
            Unwrite(label_c),
            run_time=2.0
        )
        self.wait(1)

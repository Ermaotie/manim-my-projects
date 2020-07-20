from manimlib.imports import *

# -*- coding:utf8 -*-
class scene_1(Scene):
    def construct(self):
        x = -1
        dx = 0.05
        RecGroup_1 = VGroup()
        RecGroup_2 = VGroup()
        RecGroup_3 = VGroup()
        scale = 2.7
        circle = Circle(radius=scale, color=BLUE).set_fill(color=BLUE, opacity=1)
        while x < 1:
            x = x + dx
            rec = Rectangle(width=dx, height=2*np.sqrt(1-x*x), color=BLUE).scale(scale).set_fill(color=BLUE, opacity=1)
            rec.shift(RIGHT*scale*x)
            RecGroup_1 = VGroup(RecGroup_1, rec)
            self.play(FadeIn(rec), run_time=0.1)
        span = Brace(circle, DOWN)
        text = TextMobject("2R").next_to(span, DOWN)
        self.play(ShowCreation(span),
                  Write(text))
        self.wait()
        self.play(FadeOut(text),
                  FadeOut(span))
        self.wait()
        self.play(ApplyMethod(RecGroup_1.set_opacity, 0.5))
        x = -1
        dx = 0.03
        while x < 1:
            x = x + dx
            rec = Rectangle(width=dx, height=2*np.sqrt(1-x*x), color=BLUE).scale(scale).set_fill(color=BLUE, opacity=1)
            rec.shift(RIGHT*scale*x)
            RecGroup_2 = VGroup(RecGroup_2, rec)
            self.play(FadeIn(rec), run_time=0.05)
        self.play(FadeOut(RecGroup_1))
        self.play(ApplyMethod(RecGroup_2.set_opacity, 0.5))
        x = -1
        dx = 0.01
        self.wait()
        while x < 1:
            x = x + dx
            rec = Rectangle(width=dx, height=2*np.sqrt(1-x*x), color=BLUE).scale(scale).set_fill(color=BLUE, opacity=1)
            rec.shift(RIGHT*scale*x)
            RecGroup_3 = VGroup(RecGroup_3, rec)
            self.play(FadeIn(rec), run_time=0.01)
        self.play(FadeOut(RecGroup_2))
        self.play(ApplyMethod(RecGroup_3.set_opacity, 0.5))
        self.play(FadeIn(circle))
        self.wait()
        self.play(FadeOut(RecGroup_3))
        self.play(ApplyMethod(circle.shift, (6-scale)*LEFT))

        formula = TexMobject("\int_{-R}^{R}\sqrt{1-x^2}dx", "=", "\pi R^2")
        formula[0].move_to(circle.get_center()+(scale*1.8*RIGHT)+scale*UP*0.7)
        self.play(Write(formula[0]))
        for i in range(1,3):
            formula[i].next_to(formula[i-1], RIGHT,buff=0.2)
            self.play(Write(formula[i]))
        self.wait()

class scene_2(ThreeDScene):
    def construct(self):
        def Column(dh,h):
            return ParametricSurface(
                lambda u, v: np.array([
                    scale*np.sqrt(1-h*h)*np.cos(u),
                    scale*np.sqrt(1-h*h)*np.sin(u),
                    v
                ]), u_min=0, u_max=TAU, v_min=0, v_max=dh,checkerboard_colors=None,stroke_color=BLUE,fill_color=BLUE,fill_opacity=0.8
            )
        self.set_camera_orientation(phi=35 * DEGREES, theta=-60*DEGREES, distance=5)
        scale = 1.5
        h = -1
        dh = 0.1
        while h < 1 - 1e-5:
            h += dh
            circle_1 = Circle(radius=scale*np.sqrt(1-h*h),fill_color=BLUE,fill_opacity=0.8,color=BLUE).shift(OUT*h*scale)
            circle_2 = circle_1.copy().shift(OUT*scale*dh)
            column = Column(dh,h).shift(OUT*h*scale)
            Col = VGroup(column, circle_1, circle_2)
            self.play(ShowCreation(Col))
        self.wait()

class text_1(Scene):
    def construct(self):
        text = TextMobject(
            '我们都知道',
            '圆的面积公式为',
            '$S = \\pi R^2$',
            '球的体积为',
            '$V = \\frac{4}{3}\\pi R^3$',
            '那么四维甚至',
            '更高维度的“球”',
            '它的“体积”应该如何求得呢？'
        )
        text[0].to_corner(UL, buff=0.5)
        for i in range(1, len(text)):
            text[i].next_to(text[i-1],DOWN, aligned_edge=LEFT)
        self.play(Write(text), run_time=10)
        self.wait()
        text_2 = TextMobject(
            '为了便于理解',
            '我们从低维开始',
            '对球的体积展开探索'
        )
        text_2[0].to_corner(UR, buff=2.5)
        for j in range(1, len(text_2)):
            text_2[j].next_to(text_2[j - 1], DOWN, aligned_edge=LEFT)
        self.play(Write(text_2, run_time = 10))
        self.wait()


class text_2(Scene):
    def construct(self):
        text = TextMobject(
            '    当我们回头再看一遍的时候，',
            '我们发现',
            '二维的圆的面积，',
            '是由一条长度定义过的线段，',
            '沿着垂直的方向形成的',
            '，三维的球的体积',
            '，也是由一个面积定义过的圆盘，',
            '沿着垂直的方向形成的',
            '，所以，四维的“球”其实是由体积定义过的球,',
            '沿着垂直三个坐标轴的方向形成的'
        ).scale(0.7)
        # text[0].to_corner(UL, buff=1)
        # for i in range(1, len(text)):
        #     text[i].next_to(text[i-1], DOWN, aligned_edge=LEFT)
        text[4].set_color(BLUE)
        text[7].set_color(BLUE)
        text[9].set_color(BLUE)
        self.play(Write(text), run_time=13)
        self.wait()


class text_3(Scene):
    def construct(self):
        text = TextMobject(
            '    虽然我们只能以三维的视角来观察,',
            '但是数学能帮我们看到更多,',
            '我们来重新审视一下“体积”这个概念。',
            '在高等数学中，我们可以将',
            '长度，面积，体积等',
            '抽象为一个可供度量的数字,称为',
            '测度',
        ).scale(0.8)
        text[-1].set_color(BLUE).scale(1.1)
        self.play(Write(text), run_time=10)
        self.wait()


class text_4(Scene):
    def construct(self):
        text_1 = TextMobject(
            '球面，三维空间中到定点的长度是定长的点集',
        ).shift(2*UP)
        text_2 = TextMobject('圆， 二维空间中到定点的长度是定长的点集').next_to(text_1,DOWN,aligned_edge=LEFT)
        text_3 = TextMobject('“一维的圆”，线上到定点的长度是定长的点集').next_to(text_2, DOWN,aligned_edge=LEFT)
        text3p = TextMobject('即  两个点  ').next_to(text_3, DOWN, aligned_edge=LEFT)
        text4 = TextMobject('而“一维”的圆，它的测度(M)即为长度').next_to(text3p, DOWN,aligned_edge=LEFT)
        self.play(Write(text_1), run_time=1.618)
        self.play(Write(text_2), run_time=1.618)
        self.play(Write(text_3), run_time=1.618)
        self.play(Write(text3p), run_time=1.618)
        self.play(Write(text4), run_time=1.618)
        self.wait()

class fml_1(Scene):
    def construct(self):
        fml = TexMobject(r'M_1 = \int_{-R}^{R}dx_1 = 2R')
        self.play(ShowCreation(fml))
        self.wait()
        self.play(ApplyMethod(fml.shift, 3*UP))
        dot = Dot(color=RED)
        line = Line(LEFT, RIGHT).scale(2).set_color(BLUE)
        brace = BraceLabel(line, '2R')
        self.play(ShowCreation(dot))
        self.play(Write(line), run_time=3)
        self.play(ShowCreation(brace))
        self.wait()

class fml_2(Scene):
    def construct(self):
        fml = TexMobject(r'M_2 = \int_{-R}^{R}dx_1\int_{-\sqrt{R^2-x_1^2}}^{\sqrt{R^2-x_1^2}}dx_2 = \pi R^2')
        self.play(ShowCreation(fml))
        self.play(ApplyMethod(fml.shift, 3 * UP))
        self.wait(8)


class fml_3(Scene):
    def construct(self):
        fml = TexMobject(r'M_3 = \int_{-R}^{R}dx_1\int_{-\sqrt{R^2-x_1^2}}^{\sqrt{R^2-x_1^2}}dx_2\int_{-\sqrt{R^2-x_1^2-x_2^2}}^{\sqrt{R^2-x_1^2-x_2^2}}dx_3')
        self.play(ShowCreation(fml),run_time=3)
        self.play(ApplyMethod(fml.shift, 3 * UP))
        self.wait(8)


class fml_4(Scene):
    def construct(self):
        fml = TexMobject(r'M_4 = \int_{-R}^{R}dx_1\int_{-\sqrt{R^2-x_1^2}}^{\sqrt{R^2-x_1^2}}dx_2\int_{-\sqrt{R^2-x_1^2-x_2^2}}^{\sqrt{R^2-x_1^2-x_2^2}}dx_3\int_{-\sqrt{R^2-x_1^2-x_2^2-x_3^2}}^{\sqrt{R^2-x_1^2-x_2^2-x_3^2}}dx_4').scale(0.8)
        self.play(ShowCreation(fml),run_time=3)
        self.play(ApplyMethod(fml.shift, 3 * UP))
        self.wait(5)
        fmln = TexMobject(r'M_4 = \frac{1}{2}{\pi}^2R^4').shift(3*UP)
        self.play(ReplacementTransform(fml, fmln),run_time=2)
        self.wait()
        fm = TexMobject(r'M_n = M_{n-1}\int_{-\sqrt{R^2-x_1^2-x_2^2-\dots -x_{n-1}^2}}^{\sqrt{R^2-x_1^2-x_2^2-\dots -x_{n-1}^2}}dx_n')
        self.play(Write(fm),run_time=3)
        self.wait()


class pl(Scene):
    def construct(self):
        S = TexMobject('V = \\frac{4}{3}\\pi R^3').scale(3)
        self.play(Write(S))
        self.wait(2)










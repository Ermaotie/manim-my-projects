from manimlib.imports import *
from from_3b1b.active.diffyq.part2.fourier_series import FourierCirclesScene
from numpy import sqrt

class Target(Scene):
    def construct(self):
        circle_list = []
        shoot_list = [
            [1, 1, 0],
            [-2, -1, 0],
            [0, 0, 0],
            [2, 0, 0]
        ]
        aim_scape = VGroup(
            Circle(radius=0.7, color=BLUE, fill_color=BLUE, fill_opacity=0.6),
            Line([0, 0.7, 0], [0, -0.7, 0]),
            Line([0.7, 0, 0], [-0.7, 0, 0])
        )
        for i in range(-1, 2):
            for j in range(-2, 3):
                cir = Circle(color=YELLOW, fill_color=YELLOW, radius=0.5, fill_opacity=0.5)
                cir.shift([1.5*j, 1.5*i, 0])
                self.play(FadeIn(cir))
                circle_list.append(cir)
        self.wait()
        self.play(ShowCreation(aim_scape))
        def shoot(position):
            odn = (2+position[0])+(1+position[1])*5
            self.play(ApplyMethod(aim_scape.next_to, circle_list[odn], 0))
            self.wait()
            self.play(ApplyMethod(circle_list[odn].set_fill, GREY),
                      ApplyMethod(circle_list[odn].set_color, GREY)
                      )
            text = TextMobject('( ', str(position[0]), ', ', str(position[1]), ' )').scale(0.8)
            text.next_to(circle_list[odn], DOWN, 0.1)
            self.play(Write(text))
        for k in shoot_list:
            shoot(k)
        # shoot(shoot_list[0])

class Heart(Scene):
    def construct(self):
        cir_1 = Circle(radius=1, color=RED, fill_color=RED, fill_opacity=0.5)
        cir_2 = Circle(radius=1, color=RED, fill_color=RED, fill_opacity=0.5)
        square = Square(color=RED, fill_color=RED, fill_opacity=0.5)
        square.rotate(PI/4)
        cir_1.shift(2**0.5/2*UL)
        cir_2.shift(2**0.5/2*UR)
        VGroup_1 = VGroup(cir_1, cir_2, square)

        rec_1 = Rectangle(height=4, width=.5, color=RED, fill_color=RED, fill_opacity=0.5).rotate(PI/4)
        rec_2 = rec_1.copy().rotate(PI/2)
        VGroup_2 = VGroup(rec_1, rec_2)

        square_1 = Square(color=RED, fill_color=RED, fill_opacity=0.5).scale(1.5)
        cir_3 = Circle(radius=0.4, color=RED, fill_color=RED, fill_opacity=0.5)
        cir_3.shift([-0.8, 0.6, 0])
        cir_4 = cir_3.copy().shift(1.6*RIGHT)
        VGroup_3 = VGroup(square_1, cir_3, cir_4)
        VGroup_3.next_to(RIGHT_SIDE, LEFT)

        V_all = VGroup(VGroup_1, VGroup_2, VGroup_3)

        _line = Line(LEFT_SIDE, RIGHT_SIDE, color=RED)
        _line.shift(1.4*DOWN)
        text = TextMobject('Sophon helps me', color=RED).shift(1.4*DOWN).scale(1.5)
        self.play(
            ShowCreation(VGroup_1),
        )
        self.play(ApplyMethod(VGroup_1.next_to, LEFT_SIDE))
        self.play(Write(VGroup_2))
        self.play(ShowCreation(VGroup_3))
        self.play(
            ApplyMethod(cir_3.set_fill, BLACK),
            ApplyMethod(cir_4.set_fill, BLACK)
        )
        self.play(ApplyMethod(V_all.set_opacity, 1))
        self.play(ApplyMethod(V_all.shift, 0.5*UP))
        self.play(Write(_line))
        self.play(Transform(_line, text), run_time=2)
        self.wait(2)


class Paint_sin(GraphScene):
    CONFIG = {
            # "x_min": -10,
            # "x_max": 10,
            # "y_min": -1.5,
            # "y_max": 1.5,
            # "y_tick_frequency": 0.5,
            'graph_origin': ORIGIN,
            # "x_labeled_num": range(-10, 12, 2),
            # 'x_leftmost_tick': 4,
            # "x_axis_width": 1
        }
    def construct(self):
        self.setup_axes(animate=False)
        func_gragh = self.get_graph(
            lambda x, y: np.array([

            ])
        )
        self.play(ShowCreation(func_gragh))
        self.wait()
    # def setup_axes(self, animate=False):
    #     pass

class FourierOfPiSymbol_1(FourierCirclesScene):
    CONFIG = {
        "n_vectors": 51,
        "center_point": ORIGIN,
        "slow_factor": 0.1,
        "n_cycles": 1,
        "tex": "\\pi",
        "start_drawn": False,
        "max_circle_stroke_width": 1,
    }

    def construct(self):
        self.add_vectors_circles_path()
        for n in range(self.n_cycles):
            self.run_one_cycle()

    def add_vectors_circles_path(self):
        path = self.get_path()
        coefs = self.get_coefficients_of_path(path)
        vectors = self.get_rotating_vectors(coefficients=coefs)
        circles = self.get_circles(vectors)
        self.set_decreasing_stroke_widths(circles)
        # approx_path = self.get_vector_sum_path(circles)
        drawn_path = self.get_drawn_path(vectors)
        if self.start_drawn:
            self.vector_clock.increment_value(1)

        self.add(path)
        self.add(vectors)
        self.add(circles)
        self.add(drawn_path)

        self.vectors = vectors
        self.circles = circles
        self.path = path
        self.drawn_path = drawn_path


class My_Arrow(Scene):
    def construct(self):
        text = TextMobject(
            'L C G',
            'D Z Y'
        )
        text[0].to_edge(LEFT)
        text[1].to_edge(RIGHT)
        arrow = Arrow(text[0].get_right(), text[1].get_left(), buff=.1)
        self.play(
            ShowCreation(text)
        )
        self.wait()
        self.play(GrowArrow(arrow))
        self.wait()


class chemisty(Scene):
    CONFIG = {
        "stroke_width": 3,
        "stroke_opacity": 1
    }
    def construct(self):
        formulae = TextMobject("\chemfig{A*5(-B=C-D-E=)}")
        self.play(Write(formulae), run_time=3)
        self.wait()

class E_Loge(Scene):
    def construct(self):
        mao_1 = RegularPolygon(5, color='Orange').rotate(PI / 6).scale(1.8).rotate(PI/180*42).shift(UP*0.2)
        mao_2 = mao_1.copy().scale(1.1)
        text = TextMobject("Fe", color=GOLD).scale(1.5)
        surround_cir = Circle(radius=1, color=GOLD)
        center = VGroup(text, surround_cir).shift(DOWN*0.2)
        all = VGroup(mao_1, mao_2, text, surround_cir)
        U_line = Underline(mao_2, small_buff=1, color=GREY)
        name = TextMobject("二", '·', "茂", '·', "铁", color=GOLD).move_to(U_line)


        mao_1.to_edge(LEFT)
        mao_2.to_edge(RIGHT)

        self.play(
            Write(mao_1),
            Write(mao_2)
        )
        self.play(Rotate(mao_1, PI/180*72*3),
                  Rotate(mao_2, PI/180*72*4),
                  run_time=3)
        self.play(ApplyMethod(mao_2.move_to, ORIGIN),
                  ApplyMethod(mao_1.move_to, ORIGIN),
                  run_time=1.2)

        self.play(FadeIn(center))
        self.play(ApplyMethod(all.shift, UP*0.8))
        self.play(FadeIn(U_line, ORIGIN))
        self.play(Transform(U_line, name))
        self.wait()

class San_Logo(Scene):
    def construct(self):
        back_gragh = RegularPolygon(int=6).rotate(PI/6)
        text = TextMobject("炔", color=RED).scale(2)
        line1 = Line([0, 0, 0], [0, 1, 0], color=BLUE).shift([-0.72, -0.5, 0]).scale(0.9)
        line2 = line1.copy().rotate_about_origin(2*PI/3)
        line3 = line2.copy().rotate_about_origin(2 * PI / 3)
        group = VGroup(back_gragh, text, line1, line2, line3)
        name = TextMobject("三 聚 乙 炔", color=RED, opacity=0.7).shift(DOWN*0.5)
        self.play(
            Write(back_gragh),
            run_time=3
        )
        self.play(
            Write(line1),
            Write(line2),
            Write(line3)
        )
        self.play(Write(text))
        self.wait()
        self.play(ApplyMethod(group.shift, UP))
        self.play(Write(name))
        self.play(ApplyMethod(name.set_opacity, 1))
        self.wait()

class demo_text(Scene):
    def construct(self):
        text = TextMobject(
            """
            111113333333333333333333333333333333333333333333333333333
            2222222222222222
            3333333333333333333
            44444444444444444444444
            5555555555555555555555555
            """
        )
        self.play(Write(text))
        self.wait()
class ellipse(Scene):
    def construct(self):
        cir_1 = Ellipse(height=2, width=4, fill_color=RED, fill_opacity = 0.5)
        self.play(ShowCreation(cir_1))
        self.wait()
        self.play(ApplyMethod(cir_1.set_opacity, 1))
        self.wait()

class tangle_test(Scene):
    def construct(self):
        tan = RegularPolygon(3)
        self.play(FadeInFromPoint(tan, ORIGIN))
        self.wait()

class update_demo(Scene):
    def construct(self):
        squ = Square(color=RED, fill_color=RED)
        label = TextMobject('这是一个方块')

        squ.to_edge(UP)
        label.add_updater(lambda x: x.next_to(squ, RIGHT, buff=1))

        self.play(ApplyMethod(squ.to_edge, DOWN), ShowCreation(label), run_time=5)
        self.wait()

class draw_a_ellipse(Scene):
    def construct(self):
        dot_a = Dot(np.array([-sqrt(3), 0, 0]))
        dot_b = dot_a.copy().shift(RIGHT*2*sqrt(3))
        dt = 0.1

class ellipse(Scene):
    def get_ellipse(self, a, b, **kwargs):
        return ParametricFunction(lambda t: a*np.cos(t)*RIGHT+b*np.sin(t)*UP, t_min=-PI, t_max=PI)

    def get_ellipse_tg_line(self, a, b, x0, y0, **kwargs):
        return ParametricFunction(lambda t: (y0+b**2*x0*t)*UP+(x0-a**2*y0*t)*RIGHT, t_min=-10, t_max=10)

    CONFIG = {"const_a": 3.0, "const_b": 2.0, "theta": PI/6}

    def construct(self):
        var = ValueTracker(self.theta)
        graph = self.get_ellipse(self.const_a, self.const_b)\
            .set_color("#0077FF")
        dot_ = Dot().add_updater(lambda a: a.move_to(
            self.const_a*np.cos(var.get_value())*RIGHT+self.const_b*np.sin(var.get_value())*UP))
        tg = self.get_ellipse_tg_line(self.const_a, self.const_b,
                                      self.const_a*np.cos(var.get_value()),
                                      self.const_b*np.sin(var.get_value())).set_color("#FFFF00")
        tg.add_updater(lambda m: m.become(
            self.get_ellipse_tg_line(self.const_a, self.const_b,
                                     self.const_a * np.cos(var.get_value()),
                                     self.const_b*np.sin(var.get_value())).set_color("#FFFF00")))
        self.add(graph)
        self.add(tg)
        self.add(dot_)
        self.play(var.increment_value, 2*PI/3)
        self.play(var.increment_value, -PI/2)
        self.wait(0.8)


class circle_tg(Scene):
    CONFIG = {
        'radius': 2,
        'theta': PI/4
    }
    def get_Func(self, r, x0, y0, **kwargs):
        return ParametricFunction(lambda t: (y0+r**2*x0*t)*UP+(x0-r**2*y0*t)*RIGHT, t_min=-15, t_max=15)
    def construct(self):
        graph = Circle(radius=self.radius, fill_color=BLUE)
        var = ValueTracker(self.theta)
        dot = Dot().add_updater(lambda d: d.move_to(np.array([
            2*np.cos(var.get_value()),
            2*np.sin(var.get_value()),
            0
        ])))

        tg = self.get_Func(self.radius, self.radius*np.cos(var.get_value()), self.radius*np.sin(var.get_value()))
        tg.add_updater(
            lambda k: k.become(
                self.get_Func(self.radius, self.radius * np.cos(var.get_value()), self.radius * np.sin(var.get_value()))
            )
        )

        self.add(graph, tg)
        self.play(var.increment_value, PI, run_time=10)
        self.wait()


class buy_2(Scene):
    def construct(self):
        text_1 = TextMobject("UP主已经申请过一次,所以没法继续录制",
                             "接下来的流程",
                             "身份认证",
                             "学生认证",
                             "完成考验（百度+常识即可）",
                             "选择镜像",
                             "购买成功")
        text_2 = TextMobject("1",
                             "22",
                             "333",
                             "4444",
                             "55555",
                             "666666",
                             "7777777")
        text_3 = TextMobject("由于为阿里云服务器",
                             "需要先对实例进行管理，才能正常连接使用",
                             "分别是",
                             "ssh密钥创立与绑定",
                             "安全组放行",
                             "在设置时旁边的提示会有很大帮助",
                             )
        # text_1[0].to_corner(UL)
        # # text_1[0].to_edge(UP)
        # for i in range(1, len(text_1)):
        #     text_1[i].next_to(text_1[i-1], DOWN,
        #                       aligned_edge=LEFT
        #                       )
        group = VGroup()
        for i in text_3:
            group.add(i)
        group.arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT)
        self.play(Write(group), run_time=10)

        # text_3[0].to_corner(UL)
        # for i in range(1, len(text_3)):
        #     text_3[i].next_to(text_3[i - 1], DOWN, aligned_edge=LEFT)
        # self.play(Write(text_3))

class TD_test(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = Sphere()
        self.set_camera_orientation(PI/4, 3*PI/4, 9, 0)
        self.add(axes)
        self.wait()
        surfice = ParametricSurface(lambda u, v: np.array([u, v, np.sin(u+v)]),
                                    u_min=-5,
                                    u_max=5,
                                    v_min=-5,
                                    v_max=5)
        # self.play(ShowCreation(surfice), run_time=10)
        self.add(surfice)
        self.wait()
class my_spiral_line(ThreeDScene):
    def construct(self):
        # self.set_to_default_angled_camera_orientation(self.default_angled_camera_orientation_kwargs)
        axes = ThreeDAxes()
        self.set_camera_orientation()
        spiral = ParametricFunction(lambda t: complex_to_R3(np.exp(1j*2*t))+0.5*t*OUT, t_min=0, t_max=10)
        self.add(spiral, axes)
        self.wait()


class chemfig(Scene):
    def construct(self):
        pass

class zgd(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        # var = ValueTracker(self.theta)
        self.set_camera_orientation(0, PI/2, 15)
        dot_a = Dot([0, 3, 0])
        dot_b = Dot([3.5, 1, 2.5])
        ball = Sphere().scale(0.2)
        ball.move_to(dot_a)
        ball_b = ball.copy().move_to(dot_b)
        text = TextMobject('A', 'B')
        text[0].next_to(dot_a, RIGHT, buff=0.2)
        text[1].next_to(dot_b, RIGHT, buff=0.2)
        self.add(axes, text)
        dt = 1/10
        da = 1*DEGREES
        a = 0
        for i in range(45):
            a += da
            self.set_camera_orientation(PI/2 - a, a)
            self.wait(dt)
        self.wait()


class wlzy(Scene):
    def construct(self):
        text_1 = TexMobject(
            '''
            x^2+y^2=z^2
            '''
        )
        self.play(Write(text_1))
        self.wait()
# class test_1(Scene):
#     def construct(self):


class Processing(Scene):
    CONFIG = {
        'camera_config':{
            'background_color': WHITE,
        }
    }
    def construct(self):
        line = Line(color = BLUE).shift(2.5*UP).scale(3)
        dot = Dot(color = BLUE).shift(1.5*UP)
        P = Dot(line.get_left(), color=RED)
        line_active = Line(P,dot, color=PINK, stroke_width=0.9)
        line_t = line_active.copy().scale(10).rotate(TAU/4).set_color(GRAY)
        dt = 0.1
        self.play(ShowCreation(line),Write(dot),FadeIn(P))
        # self.add(line_active, line_t)
        self.play(
            Write(line_active),
        )
        self.play(
            Write(line_t)
        )
        self.wait()
        t = 0
        while t < 6:
            # PP = P.add_updater(
            #             lambda p: p.shift(dt*RIGHT)
            # )
            P.shift(dt * RIGHT)
            line_active.add_updater(
                            lambda l: l.become(Line(P, dot, color=PINK,stroke_width=0.9))
            )
            # line_2 = line_t.add_updater(
            #     lambda l: l.copy().become(line_active.scale(10).rotate(TAU/4).set_color(YELLOW))
            # )
            # line_1 = line_active.become(Line(P, dot, color=PINK))
            line_2 = line_t.become(line_active.scale(10).rotate(TAU / 4).set_color(GRAY)).set_stroke(width=1.1)
            self.add(line_2.copy())
            self.wait(dt)
            t = t+dt
        self.wait()
class math_1(GraphScene):
    def construct(self):
        self.setup_axes(animate=True)
        exp = self.get_graph(self.eee,color=BLUE, x_min=0.01)
        sq = self.get_graph(self.square, x_min=0)
        self.play(ShowCreation(exp),ShowCreation(sq), run_time= 3)
        self.wait()

    def eee(self, x):
        return np.exp(x)*np.log(x)
        # return np.log2(x)
    def square(self,x):
        return np.square(x)



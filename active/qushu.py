from manimlib.imports import *


class intruduction(Scene):
    CONFIG = {
        't_size': 0.5,
        'camera_config': {
            'background_color': WHITE,
        },
    }

    def construct(self):
        Q = TextMobject(
            'Question:',
            '在 [0, 1]上一个一个地随机取数',
            '当它们的和大于一时停止',
            '求停止时取了几个数的数学期望'
        )
        Q = Text('Question:').scale(0.5).to_corner(UL, buff=0.8)
        sepLine = Line(LEFT_SIDE, RIGHT_SIDE, color=BLACK).to_edge(UP, buff=1.5)
        Des1 = Text('在 [0, 1]上一个一个地随机取数').next_to(sepLine, DOWN, buff=0.5).scale(0.5)
        Des2 = Text('当它们的和大于一时停止').scale(0.5).next_to(Des1, DOWN).align_to(Des1, LEFT)
        Des3 = Text('求停止时取了几个数的数学期望?').scale(0.5).next_to(Des2, DOWN).align_to(Des2, LEFT)
        self.play(ShowCreation(Q),
                  ShowCreation(sepLine))
        self.play(
            ShowCreation(Des1),
            run_time=1.5,
        )
        self.play(
            ShowCreation(Des2),
            run_time=1.5
        )
        self.play(
            ShowCreation(Des3),
            run_time=1.5,
        )
        self.wait(2)
        sepLine2 = sepLine.copy().to_edge(DOWN, buff=2.5)

        R = Text('Requirements:').scale(self.t_size).next_to(sepLine2, UP).align_to(Q, LEFT)
        Need1 = Text('一点点的泰勒公式').scale(self.t_size).next_to(sepLine2, DOWN).align_to(Des1, LEFT)
        Need2 = Text('数学期望的含义').scale(self.t_size).next_to(Need1, DOWN).align_to(Des1, LEFT)
        self.play(
            ShowCreation(sepLine2),
            ShowCreation(R),
            run_time=1.2
        )
        self.play(
            Write(Need1),
            Write(Need2),
            run_time=1.4
        )
        self.wait(3)


class Convertion1(Scene):
    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }
    size = 2

    def construct(self):
        slogan = Text('Solution:').scale(0.5).to_corner(UL, buff=0.7)
        sepline = Line(LEFT_SIDE, RIGHT_SIDE, color=BLACK).to_edge(UP, buff=1.4)
        text1 = TextMobject('设取出的第一个数为 $x_1$ ,第二个数为 $x_2$ ,第三个数为 $x_3$ ,以此类推...', color=BLACK).scale(0.8).next_to(
            sepline, DOWN).to_edge(LEFT, buff=1)
        text2 = TextMobject('设n为停止时取出的个数,$P(N=n)$为取出n个球停止的概率。', color=BLACK).scale(0.8).next_to(text1, DOWN).align_to(
            text1, LEFT)
        text3 = TextMobject(r'第一个数字是一定可以取到的也就是说 n大于等于2,所以$P(N\geqslant 2)=1$', color=BLACK).scale(0.65).next_to(text2, DOWN, buff=0.5).align_to(text2, LEFT).shift(RIGHT * 0.5)

        line = Line(color=DARK_GRAY).next_to(text3, DOWN, buff=2).scale(self.size)
        arrow = ArrowTip(color=BLUE_A).scale(self.size).rotate(PI/2).next_to(line, UP).shift(self.size*LEFT)
        brace = Brace(line, DOWN,color=ORANGE)
        num = TextMobject('1',color=BLACK).next_to(brace,DOWN)
        dec = DecimalNumber(0, num_decimal_places=2, color=DARK_BLUE)

        dec.add_updater(
            lambda m: m.next_to(arrow, UP).align_to(arrow)
        )
        dec.add_updater(
            lambda m: m.set_value((self.size+arrow.get_center()[0])/self.size/2+0.04)
        )

        self.play(ShowCreation(slogan), ShowCreation(sepline), run_time=1.4)
        self.play(
            ShowCreation(text1),
            run_time=3,
            rate_func=linear
        )
        self.wait()
        self.play(
            ShowCreation(text2),
            run_time=3,
            rate_func=linear
        )
        self.wait()
        self.play(ShowCreation(text3), ShowCreation(line), run_time=3,rate_func=linear)
        self.wait(2)
        self.play(ShowCreation(brace), ShowCreation(arrow), Write(dec),Write(num))
        self.wait(2)
        self.play(
            ApplyMethod(arrow.shift, np.array([line.get_length(),0,0])),
            run_time=5,
            rate_func=there_and_back
        )
        self.wait(3)


class Convertion2(Scene):
    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }
    size = 2
    def construct(self):
        slogan = Text('Solution:').scale(0.5).to_corner(UL, buff=0.7)
        sepline = Line(LEFT_SIDE, RIGHT_SIDE, color=BLACK).to_edge(UP, buff=1.4)
        self.add(slogan,sepline)

        text1 = TextMobject('取第二个数 $x_2$ 时,似乎直接解决不太方便',color=BLACK).next_to(sepline, DOWN)
        line = Line(color=DARK_GRAY).next_to(text1, DOWN, buff=3).scale(self.size)
        text2 = TextMobject('$x_1$','+','$x_2$','=', color=BLACK).next_to(line, RIGHT, buff=0.8)
        text2[0].set_color(DARK_BLUE)
        text2[2].set_color(RED)

        arrow1 = ArrowTip(color=BLUE_A).scale(self.size).rotate(PI / 2).next_to(line, UP).shift(self.size * LEFT)
        dec1 = DecimalNumber(0, num_decimal_places=2, color=DARK_BLUE)
        arrow2 = ArrowTip(color=BLUE_A).scale(self.size).rotate(PI / 2).next_to(line, UP).shift(self.size * RIGHT/2)
        dec2 = DecimalNumber(0, num_decimal_places=2, color=RED)
        sum = DecimalNumber(0, num_decimal_places=2, color=BLACK).next_to(text2,RIGHT)
        dec1.add_updater(
            lambda m: m.next_to(arrow1, UP).align_to(arrow1)
        )
        dec1.add_updater(
            lambda m: m.set_value((self.size + arrow1.get_center()[0]) / self.size / 2)
        )
        dec2.add_updater(
            lambda m: m.next_to(arrow2, UP).align_to(arrow1)
        )
        dec2.add_updater(
            lambda m: m.set_value((self.size + arrow2.get_center()[0]) / self.size / 2)
        )
        sum.add_updater(lambda m: m.set_value(dec1.get_value()+dec2.get_value()))

        self.play(Write(text1),run_time=1.5)
        self.play(ShowCreation(line))
        self.play(ShowCreation(arrow1), Write(dec1))
        self.wait(2)
        self.play(
            ApplyMethod(arrow1.shift, np.array([line.get_length(), 0, 0])),
            run_time=5,
            rate_func=there_and_back
        )
        self.wait(2)
        self.play(FadeIn(arrow2), FadeIn(dec2),FadeIn(sum),FadeIn(text2))
        self.wait(2)
        self.play(
            ApplyMethod(arrow1.shift, np.array([line.get_length(), 0, 0])),
            ApplyMethod(arrow2.shift, np.array([-line.get_length()/2, 0, 0])),
            run_time=5,
            rate_func=there_and_back
        )
        self.wait(3)


class Convertion3(GraphScene):
    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
    }
    size = 3

    def construct(self):
        slogan = Text('Solution:').scale(0.5).to_corner(UL, buff=0.7)
        sepline = Line(LEFT_SIDE, RIGHT_SIDE, color=BLACK).to_edge(UP, buff=1.4)
        self.add(slogan,sepline)

        text1 = TextMobject('不妨考虑一下','$x_1$','+','$x_2$','>1的对立面,即和小于等于一的概率',color=BLACK).next_to(sepline,DOWN)
        text1[1].set_color(DARK_BLUE)
        text1[3].set_color(RED)
        # text2 = TextMobject('$x_1$', '+', '$x_2$', '=', color=BLACK).to_edge(RIGHT, buff=0.8)
        # text2[0].set_color(DARK_BLUE)
        # text2[2].set_color(RED)

        axis = Axes(x_min=0,y_min=0,x_max=1.3*self.size,y_max=1.3*self.size)
        square = Square(color=BLACK).scale(self.size/2).move_to(ORIGIN,aligned_edge=DL)
        ver = square.get_vertices()
        line = Line(ver[0], ver[2],color = PURPLE_A).scale(1.1)
        tag = TextMobject('$x_1$','+','$x_2$','=','1',color=PURPLE_A).next_to(line,DR)
        tag[0].set_color(DARK_BLUE)
        tag[2].set_color(RED)
        sumTag = tag[0:-1].copy().next_to(axis,RIGHT,buff=1.5).align_to(ORIGIN)
        sum = DecimalNumber(0, num_decimal_places=2, color=PURPLE_C).next_to(sumTag)
        tri = Polygon(ver[0],ver[2],ver[3],stroke_width=0,fill_color=GREEN_A,fill_opacity=0.8)

        dot1 = Dot(color=DARK_BLUE).move_to((ver[2]-ver[3])/3)
        # x1 = (dot1.get_center()-axis[0].get_left())[1]
        dot2 = Dot(color=RED).move_to((ver[0]-ver[3])*2/3)
        # x2 = (dot2.get_center() - axis[1].get_bottom())[0]
        line1 = Line(dot1.get_center(),dot1.get_center()+self.size*UP,color=DARK_BLUE).align_to(dot1,DOWN)
        line2 = Line(dot2.get_center(),dot2.get_center()+self.size*RIGHT,color=RED_B).align_to(dot2,LEFT)
        dot3 =Dot(color=PURPLE_C)

        Group = VGroup(axis, line, line1, line2, dot1, dot2, dot3,tri,square,tag,sumTag,sum).to_corner(DL,buff=2.2).shift(DOWN)
#         Add_updater

        sum.add_updater(lambda n: n.set_value(((dot1.get_center()-axis[0].get_left())[0]+(dot2.get_center() - axis[1].get_bottom())[1])/self.size))
        line1.add_updater(lambda l: l.shift(np.array([(dot1.get_center()-line1.get_center())[0],0,0])))
        line2.add_updater(lambda l: l.shift(np.array([0,(dot2.get_center()-line2.get_center())[1],0])))
        dot3.add_updater(lambda d: d.move_to(np.array([dot1.get_center()[0],dot2.get_center()[1],0])))

        # Play
        self.play(Write(text1),run_time=3,rate_func=linear)
        self.wait()
        self.play(
            ShowCreation(axis),
            run_time=1.3
        )
        self.play(
            ShowCreation(square),
        )
        self.wait()
        self.play(
            ShowCreation(line),
            ShowCreation(tag),
            run_time=1.6
        )
        self.wait(2.8)
        self.play(
            FadeIn(tri),
        )
        self.wait()
        self.play(
            ShowCreation(dot1),
            ShowCreation(line1),
            run_time=1.5
        )
        self.wait()
        self.play(
            dot1.shift, RIGHT*self.size/3,
            run_time=1.5,
            rate_func=there_and_back
        )
        self.wait()
        self.play(
            ShowCreation(dot2),
            ShowCreation(line2),
        )
        self.wait()
        self.play(
            FadeIn(dot3),
            ShowCreation(sumTag),
            ShowCreation(sum),
            run_time=1.8
        )
        self.wait()
        self.play(
            dot1.shift,RIGHT*self.size/3,
            dot2.shift, DOWN*self.size/2,
            run_time=4.5,
            rate_func=there_and_back
        )
        self.play(
            dot1.shift, RIGHT*self.size/2,
            dot2.shift, DOWN*self.size/4,
            run_time=2,
        )
        self.wait(2)

        conclusion = TexMobject(r'P\left(x_1+x_2\le 1\right)=\frac{1}{2}',color=BLACK).to_corner(DR,buff=2.2)
        rec = SurroundingRectangle(conclusion,color=RED,stroke_width=2)
        self.play(Write(conclusion))
        self.play(ShowPassingFlash(rec))
        self.wait(2)


class ThreeD(ThreeDScene):
    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
    }
    def construct(self):
        self.set_camera_orientation(PI/3,23*DEGREES,6)
        axes = ThreeDAxes()
        self.play(ShowCreation(axes))
        cube = Cube(fill_opacity=0.5).shift(np.array([1,1,1]))
        self.play(ShowCreation(cube))
        face = ParametricFunction()


class MoveCamera1(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.move_camera(phi=30*DEGREES,theta=-45*DEGREES,run_time=3)
        self.wait()

class MoveCamera2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=80 * DEGREES)
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.begin_ambient_camera_rotation(rate=0.1)            #Start move camera
        self.wait(5)
        self.stop_ambient_camera_rotation()                     #Stop move camera
        self.move_camera(phi=80*DEGREES,theta=-PI/2)            #Return the position of the camera
        self.wait()

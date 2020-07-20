from manimlib.imports import *

class CodeLine(Text):

    CONFIG = {
        't2c': {
            'RIGHT': ORANGE,
            'LEFT': ORANGE,
            'DOWN': ORANGE,
            'UP': ORANGE,
            'UR': ORANGE,
            'UL': ORANGE,
            'DR': ORANGE,
            'DL': ORANGE,
            'ORIGIN': ORANGE,
            'FadeIn': average_color(RED, ORANGE),
            'move_to': BLUE_D,
            'shift': BLUE_D,
            'next_to': BLUE_D,
            'to_corner': BLUE_D,
            'to_edge': BLUE_D,
            'align_to': BLUE_D,
            'scale': BLUE_D,
            'rotate': BLUE_D,
            'flip': BLUE_D,
            'add': BLUE_D,
            'play': BLUE_D,
            'set_width': BLUE_D,
            'set_stroke': BLUE_D,
            'set_fill': BLUE_D,
            'round_corners': BLUE_D,
            'np': BLACK,
            'array': BLUE,
            'Polygon': RED,
            'RegularPolygon': RED,
            'Triangle': RED,
            'color': RED_C,
            'opacity': RED_C,
            'width': RED_C,
            'radius':RED_C,
            '0': average_color(BLUE, PINK),
            '1': average_color(BLUE, PINK),
            '2': average_color(BLUE, PINK),
            '3': average_color(BLUE, PINK),
            '4': average_color(BLUE, PINK),
            '5': average_color(BLUE, PINK),
            '6': average_color(BLUE, PINK),
            '7': average_color(BLUE, PINK),
            '8': average_color(BLUE, PINK),
            '9': average_color(BLUE, PINK),
            'self': PINK,
            'mob': RED_D,
            'p1': BLACK,
            'p2': BLACK,
            'p3': BLACK,
            '~': WHITE, # 随便搞个不常用的字符设成白色，以便在有时不能用空格占位时（比如涉及Transform）当空格用
        },
        'font': 'Consolas',
        # 'size': 0.36,
        'color': DARK_GRAY,
        'plot_depth': 2,
    }

    def __init__(self, text, **kwargs):
        # digest_config(self, kwargs)
        Text.__init__(self, text, **kwargs)
        self.scale(0.36)

class Emote(SVGMobject):

    CONFIG = {
        'file_name': r'D:\Documents\TIM_Catch\emote_01.svg',
        'shake_color': average_color(YELLOW, ORANGE),
    }
    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        SVGMobject.__init__(self, file_name=self.file_name, **kwargs)
        self.list = [0, 1, 2, 3, 5, 6, 9]
        for i in self.list:
            self[i].set_fill(self.shake_color, 0)

        self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]
        # self.add_updater(self.update_emote)

    def update_emote(self, mob):
        h, w, c = self.get_height(), self.get_width(), self.get_center()

        add_shake = not((h == self.attribute_list[0]) and (w == self.attribute_list[1])
                        and (c[0] == self.attribute_list[2][0]) and (c[1] == self.attribute_list[2][1]))
        self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]

        if add_shake:
            for i in self.list:
                self[i].set_opacity(1)
        else:
            for i in self.list:
                self[i].set_opacity(0)

    # def update_emote_02(self, mob):
    #     h, w, c = self.get_height(), self.get_width(), self.get_center()
    #
    #     add_shake = not((h == self.attribute_list[0]) and (w == self.attribute_list[1])
    #                     and (c[0] == self.attribute_list[2][0]) and (c[1] == self.attribute_list[2][1]))
    #     self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]
    #
    #     if add_shake:
    #         self.set_opacity(1)
    #     else:
    #         self.set_opacity(0)

    def shake_on(self):
        self.set_opacity(1)
        return self

    def shake_off(self):
         for i in self.list:
            self[i].set_fill(self.shake_color, 0)
         return self

class Emote_new(VGroup):
    CONFIG = {
        'file_name': r'D:\Documents\TIM_Catch\emote_01.svg',
        'shake_color': average_color(YELLOW, ORANGE),
        'height': 2.5,
    }
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.emote = SVGMobject(self.file_name, **kwargs).set_height(self.height)
        self.emote_02 = SVGMobject(self.file_name, **kwargs).set_height(self.height)
        self.center_dot = Dot().move_to(self.emote.get_center()).shift((DOWN + RIGHT*0.4) * self.height * 0.18).set_opacity(0)
        list = [0, 1, 2, 3, 5, 6, 9]
        for i in list:
            self.emote[i].set_fill(self.shake_color, 0)
            self.emote_02[i].set_fill(self.shake_color, 0)
        self.add(self.emote_02, self.center_dot, self.emote)
        self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]
        self.emote_02.add_updater(self.update_emote)

    def update_emote(self, mob):
        h, w, c = self.get_height(), self.get_width(), self.get_center()

        add_shake = not((h == self.attribute_list[0]) and (w == self.attribute_list[1])
                        and (c[0] == self.attribute_list[2][0]) and (c[1] == self.attribute_list[2][1]))
        self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]

        if add_shake:
            mob.set_opacity(1)
        else:
            mob.set_opacity(0)

    def shake_on(self):
        self.emote_02.set_opacity(1)
        return self
    def shake_off(self):
        self.emote_02.set_opacity(0)
        return self

class 代码风格测试(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        emote = Emote_new(color=BLACK, plot_depth=1).set_height(2.4).shift(LEFT * 4 + UP)

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=LIGHT_GREY, fill_opacity=0.25, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        loc = UP * 2.9 + RIGHT * 2.64
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)
        tex_add = CodeLine('self.add(mob)').move_to(loc)
        tex_shift_l = CodeLine('mob.shift(LEFT)').next_to(tex_add, DOWN).align_to(tex_add, LEFT)
        tex_flip_1 = CodeLine('mob.flip()').next_to(tex_shift_l, DOWN).align_to(tex_shift_l, LEFT)
        tex_flip_2 = CodeLine('mob.flip()').next_to(tex_flip_1, DOWN).align_to(tex_flip_1, LEFT)
        tex_shift_r2 = CodeLine('mob.shift(RIGHT * 2)').next_to(tex_flip_2, DOWN).align_to(tex_flip_2, LEFT)
        tex_scale_2 = CodeLine('mob.scale(2)').next_to(tex_shift_r2, DOWN).align_to(tex_shift_r2, LEFT)
        tex_annotation = CodeLine('# 所有对mob的变换均为瞬间完成的，\n\n'
                                  '# 但为了演示变换过程，\n\n'
                                  '# 实际执行的是将变换放入\n\n'
                                  '# self.play()后的对应动画过程', font='思源黑体 Bold', size=0.29)\
                        .next_to(tex_scale_2, DOWN).align_to(tex_scale_2, LEFT).set_color(GREEN)

        loc_02 = DOWN * 1.2
        caption_add = CodeLine('使用self.add(mob)将物体（mob）加入场景', font='思源黑体 Bold', size=0.32).to_edge(loc_02)
        caption_shift_1 = CodeLine('使用mob.shift(LEFT)将mob向左移动1个单位', font='思源黑体 Bold', size=0.32).to_edge(loc_02)
        caption_flip_1 = CodeLine('使用mob.flip()将mob翻转', font='思源黑体 Bold', size=0.32).to_edge(loc_02)
        caption_flip_2 = CodeLine('使用mob.flip()将mob再次翻转', font='思源黑体 Bold', size=0.32).to_edge(loc_02)
        caption_shift_r2 = CodeLine('使用mob.shift(RIGHT*2)将mob向右移动2个单位', font='思源黑体 Bold', size=0.32).to_edge(loc_02)
        caption_scale_2 = CodeLine('使用mob.scale(2)将mob沿自身中心放大2倍', font='思源黑体 Bold', size=0.32).to_edge(loc_02)

        self.wait()
        self.play(FadeInFromDown(tex_bg))
        self.play(Write(tex_add), Write(caption_add), run_time=1.5)
        self.add(emote)
        self.wait()

        self.play(Write(tex_shift_l), ReplacementTransform(caption_add, caption_shift_1), run_time=1.5)
        self.play(emote.shift, LEFT, run_time=1.6)
        self.wait()

        self.play(Write(tex_flip_1), ReplacementTransform(caption_shift_1, caption_flip_1), run_time=1.5)
        self.play(emote.flip, run_time=1.25)
        self.wait(0.5)
        self.play(Write(tex_flip_2), ReplacementTransform(caption_flip_1, caption_flip_2), run_time=1.5)
        self.play(emote.flip, run_time=1.25)
        self.wait()

        self.play(Write(tex_shift_r2), ReplacementTransform(caption_flip_2, caption_shift_r2), run_time=1.5)
        self.play(emote.shift, RIGHT * 2, run_time=1.6)
        self.wait()

        self.play(Write(tex_scale_2), ReplacementTransform(caption_shift_r2, caption_scale_2), run_time=1.5)
        self.play(emote.scale, 2, run_time=1.6)

        self.wait(0.4)
        self.play(Write(tex_annotation), FadeOut(caption_scale_2), run_time=4)

        self.wait(5)

class Emote_bounce_around(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        emote = Emote_new(height=3.2, plot_depth=-1, color=BLACK).shift(UP * 1.234) #.set_opacity(0.12)
        emote.emote_02.remove_updater(emote.update_emote)
        self.emote_velocity = (RIGHT * 2 + UP * 1.25) * 2.4e-2
        self.rotate_speed = 2.5 * DEGREES

        def update_emote(l, dt):
            l.shift(self.emote_velocity)
            l.rotate(self.rotate_speed, about_point=l.center_dot.get_center())
            self.emote_velocity += (RIGHT * 2 + UP * 1.25) * 2.8e-5 * np.sign(self.emote_velocity)

            if abs(l.get_center()[1]) > (FRAME_HEIGHT - l.get_height())/2:
                self.emote_velocity *= DR # or we can use self.emote_velocity[1] *= -1
                self.rotate_speed *= -1
                l.shake_on()
            if abs(l.get_center()[0]) > (FRAME_WIDTH - l.get_width())/2:
                self.emote_velocity *= UL # or we can use self.emote_velocity[0] *= -1
                self.rotate_speed *= -1
                l.shake_on()
            else:
                l.emote_02.set_opacity(l.emote_02.get_fill_opacity() - 0.02 if l.emote_02.get_fill_opacity() > 0 else 0)

        emote.add_updater(update_emote)
        self.add(emote)

        self.wait(24)


class PolygonsShow(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }
    """
    5.Polygon+RegularPolygon+Triangle
    具体内容：
    1.使用Polygon创建各种多边形，自己发挥吧
    2.填充效果，线宽效果，圆角效果（round_corners方法）
    3.提下子类RegularPolygon，Triangle的效果（不用讲太详细）
    二茂铁Fe已预订
    """
    def construct(self):
        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=LIGHT_GREY, fill_opacity=0.25, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        loc = UP * 2.9 + RIGHT * 3.5
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)
        self.play(ShowCreation(tex_bg))
        self.wait()
        p1 = np.array([-1, 0, 0])
        p2 = np.array([-1, 1.25, 0])
        p3 = np.array([1, 0, 0])
        pGroup = [p1, p2, p3]
        d1 = Dot(p1,color=BLUE).scale(0.2)
        d2 = Dot(p2, color=BLUE).scale(0.2)
        d3 = Dot(p3, color=BLUE).scale(0.2)
        dGroup = VGroup(d1,d2,d3)
        tri = Polygon(*pGroup, stroke_width=1, color=BLUE).set_stroke(width=2)
        triangle = VGroup(dGroup, tri).shift(LEFT*2.5).scale(3)

        Pentagon = RegularPolygon(5, color=ORANGE, fill_color=ORANGE, fill_opacity=0.7).scale(2.3).shift(LEFT*4.8)
        vl = Pentagon.get_vertices()
        Pentagram = Polygon(vl[0], vl[2], vl[-1], vl[1],vl[3],color=ORANGE, fill_color=ORANGE, fill_opacity=0.7).move_to(LEFT*1.1)
        p7 = RegularPolygon(7, color=ORANGE, fill_color=BLUE_A, fill_opacity=0.7).scale(2.3).shift(LEFT*2.3)
        p6 = RegularPolygon(6, color=ORANGE, fill_color=YELLOW_B, fill_opacity=0.7).scale(2.3).shift(LEFT * 2.3)
        Regtri = Triangle().next_to(Pentagon,buff=1).shift(2.5*UP).scale(1.5).set_fill(BLUE, 0.8)

        c1 = CodeLine('p1 = np.array([-1, 0, 0])').move_to(loc).scale(0.8)
        c2 = CodeLine('p2 = np.array([-1, 1.25, 0])').next_to(c1, DOWN).scale(0.8).align_to(c1, LEFT)
        c3 = CodeLine('p3 = np.array([1, 0, 0])').next_to(c2, DOWN).scale(0.8).align_to(c2, LEFT)
        c4 = CodeLine('triangle = Polygon(p1, p2, p3)').next_to(c3, DOWN).scale(0.8).align_to(c3, LEFT)
        c5 = CodeLine(
                    '''
                    triangle.set_fill(color=ORANGE,
                    opacity=0.8)
                    '''
                      ).next_to(c4, DOWN).scale(0.8).align_to(c4, LEFT)
        c6 = CodeLine('triangle.set_fill(opacity=0.2)').next_to(c5, DOWN).scale(0.8).align_to(c5, LEFT)
        c7 = CodeLine('''
                      triangle.set_stroke(color=ORANGE,
                      width=2)
                      ''').next_to(c6, DOWN).scale(0.7).align_to(c6, LEFT)
        c8 = CodeLine('triangle.round_corners(0.2)').next_to(c7, DOWN).scale(0.8).align_to(c7, LEFT)

        c11 = CodeLine('Reghep= RegularPolygon(7)').move_to(loc).scale(0.8)
        c12 = CodeLine('Hexagon = RegularPolygon(6)').next_to(c11, DOWN).scale(0.8).align_to(c11, LEFT)
        c9 = CodeLine('Pentagon = RegularPolygon(5)').next_to(c12, DOWN).scale(0.8).align_to(c12, LEFT)
        c10 = CodeLine('Regtri = Triangle()').next_to(c9, DOWN).scale(0.8).align_to(c9, LEFT)




        loc_02 = DOWN * 1.2
        t1 = CodeLine('manim中通过点的位置来确定多边形的形状与位置', font='思源黑体').to_edge(loc_02)
        t2 = CodeLine('我们可以设置其内部的填充效果(set_fill)', font='思源黑体').to_edge(loc_02)
        t3 = CodeLine('改变颜色(color)或不透明度(opacity)', font='思源黑体').to_edge(loc_02)
        t4 = CodeLine('通过(set_stroke)改变其线宽(width)及线的颜色(color)', font='思源黑体').to_edge(loc_02)
        t5 = CodeLine('设置圆角半径(radius)，获得圆角效果', font='思源黑体').to_edge(loc_02)

        t6 = CodeLine('但更多时候我们需要的是规则正多边形', font='思源黑体').to_edge(loc_02)
        t7 = CodeLine('而正三角形更具独特性,因此用的也更多', font='思源黑体').to_edge(loc_02)

        self.play(
                  ShowCreation(dGroup),
                  FadeIn(t1),
                  Write(c1),
                  run_time=1,
        )
        self.play(
            Write(c2),
            Write(c3),
        )
        self.play(ShowCreation(tri),
                  Write(c4))
        self.wait(1.1)

        self.play(
            ReplacementTransform(t1, t2),
            ApplyMethod(tri.set_fill, ORANGE, 0.8),
            Write(c5),
            run_time=1.3
        )
        self.wait(3.5)

        self.play(
            ReplacementTransform(t2, t3),
            Write(c6),
            ApplyMethod(tri.set_fill, ORANGE, 0.2),
        )
        self.wait(3.5)

        self.play(
            ReplacementTransform(t3, t4),
            Write(c7),
            ApplyMethod(tri.set_stroke, GRAY, 4),
            run_time=1.5
        )
        self.wait(3.5)

        self.play(
            Write(c8),
            FadeOut(d1),
            FadeOut(d2),
            FadeOut(d3),
            ApplyMethod(tri.round_corners, 0.2),
            ReplacementTransform(t4, t5),
            run_time=1.2
        )
        self.wait(3.5)

        self.play(
            FadeOut(c1),
            FadeOut(c2),
            FadeOut(c3),
            FadeOut(c4),
            FadeOut(c5),
            FadeOut(c6),
            FadeOut(c7),
            FadeOut(c8),
            FadeOut(tri),
            run_time = 1
        )
        self.wait(0.5)

        self.play(
            ReplacementTransform(t5,t6),
            Write(c11),
            ShowCreation(p7),
            run_time=1.4
        )
        self.wait(3)
        self.play(
            ReplacementTransform(p7, p6),
            Write(c12),
            run_time=1.3
        )
        self.wait(2)
        self.play(
            ReplacementTransform(p6, Pentagon),
            Write(c9),
            run_time=1.2
        )
        self.wait(4)

        self.play(
            ReplacementTransform(t6, t7),
            Write(c10),
            ShowCreation(Regtri),
        )
        self.wait(4)

        self.play(
            FadeOut(Regtri),
            FadeOut(t7),
            ApplyMethod(Pentagon.move_to, ORIGIN+LEFT*1.1)
        )
        self.play(
            ReplacementTransform(Pentagon, Pentagram),
            run_time=1.3
        )

        self.wait(5)








class tri(Scene):
    def construct(self):
        tru = Triangle(fill_color=BLUE, fill_opacity=0.8).round_corners(0.1)
        self.play(ShowCreation(tru))
        self.wait()
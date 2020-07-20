from manimlib.imports import *

class Introduction(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        img = ImageMobject('npl.jpg').scale(2.5).to_corner(UR)
        tt1 = TextMobject("对于法国人来说,",color=BLACK).scale(0.7).to_corner(UL).shift(DOWN)
        tt2 = TextMobject("拿破仑·波拉巴,这个妇孺皆知的名字是他们的骄傲。",color=BLACK).scale(0.7).next_to(tt1,DOWN,aligned_edge=LEFT)
        tt3 = TextMobject("1793年，24岁的拿破仑在土仑战役中崭露头角", color=BLACK).scale(0.7).next_to(tt2, DOWN, aligned_edge=LEFT)
        tt4 = TextMobject("打了一个大胜仗。", color=BLACK).scale(0.7).next_to(tt3, DOWN, aligned_edge=LEFT)
        tt5 = TextMobject("一夜之间，拿破仑就成了家喻户晓的英雄。", color=BLACK).scale(0.7).next_to(tt4, DOWN, aligned_edge=LEFT)
        tt6 = TextMobject("拿破仑是天才的军事家", color=BLACK).scale(0.7).next_to(tt5, DOWN, aligned_edge=LEFT)
        tt7 = TextMobject("在接下去的几次战役中，他所向披靡，风头出尽", color=BLACK).scale(0.7).next_to(tt6, DOWN, aligned_edge=LEFT)
        ttGroup = [tt1,tt2,tt3,tt4,tt5,tt6,tt7]

        t1 = TextMobject("他几次打垮了欧洲的封建君主们的反法联盟，", color=BLACK).scale(0.7).to_corner(UL).shift(DOWN)
        t2 = TextMobject("并把大半个欧洲置于他的帝辇之下。", color=BLACK).scale(0.7).next_to(t1, DOWN, aligned_edge=LEFT)
        t3 = TextMobject("但他在1815年6月的滑铁卢战役中兵败，", color=BLACK).scale(0.7).next_to(t2, DOWN, aligned_edge=LEFT)
        t4 = TextMobject("被流放到一座小岛。", color=BLACK).scale(0.7).next_to(t3, DOWN, aligned_edge=LEFT)
        t6 = TextMobject("由于拿破仑是炮兵军官出身，", color=BLACK).scale(0.7).next_to(t4, DOWN,
                                                                                                    aligned_edge=LEFT)
        t7 = TextMobject("所以他的几何与三角学学得相当不错。", color=BLACK).scale(0.7).next_to(t6,
                                                                                                                 DOWN,
                                                                                                       aligned_edge=LEFT)
        t8 = TextMobject("在绚丽的数学大花园中，就开着一朵以他名字命名的小花", color=BLACK).scale(0.7).next_to(t7, DOWN, aligned_edge=LEFT)
        t9 = TextMobject("拿破仑三角形", color=BLACK).scale(0.7).next_to(t8, DOWN, aligned_edge=LEFT)
        tGroup = [t1, t2, t3, t4, t6, t7, t8, t9]
        self.play(FadeIn(img),run_time=1.8)
        for i in ttGroup:
            self.play(Write(i),run_time=len(i)*1.8)
            self.wait(0.7)
        for i in ttGroup:
            self.play(FadeOut(i),run_time=0.2)
        for i in tGroup:
            self.play(Write(i),run_time=len(i)*1.8)
            self.wait(0.7)
        self.wait(3)
        tG = VGroup(*tGroup[:-1])
        self.play(FadeOut(tG))
        self.play(t9.scale,2.5,t9.move_to,ORIGIN,run_time=1.6)
        self.wait(3)
class NTriangle(Scene):
    def construct(self):
        d1 = np.array([1, 1, 0])
        d2 = np.array([-1, 1, 0])
        d3 = np.array([0, -1, 0])
        dList = [d1, d2, d3]
        l1 = Line(d1, d2).set_stroke(color=YELLOW,opacity=1)
        l2 = Line(d2, d3).set_stroke(color=RED,opacity=1)
        l3 = Line(d3, d1).set_stroke(color=BLUE,opacity=1)
        lList = [l1, l2, l3]
        TList = []
        CList = []
        NList = []
        for i in range(-1, 2):
            newLine = lList[i].copy().rotate(PI/2,IN,about_point=dList[i]).shift(-(dList[i]-dList[i+1])/2).scale_about_point(np.sqrt(3), (dList[i+1]+dList[i])/2)
            NList.append(newLine)
            D = newLine.get_center_of_mass()
            T = Polygon(D, dList[i], dList[i+1])
            TList.append(T)
            C = T.get_center_of_mass()
            CList.append(C)
        CT = Polygon(*CList)
        self.add(*lList,CT,*TList)
        self.wait()

class demoScene1(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        t1 = TextMobject("任意三角形",color=GRAY).scale(0.5).to_edge(DOWN)
        t2 = TextMobject("以每条边向外做等边三角形",color=GRAY).scale(0.5).to_edge(DOWN)
        t3 = TextMobject("连接三个等边三角形中心",color=GRAY).scale(0.5).to_edge(DOWN)
        t4 = TextMobject("所得仍为等边三角形",color=GRAY).scale(0.5).to_edge(DOWN)
        t5 = TextMobject("这个三角形就称之为拿破仑三角形", color=GRAY).scale(0.5).to_edge(DOWN)
        d1 = Dot(np.array([1, 1, 0]),color=BLACK)
        d2 = Dot(np.array([-1, 1, 0]),color=BLACK)
        d3 = Dot(np.array([0, -1, 0]),color=BLACK)
        dList = VGroup(d1, d2, d3)
        original = Polygon(d1.get_center(),d2.get_center(),d3.get_center())
        l1 = Line().add_updater(lambda l: l.become(Line(d1.get_center(), d2.get_center())))
        l2 = Line().add_updater(lambda l: l.become(Line(d2.get_center(), d3.get_center())))
        l3 = Line().add_updater(lambda l: l.become(Line(d3.get_center(), d1.get_center())))
        newLine1 = Line().add_updater(lambda l: l.become(l1.rotate(PI/2,IN,about_point=dList[0].get_center()).shift(-(dList[0].get_center()-dList[1].get_center())/2).scale_about_point(np.sqrt(3), (dList[0].get_center()+dList[1].get_center())/2)))
        newLine2 = Line().add_updater(lambda l: l.become(l2.rotate(PI / 2, IN, about_point=dList[1].get_center()).shift(
            -(dList[1].get_center() - dList[2].get_center()) / 2).scale_about_point(np.sqrt(3), (dList[1].get_center() + dList[2].get_center()) / 2)))
        newLine3 = Line().add_updater(lambda l: l.become(l3.rotate(PI / 2, IN, about_point=dList[2].get_center()).shift(
            -(dList[2].get_center() - dList[0].get_center()) / 2).scale_about_point(np.sqrt(3), (dList[2].get_center() + dList[0].get_center()) / 2)))
        T1 = RegularPolygon(3).add_updater(lambda p: p.become(Polygon(newLine1.get_center_of_mass(), dList[0].get_center(), dList[1].get_center()).set_stroke(color=ORANGE, opacity=1)))
        T2 = RegularPolygon(3).add_updater(
            lambda p: p.become(Polygon(newLine2.get_center_of_mass(), dList[1].get_center(), dList[2].get_center()).set_stroke(color=RED, opacity=1)))
        T3 = RegularPolygon(3).add_updater(
            lambda p: p.become(Polygon(newLine3.get_center_of_mass(), dList[2].get_center(), dList[0].get_center()).set_stroke(color=BLUE, opacity=1)))
        CT = RegularPolygon(3).add_updater(lambda p: p.become(Polygon(T1.get_center_of_mass(),T2.get_center_of_mass(),T3.get_center_of_mass(),color=GREEN,fill_opacity=0.7).set_stroke(color=GREEN, opacity=0.7)))
        TGroup = VGroup(T1,T2,T3)
        # self.play(ShowCreation(newLine3),ShowCreation(newLine1),ShowCreation(CT),ShowCreation(l1),ShowCreation(l2),ShowCreation(l3),ShowCreation(TGroup),
        #           )
        # self.play(ApplyMethod(d1.move_to, np.array([2,2,0])))
        self.wait()
        self.play(
            ShowCreation(l1),
            ShowCreation(l2),
            ShowCreation(l3),
            ShowCreation(newLine3), ShowCreation(newLine1),ShowCreation(newLine2),
            ShowCreation(dList)
        )
        self.play(ShowCreation(original.set_stroke(color=PURPLE,opacity=0.8)),ShowCreation(t1),run_time=0.7)
        self.wait(2)
        self.play(
            ShowCreation(T1),
            ReplacementTransform(t1,t2)
        )
        self.play(ShowCreation(T2))
        self.play(ShowCreation(T3))
        self.remove(original)
        self.wait(1.5)

        self.play(ShowCreation(CT),ReplacementTransform(t2,t3))
        self.wait(1)
        self.play(ReplacementTransform(t3,t4))
        self.play(ApplyMethod(d1.move_to, np.array([1.6, 1.8, 0])))
        self.wait(1.3)

        self.play(ApplyMethod(d2.shift, LEFT+DOWN),run_time=1.5)
        self.wait()

        self.play(ApplyMethod(d3.shift, 1.5*DOWN+RIGHT*0.75),run_time=1.3)
        self.wait(1.3)
        self.play(ReplacementTransform(t4,t5),run_time=0.8)
        self.wait(1.5)


class proof(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        t1 = TextMobject("外接圆", color=GRAY).scale(0.5).to_edge(DOWN)
        t2 = TextMobject("外接圆交点", color=GRAY).scale(0.5).to_edge(DOWN)
        t3 = TextMobject("连接交点与原三角形顶点", color=GRAY).scale(0.5).to_edge(DOWN)
        t4 = TextMobject("圆内接四边形，对角互补", color=GRAY).scale(0.5).to_edge(DOWN)
        t5 = TextMobject("所以该角为120°", color=GRAY).scale(0.5).to_edge(DOWN)
        t6 = TextMobject("因此这点也在另一个外接圆上", color=GRAY).scale(0.5).to_edge(DOWN)
        t7 = TextMobject("连接", color=GRAY).scale(0.5).to_edge(DOWN)
        t8 = TextMobject("垂直", color=GRAY).scale(0.5).to_edge(DOWN)
        t9 = TextMobject("互补", color=GRAY).scale(0.5).to_edge(DOWN)
        t10 = TextMobject("均为60°", color=GRAY).scale(0.5).to_edge(DOWN)
        d1 = np.array([1.2, 1.2, 0])
        d2 = np.array([-1.5, 0.8, 0])
        d3 = np.array([-0.2, -1.9, 0])
        dList = [d1, d2, d3]
        l1 = Line(d1, d2).set_stroke(color=ORANGE,opacity=1)
        l2 = Line(d2, d3).set_stroke(color=RED,opacity=1)
        l3 = Line(d3, d1).set_stroke(color=BLUE,opacity=1)
        lList = [l1, l2, l3]
        TList = []
        CList = []
        NList = []
        Colors = [ORANGE,RED,BLUE]
        outsideCircles = []
        DLL = []
        dlL =[]
        for i in range(-1, 2):
            newLine = lList[i].copy().rotate(PI/2,IN,about_point=dList[i]).shift(-(dList[i]-dList[i+1])/2).scale_about_point(np.sqrt(3), (dList[i+1]+dList[i])/2)
            NList.append(newLine)
            D = newLine.get_center_of_mass()
            T = Polygon(D, dList[i], dList[i+1]).set_stroke(color=Colors[i])
            TList.append(T)
            C = T.get_center_of_mass()
            CList.append(C)
            OCir = DashedVMobject(Circle().scale(newLine.get_length()/3).set_stroke(color=BLACK).move_to(C))
            outsideCircles.append(OCir)
        greenT1 = Line(CList[0],CList[1]).set_stroke(color=GREEN)
        greenT2 = Line(CList[1], CList[2]).set_stroke(color=GREEN)
        greenT3 = Line(CList[2], CList[0]).set_stroke(color=GREEN)

        CT = VGroup(greenT1,greenT2,greenT3)

        f1 = Line(CList[0],CList[1],color=PINK).rotate_about_origin(PI/2).move_to(dList[0])
        f2 = Line(CList[1], CList[2], color=PINK).rotate_about_origin(PI / 2).move_to(dList[1])

        P = get_intersect(f1,f2)
        FL =[]
        for d in dList:
            fzl = DashedLine(P,d,color=GRAY)
            FL.append(fzl)
        arc3 = VGroup(FL[0],FL[1])
        arc1 = VGroup(FL[1],FL[2])
        arc2 = VGroup(FL[2],FL[0])

        lx1 = DashedLine(P,CList[2],color=GRAY)
        lx2 = DashedLine(P, CList[0], color=GRAY)
        lx3 = DashedLine(d3, CList[2], color=GRAY)
        lx4 = DashedLine(d3, CList[0], color=GRAY)
        lxGroup = VGroup(lx1,lx2,lx3,lx4)

        demeG1 = VGroup(FL[2],greenT3)
        demeG2 = VGroup(FL[0], greenT1)
        _arc1 = Angle(CList[1],CList[0],CList[2])
        _arc2 = Angle(d1,P,d3)

        _arc3 = Angle(CList[2],CList[1],CList[0])
        _arc4 = Angle(CList[1], CList[2], CList[0])

        self.play(ShowCreation(l1),ShowCreation(l2),ShowCreation(l3),run_time=1.3)
        self.play(ShowCreation(TList[0]),ShowCreation(TList[1]),ShowCreation(TList[2]),run_time=1.4)
        self.play(ShowCreation(CT),run_time=0.7)
        self.wait(2.5)
        self.play(ShowCreation(outsideCircles[1]),ShowCreation(t1),run_time=1.3)
        self.play(ShowCreation(outsideCircles[2]),run_time=1)
        self.play(ReplacementTransform(t1,t2))

        self.wait(2.5)
        self.play(ShowCreation(FL[0]),ShowCreation(FL[1]),ShowCreation(FL[2]),ReplacementTransform(t2,t3),run_time=0.7)
        self.wait(2.5)
        self.play(ApplyWave(TList[1]),ApplyWave(arc3),ApplyWave(outsideCircles[1]),rate_func=there_and_back)
        self.play(ReplacementTransform(t3,t4))
        self.wait(2.5)
        self.play(ApplyWave(TList[2]), ApplyWave(arc1), ApplyWave(outsideCircles[2]), rate_func=there_and_back)
        self.wait(2.5)
        self.play(ApplyWave(arc3),ReplacementTransform(t4,t5))
        self.wait(2.5)
        self.play(ApplyWave(arc1),run_time=1.3)
        self.wait(2.5)

        self.play(ApplyWave(arc2),run_time=1.3)
        self.play(ShowCreation(outsideCircles[0]), ReplacementTransform(t5, t6),run_time=1.3)
        self.wait(2.5)

        self.play(ReplacementTransform(t6,t7),run_time=1)
        self.wait()
        self.play(Write(lxGroup),run_time=3)
        self.wait(6)

        self.play(ApplyWave(demeG1),ReplacementTransform(t7,t8),run_time=1.3)
        self.wait(2.5)
        self.play(ApplyWave(demeG2),run_time=1.3)
        self.wait(1.5)

        self.play(ShowCreation(_arc1),ShowCreation(_arc2),ReplacementTransform(t8,t9),run_time=1.3)
        self.wait(2.5)

        self.play(FadeOut(_arc2),run_time=1.3)
        self.play(ShowCreation(_arc3),ShowCreation(_arc4),ReplacementTransform(t9,t10),run_time=1.3)
        self.wait(5)

        self.play(ApplyWave(CT),ApplyWave(_arc4),ApplyWave(_arc1),ApplyWave(_arc3),run_time=1.3)
        self.wait(5)



class Angle(VGroup):

    CONFIG = {
        'radius': 1,
        'color': RED,
        'opacity': 0.4,
        'stroke_width': 10,
        'below_180': True,
    }

    def __init__(self, A, O, B, **kwargs):

        VMobject.__init__(self, **kwargs)
        OA, OB = A-O, B-O
        if self.below_180:
            theta = np.angle(complex(*OA[:2])/complex(*OB[:2])) # angle of OB to OA
        else:
            theta = TAU + np.angle(complex(*OA[:2])/complex(*OB[:2]))

        self.add(Arc(start_angle=Line(O, B).get_angle(), angle=theta, radius=self.radius/2*0.35,
                     stroke_width=100 * self.radius*0.35, color=self.color, arc_center=O).set_stroke(opacity=self.opacity))
        self.add(Arc(start_angle=Line(O, B).get_angle(), angle=theta, radius=self.radius*0.35,
                     stroke_width=self.stroke_width*0.35, color=self.color, arc_center=O))


def get_intersect(line1, line2, parallel=1):
    p1, p2 = line1.get_start_and_end()
    p3, p4 = line2.get_start_and_end()

    # Line1 is a1*x+b1*y=c1
    a1 = p2[1] - p1[1]
    b1 = p1[0] - p2[0]
    c1 = a1 * p1[0] + b1 * p1[1]

    # Line2 is a2*x+b2*y=c2
    a2 = p4[1] - p3[1]
    b2 = p3[0] - p4[0]
    c2 = a2 * p3[0] + b2 * p3[1]

    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        return parallel
    else:
        x = (b2 * c1 - b1 * c2) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        return x * RIGHT + y * UP


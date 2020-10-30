from manimlib.imports import *


class sticks(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        t = 1.5;
        stick1 = Line(UP*2*t,DOWN*2*t).set_stroke(BLACK).next_to(LEFT_SIDE)
        stick2 = stick1.copy().rotate(PI/2,OUT).scale(1.2).next_to(stick1.get_bottom(),buff=0)
        print(stick1.get_bottom())
        self.add(stick1, stick2)
        self.wait()

        demoStick1= stick1.copy().scale(0.9).set_color(ORANGE).next_to(stick1.get_bottom(),buff=0,direction=UP)
        # demoStick2 = demoStick1.copy().next_to(stick1.get_bottom(),buff=0)

        lenth = demoStick1.get_length()
        O = demoStick1.get_bottom()
        dotStart = Dot(demoStick1.get_top()).set_color(ORANGE)
        dotEnd = Dot(demoStick1.get_bottom()).set_color(ORANGE)
        print(np.sqrt(lenth*lenth-np.square(dotStart.get_center()[1]-O[1])))

        stick = Line().add_updater(
            lambda x: x.become(Line(dotStart, dotEnd).set_color(ORANGE)),
        )

        dotEnd = dotEnd.add_updater(
            lambda x: x.move_to(O+RIGHT*np.sqrt(lenth*lenth-(dotStart.get_center()[1]-O[1])*(dotStart.get_center()[1]-O[1])))
        )

        n = 5
        dots = VGroup()
        for i in range(1,n):
            dot = Dot(i/n*dotStart.get_center()+(n-i)/n*dotEnd.get_center()).set_color_by_gradient(RED,BLUE)
            dots.add(dot)

        dots[0].add_updater(lambda x:x.move_to((1)/n*dotStart.get_center()+(n-1)/n*dotEnd.get_center()))
        dots[1].add_updater(lambda x: x.move_to((2) / n * dotStart.get_center() + (n - 2) / n * dotEnd.get_center()))
        dots[2].add_updater(lambda x: x.move_to((3) / n * dotStart.get_center() + (n - 3) / n * dotEnd.get_center()))
        dots[3].add_updater(lambda x: x.move_to((4) / n * dotStart.get_center() + (n - 4) / n * dotEnd.get_center()))

        self.add(stick1,stick2,dotStart,dotEnd,stick,dots)
        self.play(
            ApplyMethod(dotStart.shift, DOWN*lenth),
            run_time = 5
        )
        print(dotEnd.get_center())
        print(np.sqrt(lenth*lenth-(dotStart.get_center()[1]-O[1])*(dotStart.get_center()[1]-O[1])))


class Trail(VGroup):

    CONFIG = {
        'max_width': 5,
        'nums': 500,
        'trail_color': BLUE_B,
        # 'rate_func': linear,
        'rate_func': lambda t: t ** 1.25,
    }

    def __init__(self, mob, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.add(mob)
        self.trail = VGroup()
        self.path_xyz = []
        self.add(self.trail)
        self.pos_old = self[0].get_center()

    def update_trail(self, trail):
        err = 1e-6
        pos_new = self[0].get_center()
        pos_old = self.pos_old
        self.pos_old = pos_new
        # if np.sqrt(sum((pos_new - pos_old) ** 2))>err:
        if sum(abs(pos_new - pos_old))>err:
            trail.add(Line(pos_old, pos_new, color=self.trail_color, plot_depth=0))

        if len(trail) > self.nums:
            trail.remove(trail[0])
            # for k in range(self.nums):
            #     trail[k].set_stroke(width=self.max_width * self.rate_func(k/self.nums),
            #                         opacity=self.rate_func(k/self.nums))
            for l in trail:
                k = trail.submobjects.index(l)
                l.set_stroke(width=self.max_width * self.rate_func(k/self.nums),
                             opacity=self.rate_func(k/self.nums))

        if len(trail) <= self.nums and len(trail) > 0:
            # for k in range(len(trail)):
            #     trail[k].set_stroke(width=self.max_width * self.rate_func(k/len(trail)),
            #                         opacity=self.rate_func(k/len(trail)))
            for l in trail:
                k = trail.submobjects.index(l)
                l.set_stroke(width=self.max_width * self.rate_func(k/len(trail)),
                             opacity=self.rate_func(k/len(trail)))

    def get_path_xyz(self, err=1e-4):
        pos_new = self[0].get_center()
        pos_old = self.pos_old
        if sum(abs(pos_new - pos_old))>err:
            self.path_xyz.append(pos_new)
        self.pos_old = pos_new
        while len(self.path_xyz) > self.nums:
            self.path_xyz.remove(self.path_xyz[0])

    def create_path(self):
        path = VGroup()
        self.get_path_xyz()
        if len(self.path_xyz) > 1:
            for i in range(len(self.path_xyz)-1):
                path.add(Line(self.path_xyz[i], self.path_xyz[i+1], stroke_color=self.trail_color,
                              stroke_opacity=self.rate_func(i/len(self.path_xyz)), plot_depth=self.rate_func(i/len(self.path_xyz)),
                              stroke_width=self.max_width * self.rate_func(i/len(self.path_xyz))))
        return path

    def update_path(self, trail):
        trail.become(self.create_path())

    def start_trace(self):
        # self.trail.add_updater(self.update_trail)
        self.trail.add_updater(self.update_path)

    def stop_trace(self):
        self.trial.remove_updater(self.update_path)

class sticks2(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        t = 1.5;
        stick1 = Line(UP*2*t,DOWN*2*t).set_stroke(BLACK).next_to(LEFT_SIDE)
        stick2 = stick1.copy().rotate(PI/2,OUT).scale(1.2).next_to(stick1.get_bottom(),buff=0)
        print(stick1.get_bottom())
        self.add(stick1, stick2)
        self.wait()

        demoStick1= stick1.copy().scale(0.9).set_color(ORANGE).next_to(stick1.get_bottom(),buff=0,direction=UP)
        # demoStick2 = demoStick1.copy().next_to(stick1.get_bottom(),buff=0)

        lenth = demoStick1.get_length()
        O = demoStick1.get_bottom()
        dotStart = Dot(demoStick1.get_top()).set_color(ORANGE)
        dotEnd = Dot(demoStick1.get_bottom()).set_color(ORANGE)
        print(np.sqrt(lenth*lenth-np.square(dotStart.get_center()[1]-O[1])))

        stick = Line().add_updater(
            lambda x: x.become(Line(dotStart, dotEnd).set_color(ORANGE)),
        )

        dotEnd = dotEnd.add_updater(
            lambda x: x.move_to(O+RIGHT*np.sqrt(lenth*lenth-(dotStart.get_center()[1]-O[1])*(dotStart.get_center()[1]-O[1])))
        )

        n = 6
        dots = VGroup()
        trails = VGroup()
        for i in range(1,n):
            dot = Dot(i/n*dotStart.get_center()+(n-i)/n*dotEnd.get_center()).set_color_by_gradient(RED,BLUE)
            trail = Trail(dot)
            trail.start_trace()
            dots.add(dot)
            trails.add(trail)

        dots[0].add_updater(lambda x: x.move_to((1)/n*dotStart.get_center()+(n-1)/n*dotEnd.get_center()))
        dots[1].add_updater(lambda x: x.move_to((2) / n * dotStart.get_center() + (n - 2) / n * dotEnd.get_center()))
        dots[2].add_updater(lambda x: x.move_to((3) / n * dotStart.get_center() + (n - 3) / n * dotEnd.get_center()))
        dots[3].add_updater(lambda x: x.move_to((4) / n * dotStart.get_center() + (n - 4) / n * dotEnd.get_center()))
        dots[4].add_updater(lambda x: x.move_to((5) / n * dotStart.get_center() + (n - 5) / n * dotEnd.get_center()))

        self.add(stick1,stick2,dotStart,dotEnd,stick,dots,trails)
        self.play(
            ApplyMethod(dotStart.shift, DOWN*lenth),
            run_time = 5
        )
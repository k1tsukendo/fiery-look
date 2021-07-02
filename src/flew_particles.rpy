init python:
    def new_particle_profile(trans, st=0):
        return {
            'current_angle': renpy.random.randint(0, 628) * .01,
            'new_angle': .002 - renpy.random.random() * .004,
            'lifetime': st + renpy.random.randint(15, 40)
        }

    def particle_working(trans, st, at):
        try:
            trans.particle['current_angle'] += trans.particle['new_angle']
            trans.xalign += convert_pixels_to_position(math.cos(trans.particle['current_angle']), 'x') + .0005
            trans.yalign += convert_pixels_to_position(math.sin(trans.particle['current_angle']), 'y') + .0001

            if trans.xalign > 1.1 or trans.xalign < -0.1 or trans.xalign > 1.1 or trans.xalign < -0.1:
                trans.xalign, trans.yalign = renpy.random.randint(0, 350) * .001, renpy.random.random()
                trans.zoom = renpy.random.randint(2, 12) * .1
                trans.particle = new_particle_profile(trans, st)
            if trans.particle['lifetime'] - st < 0:
                trans.particle = new_particle_profile(trans, st)
                trans.xalign, trans.yalign = renpy.random.randint(0, 350) * .001, renpy.random.random()
                trans.zoom = renpy.random.randint(2, 12) * .1
                return renpy.random.choise([renpy.random.randint(1, 5) + renpy.random.random(), None])

            elif trans.particle['lifetime'] - st < 5:
                if trans.alpha > 0: trans.alpha -= .02  # He s dying..
            elif trans.alpha < .6: trans.alpha += .005  # ..now he s alive.
            return .02

        except:
            trans.xalign, trans.yalign = renpy.random.randint(0, 350) * .001, renpy.random.random()
            trans.zoom = renpy.random.randint(2, 12) * .1
            trans.particle = new_particle_profile(trans, st)
            return renpy.random.randint(0, 15) + renpy.random.random()


        # what de..
        def gravity_force(trans, st, at):
            trans.yalign -= .24 - st * .4
            if trans.yalign > 5:
                return
            return .01
        # ..fuck is this?......


init:
    transform particle_moves:
        alpha 0
        function particle_working
        pause 5
        repeat

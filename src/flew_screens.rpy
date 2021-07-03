init 100:
    transform DissolveSH(speed = 1):
        on show:
            alpha 0
            linear speed alpha 1
        on hide:
            linear speed alpha 0

    transform chibijump:
        xalign -2.0
        block:
            pause 60
            xalign 0.2
            yalign 4
            function gravity_force
            repeat

    python:
        # This method converts pixels to position for |align| method.
        def convert_pixels_to_position(px, axis='x'): return px / {'x': 1920, 'y': 1080}[axis]

        # what de..
        def gravity_force(trans, st, at):
            trans.yalign -= .24 - st * .4
            if trans.yalign > 5:
                return
            return .01
        # ..fuck is this?......

        import datetime
        persistent.last_session_time = datetime.datetime.now()
        if persistent.game_time is None:
            persistent.game_time = 0

        def get_game_time(st, at):
            t = datetime.datetime.now()
            dt = t - persistent.last_session_time

            persistent.last_session_time = t
            persistent.game_time += dt.total_seconds()

            minutes, seconds = divmod(int(persistent.game_time), 60)
            hours, minutes = divmod(minutes, 60)

            img = Text('%0*d:%0*d:%0*d' % (2, hours, 2, minutes, 2, seconds))
            return img, .1

    image game_time = DynamicDisplayable(get_game_time)

screen flew_debug_screen:
    zorder 1000
    add 'game_time' align(.95, .05)

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

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
            pause 30
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


screen flew_say_wndw:
    window background None id 'window'
    $ timeofday = persistent.timeofday

    if persistent.font_size == "large":

        imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/backward_%s.png") xpos 38 ypos 924 action ShowMenu("text_history")

        add get_image("gui/dialogue_box/"+timeofday+"/dialogue_box_large.png") xpos 174 ypos 866

        imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/hide_%s.png") xpos 1508 ypos 883 action HideInterface()
        imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/save_%s.png") xpos 1567 ypos 883 action ShowMenu('save')
        imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/menu_%s.png") xpos 1625 ypos 883 action ShowMenu('game_menu_selector')
        imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/load_%s.png") xpos 1682 ypos 883 action ShowMenu('load')

        if not config.skipping:
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/forward_%s.png") xpos 1768 ypos 924 action Skip()
        else:
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/fast_forward_%s.png") xpos 1768 ypos 924 action Skip()

        text what id "what" xpos 194 ypos 914 xmaximum 1541 size 35 line_spacing 1
        if who:
            text who id "who" xpos 194 ypos 877 size 35 line_spacing 1

    elif persistent.font_size == "small":

        imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/backward_%s.png") xpos 38 ypos 949 action ShowMenu("text_history")

        add get_image("gui/dialogue_box/"+timeofday+"/dialogue_box.png") xpos 174 ypos 916

        imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/hide_%s.png") xpos 1508 ypos 933 action HideInterface()
        imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/save_%s.png") xpos 1567 ypos 933 action ShowMenu('save')
        imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/menu_%s.png") xpos 1625 ypos 933 action ShowMenu('game_menu_selector')
        imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/load_%s.png") xpos 1682 ypos 933 action ShowMenu('load')

        if not config.skipping:
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/forward_%s.png") xpos 1768 ypos 949 action Skip()
        else:
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/fast_forward_%s.png") xpos 1768 ypos 949 action Skip()

        text what id "what" xpos 194 ypos 964 xmaximum 1541 size 28 line_spacing 2 font flew_preference_setFont
        if who:
            text who id "who" xpos 194 ypos 931 size 28 line_spacing 2 font flew_preference_setFont

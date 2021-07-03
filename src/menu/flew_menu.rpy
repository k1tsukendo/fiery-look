label flew_start:
    window hide

    scene bg black with Dissolve(4)

    stop music fadeout 4
    stop ambience fadeout 4
    stop sound_loop fadeout 4
    stop sound fadeout 4

    python:
        renpy.start_predict_screen('flew_menu_screen')
        renpy.start_predict_screen('flew_menu_ui')
        renpy.start_predict_screen('flew_dynamic_particles')
        persistent.sprite_time = 'day'
        day_time()  
        # PEP8 says that whitespace before
        # method is bad looking :)

    $ renpy.pause(2, hard=True)  
    # Btw, PEP8 says, that whitespaces
    # between arg and his value is bad looking :3

    show image Text('{size=70}{font=mods/flew/res/fonts/futura_md.ttf}{color=#db4507}RedHead Team{/color}\nПредставляет{/font}{/size}', slow_cps=25) at truecenter with dspr
    $ renpy.pause(2, hard=True)

    hide text with dissolve
    $ renpy.pause(.4, hard=True)

    if flew_preferences['misc']['debug_mode']:
        scene image im.MatrixColor(get_image('bg/ext_house_of_dv_day.jpg'), im.matrix.desaturate()) with Dissolve(1.3)
    else:
        scene bg ext_house_of_dv_day with Dissolve(1.3)

    $ renpy.pause(2, hard=True)
    scene bg ext_house_of_dv_day:
        xalign 0.65 yalign 0.5
        linear 5 zoom 10.5

    $ renpy.block_rollback()

    scene white with Dissolve(0.2)
    $ renpy.pause(2)

    if not flew_preferences['misc']['debug_mode']:
        play music bv_rideon
    else:
        play music debug_meditation

    if not flew_preferences['misc']['debug_mode']:
        scene bg int_house_of_dv_day with Dissolve(1.3)
    else:
        scene image im.MatrixColor(get_image('bg/int_house_of_dv_day.jpg'), im.matrix.desaturate()) with Dissolve(1.3)

    call screen flew_menu_screen

    return

screen flew_menu_screen:
    modal True
    zorder 999

    fixed at DissolveSH:
        use flew_dynamic_particles
        use flew_menu_ui


screen flew_menu_ui:
    tag menu
    imagemap:
        alpha False
        cache True
        idle 'mods/flew/res/gui/menu/overlay_idle.png'
        hover 'mods/flew/res/gui/menu/overlay_hover.png'

        hotspot adapt_hotspot(996, 505, 740, 110) action Jump('flew_entering')
        hotspot adapt_hotspot(912, 615, 834, 110) action ShowMenu('flew_gallery')  # Preferences
        hotspot adapt_hotspot(1090, 725, 650, 110) action ShowMenu('flew_preferences_ui')  # Gallery
        hotspot adapt_hotspot(1330, 835, 410, 110) action ShowMenu('flew_exit_prompt')  # Exit
        hotspot adapt_hotspot(184, 806, 196, 196) action ShowMenu('flew_vk_redirect')

    if flew_preferences['misc']['debug_mode']:
        text 'Version ' + K1TSU_MOD_VERSION xalign 0.85 yalign 0.11:
            size 24
            color '#AAA'


screen flew_indev_notice:
    tag menu
    imagebutton at DissolveSH(.5):
        idle 'mods/flew/res/gui/menu/in_progress.jpg'
        action Return()


screen flew_exit_prompt:
    tag menu
    fixed at DissolveSH(.5):
        add 'mods/flew/res/gui/menu/exit.jpg'
        use flew_confirmation((Hide('flew_menu_screen', dissolve), Hide('menu', dissolve), Jump('flew_terminate')), Return())


screen flew_vk_redirect:
    tag menu
    fixed at DissolveSH(.5):
        add 'mods/flew/res/gui/menu/vk_link.jpg'
        use flew_confirmation(OpenURL('https://vk.com/redhead_team'), Return())


screen flew_confirmation(true_act, false_act):
    imagebutton xalign 0.60 yalign 0.6:
        auto 'mods/flew/res/gui/ask_user/yes_%s.png'
        action true_act
    imagebutton xalign 0.8 yalign 0.6:
        auto 'mods/flew/res/gui/ask_user/no_%s.png'
        action false_act


screen flew_dynamic_particles:
    for i in range(26):
        add 'mods/flew/res/gui/particle.png' at particle_moves
    add 'mods/flew/res/gui/dv_chibi.png' at chibijump


label flew_terminate:
    stop music fadeout 4
    scene bg black with Dissolve(4)

    python:
        renpy.stop_predict_screen('flew_menu_screen')
        renpy.stop_predict_screen('flew_menu_ui')
        renpy.stop_predict_screen('flew_dynamic_particles')

    show image Text('Also try \"Project Owl: Reborn\" :3') at fleft with dspr
    $ renpy.pause(1, hard=True)

    $ MainMenu(confirm=False)()


label flew_entering:
    stop music fadeout 4
    scene bg black with dissolve2

    python:
        renpy.stop_predict_screen('flew_menu_screen')
        renpy.stop_predict_screen('flew_menu_ui')
        renpy.stop_predict_screen('flew_dynamic_particles')
        renpy.pause(3, hard=True)
    jump flew_prologue

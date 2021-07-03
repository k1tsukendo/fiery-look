
init -127001 python:
    flew_preferences = {
        "colors": 
        {
            "white": "#fff",
            "prowl": "#c21010",
            "redhead": "#db4507",
            "rb": "#e8ad16",
            "hotline": "#e81689",
            "doomguy": "#128f00",
            "doomslayer": "#213823",
            "kitsukendo": "#ff7ae9",
            "prowl_old": "#32d2db",
            "forchev": "#0c6200",

            "ubuntu_accent": "#dd4814",
            "ubuntu_backgr": "#4d1465"
        },
        "fonts": 
        {
            "Futura Md": "mods/flew/res/fonts/futura_md.ttf"
        },
        "misc": 
        {
            "debug_mode": False,  # Change this, Mik.
        }
    }

    flew_preference_meColor = flew_preferences["colors"]["kitsukendo"]
    flew_preference_setFont = flew_preferences["fonts"]["Futura Md"]


screen flew_preferences_ui:
    tag menu

    use flew_dynamic_particles
    use flew_preferences_ui_tint

    # Color selector
    imagemap:
        alpha True
        cache True
        idle 'mods/flew/res/gui/menu/overlay_preferences_idle.png'
        hover 'mods/flew/res/gui/menu/overlay_preferences_hover.png'

        hotspot adapt_hotspot(274, 356, 85, 82) action SetVariable('flew_preference_meColor', flew_preferences['colors']['prowl'])
        hotspot adapt_hotspot(360, 356, 85, 82) action SetVariable('flew_preference_meColor', flew_preferences['colors']['redhead'])
        hotspot adapt_hotspot(443, 356, 85, 82) action SetVariable('flew_preference_meColor', flew_preferences['colors']['rb'])
        hotspot adapt_hotspot(526, 356, 85, 82) action SetVariable('flew_preference_meColor', flew_preferences['colors']['hotline'])
        hotspot adapt_hotspot(610, 356, 85, 82) action SetVariable('flew_preference_meColor', flew_preferences['colors']['doomguy'])
        hotspot adapt_hotspot(694, 356, 85, 82) action SetVariable('flew_preference_meColor', flew_preferences['colors']['doomslayer'])
        hotspot adapt_hotspot(780, 356, 85, 82) action SetVariable('flew_preference_meColor', flew_preferences['colors']['kitsukendo'])
        hotspot adapt_hotspot(274, 444, 85, 82) action SetVariable('flew_preference_meColor', flew_preferences['colors']['prowl_old'])
        hotspot adapt_hotspot(358, 444, 85, 82) action SetVariable('flew_preference_meColor', flew_preferences['colors']['forchev'])
        hotspot adapt_hotspot(444, 444, 85, 82) action SetVariable('flew_preference_meColor', flew_preferences['colors']['ubuntu_accent'])
        hotspot adapt_hotspot(526, 444, 85, 82) action SetVariable('flew_preference_meColor', flew_preferences['colors']['ubuntu_backgr'])
        hotspot adapt_hotspot(621, 462, 188, 54) action SetVariable('flew_preference_meColor', flew_preferences['colors']['white'])


        hotspot adapt_hotspot(195, 888, 233, 96) action Return()

    if flew_preferences['misc']['debug_mode']:
        text 'Version ' + K1TSU_MOD_VERSION xalign 0.85 yalign 0.11:
            size 24
            color '#AAA'
    text 'Розовые волосы - это круто!' xalign 0.20 yalign 0.50:
        size 44
        color flew_preference_meColor
        font flew_preferences['fonts']['Futura Md']


screen flew_preferences_ui_tint:
    zorder 995
    image 'mods/flew/res/gui/menu/tint.jpg':
        at transform:
            linear 0.5 alpha 0.5

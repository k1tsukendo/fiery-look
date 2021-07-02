
init -127001 python:
    flew_preferences = {
        "colors": 
        {
            "prowl": "#c21010",
            "redhead": "#db4507",
            "rb": "#db4507",
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
            "Futura Md": "mods/fierly_look/res/fonts/futura_md.ttf"
        },
        "misc": 
        {
            "debug_mode": True,  # Change this, Mik.
        }
    }

    flew_preference_meColor = flew_preferences["colors"]["kitsukendo"]
    flew_preference_setFont = flew_preferences["fonts"]["Futura Md"]


screen flew_preferences_ui:
    tag menu

    # Color selector
    imagemap:
        alpha True
        cache True
        idle 'mods/flew/res/gui/menu/overlay_preferences_idle.png'
        hover 'mods/flew/res/gui/menu/overlay_preferences_hover.png'

        hotspot adapt_hotspot(274, 356, 85, 82) action (SetVariable('flew_preference_meColor', flew_preferences['colors']['prowl']))
        hotspot adapt_hotspot(360, 356, 85, 82) action (SetVariable('flew_preference_meColor', flew_preferences['colors']['redhead']))
        hotspot adapt_hotspot(443, 356, 85, 82) action (SetVariable('flew_preference_meColor', flew_preferences['colors']['rb']))
        hotspot adapt_hotspot(526, 356, 85, 82) action (SetVariable('flew_preference_meColor', flew_preferences['colors']['hotline']))
        hotspot adapt_hotspot(610, 356, 85, 82) action (SetVariable('flew_preference_meColor', flew_preferences['colors']['doomguy']))
        hotspot adapt_hotspot(694, 356, 85, 82) action (SetVariable('flew_preference_meColor', flew_preferences['colors']['doomslayer']))
        hotspot adapt_hotspot(780, 356, 85, 82) action (SetVariable('flew_preference_meColor', flew_preferences['colors']['kitsukendo']))
        hotspot adapt_hotspot(274, 444, 85, 82) action (SetVariable('flew_preference_meColor', flew_preferences['colors']['prowl_old']))
        hotspot adapt_hotspot(358, 444, 85, 82) action (SetVariable('flew_preference_meColor', flew_preferences['colors']['forchev']))
        hotspot adapt_hotspot(444, 444, 85, 82) action (SetVariable('flew_preference_meColor', flew_preferences['colors']['ubuntu_accent']))
        hotspot adapt_hotspot(526, 444, 85, 82) action (SetVariable('flew_preference_meColor', flew_preferences['colors']['ubuntu_backgr']))

        hotspot adapt_hotspot(190, 882, 246, 106) action Return()

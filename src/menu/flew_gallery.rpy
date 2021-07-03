init python:
    flew_gal = Gallery()
    flew_gal.transition = Dissolve(.5)


screen flew_gallery_overlay:
    add 'mods/flew/res/gui/menu/overlay_gallery.png'

screen flew_gallery:
    use flew_preferences_ui_tint
    use flew_gallery_overlay

    python:
        flew_gal.button('fl_lm_island')
        if persistent.fl_lm_island:
            flew_gal.image('images/gui/gallery/thumbnail_hover.png', 'mods/flew/res/images/cg/fl_lm_island.png')

        flew_gal.button('fl_lm_relax')
        if persistent.fl_lm_relax:
            flew_gal.image('images/gui/gallery/thumbnail_hover.png', 'mods/flew/res/images/cg/fl_lm_relax.png')

        flew_gal.button('ov_alisa_running')
        if persistent.ov_alisa_running:
            flew_gal.image('images/gui/gallery/thumbnail_hover.png', 'mods/flew/res/images/cg/ov_alisa_running.png')

    add flew_gal.make_button('fl_lm_island', 'mods/flew/res/gallery/fl_lm_island_thumb.jpg', locked='images/gui/gallery/not_opened_idle.png', xalign=0.15, yalign=0.25)
    add flew_gal.make_button('fl_lm_relax', 'mods/flew/res/gallery/fl_lm_relax_thumb.jpg', locked='images/gui/gallery/not_opened_idle.png', xalign=0.380, yalign=0.25)
    add flew_gal.make_button('ov_alisa_running', 'mods/flew/res/gallery/ov_alisa_running.png', locked='images/gui/gallery/not_opened_idle.png', xalign=0.600, yalign=0.25)

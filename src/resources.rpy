init:

    # Transitions # thx, cap.
    $ fla = Fade(.25,  .75, .75, color="#FFF")
    $ bol = Fade(.25,   .5, .75, color="#F00")
    $ boo = Fade(.25,   .5, .75)
    $ blt = Fade(.75,  1.0, .75)
    $ ov_trise = Dissolve(1.5)

    # Transformations #
    transform running:
        zoom 1.01 align (0.5, 0.5)
        ease 0.35 xalign 0.35 yalign 0.65
        ease 0.35 xalign 0.50 yalign 0.50
        ease 0.35 xalign 0.65 yalign 0.65
        ease 0.35 xalign 0.50 yalign 0.50
        repeat

    # etc. #
    image dv sad swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900, 1080), (0,0), get_image("sprites/normal/dv/dv_3_body.png"),(0,0), "mods/flew/res/images/sprites/dv/composite/dv_3_swim.png",(0,0), get_image("sprites/normal/dv/dv_3_sad.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900, 1080), (0,0), get_image("sprites/normal/dv/dv_3_body.png"),(0,0), "mods/flew/res/images/sprites/dv/composite/dv_3_swim.png",(0,0), get_image("sprites/normal/dv/dv_3_sad.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900, 1080), (0,0), get_image("sprites/normal/dv/dv_3_body.png"),(0,0), "mods/flew/res/images/sprites/dv/composite/dv_3_swim.png",(0,0), get_image("sprites/normal/dv/dv_3_sad.png")) )

    image dv shy swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900, 1080), (0,0), get_image("sprites/normal/dv/dv_3_body.png"),(0,0), "mods/flew/res/images/sprites/dv/composite/dv_3_swim.png",(0,0), get_image("sprites/normal/dv/dv_3_shy.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900, 1080), (0,0), get_image("sprites/normal/dv/dv_3_body.png"),(0,0), "mods/flew/res/images/sprites/dv/composite/dv_3_swim.png",(0,0), get_image("sprites/normal/dv/dv_3_shy.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900, 1080), (0,0), get_image("sprites/normal/dv/dv_3_body.png"),(0,0), "mods/flew/res/images/sprites/dv/composite/dv_3_swim.png",(0,0), get_image("sprites/normal/dv/dv_3_shy.png")) )

    image dv angry swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900, 1080), (0,0), get_image("sprites/normal/dv/dv_5_body.png"),(0,0), "mods/flew/res/images/sprites/dv/composite/dv_5_swim.png",(0,0), get_image("sprites/normal/dv/dv_5_angry.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900, 1080), (0,0), get_image("sprites/normal/dv/dv_5_body.png"),(0,0), "mods/flew/res/images/sprites/dv/composite/dv_5_swim.png",(0,0), get_image("sprites/normal/dv/dv_5_angry.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900, 1080), (0,0), get_image("sprites/normal/dv/dv_5_body.png"),(0,0), "mods/flew/res/images/sprites/dv/composite/dv_5_swim.png",(0,0), get_image("sprites/normal/dv/dv_5_angry.png")) )

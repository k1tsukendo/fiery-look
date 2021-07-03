# Copyright (c) k1tsukendo 2021. Some rights reserved. #
# Notice: GNU General Public License 3.0

init -6969:

    # Mobile adaptaition. Thx Mik.
    if renpy.variant('mobile'):
        transform mobile_zoom:
            zoom 0.66666666

    python:
        # Sooooo i dont wanna do it, but... ok?
        import os

        # Adaptive hotspot #
        def adapt_hotspot(*points): return points if len(points) > 1 else points[0] or 0

        # Auto-initialization. It s written by Jesus Christ.
        for file in renpy.list_files():
            if 'flew' in file:
                _filename = os.path.splitext(os.path.basename(file))[0]
                if file.endswith(('.jpg', '.png', '.webp')):
                    if 'sprites' in file and not 'composite' in file:
                        renpy.image(_filename.replace('_', ' '), ConditionSwitch('persistent.sprite_time == "sunset"', im.MatrixColor(file, im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time == 'night'", im.MatrixColor(file, im.matrix.tint(0.63, 0.78, 0.82)), True, file))
                    elif not 'gui' in file:
                        renpy.image(file.split('/')[-2]+' '+_filename, file)
                elif file.endswith(('.wav', '.ogg', '.opus', '.mp2', '.mp3')):
                    globals()[_filename] = file


init python:
    # Misc #
    def mod_exists(namespace):
        if namespace in mods:
            return True
        else:
            return False

    if not mod_exists('prowl'):

        def build_generator(flag):
            import datetime
            now = datetime.datetime.now()
            if flag == 11: 
                return 'build-{}{}-{}'.format(now.day, now.hour, now.year)
            if flag == 12:
                import random
                hash = random.getrandbits(128)
                return 'build : %032x' % hash

        def get_user_system_uname():
            global system_name, system_release, system_version, system_architecture
            import os

            system_name = os.uname()[0]
            system_release = os.uname()[2]
            system_version =  os.uname()[3]
            system_architecture = os.uname()[4]

    # Constants #
    K1TSU_MOD_VERSION = 'kitsudance 1.2.2'
    K1TSU_MOD_NAMESPACE = 'flew'
    K1TSU_MOD_STARTPOINT = 'flew_start'

    if flew_preferences["misc"]["debug_mode"]:
        K1TSU_MOD_NAME = '{font=mods/flew/res/fonts/futura_md.ttf}Огненный Взгляд %s{/font}' % K1TSU_MOD_VERSION
    else:
        K1TSU_MOD_NAME = '{font=mods/flew/res/fonts/futura_md.ttf}Огненный Взгляд{/font}'

    if mod_exists('prowl'):
        K1TSU_BUILDHASH = build_generator(BUILDGEN_BUILDHASH)
        K1TSU_BUILDTIME = build_generator(BUILDGEN_BUILDTIME)
    else:
        BUILDGEN_BUILDHASH = 11
        BUILDGEN_BUILDTIME = 12 

        K1TSU_BUILDHASH = build_generator(BUILDGEN_BUILDHASH)
        K1TSU_BUILDTIME = build_generator(BUILDGEN_BUILDTIME)

    # Initialize #
    mods[K1TSU_MOD_STARTPOINT] = K1TSU_MOD_NAME

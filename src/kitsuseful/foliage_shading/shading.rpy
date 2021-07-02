init python:
    def show_shaded_foliage_sprite(foliage_type, im, at, with_):
        renpy.show(im, at)
        renpy.show(AlphaMask('folliage_{}.png'.format(foliage_type), At(im, center), tag=mask))
        renpy.with_statement(with_)

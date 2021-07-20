from pygame.image import load


def load_sprite(name, with_alpha=True):
    path = f"B:/Programming/Python/UAVs/assets/sprites/{name}.png"

    print(path)
    loaded_sprite = load(path)

    if with_alpha:

        return loaded_sprite.convert_alpha()

    else:

        return loaded_sprite.convert()
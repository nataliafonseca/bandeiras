from PIL import Image, ImageDraw
import os


def vertices_estrela(c, w, h):
    vertices = [(-40, -10), (-10, -10), (0, -40), (10, -10), (40, -10), (15, 10), (25, 40), (0, 20), (-25, 40),
                (-15, 10)]
    vertices_finais = [((x * w // 80) + c[0], (y * h // 80) + c[1]) for (x, y) in vertices]

    return vertices_finais


def franca():
    for width in [16, 32, 64, 128, 256, 512, 1024]:
        height = width * 2 // 3
        blue = (0, 85, 164)
        white = (255, 255, 255)
        red = (239, 65, 53)

        image = Image.new("RGB", (width, height), white)

        draw = ImageDraw.Draw(image)
        draw.rectangle([(0, 0), (width // 3, height)], blue)
        draw.rectangle([(2 * width // 3, 0), (width, height)], red)

        if not os.path.exists('static/images'):
            os.makedirs('static/images')
        image.save(f'static/images/franca-{width}.png')


def japao():
    for width in [16, 32, 64, 128, 256, 512, 1024]:
        height = width * 2 // 3
        white = (255, 255, 255)
        red = (189, 0, 41)

        r = 3 * height // 10
        c = (width // 2, height // 2)

        image = Image.new("RGB", (width, height), white)

        draw = ImageDraw.Draw(image)
        draw.ellipse([(c[0] - r, c[1] - r), (c[0] + r, c[1] + r)], red)

        if not os.path.exists('static/images'):
            os.makedirs('static/images')
        image.save(f'static/images/japao-{width}.png')


def dinamarca():
    for width in [16, 32, 64, 128, 256, 512, 1024]:
        height = width * 28 // 37
        white = (255, 255, 255)
        red = (198, 12, 48)

        image = Image.new("RGB", (width, height), red)

        draw = ImageDraw.Draw(image)
        draw.rectangle([(width * 12 // 37, 0), (width * 16 // 37, height)], white)
        draw.rectangle([(0, (height // 2) - (height * 2 // 28)), (width, (height // 2) + (height * 2 // 28))], white)

        if not os.path.exists('static/images'):
            os.makedirs('static/images')
        image.save(f'static/images/dinamarca-{width}.png')


def porto_rico():
    for width in [16, 32, 64, 128, 256, 512, 1024]:
        height = width * 2 // 3
        white = (255, 255, 255)
        red = (239, 0, 0)
        blue = (0, 79, 240)

        image = Image.new("RGB", (width, height), white)

        draw = ImageDraw.Draw(image)
        draw.rectangle([(0, 0), (width, height // 5)], red)
        draw.rectangle([(0, 2 * height // 5), (width, 3 * height // 5)], red)
        draw.rectangle([(0, 4 * height // 5), (width, height)], red)
        draw.polygon([(0, 0), (0, height), (width * 512 // 900, height // 2)], blue)
        estrela = vertices_estrela((width * 173 // 900, height // 2), width * 192 // 900, height * 183 // 600)
        draw.polygon(estrela, white)

        if not os.path.exists('static/images'):
            os.makedirs('static/images')
        image.save(f'static/images/porto_rico-{width}.png')


def islandia():
    for width in [16, 32, 64, 128, 256, 512, 1024]:
        height = width * 18 // 25
        white = (255, 255, 255)
        red = (220, 30, 53)
        blue = (2, 82, 156)

        image = Image.new("RGB", (width, height), blue)

        draw = ImageDraw.Draw(image)
        draw.line([(0, height // 2), (width, height // 2)], white, width * 200 // 900)
        draw.line([(width * 450 // 1250, 0), (width * 450 // 1250, height)], white, width * 200 // 900)
        draw.line([(0, height // 2), (width, height // 2)], red, width * 100 // 900)
        draw.line([(width * 450 // 1250, 0), (width * 450 // 1250, height)], red, width * 100 // 900)

        if not os.path.exists('static/images'):
            os.makedirs('static/images')
        image.save(f'static/images/islandia-{width}.png')


def irlanda():
    for width in [16, 32, 64, 128, 256, 512, 1024]:
        height = width * 1 // 2
        white = (255, 255, 255)
        green = (14, 156, 98)
        orange = (255, 137, 60)

        image = Image.new("RGB", (width, height), white)

        draw = ImageDraw.Draw(image)
        draw.rectangle([(0, 0), (width // 3, height)], green)
        draw.rectangle([(width * 2 // 3, 0), (width, height)], orange)

        if not os.path.exists('static/images'):
            os.makedirs('static/images')
        image.save(f'static/images/irlanda-{width}.png')


def alemanha():
    for width in [16, 32, 64, 128, 256, 512, 1024]:
        height = width * 3 // 5
        black = (0, 0, 0)
        red = (222, 0, 0)
        yellow = (255, 207, 0)

        image = Image.new("RGB", (width, height), black)

        draw = ImageDraw.Draw(image)
        draw.rectangle([(0, height // 3), (width, 2 * height // 3)], red)
        draw.rectangle([(0, 2 * height // 3), (width, height)], yellow)

        if not os.path.exists('static/images'):
            os.makedirs('static/images')
        image.save(f'static/images/alemanha-{width}.png')


def reino_unido():
    for width in [16, 32, 64, 128, 256, 512, 1024]:
        height = width * 3 // 5
        white = (255, 255, 255)
        red = (200, 16, 46)
        blue = (1, 33, 105)

        image = Image.new("RGB", (width, height), blue)

        draw = ImageDraw.Draw(image)
        draw.line([(0, 0), (width, height)], white, 120 * width // 1000)
        draw.line([(width, 0), (0, height)], white, 120 * width // 1000)

        draw.line([(0, height), (width, 0)], red, 40 * width // 1000)
        draw.line([(0, 0), (width, height)], red, 40 * width // 1000)

        draw.line([(0, height // 2), (width, height // 2)], white, 200 * width // 1000)
        draw.line([(width // 2, 0), (width // 2, height)], white, 200 * width // 1000)

        draw.line([(0, height // 2), (width, height // 2)], red, 120 * width // 1000)
        draw.line([(width // 2, 0), (width // 2, height)], red, 120 * width // 1000)

        if not os.path.exists('static/images'):
            os.makedirs('static/images')
        image.save(f'static/images/reino_unido-{width}.png')


def tanzania():
    for width in [16, 32, 64, 128, 256, 512, 1024]:
        height = width * 2 // 3
        black = (0, 0, 0)
        yellow = (252, 209, 22)
        green = (30, 181, 58)
        blue = (0, 163, 221)

        image = Image.new("RGB", (width, height), green)

        draw = ImageDraw.Draw(image)
        draw.polygon([(0, height), (width, 0), (width, height)], blue)
        draw.line([(0, height), (width, 0)], yellow, 237 * width // 900)
        draw.line([(0, height), (width, 0)], black, 162 * width // 900)

        if not os.path.exists('static/images'):
            os.makedirs('static/images')
        image.save(f'static/images/tanzania-{width}.png')


def nigeria():
    for width in [16, 32, 64, 128, 256, 512, 1024]:
        height = width * 1 // 2
        white = (255, 255, 255)
        green = (0, 136, 80)

        image = Image.new("RGB", (width, height), green)

        draw = ImageDraw.Draw(image)
        draw.rectangle([(width // 3, 0), (2 * width // 3, height)], white)

        if not os.path.exists('static/images'):
            os.makedirs('static/images')
        image.save(f'static/images/nigeria-{width}.png')


def gerar_imagens():
    franca()
    japao()
    dinamarca()
    porto_rico()
    islandia()
    irlanda()
    alemanha()
    reino_unido()
    tanzania()
    nigeria()


if __name__ == '__main__':
    gerar_imagens()

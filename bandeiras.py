from PIL import Image, ImageDraw
import os


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


def gerar_imagens():
    franca()
    japao()


if __name__ == '__main__':
    gerar_imagens()

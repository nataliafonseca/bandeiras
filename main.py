from PIL import Image, ImageDraw


def bandeira_franca(width):
    height = width * 2 // 3
    blue = (0, 85, 164)
    white = (255, 255, 255)
    red = (239, 65, 53)

    image = Image.new("RGB", (width, height), white)

    draw = ImageDraw.Draw(image)
    draw.rectangle([(0, 0), (width // 3, height)], blue)
    draw.rectangle([(2 * width // 3, 0), (width, height)], red)

    return image


def bandeira_japao(width):
    height = width * 2 // 3
    white = (255, 255, 255)
    red = (189, 0, 41)

    r = 3 * height // 10
    c = (width // 2, height // 2)

    image = Image.new("RGB", (width, height), white)

    draw = ImageDraw.Draw(image)
    draw.ellipse([(c[0] - r, c[1] - r), (c[0] + r, c[1] + r)], red)

    return image


if __name__ == "__main__":
    bandeira = bandeira_japao(700)
    bandeira.show()

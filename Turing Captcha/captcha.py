import random
import string
from PIL import Image, ImageDraw, ImageFont


def makeCaptchaText(n=6):
    chars = string.ascii_letters + string.digits
    text = ""

    for i in range(n):
        text += random.choice(chars)

    return text


def makeImage(text):
    w = 200
    h = 80

    img = Image.new("RGB", (w, h), "white")
    d = ImageDraw.Draw(img)

    try:
        f = ImageFont.truetype("arial.ttf", 40)
    except:
        f = ImageFont.load_default()

    d.text((40, 20), text, fill="black", font=f)

    # adding some random lines for noise
    for i in range(5):
        x1 = random.randint(0, w)
        y1 = random.randint(0, h)
        x2 = random.randint(0, w)
        y2 = random.randint(0, h)

        d.line((x1, y1, x2, y2), fill="gray")

    img.save("captcha_img.png")
    img.show()


def checkCaptcha(realText):
    user = input("Enter the CAPTCHA shown: ")

    if user == realText:
        print("Correct! You are verified.")
    else:
        print("Wrong CAPTCHA.")


def main():
    print("Generating CAPTCHA...\n")

    captcha = makeCaptchaText()
    makeImage(captcha)

    checkCaptcha(captcha)


main()
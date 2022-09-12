import sys
import os
from PIL import Image, ImageOps


def main():
    image_input, image_output = get_images()
    create_new_image(image_input, image_output)


def get_images():
    extensions = ['.jpg', '.jpeg', '.png']

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    image_input = sys.argv[1]
    image_output = sys.argv[2]

    image_input_extension = os.path.splitext(image_input)[1].lower()

    image_output_extension = os.path.splitext(image_output)[1].lower()

    if image_output_extension not in extensions:
        sys.exit("Invalid output")

    if image_input_extension == ".png" and image_output_extension != ".png":
        sys.exit("Input and output have different extensions")
    elif image_input_extension in [".jpg", ".jpeg"] and image_output_extension not in [".jpg", ".jpeg"]:
        sys.exit("Input and output have different extensions")

    return [image_input, image_output]


def create_new_image(image, name_image_output):
    try:
        image_input = Image.open(image)
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirt = Image.open("shirt.png")
    size = shirt.size
    muppet = ImageOps.fit(image_input, size)
    muppet.paste(shirt, shirt)
    muppet.save(name_image_output)


if __name__ == "__main__":
    main()

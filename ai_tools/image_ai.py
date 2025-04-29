from PIL import Image, ImageFilter

def blur_image(image_path):
    img = Image.open(image_path)
    blurred = img.filter(ImageFilter.GaussianBlur(5))
    blurred.save("blurred_output.png")
    return "blurred_output.png"

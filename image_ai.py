from PIL import Image, ImageFilter
import io

def blur_image(file: bytes):
    image = Image.open(io.BytesIO(file))
    blurred = image.filter(ImageFilter.GaussianBlur(radius=5))
    output = io.BytesIO()
    blurred.save(output, format="PNG")
    return output.getvalue()

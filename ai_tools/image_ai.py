from PIL import Image, ImageFilter
import io

def blur_image(image_bytes: bytes) -> bytes:
    image = Image.open(io.BytesIO(image_bytes))
    blurred = image.filter(ImageFilter.GaussianBlur(radius=5))
    byte_io = io.BytesIO()
    blurred.save(byte_io, format='PNG')
    return byte_io.getvalue()

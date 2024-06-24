import os
from PIL import Image, ImageEnhance, ImageFilter

output_folder = 'image'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def process_image(input_image_path, a, b, c, d, e):
    # Đọc ảnh gốc
    img = Image.open(input_image_path)

    # 1. Xoay ảnh theo thông số a
    img_rotated = img.rotate(a, expand=True)

    # 2. Thu nhỏ ảnh theo b% ảnh gốc
    width, height = img.size
    new_size = (int(width * b / 100), int(height * b / 100))
    img_resized = img.resize(new_size)

    # 3. Chuyển ảnh gốc thành ảnh xám
    img_gray = img.convert('L')

    # 4. Cắt ảnh thành 2 ảnh (trái phải)
    half_width = width // 2
    img_left = img.crop((0, 0, half_width, height))
    img_right = img.crop((half_width, 0, width, height))

    # 5. Đổi brightness của ảnh phải theo thông số c
    enhancer_brightness = ImageEnhance.Brightness(img_right)
    img_right_brightened = enhancer_brightness.enhance(c)

    # 6. Đổi contrast của ảnh trái theo thông số d
    enhancer_contrast = ImageEnhance.Contrast(img_left)
    img_left_contrasted = enhancer_contrast.enhance(d)

    # 7. Làm mờ ảnh gốc theo thông số e
    img_blurred = img.filter(ImageFilter.GaussianBlur(radius=e))

    return {
        'rotated': img_rotated,
        'resized': img_resized,
        'gray': img_gray,
        'left': img_left,
        'right_brightened': img_right_brightened,
        'left_contrasted': img_left_contrasted,
        'blurred': img_blurred}


input_image_path = 'unnamed.png'
a = 90
b = 50
c = 1.5
d = 1.5
e = 2.0
processed_images = process_image(input_image_path, a, b, c, d, e)
for name, img in processed_images.items():
    img.save(os.path.join(output_folder, f'{name}.png'))

print("Result:")

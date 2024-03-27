def image_info(img):
    if ('image_title' not in img):
        raise ValueError("Image title must be present")
    elif ('image_id' not in img):
        raise ValueError("Image ID must be present")
    return (f"Image {img['image_title']} has id {img['image_id']} ")


image1 = {
    'image_title': 'My cat',
    'image_id': 5136,
}
print(image_info(image1))

image2 = {
    'image_title': 'My cat',
}
print(image_info(image2))

image3 = {
    'image_id': 5136,
}
print(image_info(image3))

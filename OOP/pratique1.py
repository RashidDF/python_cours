class Image:
    def __init__(self, title, resolution, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_resolution):
        self.resolution = new_resolution

    def __str__(self):
        return (f"{self.title},\n{self.resolution},\n{self.extension};\n")

    @staticmethod
    def merge_comment(first, second):
        return f"{first} {second}"


image1 = Image('first', '600X300', 'jpg')
print(image1)

image1.resize('300X150')
print(image1)

print(Image.merge_comment("Thanks!", "Excellent."))
print(image1.merge_comment("Great.", "OK."))

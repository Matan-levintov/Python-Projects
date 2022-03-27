class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_cords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        average = int((self._blue + self._green + self._red)/3)
        self._green = self._blue = self._red = average

    def print_pixel_info(self):
        count = 0
        dictOfColors = {'Red': self._red,
                        'Green': self._green, 'Blue': self._blue}
        for key, value in dictOfColors.items():
            if value == 0:
                count += 1
            else:
                color = key
        if count == 2:
            print(
                f"X : {self._x}, Y : {self._y}, Color: ({self._red},{self._green},{self._blue}) {color}")
        else:
            print(
                f"X : {self._x}, Y : {self._y}, Color: ({self._red},{self._green},{self._blue})")


my_pixel = Pixel(5, 6, 250, 0, 0)
my_pixel.print_pixel_info()
my_pixel.set_grayscale()
my_pixel.print_pixel_info()

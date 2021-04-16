from Image.Image import Image
from mouse.Mouse import Mouse
from paint.Paint import Paint


class App:
    def __init__(self):
        self.image = Image('assets/circle.png')
        self.mouse = Mouse()

    def run(self):
        while True:
            pos = self.mouse.get_position()
            print(pos)


if __name__ == "__main__":
    app = App()
    app.run()

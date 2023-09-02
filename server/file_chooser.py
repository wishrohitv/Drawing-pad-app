from plyer import filechooser


def file():
    filechooser.open_file(on_selection=selected)


def selected(selection):
    print(selection[0])


file()

import sys
import mymodule as layer_1
import mymodule.game as layer_2


def main():
    ver = sys.version

    print(f'Start {ver} package test \n')
    # print(mymodule.__doc__)
    layer_1.game.import_test2.game_test()
    layer_2.import_test2.game_test()
    print("")

    print("="*8, "graphic", "="*8)
    layer_2.render.render_test()
    print("")
    layer_2.graphic.render.render_test()

    print("="*8, "sound", "="*8)
    layer_2.sound.echo.echo_test()

    # simple_cal = layer_1.Calculator()
    # a = simple_cal.multiadd()
    print("")
    print("===add numbers===")
    layer_1.funset.add_number(3, 4)
    data = {"x": 1, "y": 2, "z": 3}
    layer_1.funset.add_numbers(10, 11, 12, 13, **data)
    layer_1.add_numbers(3,7,3,3,4)
    # print(layer_1.MODULENAME, "\n")

if __name__ == "__main__":
    main()

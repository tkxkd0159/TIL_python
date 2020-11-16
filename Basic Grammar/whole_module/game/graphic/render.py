from .. import sound

def render_test():
    print("render.py is executed")
    sound.echo_test()
    print("Relative Package : sound")
    print("when import other modules, it can use '..'  only in the module file")

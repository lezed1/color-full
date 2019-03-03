import importlib


def get_effect(name):
    return importlib.import_module(__name__ + "." + name).effect()

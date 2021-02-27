from ipywidgets import interact


def func(x):
    return x


interact(func, x=(-10, 10, 1))

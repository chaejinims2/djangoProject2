def decorator(func):
    def decorated(h, w):
        if w >= 0 and h >= 0:
            return func(h, w)
        else:
            raise ValueError('Input must be positive value')
    return decorated


@decorator
def trianlge(h, w):
    return h*w*(1/2)

@decorator
def Ractangle(h, w):
    return h*w
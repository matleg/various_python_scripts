import math

EPSILON = 1e-15


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({} {})".format(self.x, self.y)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def round(self):
        return Point(round(self.x), round(self.y))

    def distance(self, p):
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

    def distance2(self, p):
        """square of the distance"""
        return (self.x - p.x) ** 2 + (self.y - p.y) ** 2

    def closest(self, a, b):
        """ return the closest point on the line a-b"""
        da = b.y - a.y
        db = a.x - b.x
        c1 = da * a.x + db * a.y
        c2 = -db * self.x + da * self.y
        det = da * da + db * db
        if det != 0:
            cx = (da * c1 - db * c2) / det
            cy = (da * c2 + db * c1) / det
        else:  # The point is already on the line
            cx = self.x
            cy = self.y
        return Point(cx, cy)


# TODO : same with an angle ?


class Vector:  # 2D
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def __sub__(self, v):
        return Vector(self.x - v.x, self.y - v.y)

    def __mul__(self, v):
        """ Returns the dot product if multiplied by another Vector.
        otherwise multiplies each component by v.
        """
        if type(v) == type(self):
            return self.inner(v)
        elif type(v) in (int, float):
            return Vector(self.x * v, self.y * v)

    # def __rmul__(self, v):
    #     return self.__mul__(v)

    def __div__(self, v):
        if type(v) in (int, float):
            return Vector(self.x / v, self.y / v)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def inner(self, v):
        """ Returns the dot product (inner product) of self and vector
        np.dot and np.inner are identical for 1-dimensions arrays
        np.inner is also "vector product". It includes matrix-vector multiplication
        np.dot corresponds to a "tensor product". It includes matrix-matrix multiplication.
        """
        return self.x * v.x + self.y * v.y

    def norm(self):
        """ the norm (length, magnitude) of the vector """
        return abs(self)

    def length(self):
        """ the norm (length, magnitude) of the vector """
        return abs(self)

    def norm2(self):
        """ norm squared of the vector """
        return self.x ** 2 + self.y ** 2

    def normalize(self):
        """ Return a normalized unit vector """
        norm = self.norm()
        return Vector(self.x / norm, self.y / norm)

    def angle(self):
        """ angle in radians between x+ axis and point in a plan"""
        # only for 2D vectors
        return math.atan2(self.y, self.x)

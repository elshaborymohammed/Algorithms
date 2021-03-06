class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def plus(self, v):
	new_coordinates = [x+y dor x,y in zip(self.coordinates,v.coordinates)]
	return Vector(new_coordinates)

    def minus(self, v):
	new_coordinates = [x-y dor x,y in zip(self.coordinates,v.coordinates)]
	return Vector(new_coordinates)

    def times_scaler(self, c):
	new_coordinates = [c*x for x in self.coordinate]
	return Vector(new_coordinates)

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

my_vector = Vector([-1,1,1]);
print my_vector

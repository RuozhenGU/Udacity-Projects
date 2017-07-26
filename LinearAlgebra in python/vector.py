from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
            self.idx = 0

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def plus(self,v):
        new_coordinates = [x + y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)


    def minus(self,v):
        new_coordinates = [x - y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self,c):
        new_coordinates = [Decimal(c) * x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return Decimal(sqrt(sum(coordinates_squared)))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal('1.0') / magnitude)

        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)


    def is_orthogonal_to(self, v, tolerance = 1e-10):
        return abs(self.dot(v)) < tolerance

    def is_parellel_to(self, v):
        return (self.is_zero() or v.is_zero() or self.angle_with(v) == 0 
            or self.angle_with(v) == pi)

    def is_zero(self, tolerance = 1e-10):
        return self.magnitude() < tolerance


    def dot(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees = False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_radians = acos(u1.dot(u2))
            if in_degrees:
                degrees_per_radian = 180. / pi
                return angle_in_radians * degrees_per_radian
            else:   
                return angle_in_radians
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
    

    def projection(self, v):
        try:
            standard_v = v.normalized()
            d1 = self.dot(standard_v)
            return standard_v.times_scalar(d1)
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def projection_orthogonal_vector(self, v):
        try:
            projection = self.projection(v)
            return self.minus(projection)

        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e   

    def cross(self, v):
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates
            new_coordinates = [ y_1*z_2 - y_2*z_1,
                              -(x_1*z_2 - x_2*z_1),
                                x_1*y_2 - x_2 * y_1 ]
            return Vector(new_coordinates)

        except ValueError as e:   #in case that the vector is less than three dimension
            msg = str(e)
            if msg == 'need more than 2 values to unpack':
                self.embedded_in_R3 = Vector(self.coordinates + ('0',))
                v_embedded_in_R3 = Vector(v.coordinates + ('0',))
                return self_embedded_in_R3.cross(v_embedded_in_R3)
            elif (msg == 'too many values to unpack' or msg == 'need more than 1 value to unpack'):
                raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
            else:
                raise e

    def area_of_triangle_with(self, v):
        return self.area_of_parallelogram_with(v) / Decimal('2.0')

    def area_of_parallelogram_with(self, v):
        cross_product = self.cross(v)
        return cross_product.magnitude()


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

'''

###########################################

#v1 = Vector([-0.221,7.437])
#print v.magnitude()

#v2 = Vector([9.3,-1.32,-6.42])
#print v.normalized()

#v3 = Vector([7.887,4.138])
#w3 = Vector(['-8.802','6.776'])
#print v3.dot(w3)


v4 = Vector(['3.183','7.627'])
w4 = Vector(['2.668','5.319'])
print v4.angle_with(w4)
'''

'''
v = Vector([7.35,0.221,5.188])
w = Vector(['2.751','8.259',4.985])
print v.angle_with(w, in_degrees = True)


'''

'''
print 'first pair...'
v = Vector(['-7.579','-7.88'])
w = Vector(['22.737','23.64'])
print 'is parallel:' , v.is_parellel_to(w)
print 'is orthogonal:', v.is_orthogonal_to(w)
'''

'''
print '#1'
v= Vector([3.039,1.879])
w= Vector([0.825,2.036])
print v.projection(w)

print '#2'
v= Vector([3.009,-6.172,3.692,-2.51])
w= Vector([0,0,0,0])
vpar= w.projection(v)
vort= w.projection_orthogonal_vector(v)

print "parallel component:", vpar
print "orthogonal component:", vort
'''
'''
v = Vector(['8.462','7.893','-8.187'])
w = Vector(['6.984','-5.975','4.778'])
print '#1',v.cross(w)


v = Vector(['-8.987','-9.838','5.031'])
w = Vector(['-4.268','-1.861','-8.866'])
print '#2',v.area_of_parallelogram_with(w)


v = Vector(['1.5','9.547','3.691'])
w = Vector(['-6.007','0.124','5.772'])
print '#3',v.area_of_triangle_with(w)
'''











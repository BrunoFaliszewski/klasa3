from math import  *

class Rectangle:

    def get_points(self):
        point1 = (int(input("Podaj x dla 1 punktu: ")), int(input("Podaj y dla 1 punktu: ")))
        point2 = (int(input("Podaj x dla 2 punktu: ")), int(input("Podaj y dla 2 punktu: ")))

        return point1, point2

    def calculate_space(self, points):
        return fabs(points[0][0] - points[1][0]) * fabs(points[0][1] - points[1][1])

    def calculate_circuit(self, points):
        return fabs(points[0][0] - points[1][0]) * 2 + fabs(points[0][1] - points[1][1]) * 2

if __name__ == "__main__":
    rectangle = Rectangle()
    print(rectangle.calculate_space(rectangle.get_points()))
    print(rectangle.calculate_circuit(rectangle.get_points()))
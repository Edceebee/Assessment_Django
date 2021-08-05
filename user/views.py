import math
from math import sin, cos, acos

from rest_framework import views
from rest_framework.response import Response


class distance_view(views.APIView):

    def get(self, request):
        lat1 = self.request.query_params.get('latitude1')
        long1 = self.request.query_params.get('longitude1')
        lat2 = self.request.query_params.get('latitude2')
        long2 = self.request.query_params.get('longitude2')
        try:
            calculate_distance(lat1, long1, lat2, long2)
        except TypeError as e:
            return Response({"Error": str(e)})
        except ValueError as m:
            return Response({'Error': str(m)})

        values = {
            'latitude1': lat1,
            'longitude1': long1,
            'latitude2': lat2,
            'longitude2': long2,
            'distance is': calculate_distance(lat1, long1, lat2, long2)
        }
        return Response(values)


def calculate_distance(lat1, long1, lat2, long2):
    test = [lat1, long1, lat2, long2]
    converted = []
    for i, t in enumerate(test):
        print(t, i)
        value = ''
        if i == 0:
            value = 'latitude1'
        elif i == 1:
            value = 'longitude1'
        elif i == 2:
            value = 'latitude2'
        elif i == 3:
            value = 'longitude2'

        try:
            converted.append(int(t))
        except ValueError:
            raise ValueError(f"{t} is an invalid number")
        except TypeError:
            raise TypeError(f"{test} {value} --> cannot be empty ")

    lat1 = math.radians(int(lat1))
    long1 = math.radians(int(long1))
    lat2 = math.radians(int(lat2))
    long2 = math.radians(int(long2))
    earthRadius = 6371.01

    distance = earthRadius * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(long1 - long2))
    new_distance = str(round(distance, 2))
    return f"{new_distance}km"

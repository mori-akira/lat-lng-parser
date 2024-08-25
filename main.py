from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time


target_file = 'target.txt'
result_file = 'result.csv'


def get_lat_lng(geolocator, place_name):
    try:
        location = geolocator.geocode(place_name)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        return get_lat_lng(geolocator, place_name)


if __name__ == '__main__':
    with open(target_file, mode='r', encoding='utf-8') as f:
        places = f.readlines()

    geolocator = Nominatim(user_agent="geoapiExercises")
    with open(result_file, mode='w', encoding='utf-8') as f:
        for place in places:
            place = place.replace('\n', '')
            lat, lng = get_lat_lng(geolocator, place)
            if lat and lng:
                print(f"{place}: 緯度={lat}, 経度={lng}")
                print(f'{place}\t{lat}\t{lng}', file=f)
            else:
                print(f"{place}: 緯度/経度が見つかりませんでした。")
                print(f'{place}', file=f)
            time.sleep(1)  # リクエスト制限にかからないように1秒待つ

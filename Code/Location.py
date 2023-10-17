import geocoder  # Install the geocoder library: pip install geocoder
from geopy.geocoders import Nominatim  # install the geopy library :pip install geopy


def get_current_location():
    # Use IP-API to get the current location based on IP address
    g = geocoder.ip('me')
    address = get_address_from_latlng(g.latlng[0], g.latlng[1])
    return address


def get_address_from_latlng(latitude, longitude):
    geolocator = Nominatim(user_agent="usertesting")
    location = geolocator.reverse((latitude, longitude), language='en')

    if location:
        return location.address
    else:
        return "Address not found."


if __name__ == "__main__":
    location = get_current_location()
    print(location)

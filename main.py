import phonenumbers
from phonenumbers import geocoder, carrier, timezone, phonenumberutil

def get_phone_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)

        # Ülke Bilgisi
        country = geocoder.country_name_for_number(parsed_number, "en")

        # Bölge Bilgisi
        region = geocoder.description_for_number(parsed_number, "en", region=True)

        # Operatör Bilgisi
        operator = carrier.name_for_number(parsed_number, "en")

        # Numara Türü
        number_type = phonenumberutil.number_type(parsed_number)

        # Geokoordinatlar
        location = geocoder.description_for_number(parsed_number, "en")

        # Zaman Dilimi
        time_zones = timezone.time_zones_for_number(parsed_number)
        time_zone = ", ".join(time_zones)

        # Numara Durumu
        is_valid = phonenumbers.is_valid_number(parsed_number)

        return country, region, operator, number_type, location, time_zone, is_valid
#https://www.instagram.com/efe1sus/
    except phonenumbers.phonenumberutil.NumberParseException:
        return None

# Kullanıcıdan telefon numarasını alın
phone_number = input("Telefon numarasını girin: ")

# Telefon bilgilerini alın
result = get_phone_info(phone_number)

if result:
    country, region, operator, number_type, location, time_zone, is_valid = result
    print("Ülke: ", country)
    print("Bölge: ", region)
    print("Operatör: ", operator)
    print("Numara Türü: ", number_type)
    print("Geokoordinatlar: ", location)
    print("Zaman Dilimi: ", time_zone)
    print("Numara Durumu: ", "Geçerli" if is_valid else "Geçersiz")
else:
    print("Geçersiz telefon numarası.")

from address import Address
from mailing import Mailing


to_address = Address(555777, "Подольск", "Гаражный", "81", "37")
from_address = Address(777555, "Москва", "Коломенская", "53", "75")
cost = 275
track = "track_07"


mailing = Mailing(track, from_address, to_address, cost)


print(mailing)

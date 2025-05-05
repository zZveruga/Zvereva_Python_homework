from smartphone import Smartphone


catalog = [
    Smartphone("Samsung", "M031", "+79996669999"),
    Smartphone("Honor", "P55", "+79995511888"),
    Smartphone("Sony", "F.1", "+79661112233"),
    Smartphone("Apple", "16 Pro Max", "+79660000000"),
    Smartphone("LG", "K9", "+79990009900")
]


for smartphone in catalog:
    print(f"{smartphone.phone_brand} - {smartphone.phone_model} - {smartphone.number}")
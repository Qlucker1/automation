from Address import Address
from mail import Mailing

ot_adress = []
to_address = Address(123, 'Moscow', 'Lenina', 1, 2)
from_address = Address(456, 'Saint Petersburg', 'Pushkin', 3, 4)

ot_adress.append(
    Mailing(
        to_address,
        from_address,
        cost= 1900,
        track= 1488
    )
)


for Mailing in ot_adress:
    print(f'Отправление {Mailing.track} из {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house}, {from_address.apartment}')
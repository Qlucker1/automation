from smartphone import Smartphone
import random

catalog = []
catalog_brand = ['xiaomi', 'honor', 'huawei', 'realme', 'hyilmi']
catalog_model = ['14', '13', '12', '11', '9', '10', '7', '6']
catalog_number = ['790000000', '790000001', '790000011', '790000111', '790001111', '790011111', '790111111', '791111111']


# Наполнение списка пятью разными экземплярами
for _ in range(5):
    catalog.append(
        Smartphone(
            phone_brand= random.choice(catalog_brand),
            phone_model= random.choice(catalog_model),
            subscriber_number= random.choice(catalog_number)
        )
    )

for smartphone in catalog:
    print(f"{smartphone.phone_brand} - {smartphone.phone_model}. {smartphone.subscriber_number}")
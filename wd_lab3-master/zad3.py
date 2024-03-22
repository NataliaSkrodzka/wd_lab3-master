produkty_spozywcze = {'jablka': 'kg', 'bulki': 'sztuki', 'banany': 'kg', 'mleko': 'butelki'}
produkty_na_sztuki = {key: value for key, value in produkty_spozywcze.items() if value == 'sztuki'}
print(produkty_na_sztuki)

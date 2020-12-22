import requests


API_KEY = '30505da054ac8810c3c22bd360f9f57e'
PASSWORD = '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'
shop_url = 'https://%s:%s@duyutc812.myshopify.com/admin/api/2020-10/customers.json' % (API_KEY, PASSWORD)
response = requests.get(shop_url)
data_customer = response.json()["customers"]
# print(data_customer)
col_data = [customer_key for customer_key in data_customer[0].keys() if customer_key not in ['addresses', 'default_address']]
file = open('customer_write.csv', 'w')
file.write(','.join(col_data))
for i in range(0, len(data_customer)):
    row_data = [str(v) for k, v in data_customer[i].items() if k not in ['addresses', 'default_address']]
    print(row_data)
    file.write('\n')
    file.write(','.join(row_data))
file.close()

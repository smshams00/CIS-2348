# Syed Shams
# 1820287

print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')

service = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax': 12,
    '-': 'No service'
}

print()

print('Select first service:')
first_service = input()
print('Select second service:')
second_service = input()

print()

print("Davy's auto shop invoice")

print()

service_1 = service[first_service]
service_2 = service[second_service]

if service_1 == 'No service':
    print('Service 1:', service_1)
    print('Service 2:', second_service + ',', '${:,.0f}'.format(service_2))
elif service_2 == 'No service':
    print('Service 1:', first_service + ',', '${:,.0f}'.format(service_1))
    print('Service 2:', service_2)
else:
    print('Service 1:', first_service + ',', '${:,.0f}'.format(service_1))
    print('Service 2:', second_service + ',', '${:,.0f}'.format(service_2))

print()

if service_1 == 'No service':
    print('Total:', '${:,.0f}'.format(service_2))
elif service_2 == 'No service':
    print('Total:', '${:,.0f}'.format(service_1))
else:
    print('Total:', '${:,.0f}'.format(int(service_1) + int(service_2)))

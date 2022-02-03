from accounts.models import Client

client = Client.objects.create(phone_number='90')

print(client.id)

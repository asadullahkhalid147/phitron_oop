def call():
    print('calling someone i dont know')
    return 'call done'


class Phone:
    price = 200000
    color = 'black'
    brand ='I phone'
    features = ['camera','speaker','hammer']

    def call(self):#python a method a parameter thakuk ba na thakuk self likhte hoy
        print('calling one person')

    def send_sms(self,phone,sms):
        text = f'sending SMS to: {phone} and message:{sms}'
        return text

my_phone = Phone()
print(my_phone.features)

my_phone.call()
result = my_phone.send_sms(4444,'I forgot to miss you')
print(result)

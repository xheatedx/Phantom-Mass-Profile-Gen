import json, time, random, configparser

config = configparser.ConfigParser()
config.read('config.ini')

profiles = []

email_prefix = config['MAIN']['EMAIL_PREFIX']
domain = config['MAIN']['DOMAIN']
address_1 = config['MAIN']['ADDRESS_1']
address_2 = config['MAIN']['ADDRESS_2']
f_names = config['MAIN']['F_NAMES']
l_names = config['MAIN']['L_NAMES']
city = config['MAIN']['CITY']
state = config['MAIN']['STATE']
post_code = config['MAIN']['POST_CODE']
phone_prefix = config['MAIN']['PHONE_PREFIX']
profile_prefix = config['MAIN']['PROFILE_PREFIX']

if len(address_2) == 0:
    address_2 = ''

f_names = f_names.split(',')
l_names = l_names.split(',')

def random_email(email_prefix,domain):
    return email_prefix+random.choice('qwertyuioopasdfghjklzxcvbnm')+str(random.randint(1111,99999))+domain
def jig_address(address_1):
    address0 = address_1.split(' ')
    return address0[0]+' '+random.choice('QWERTYUIOPASDFGHJKLZXCVBNM')+str(random.randint(0,19))+' '+address0[1]+' '+address0[2]+' '+address0[3]
with open('cards.txt','r') as file:
    c = 1
    for line in file:
        data = line.split('\t')
        exp_month = data[2]
        if len(exp_month) == 1:
            exp_month = '0'+exp_month
        f_name = random.choice(f_names)
        l_name = random.choice(l_names)
        address_jigged = jig_address(address_1)
        profiles.append(
        {
            'CCNumber':data[0],
            'CVV':data[1],
            'ExpMonth':exp_month,
            'ExpYear':data[3],
            'Email':random_email(email_prefix,domain),
            'CardType':data[4][:-1],
            'Same':True,
            'Shipping':{
            'FirstName':f_name,
            'LastName':l_name,
            'Address':address_jigged,
            'Apt':address_2,
            'City':city,
            'State':state,
            'Zip':post_code
        },
            'Billing':{
            'FirstName':f_name,
            'LastName':l_name,
            'Address':address_jigged,
            'Apt':address_2,
            'City':city,
            'State':state,
            'Zip':post_code
        },
            'Phone':phone_prefix+str(random.randint(1231231,9879878)),
            'Name':profile_prefix+str(c),
            'Country':'US'
        }
        )
        c = c + 1

for profile in profiles:
    print profile

with open('Phantom Profiles.json','w') as file:
    json.dump(profiles,file)

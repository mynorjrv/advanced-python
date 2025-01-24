import configparser

config = configparser.ConfigParser()
print(config.read('./Python-advanced-5-File-Processing/config.ini'))

print('Sections:', config.sections(),'\n')

# Sections names are casesensitive, keys are not
print('mariadb section:')
print('Host:', config['mariadb']['host'])
print('Database:', config['mariadb']['name'])
print('Username:', config['mariadb']['user'])
print('Password:', config['mariadb']['password'], '\n')

print('redis section:')
print('Host:', config['redis']['host'])
print('Port:', int(config['redis']['port']))
print('Database number:', int(config['redis']['db']))


# It is possible to read dictionaries
# (and from strings and open files)
conf_dict = {
    'DEFAULT': {
        'host': 'localhost'
    },
    'mariadb': {
        'name': 'hello',
        'user': 'root',
        'password': 'password'
    },
    'redis': {
        'port': 6379,
        'db': 0
    }
}

config.read_dict(conf_dict)

print('Sections:', config.sections(),'\n')

print('mariadb section:')
print('Host:', config['mariadb']['host'])
print('Database:', config['mariadb']['name'])
print('Username:', config['mariadb']['user'])
print('Password:', config['mariadb']['password'], '\n')

print('redis section:')
print('Host:', config['redis']['host'])
print('Port:', int(config['redis']['port']))
print('Database number:', int(config['redis']['db']))



# Aaaaaand it is possible to write config files
# using dictionaries
# config['DEFAULT'] = {'host': 'localhost'}
# config['mariadb'] = {'name': 'hello',
#                      'user': 'root',
#                      'password': 'password'}
# config['redis'] = {'port': 6379,
#                    'db': 0}

# with open('config.ini', 'w') as configfile:
#     config.write(configfile)
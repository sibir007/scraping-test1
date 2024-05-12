import configparser

config = configparser.ConfigParser()

print(config.read('example.ini'))
print(config.sections())
print(config['forge.example']['User'])
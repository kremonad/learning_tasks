# Напишите декоратор obfuscator
def obfuscator(func):
    def wrapper():
        result = func()
        name = result['name']
        passw = result['password']
        name_obfuscated = name[0] + (len(name)-2) * '*' + name[-1]
        passw_obfuscated = len(passw) * '*'
        return {
            'name': name_obfuscated,
            'password': passw_obfuscated
        }
    return wrapper

@obfuscator
def get_credentials():
    return {
        'name': 'StasBasov',
        'password': 'iamthebest'
    }


print(get_credentials())
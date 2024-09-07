calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, strings_list):
    count_calls()
    contains = False
    for i in strings_list:
        if str(string.lower()) in str(i.lower()):
            contains = True
            break
    return contains

print(string_info("hello"))
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
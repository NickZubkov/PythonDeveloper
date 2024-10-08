def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()

#inner_function()

#Traceback (most recent call last):
#  File "C:\Users\Николай\PycharmProjects\HomeWorks\module_4\module_4_2.py", line 8, in <module>
#    inner_function()
#    ^^^^^^^^^^^^^^
#NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?

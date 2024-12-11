#!/usr/bin/python
# -*- coding: UTF-8 -*-

def introspection_info(obj):
    obj_type = type(obj)
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    module = getattr(obj, "__module__", "built-in")
    additional_properties = {"is_instance": isinstance(obj, obj_type)}

    result = {"type": obj_type.__name__, "attributes": attributes, "methods":  methods, "module":  module, "additional_properties":  additional_properties}

    return result

class TestClass:

    def __init__(self, value):
        self.value = value

    def test_method(self):
        return f"Value is {self.value}"


test_obj = TestClass(42)

info = introspection_info(test_obj)

print(info)

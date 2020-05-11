def camel_to_snake(name):
    """
    A function that converts camelCase to snake_case.
    Referred from: https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
    """
    import re
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

class SnakeCaseMetaclass(type):
    def __new__(snakecase_metaclass, future_class_name,
                future_class_parents, future_class_attr):
        snakecase_attrs = {}
        for name, val in future_class_attr.items():
            snakecase_attrs[camel_to_snake(name)] = val
        return type(future_class_name, future_class_parents,
                    snakecase_attrs)



class SomeClass(metaclass=SnakeCaseMetaclass):
    camelCaseVar = 5
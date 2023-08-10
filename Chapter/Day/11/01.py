"""Method Overrides"""


class BaseClass():
    def simple_method(self):
        """
        A simple method that returns a greeting.

        Returns:
            str: A greeting message.
        """
        return 'hello'


class SimpleClass(BaseClass):
    def simple_method(self):
        """
        Overrides the simple_method from the base class and adds 'world'.

        Returns:
            str: A greeting message with 'world'.
        """
        return super().simple_method() + ' world'


obj = SimpleClass()
print(obj.simple_method())

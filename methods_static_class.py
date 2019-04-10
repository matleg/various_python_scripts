
# From PyTricks realpython.com


class A:
    def method(self):
        return 'instance:', self

    @classmethod
    def classmethod(cls):
        return 'class method:', cls

    @staticmethod
    def staticmethod():
        return 'static method'


obj = A()
print(obj.method())
#('instance:', <__main__.A instance at 0x00000000036406C8>)
print(obj.classmethod())
# ('class method:', <class __main__.A at 0x000000000368E528>)
print(obj.staticmethod())
# static method


print(A.classmethod())
# ('class method:', <class __main__.A at 0x000000000368E528>)
print(A.staticmethod())
# static method
print(A.method())
# TypeError: unbound method method() must be called with A instance as first argument (got nothing instead)


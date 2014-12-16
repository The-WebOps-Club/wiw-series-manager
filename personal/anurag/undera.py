class A(object):
    def __init__(self):
        self.x = 'Hello'

    def method_a(self, foo):
        print self.x + ' ' + foo
a = A()              
a.method_a('Sailor!')
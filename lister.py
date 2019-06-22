"File with mix-in classes that display class inheritance that displays when str(obj) or print(obj) is called."

class ListInstance:
    """
    Mix-in class that provides a formatted print() or str() of
    instances via inheritance of __str__, coded here; displays
    instance attrs only; self is the instance of lowest class;
    uses __X names to avoid clashing with client's attrs
    """
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__,
            hex(id(self)),
            self.__attrnames())
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tname %s=%s\n' % (attr, self.__dict__[attr])
        return result

class ListInherited:
    """
    Use dir() to collect both instance attrs and names
    inherited from its classes; Python 3 shows more
    names than 2.6 and 2.7 because of the implied object
    superclass in the new-style class model; getattr()
    fetches inherited names not in self.__dict__; use
    __str__ , not __repr__, or else this loops when
    printing bound methods!
    """
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__,
            hex(id(self)),
            self.__attrnames()
        )
    def __attrnames(self):
        result = ''
        for attr in dir(self):
            if attr.startswith('__') and attr.endswith('__'):
                result += '\tname %s=<>\n' % attr
            else:
                result += '\tname %s=%s\n' % (attr, getattr(self, attr))
        return result

class ListTree:
    """
    Mix-in that returns an __str__ trace of the entire class
    tree and all its objects' attrs at and above self;
    run by print(), str() returns constructed string;
    """
    def __str__(self):
        self.__visited = set()
        return '<Instance of {0}, address {1}:\n{2}{3}>'.format(
            self.__class__.__name__,
            hex(id(self)),
            self.__attrnames(self, 0), #flag
            self.__listclass(self.__class__, 4)
        )
    
    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{0}<Class {1}, address {2}: (see above)>\n'.format(
                dots,
                aClass.__name__,
                hex(id(aClass))
            )
        else:
            self.__visited.add(aClass)
            genabove = (self.__listclass(c, indent+4) for c in aClass.__bases__)
            return '\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n'.format(
                dots,
                aClass.__name__,
                hex(id(aClass)),
                self.__attrnames(aClass, indent),
                ''.join(genabove),
                dots
            )
    
    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 4)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0}=<>\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result

class ListRepr:
    def __repr__(self):
        attrs = {}
        init = self.__init__.__code__
        for attr in dir(self):
            if attr in init.co_varnames:
                attrs[attr] = getattr(self, attr)
        attrlist = []
        for (attrname, attr) in attrs.items():
            attrlist.append('%s=%r' % (attrname, attr))
        return '%s(%s)' % (self.__class__.__qualname__, ', '.join(attrlist))
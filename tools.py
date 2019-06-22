"A module with tools to help you program with python"

from time import clock as applicationruntime
import os, sys

def dictformat(dic):
    """Format a dictionary object into a pretty format
    
    Parameters
    ----------
    dic : dict
    
    Returns
    -------
    str"""
    greatest = max(len(key) for key in dic.keys())
    ident = '\n    '
    res = []
    for (key, item) in dic.items():
        res.append('%-*s =>' % (greatest, key))
        if hasattr(item, 'items'):
            try: sub = dictformat(item)
            except TypeError: pass
            else:
                res[-1] += ident + sub.replace('\n', ident)
                continue
        res[-1] += ' %r' % item
    return '\n'.join(res)

def fix_none(var, desired_type): 
    """Returns var if var isn't None, otherwise it returns desired_type()
    
    Parameters
    ----------
    var
    desired_type"""
    return (desired_type() if var == None else desired_type(var))

def str_split_len(string, substrLength):
    """Returns a list of strings of the length specified in substrLength
    
    Parameters
    ----------
    string : str
    substrLength : int
    
    Returns
    -------
    list of str"""
    words = []
    for i in range((len(string) // substrLength) + 1):
        i *= substrLength
        words.append(substr(string, i, substrLength) if len(string) - i >= substrLength else substr(string, i, len(string) - i))
    if '' in words: words.remove('')
    return words

def substr(string, start, length):
    "Provides a classic substring function"
    return string[start:start + length]

def impfile(path, fromlist=()):
    """Imports a file from specified in path
    
    Warnings
    --------
    You need to be careful when using this tool due to the way it works
    
    Parameters
    ----------
    path : str
    fromlist : tuple
        corresponds to the fromlist parameter of the __import__ function"""
    path = os.path.split(path)
    path = (path[0], os.path.splitext(path[-1])[0])
    sys.path.insert(0, path[0])
    mod = __import__(path[1], fromlist=fromlist)
    sys.path[:1] = []
    return mod
# def impfile(path, name=None):
    # path = path.split(os.sep)
    # if not name:
    #     name = path[-1]
    # sys.path.append(os.path.join(path[:-1]))
    # exec('import %s as %s' % (path[-1], name))
    # sys.path[-1] = []

# def runfile(file, *args):
#     if sys.platform[:3] == 'win': os.startfile(os.path.abspath(file))
#     else:
#         if os.fork() == 0: os.execl(file, *args)

# import pickle, types, heapq
# def pickle_function_dumps(func,
#     proto = None):
#     codeobj = func.__code__
#     code = {}
#     for item in dir(codeobj):
#         if item[:2] != '__' and item[-2:] != '__':
#             code[item] = getattr(codeobj, item)
#     pkldict = dict(
#         name = func.__name__,
#         defaults = func.__defaults__,
#         code = code
#     )
#     return pickle.dumps(pkldict, proto)
# def pickle_function_loads(data,
#     encoding = 'ASCII',
#     errors = 'strict'):
#     pkldict = pickle.loads(data, encoding=encoding, errors=errors)
#     code = types.CodeType(**pkldict['code'])
#     # code = pkldict['code']
#     # code.__class__ = types.CodeType
#     func = types.FunctionType(code, name=pkldict['name'])
#     func.__defaults__ = pkldict['defaults']
#     return func

if __name__ == "__main__":
    pass
    # dic = dict(
    #     test = 35,
    #     test2 = 360,
    #     test3 = 'Jump up',
    #     test4 = 'hello World',
    #     test63 = dict(
    #         test2 = 'pu pmuJ',
    #         test1 = 'dlroW olleh'
    #     )
    # )
    # print(dictformat(dic))
    # hello = impfile(r"C:\Users\josia\MEGA\Projects\Programming Languages\Python\PP4E\Gui\Tour\toplevel0.py")
    # print(hello.win1)
    # print(hello.message('impfile... does it work?'))
    # var = {1:10,2:20,3:30}
    # var = fix_none(var, dict)
    # print(repr(var))
    # def test(data='Something'):
    #     print(data)
    # print(test())
    # pkl = pickle_function_dumps(test)
    # print(pkl)
    # new = pickle_function_loads(pkl)
    # print(new())
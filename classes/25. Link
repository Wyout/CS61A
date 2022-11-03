class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest
    
    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + repr(list) + ')'
    
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

def empty(s):
    return True if s == Link.empty else False

def range_link(start, end):
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start+1, end))

def add(s, v):
    assert s is not Link.empty
    assert isinstance(s, Link)
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest) 
        # 后面的s依旧是老s，这种写法可以简化代码，不用单独再写个temp啥的
    elif s.first < v and empty(s.rest):
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest, v)
    return s
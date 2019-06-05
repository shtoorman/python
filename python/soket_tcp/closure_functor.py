def addClosure(val1):
    def closure(val2):
        return val1 + val2

    return closure


class AddFunctor(object):
    def __init__(self, val1):
        self.val1 = val1

    def __call__(self, val2):
        return self.val1 + val2


cl = addClosure(2)
fn = AddFunctor(2)

print(cl(1), fn(1))
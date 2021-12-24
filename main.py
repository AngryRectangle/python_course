class mydefaultdict(dict):
    def __init__(self, default_factory):
        super().__init__()
        self.factory = default_factory

    def __getitem__(self, y):
        if y not in self:
            self.__setitem__(y, self.factory())
        return super().__getitem__(y)


s = 'mississippi'
d = mydefaultdict(int)
for k in s:
    d[k] += 1

print(sorted(d.items()))

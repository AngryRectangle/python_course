class mydefaultdict(dict):
    def __init__(self, default_factory, seq=None, **kwargs):
        super().__init__(**kwargs) if seq is None else super().__init__(seq, **kwargs)
        self.factory = default_factory
    def __getitem__(self, y):
        if y not in self: self.__setitem__(y, self.factory())
        return super().__getitem__(y)

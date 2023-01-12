class Names:
    def __init__(self, names):
        self.names = names

    def add_name(self, names):
        return(names.append(self))

    def remove_name(self, names):
        return(names.remove(names[0]))

    def peek(self, names):
        return(names[0])

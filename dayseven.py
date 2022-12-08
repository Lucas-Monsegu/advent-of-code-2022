class Node:
    def __init__(self, childrens=None,parent=None, size=0):
        self.parent = parent
        self.childrens = childrens if childrens else []
        self.size = size
        
    def __str__(self, level=0):
        ret = "\t"*level+repr(self)+"\n"
        for child in self.childrens:
            ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return f'(size: {self.size} isDir: {len(self.childrens) != 0})'


class Computer:

    def __init__(self):
        self.base = Node()
        self.currentNode = self.base
        self.lines_index = 0
        with open('input.txt', 'r') as f:
            self.lines = f.readlines()


    def cd(self, directory):
        if directory == '/':
            self.currentNode = self.base
        elif directory == '..':
            if self.currentNode.parent is not None:
                self.currentNode = self.currentNode.parent
        else:
            self.currentNode.childrens.append(Node(parent=self.currentNode))
            self.currentNode = self.currentNode.childrens[-1]

    def ls(self):
        self.lines_index += 1
        while self.lines[self.lines_index][0] not in '%$':
            words = self.lines[self.lines_index].split()
            if words[0] == 'dir':
                self.lines_index += 1
                continue
            if words[0].isnumeric():
                self.currentNode.childrens.append(Node(parent=self.currentNode,size=int(words[0])))
            self.lines_index += 1
            
    def compute(self):
        while self.lines[self.lines_index][0] != '%':
            line = self.lines[self.lines_index]
            if line[0] == '$':
                words = line.split()
                command = words[1]
                if command == 'ls':
                    self.ls()
                    continue
                elif command == 'cd':
                    self.cd(words[2])
            self.lines_index += 1
        return self

    
    def calculate_size_dirs(self):
        def rec_calculate(node: Node):
            if len(node.childrens) == 0:
                return node.size
            s = sum(rec_calculate(n) for n in node.childrens)
            node.size = s
            return s
            
        rec_calculate(self.base)
        return self

    def get_all_directories_larger_than(self, size: int):
        def rec_get(node:Node):
            if len(node.childrens) == 0:
                return []
            else:
                li = [node]
                for i in node.childrens:
                    li += rec_get(i)
                return list(filter(lambda x: x.size >= size, li))

        return rec_get(self.base)

c = Computer().compute()
c.calculate_size_dirs()
size_needed = abs(40000000 - c.base.size)
print(min(node.size for node in c.get_all_directories_larger_than(size_needed)))
from typing import Union
from aocd import get_data
from io import StringIO
from enum import Enum

raw_data = get_data(year=2022, day=7)
test_data = '$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 g\n62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n8033020 d.log\n5626152 d.ext\n7214296 k'
input = StringIO(raw_data)

class Type(Enum):
    dir = 0
    file = 1

class Entry:
    def __init__(self, name:str, parent:'Entry', type:Type, size:int=0) -> None:
        self.children = []
        self.name = name
        self.parent = parent
        self.type = type
        self.size = size
    
    def get_child(self, name: str) -> Union['Entry', None]:
        for child in self.children:
            if name == child.name:
                return child
        return None
    
    def get_size(self) -> int:
        if self.type == Type.file:
            return self.size
        else:
            total = 0
            for child in self.children:
                total = total + child.get_size()
            return total

    def add_child(self, name:str, type:Type, size:int=0):
        self.children.append(Entry(name, self, type, size))

def buildFileSystem(console_data) -> Entry:
    root = Entry('/', None, Type.dir)
    location: Entry = root

    def cd(dir: str) -> Union[Entry, None]:
        if dir == '/':
            return root
        elif dir == '..':
            return location.parent
        else:
            return location.get_child(dir)
    
    for line in console_data:
        line = line.replace('\n', '')
        parts = line.split(' ')
        if parts[0] == '$':
            if parts[1] == 'cd':
                location = cd(parts[2])
        elif parts[0] == 'dir':
            location.add_child(parts[1], Type.dir)
        else:
            location.add_child(parts[1], Type.file, int(parts[0]))
    return root

def part1():
    file_system = buildFileSystem(input)
    max_size = 100000
    total_size = 0
    dir_stack = [file_system]

    while len(dir_stack) > 0:
        dir = dir_stack.pop()
        for child in dir.children:
            if (child.type == Type.dir):
                dir_stack.append(child)

        size = dir.get_size()
        if size <= max_size:
            total_size = total_size + size
    
    print('max size = ', max_size)
    print('sum of all dirs with size less than max = ', total_size)

def part2():
    disk_size = 70000000
    space_needed = 30000000
    file_system = buildFileSystem(input)
    used_space = file_system.get_size()
    free_space = disk_size - used_space
    needed_space = space_needed - free_space

    smallest_big_enough = used_space
    dir_stack = []
    for child in file_system.children:
        if (child.type == Type.dir):
            dir_stack.append(child)
    
    while len(dir_stack) > 0:
        dir = dir_stack.pop()
        for child in dir.children:
            if (child.type == Type.dir):
                dir_stack.append(child)

        size = dir.get_size()
        if size > needed_space and size < smallest_big_enough:
            smallest_big_enough = size
    print('the the smallest dir to delete has a size of ', smallest_big_enough)
part2()

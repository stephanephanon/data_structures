# main file for playing around
from linked_lists import LinkedList, Node
from stack import ArrayStack, LinkedListStack

print("testing data structures")

# insert first
l = LinkedList()
l.insert_first('dog')
l.insert_first('cat')
l.insert_first('bird')
print(len(l))

# insert last
l = LinkedList()
l.insert_last('c')
l.insert_last('b')
l.insert_last('a')

# insert after last
l.insert_after('a', 'last')

# insert after first
l.insert_after('c', 'first')

# insert after middle
l.insert_after('b', 'middle')

# delete first
l.delete_first()
l.delete_first()
l.delete_first()
l.delete_first()
l.delete_first()
l.delete_first()

for i in l:
    print(i)
print(len(l))

l = LinkedList()
l.insert_last('q')
l.insert_last('r')
l.delete('q')
l.delete('r')
print(len(l))

print('test linked list stack')
s = LinkedListStack()
s.push('x')
s.push('y')
s.push('z')
print(s.size())
r = s.pop()
print(r)
print(s.size())
for i in s:
    print(i)
print('stephanie')
print(s.peek())
s.pop()
s.pop()
s.peek()

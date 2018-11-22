class Node(object):
        # Classes also need descriptions
        """
        A Node class for implementing the Linkedlist class
        """
        # Include: types in your header
        # Method descriptions
        # and examples in every method
        def __init__(self,d,n=None):
            self.data=d
            self.next_node=n
        # whitespace will make your code more readable
        
        def get_next(self):
            return self.next_node
        def set_next(self,n):
            self.next_node = n
        def __str__(self):
           return str(self.data) +"->"+ str(self.next_node)
        def get_data(self):
            return self.data
        def set_data(self, d):
            self.data = d
class linkedlist(object):
        # Think carefully about how we want to call the linkedlist class
        # and how it will created a linked list from a builtin list
        def __init__(self, r = None,):
            self.root = r
            self.size = 0
        def prepend(self, data):
            new_head = Node(data)
            new_head.next_node = self.root
            self.root = new_head
            # did you test this? you don't modify self anywhere...
        def append(self, d):
            new_node=Node (d, self.root)
            self.root = new_node
            self.size += 1
            # this is what prepend should look like
        def __setitem__(self, key, item):
            if key == 0 or not self.root:
                self.prepend(item)
            else:
                node_to_insert = Node(item)
                iter_node = self.root
                pos = key
                while pos>0 and iter_node.next_node:
                    iter_node = iter_node.next_node
                    pos-=1
                node_to_insert.next_node = iter_node.next_node
                iter_node.next_node = node_to_insert # very good
        def __getitem__(self, key):
            if not self.root:
                return None
            else:
                iter_node = self.root
                pos = key
                while pos>0 and iter_node.next_node:
                    iter_node = iter_node.next_node
                    pos-=1
                return iter_node.data
        def __len__(self):
            return self.size # nice!
        def __str__(self):
            return str(self.root)
        def __delitem__(self,n):
            current = self.root
            prev = None
            while current:
                if current.get_data() == n:
                    if prev:
                        prev.set_next(current.get_next())
                    else:
                        self.root = current
                    self.size -= 1
                    return True
                else:
                    prev = current
                    current = current.get_next() # good
        def __iter__(self):
            current = self.root
            while current is not None:
                yield current.data
                current = current.next_node
        def reverse(self):
            if self.root:
                prev = None
                current = self.root
                while current:
                    future = current.next_node
                    current.next_node = prev
                    prev = current
                    current = future
                self.root = prev

    # Thank you for including your sources
    # I noticed that some of your code is a bit too similar to that of your sources' though
    # I encourage you to avoid coding immediately after consulting sources
    
    #sources:
    #https://codereview.stackexchange.com/questions/156906/python-linked-list-implementation
    #https://stackoverflow.com/questions/32617867/how-would-a-linked-list-be-faster-in-iteration-with-iter-and-next-or-wi
    #http://code.activestate.com/recipes/577355-python-27-linked-list-vs-list
    #https://stackoverflow.com/questions/20356401/setitem-and-getitem-python
    #https://github.com/wlbrough/python-algorithms/blob/master/ch4/linkedList.py
    
def selection(x):
        # this should be a method in the linkedlist class
        for i in range(len(x)):
            for j in range(i,len(x)):
                if(x[i] > x[j]):
                    x[i], x[j] = x[j], x[i]
        return x


# Many of your methods do not work
# Take a look at lltest.py to see how they should be used
# and take a minute to think about what the result of each method call should be

## Mark: correctness 25/50
## Mark: code style  28/50

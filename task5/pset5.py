
#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)
    def insert(self, val):
        newnode = Node(val)
        if self.root is None:
            self.root = newnode
            return
        
        cur = self.root
        while cur:
            if val < cur.info:
                if cur.left is None:
                    cur.left = newnode
                    return
                cur = cur.left
                
            else:
                if cur.right is None:
                    cur.right = newnode
                    return
                cur = cur.right  

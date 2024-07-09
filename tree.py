class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level
    
    def print_tree(self):
        spaces = ' ' * self.get_level() * 4
        prefix = spaces + '|---' if self.parent else ""
        print (prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
        

def build_product_tree():
    root = TreeNode("Electronics")
    
    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))
    
    phone = TreeNode("Phone")
    phone.add_child(TreeNode("Samsung Galaxy"))
    phone.add_child(TreeNode("Apple iPhone"))
    phone.add_child(TreeNode("Google Pixel"))
    
    tv = TreeNode("TVs")
    tv.add_child(TreeNode("Sony Bravia"))
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("TCL"))
    
    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(tv)
    
    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
        
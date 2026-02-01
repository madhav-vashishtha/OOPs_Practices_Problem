class StringRotation:
    def __init__(self, s, goal):
        self.s = s
        self.goal = goal
    
    def is_rotation(self):
        if len(self.s) != len(self.goal):
            return False
        

        return self.goal in (self.s + self.s)
    
obj = StringRotation("abcde", "cdeab")
print(obj.is_rotation())  

obj = StringRotation("abcde", "abced")
print(obj.is_rotation()) 
# Functional Prompt

def flat_sort(array):
    result = list()
    for i in array:
        if type(i) == list:
            for x in i:
                result.append(x)
        else:
            result.append(i)
    return sorted(result)

print(flat_sort([4,9, [2,3], [5, 6,  0 ,1]]))

# 
# How does this solution ensure data immutability? It does not change the origional it returns a new list
# Is this solution a pure function? Why or why not? Yes, it only depends on the input no outside scope 
# Is this solution a higher order function? Why or why not? No, it does not accept or return a higher order function.
# Would it have been easier to solve this problem using a different programming style? This is a simple solution to this problem so this is the esaiest way in my opinion. 



# Object Oriented Prompt

class Podracer:
    def __init__(self, max_speed, condition, price): 
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    
    def repair(self):
        self.condition = "Repaired"
        print(f"Successfully repaired!")

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def boost(self):
        self.max_speed *= 2
        print("Speed boost active!")

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def flame_jet(self, podracer):
        podracer.condition = "Trashed"
        print("Critical hit!")

pod = Podracer(1, "Trashed", 10)
pod.repair()
print(pod.condition)

new_pod = AnakinsPod(2, "Perfect", 50)
new_pod.boost()
print(new_pod.max_speed)
print(new_pod.condition)

third_pod = SebulbasPod(5, "Perfect", 100)
third_pod.flame_jet(new_pod)
print(new_pod.condition)

# 
# - How does this solution demonstrate the four pillars of OOP? 
#     - Encapsulation
#     - Abstraction
#     - Inheritance
#     - Polymorphism
# This solution encapsulates information within different classes (Podracer, AnakinsPod & SebulbasPod), and it also uses inheritance when creating both subclasses which derive from the main Podracer superclass.
# - Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# I personally think this coding style is suited perfectly for this problem because of all of the benefits that we get from using OOP programming, such as the potential use of the four pillars ans the use of classes in general.
# - How in particular did Object Oriented Programming assist in the solving of this problem?
# Being able to create a superclass along with other derivative subclasses, as well as simply being able to use the methods defined in those classes as intended to change the state of a specific object assisted in solving this problem an incredible amount.
# 
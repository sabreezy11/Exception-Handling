class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weeeeee this is fun!")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8) # 1.8 is the ratio parameter

    def walk(self):
        print("waddle, waddle, waddle")

    def swim(self):
        print("Come on it, the water's lovely!")

    def quack(self):
        print("Quack Quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def __init__(self):
        self.fly = self.aviate  # fly is a data attribute

    def walk(self):
        print("waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin a laugh? I'm a penguin")

    def aviate(self):
        print("I won the lottery and bought a learjet")
        # prints when a penguin is detected in migration.py


class Mallard(Duck):
    pass


class Flock(object):

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None: # we have now added a hint to this method
        # parameters are annotated using a colon, followed by the type of parameter,
        # and the return value you use a dash and greater than sign and the type of parameter.
        fly_method = getattr(duck, 'fly', None)
        #if isinstance(duck, Duck):
        if callable(fly_method):
            self.flock.append(duck) # adds duck parameter value to initial null flock set
        else:
            raise TypeError("Cannot add duck, are you sure it's not a " + str(type(duck).__name__))

    def migrate(self): # causes every duck in the flock to fly by calling their fly method
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                raise AttributeError("Testing exception handling in migrate") # TODO remove before release as this is for testing ONLY
            except AttributeError as e:  # a reference to the exception is stored in a variable for us to do something with
                print("one duck down")
                problem = e  # we can use this instead since we have now stored the problem as a variable
                #raise # raises an exception
        if problem:
            raise problem


# def test_duck(Duck):
#     Duck.walk()
#     Duck.swim()
#     Duck.quack()


# Testing Duck class #
if __name__ == '__main__':
    donald = Duck()
    donald.fly()

    # test_duck(donald)
    #
    # percy = Penguin()
    # # percy has the methods that the test_duck function relies on
    # test_duck(percy)
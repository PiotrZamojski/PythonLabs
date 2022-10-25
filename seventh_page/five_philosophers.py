class Fork:
    def __init__(self,name,state):
        self.name = name
        self.state = state

    def take(self):
        if self.state == False:
            print("already in use")
            return 1
        else:
            self.state = False
            return 0


    def returnFork(self):
        self.state = True

    def __str__(self):
        return str(self.state)

forks = [Fork("1",True), Fork("2",True), Fork("3",True), Fork("4",True), Fork("5",True)]

class Philosopher:
    def __init__(self, name, forkOnLeft, forkOnRight):
        self.name = name
        self.forkOnLeft = forkOnLeft-1
        self.forkOnRight = forkOnRight-1
        self.state = "think"
        self.counter = 0
        self.forks = []

    def eat(self,count):
        self.state = "eat"
        self.counter = count
        result1 = forks[self.forkOnLeft].take()
        result2 = forks[self.forkOnRight].take()
        if result1 == 1 and result2 == 0:
            self.state = "want eat"
            self.counter = 0
            forks[self.forkOnRight].returnFork()
        elif result2 == 1 and result1 == 0:
            self.state = "want eat"
            self.counter = 0
            forks[self.forkOnLeft].returnFork()
        elif result2 == 1 and result1 == 1:
            self.state = "want eat"
            self.counter = 0

    def giveFork(self, index):
        self.forks.append(index)
        if self.forks.count(self.forkOnLeft) and self.forks.count(self.forkOnRight):
            self.eat(index)

    def checkState(self):
        if self.state == "eat":
            print(self.name+" is eating...")
            self.counter -= 1
            if self.counter == 0:
                forks[self.forkOnLeft].returnFork()
                forks[self.forkOnRight].returnFork()
                self.state = "think"

        if self.state == "think":
            print(self.name + " is thinking...")
        elif self.state == "want eat":
            print(self.name + " wants to eat something...")


def main():

    philosophers = [Philosopher("A",1,5), Philosopher("B",1,2), Philosopher("C",2,3), Philosopher("D",3,4), Philosopher("E",4,5)]
    queue = []

    philosophers[0].eat(4)
    philosophers[1].eat(4)
    philosophers[2].eat(5)
    philosophers[1].state = "want eat"
    philosophers[3].state = "want eat"

    print("forks: ")
    for fork in forks:
        print(fork)

    for i in range(0,10):

        for p in philosophers:
            p.checkState()
            state = p.state
            print(state)
            if state == "want eat":
                queue.append(p)

        print()

        counter = 0
        print("forks: ")
        for fork in forks:
            print(fork)
        for p in queue:
            if forks[p.forkOnLeft].state:
                forks[p.forkOnLeft].take()
                p.giveFork(p.forkOnLeft)

            if forks[p.forkOnRight].state:
                forks[p.forkOnRight].take()
                p.giveFork(p.forkOnRight)

            if p.state == "eat":
                queue.pop(counter)
                counter -= 1
            counter += 1



if __name__ == '__main__':
    main()
import time
from hotpotServerforcat import hotpots
NUM=3000
class TestResult:
    def __init__(self, test):
        self.test = test

if __name__ == "__main__":
    MygetHot=hotpots(1)
    MygetHot.hotpotIter(NUM)
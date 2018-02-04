import time
from hotpotServer2w import hotpots
NUM=20000
class TestResult:
    def __init__(self, test):
        self.test = test

if __name__ == "__main__":
    MygetHot=hotpots(1)
    MygetHot.hotpotIter(NUM)
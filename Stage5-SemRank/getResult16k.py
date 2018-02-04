import time
from hotpotServer16k import hotpots
NUM=16000
class TestResult:
    def __init__(self, test):
        self.test = test

if __name__ == "__main__":
    MygetHot=hotpots(1)
    MygetHot.hotpotIter(NUM)
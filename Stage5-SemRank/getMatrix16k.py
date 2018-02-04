import time
import os.path
from hotpotServer16k import hotpots

__PATH2__ = '../pickpics16k'
__PATH3__='../SemRank/16k'
L=48
NUM=16000
class TestMatrix:
    def __init__(self, test):
        self.test = test

if __name__ == "__main__":
    MygetHot=hotpots(1)
    starttime=time.time()
    funcNij=MygetHot.getFuncNij(NUM)
    getMatrixtime=time.time()-starttime
    print getMatrixtime
    f = file(os.path.join(__PATH3__, 'getMatrix'+str(NUM)+'.txt'), "a+")
    f.write(str(getMatrixtime)+'\n')
    f.close()
import time
import os.path
from hotpotServer2w import hotpots

__PATH2__ = '../tencentgraphfile'
__PATH3__='../SemRank/tencent/2w'
L=48
NUM=20000
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
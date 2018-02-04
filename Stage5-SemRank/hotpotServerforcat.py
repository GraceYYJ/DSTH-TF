# coding: utf-8
from __future__ import division
from numpy import *
import numpy as np
import h5py
import datetime
import os.path
import time

__PATH2__ = '../pickpics16k'
__PATH3__='../SemRank/cat/3000'
L=48
acc1=0.00000000001
acc2=11
NUM=3000
num="cat2100"
div=2
class hotpots:
    def __init__(self, test):
        self.test = test

    def getLminusdij(self,objectNum):
        Lminusdij = mat(zeros((1, objectNum)))
        sum=0
        relationfile = h5py.File(os.path.join(__PATH2__, 'hammingrelation'+num+'_'+str(div)+'.hy'), 'r')
        relations=relationfile["hammingrelation"+num+"_"+str(div)].value
        for i in range(0,objectNum):
            for j in range(0,objectNum):            
                if i!=j and relations[i][j]!=-1:
                    print relations[i][j]
                    sum=sum+L-relations[i][j]
            Lminusdij[0, i] = sum
            sum=0
        relationfile.close()
        print Lminusdij
        return Lminusdij

    def getFuncNij(self,objectNum):
        Lminusdij=self.getLminusdij(objectNum)
        funcNij = mat(zeros((objectNum, objectNum)))
        relationfile = h5py.File(os.path.join(__PATH2__, 'hammingrelation'+num+'_'+str(div)+'.hy'), 'r')
        relations=relationfile["hammingrelation"+num+"_"+str(div)].value
        print relations
        for i in range(0,objectNum):
            for j in range(0,objectNum):
                if i!=j and relations[i][j]!=-1:
                    funcNij[i,j] = (L - relations[i][j]) / Lminusdij[0, j]
                    print funcNij[i,j] ,L,relations[i][j],Lminusdij[0, j]
                else:
                    funcNij[i,j] = 0
        print("------------firstfuncNij----------")
        print funcNij
        for i in range(0,objectNum):
            for j in range(0,objectNum):
                funcNij[i,j]=0.85*funcNij[i,j]+0.15/objectNum
        print funcNij
        funcNijfile=h5py.File(os.path.join(__PATH3__,'funcNij'+num+'.hy'),'w')
        funcNijfile.create_dataset("funcNij"+num,data=funcNij)
        funcNijfile.close()
        relationfile.close()
        return funcNij

    def hotpotIter(self,objectNum):
        funcNijfile = h5py.File(os.path.join(__PATH3__, 'funcNij'+num+'.hy'), 'r')
        funcNij=funcNijfile["funcNij"+num].value
        print funcNij
        starttime=time.time()
        print("------------firstR----------")
        R = mat(ones((objectNum, 1)))
        print R
        i=0
        Result=np.dot(funcNij,R)
        print("------------firstResult----------")
        print Result
        while not self.Equals(Result,R):
            R=Result
            Result=np.dot(funcNij,R)
            i=i+1
            print("---------------------------")
            print i
            print("Result")
            print Result
            print("R")
            print R
        print("===============final result==============")
        endtime=time.time()
        usetime=endtime-starttime
        print i,usetime
        f=file(os.path.join(__PATH3__,'itertime'+num+str(acc2)+".txt"),"a+")
        f.write("迭代次数" + str(i) + '\n' + "耗时：" + str(usetime))
        f.close()
        print("R")
        print R
        print("Result")
        print Result
        Resultfile=h5py.File(os.path.join(__PATH3__,'Result'+num+'_'+str(acc2)+'.hy'),'w')
        Resultfile.create_dataset("Result",data=Result)
        Resultfile.close()
        return Result
    
    def Equals(self,vector1,verctor2):
        result=vector1-verctor2
        flag=True
        for i in range(0,result.shape[0]):
            if not(-acc1<result[i,0]<acc1):
                flag=False
        return flag
# coding: utf-8
import csv
import time
import h5py
import os.path
import numpy as np
#from neo4j.v1 import GraphDatabase, basic_auth
__PATH__ = '../datasets/cifar10'
def hammingDist(hashstr1, hashstr2):
    """Calculate the Hamming distance between two bit strings"""
    assert len(hashstr1) == len(hashstr2)
    return sum(c1 != c2 for c1, c2 in zip(hashstr1, hashstr2))

if __name__ == "__main__":

#Neo4j Operations
#neo4j_uri = "bolt://127.0.0.1:7687"
#driver = GraphDatabase.driver(neo4j_uri, auth=basic_auth("neo4j", "123456"))
    hashstrfile = h5py.File(os.path.join(__PATH__, 'predicthashstr.hy'), 'r')
    csvfile_node = open('node_test.csv', 'ab+')
    csvfile_relation = open('relation_test.csv', 'ab+')

    hashcode=hashstrfile["predicthashstr"].value
    print hashcode[0],hashcode.shape
    node_writer = csv.writer(csvfile_node)
    node_writer.writerow(['objectName:ID','hashcode:string',':LABEL'])

    relation_writer = csv.writer(csvfile_relation)
    relation_writer.writerow([':START_ID','distance:int',':END_ID',':TYPE'])
    node_type = 'INodeObject'
    rel_type = 'Similarity'

#insert_data = []
#while r.llen(queueName) > 0:
    hashcode=hashcode[0:10]
    print len(hashcode)
    rel_insert_data = []
    count=0
    for i in range(len(hashcode)):
        print i
        node_writer.writerow([str(i), hashcode[i], node_type])
        for j in range(i+1,len(hashcode)):
            print j
            dist = hammingDist(hashcode[i], hashcode[j])
            if dist < 24:
                print i,j
                rel_insert_data.append((i, dist, j, rel_type))
                count=count+1
    relation_writer.writerows(rel_insert_data)

    csvfile_node.close()
    csvfile_relation.close()




#     while True:
#         #res = r.lpop(queueName)
#         res = r.blpop(queueName, timeout=0)
#         res_str=str(res)
#         '''
#         print 'res = ', res
#         print 'res_str = ', res_str
#         '''
#         objectName = res_str.split('&')[0]
#         if objectName != lastObjName:
#             deepHash = res_str.split('&')[1]
#             #insert_data.append((objectName,deepHash,node_type))
#             node_reader = csv.reader(csvfile_node)
#             flag = 0
#             rel_insert_data = []
#             for line in node_reader:
#                 print line
#                 if flag == 0:
#                     flag = 1
#                 else:#line[0] = objectName ; line[1] = deephash
#                     dist = hammingDist(line[1], deepHash)
#                     if dist < 24:
#                         rel_insert_data.append((objectName,dist,line[0],rel_type))
#
#             relation_writer.writerows(rel_insert_data)
#             node_writer.writerow([objectName,deepHash,node_type])
#             lastObjName = objectName
#
# #node_writer.writerows(insert_data)
#     csvfile_node.close()
#     csvfile_relation.close()


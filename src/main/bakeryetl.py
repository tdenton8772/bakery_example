# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "tdenton"
__date__ = "$Apr 18, 2019 4:06:24 PM$"

import csv
import json

import grpc

import grpc_config_pb2
import grpc_config_pb2_grpc
import grpc_query_pb2
import grpc_query_pb2_grpc
import database_pb2

from google.protobuf.any_pb2 import Any

def process_file(file_name):
#    with grpc.insecure_channel('localhost:8081') as channel:
#        stub = grpc_config_pb2_grpc.DatabaseServiceStub(channel)
#        response = stub.Connect(grpc_config_pb2.InitiateConnection(clusterUser="Administrator",
#                                                                    clusterPW="Hello",
#                                                                    version="4.5.1",
#                                                                    clusterAddress= ["127.0.0.1"],
#                                                                    kvTimeout= 9000,
#                                                                    queryTimeout= 9000,
#                                                                    DBMainPassword= "main",
#                                                                    DBTxnPassword= "txn",
#                                                                    DBHxnPassword= "hxn",
#                                                                    DBMain= "main",
#                                                                    DBTxn= "txv",
#                                                                    DBHxn= "hxn"))
#        print(response)
    
    with grpc.insecure_channel('localhost:8081') as channel:
        stub = grpc_config_pb2_grpc.DatabaseServiceStub(channel)
        response = stub.Connect(grpc_config_pb2.InitiateConnection(clusterUser="Administrator",
                                                                    clusterPW="76;AkB_d",
                                                                    version="6.0.1",
                                                                    clusterAddress= ["cbdata-101.dev.archerdx.com"],
                                                                    kvTimeout= 9000,
                                                                    queryTimeout= 9000,
                                                                    DBMain= "erp",
                                                                    DBTxn= "txn",
                                                                    DBHxn= "history"))
        print(response)
        
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = grpc_query_pb2_grpc.QueryServiceStub(channel)
        with open(file_name) as csvfile:
            freader = csv.DictReader(csvfile, delimiter=",", quotechar="|")
            for row in freader:
                docID = "{}_{}_{}".format(row['Transaction'], row['Date'], row['Time'])
                message = row
                _Item = message['Item']
                message['Item'] = []
                message['Item'].append(_Item)
                message['jsonType'] = "transaction"
                response = stub.kvUpsert(grpc_query_pb2.JsonID(docID = docID,
                                                            document = json.dumps(message)))
                print(response)
            
            
            message = grpc_query_pb2.AnyID(docID = "1234")
            anyMessage = Any()
            anyMessage.Pack(database_pb2.TxnLog(doc_id = "1234"))
            message.details.extend([anyMessage])
            stub.anyService(message)
#                                                    details = [database_pb2.TxnLog(doc_id = "1234")].))
#    with open(file_name) as csvfile:
#        freader = csv.DictReader(csvfile, delimiter=",", quotechar="|")        
#        for row in freader:
#            docID = "{}_{}".format(row['Date'], row['Time'])
#            message = row
#            _Item = message['Item']
#            message['Item'] = []
#            message['Item'].append(_Item)
#            message['jsonType'] = "transaction"
#            print(json.dumps(message))

if __name__ == "__main__":
    process_file("../resources/BreadBasket_DMS.csv")
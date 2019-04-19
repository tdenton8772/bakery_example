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

def process_file(file_name):
    with grpc.insecure_channel('localhost:8081') as channel:
        stub = grpc_config_pb2_grpc.DatabaseServiceStub(channel)
        response = stub.Connect(grpc_config_pb2.InitiateConnection(clusterUser="Administrator",
                                                                    clusterPW="Hello",
                                                                    version="4.5.1",
                                                                    clusterAddress= ["127.0.0.1"],
                                                                    kvTimeout= 9000,
                                                                    queryTimeout= 9000,
                                                                    DBMainPassword= "main",
                                                                    DBTxnPassword= "txn",
                                                                    DBHxnPassword= "hxn",
                                                                    DBMain= "main",
                                                                    DBTxn= "txv",
                                                                    DBHxn= "hxn"))
        print(response)
        
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = grpc_query_pb2_grpc.QueryServiceStub(channel)
        with open(file_name) as csvfile:
            freader = csv.DictReader(csvfile, delimiter=",", quotechar="|")
            for row in freader:
                docID = "{}_{}".format(row['Date'], row['Time'])
                message = row
                _Item = message['Item']
                message['Item'] = []
                message['Item'].append(_Item)
                message['jsonType'] = "transaction"
                response = stub.kvUpsert(grpc_query_pb2.JsonID(docID = docID,
                                                            document = json.dumps(message)))
                print(response)
            


if __name__ == "__main__":
    process_file("/home/tdenton/Desktop/Development/BreadBasket_DMS.csv")
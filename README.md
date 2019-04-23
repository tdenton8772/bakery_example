# bakery_example


Must have protoc installed </br>
This is dependant on the https://github.com/tdenton8772/cb_grpc for its protofiles. 

```
cd /opt/

git clone https://github.com/tdenton8772/bakery_example.git

protoc -I=/usr/local/include/ -I=/opt/cb_grpc/src/main/proto/api/ --python_out=/opt/bakery_example/src/main/ /opt/cb_grpc/src/main/proto/api/gRPC/*.proto

protoc -I=/usr/local/include/ -I=/opt/cb_grpc/src/main/proto/api/ --python_out=/opt/bakery_example/src/main/ /opt/cb_grpc/src/main/proto/api/database/*.proto`

python /opt/bakery_example/src/main/bakeryetl.py 
```
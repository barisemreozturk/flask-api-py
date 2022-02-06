*Girilen şehrin hava durumunu gösteren Web API.

*Dockerize etmek için;

docker build -t *tag name .

docker run -d -p 5000:5000 tag name

*Uygulamaya istek yollamak;

curl localhost:5000

curl localhost:5000/temperature?city=*şehiradı

![Screenshot from 2022-02-06 15-50-46](https://user-images.githubusercontent.com/91996015/152681700-eed35e83-5d17-4f08-9038-aaef8bc01696.png)

*Main branchine yeni bir commit geldiğinde workflow registry'e yeni bir docker image'i yollar
 

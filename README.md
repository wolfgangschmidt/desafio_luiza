# desafio_luiza
desafio_luiza

** setting up project **

	```pip install -r requirements.txt```
  
**interaction wiht api**

  - listing all resources
  ```curl -H "Content-Type: application/json" http://127.0.0.1:8000/api/cadastro/```
  
  - retrieving a single resource
  
  ```curl -H "Content-Type: application/json" http://127.0.0.1:8000/api/cadastro/<id_number>```
  
  - posting a new resource
  
  ```curl -d '{"name":"wolfgang", "email":"wolfgang@wolf.com", "dept":"dev"}' 
-H "Content-Type: application/json" -X POST http://127.0.0.1:8000/api/cadastro/```

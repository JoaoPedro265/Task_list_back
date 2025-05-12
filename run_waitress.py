# Esse código coloca sua aplicação Django no ar com um servidor de verdade,
# mais seguro e estável que o runserver, ideal para deploy em produção.(obs usado para testes antes do Deploy)
from waitress import serve
from Task_list.wsgi import application

serve(application, host="0.0.0.0", port=8000)

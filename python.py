import requests

url = 'http://inspect.mht-jcv.com/html/Empleado/Polizas/prueba.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, data = myobj)

print(x.text)
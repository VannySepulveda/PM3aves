import requests
import json
from string import Template

html = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    $body
</body>
</html>
""")

elem_template= Template("""<h2>$aveES</h2>
                           <h2>$aveIN</h2>
                           <img src="$imagen">
                        """)
aves={}
url = 'https://aves.ninjas.cl/api/birds'

def build_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        j=response.json()
        ave={}
        arch=''
        for x in range (0, len(j), 1):
            res=j[x]
            ave['nameEs']=res['name']['spanish']
            ave['nameIn']=res['name']['english']
            ave['imagen']=res['images']['thumb']    
            arch+=elem_template.substitute(aveES=ave['nameEs'],aveIN=ave['nameIn'],imagen=ave['imagen'])
            print (ave['nameEs'],ave['nameIn'],ave['imagen'])
    else:
        print(f"Error al acceder a la API. Código de estado: {response.status_code}")

    return html.substitute(body=arch)    
# for keys in aves:
#     print (f"Español: {aves[keys]['spanish']}\nIngles : {aves[keys]['english']} \nImagen : {aves[keys]['imagen']}\n")   

html=build_html('https://aves.ninjas.cl/api/birds')  
with open('aves.html', 'w') as f:
        f.write(html)
      
                    
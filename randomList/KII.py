import json
import random

def obtener_atributo(json_string):
    # Cargar los datos desde la cadena JSON
    data = json.loads(json_string)
    
    # Obtener las claves (atributos) del objeto
    atributos = list(data.keys())

    # Elegir aleatoriamente un atributo del objeto
    atributo = random.choice(atributos)

    return atributo

# Ejemplo de uso:
json_string = '{"id":"123ABC","prefix":"","firstName":"STANFORD","middleName":"","lastName":"SMITH","suffix":"MD","nameAlias1":"SMITH,STANFORD","nameAlias2":"S,F,SMOTH","nameAlias3":"","dob":"1965-01-09","ssn":"343679845","addres1Line1":"123 MAIN ST","addres1Line2":"","addres1City":"MOSCOW","addres1State":"ID","addres1Zip":"83844","address1Zip4":"","addres2Line1":"456 ELM RD","addres2Line2":"","addres2City":"MOSCOW","addres2State":"ID","addres2Zip":"83844","address2Zip4":"","phone1AreaCode":"208","phone1BaseNumber":"3450998","phone2AreaCode":"208","phone2BaseNumber":"4569845","gender":"M","similarityScore":"1.0","caseType":"SEED"}'
atributo_seleccionado = obtener_atributo(json_string)
print("Atributo seleccionado:", atributo_seleccionado)



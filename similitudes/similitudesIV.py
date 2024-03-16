import json
import Levenshtein

# Semilla
semilla_json = '{"id":"123ABC","prefix":"","firstName":"STANFORD","middleName":"","lastName":"SMITH","suffix":"MD","nameAlias1":"SMITH,STANFORD","nameAlias2":"S,F,SMOTH","nameAlias3":"","dob":"1965-01-09","ssn":"343679845","addres1Line1":"123 MAIN ST","addres1Line2":"","addres1City":"MOSCOW","addres1State":"ID","addres1Zip":"83844","address1Zip4":"","addres2Line1":"456 ELM RD","addres2Line2":"","addres2City":"MOSCOW","addres2State":"ID","addres2Zip":"83844","address2Zip4":"","phone1AreaCode":"208","phone1BaseNumber":"3450998","phone2AreaCode":"208","phone2BaseNumber":"4569845","gender":"M","similarityScore":"1.0","caseType":"SEED"}'
semilla = json.loads(semilla_json)

# Arcos
arcos_json = [
'{"id":"123ABC","prefix":"","firstName":"STANFORDD","middleName":"","lastName":"SMITH","suffix":"MD","nameAlias1":"SMITH,STANFORD","nameAlias2":"S,F,SMOTH","nameAlias3":"","dob":"1965-01-09","ssn":"343679845","addres1Line1":"123 MAIN ST","addres1Line2":"","addres1City":"MOSCOW","addres1State":"ID","addres1Zip":"83844","address1Zip4":"","addres2Line1":"456 ELM RD","addres2Line2":"","addres2City":"MOSCOW","addres2State":"ID","addres2Zip":"83844","address2Zip4":"","phone1AreaCode":"208","phone1BaseNumber":"3450998","phone2AreaCode":"208","phone2BaseNumber":"4569845","gender":"M","similarityScore":"1.0","caseType":"SEED"}',
'{"id":"123ABC","prefix":"","firstName":"STANFOR","middleName":"","lastName":"SMITH","suffix":"MD","nameAlias1":"SMITH,STANFORD","nameAlias2":"S,F,SMOTH","nameAlias3":"","dob":"1965-01-09","ssn":"343679845","addres1Line1":"123 MAIN ST","addres1Line2":"","addres1City":"MOSCOW","addres1State":"ID","addres1Zip":"83844","address1Zip4":"","addres2Line1":"456 ELM RD","addres2Line2":"","addres2City":"MOSCOW","addres2State":"ID","addres2Zip":"83844","address2Zip4":"","phone1AreaCode":"208","phone1BaseNumber":"3450998","phone2AreaCode":"208","phone2BaseNumber":"4569845","gender":"M","similarityScore":"1.0","caseType":"SEED"}',
'{"id":"456XYZ","prefix":"Dr.","firstName":"John","middleName":"Doe","lastName":"SMYTH","suffix":"PhD","nameAlias1":"SMYTH,JOHN","nameAlias2":"J,D,SMOTH","nameAlias3":"JD","dob":"1980-05-15","ssn":"123456789","addres1Line1":"789 Oak Street","addres1Line2":"Apt 2B","addres1City":"New York","addres1State":"NY","addres1Zip":"10001","address1Zip4":"5678","addres2Line1":"456 Pine Avenue","addres2Line2":"","addres2City":"Los Angeles","addres2State":"CA","addres2Zip":"90001","address2Zip4":"1234","phone1AreaCode":"310","phone1BaseNumber":"9876543","phone2AreaCode":"213","phone2BaseNumber":"1234567","gender":"M","similarityScore":"0.8","caseType":"TEST"}',
'{"id":"789XYZ","prefix":"","firstName":"MICHAEL","middleName":"JAMES","lastName":"SMITH","suffix":"PhD","nameAlias1":"SMITH,MICHAEL","nameAlias2":"M,J,SMOTH","nameAlias3":"","dob":"1978-03-21","ssn":"987654321","addres1Line1":"456 Oak Avenue","addres1Line2":"","addres1City":"Los Angeles","addres1State":"CA","addres1Zip":"90001","address1Zip4":"4321","addres2Line1":"789 Elm Street","addres2Line2":"","addres2City":"New York","addres2State":"NY","addres2Zip":"10001","address2Zip4":"5678","phone1AreaCode":"310","phone1BaseNumber":"1234567","phone2AreaCode":"213","phone2BaseNumber":"9876543","gender":"M","similarityScore":"0.9","caseType":"TEST"}'
]

arcos = [json.loads(arco_json) for arco_json in arcos_json]

# Calcular y mostrar las similitudes normalizadas
for i, arco in enumerate(arcos):
    distancia = Levenshtein.distance(semilla["firstName"].lower(), arco["firstName"].lower())
    longitud_maxima = max(len(semilla["firstName"]), len(arco["firstName"]))
    similitud_normalizada = (longitud_maxima - distancia) / longitud_maxima
    print(f"Similitud normalizada entre semilla y arco{i}: {similitud_normalizada}")

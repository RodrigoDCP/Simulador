import Levenshtein

# Semilla
semilla = {
    "id": "123ABC",
    "prefix": "",
    "firstName": "STANFORD",
    "middleName": "",
    "lastName": "SMITH",
    "suffix": "MD",
    "nameAlias1": "SMITH,STANFORD",
    "nameAlias2": "S,F,SMOTH",
    "nameAlias3": "",
    "dob": "1965-01-09",
    "ssn": "343679845",
    "addres1Line1": "123 MAIN ST",
    "addres1Line2": "",
    "addres1City": "MOSCOW",
    "addres1State": "ID",
    "addres1Zip": "83844",
    "address1Zip4": "",
    "addres2Line1": "456 ELM RD",
    "addres2Line2": "",
    "addres2City": "MOSCOW",
    "addres2State": "ID",
    "addres2Zip": "83844",
    "address2Zip4": "",
    "phone1AreaCode": "208",
    "phone1BaseNumber": "3450998",
    "phone2AreaCode": "208",
    "phone2BaseNumber": "4569845",
    "gender": "M",
    "similarityScore": "1.0",
    "caseType": "SEED"
}

# Arcos

arcos = [
{"id": "123ABC", "prefix": "", "firstName": "STANFORD", "middleName": "", "lastName": "SMITH", "suffix": "MD", "nameAlias1": "SMITH,STANFORD", "nameAlias2": "S,F,SMOTH", "nameAlias3": "", "dob": "1965-01-09", "ssn": "343679845", "addres1Line1": "123 MAIN ST", "addres1Line2": "", "addres1City": "MOSCOW", "addres1State": "ID", "addres1Zip": "83844", "address1Zip4": "", "addres2Line1": "456 ELM RD", "addres2Line2": "", "addres2City": "MOSCOW", "addres2State": "ID", "addres2Zip": "83844", "address2Zip4": "", "phone1AreaCode": "208", "phone1BaseNumber": "3450998", "phone2AreaCode": "208", "phone2BaseNumber": "4569845", "gender": "M", "similarityScore": "0.5", "caseType": "SEED"},


]

#mostrar las similitudes normalizadas para todos los campos de la semilla

for i, arco in enumerate(arcos):
    similitud_total = 0
    campos_comparados = 0
    for campo in semilla:
        if campo != "similarityScore":
            valor_semilla = str(semilla[campo]).lower()
            valor_arco = str(arco.get(campo, '')).lower()
            distancia = Levenshtein.distance(valor_semilla, valor_arco)
            longitud_maxima = max(len(valor_semilla), len(valor_arco))
            if longitud_maxima != 0:  # Verificar si la longitud máxima es cero para evitar la división por cero
                similitud_normalizada = (longitud_maxima - distancia) / longitud_maxima
                similitud_total += similitud_normalizada
                campos_comparados += 1
    if campos_comparados != 0:  # Verificar si se compararon campos para evitar la división por cero
        similitud_promedio = similitud_total / campos_comparados
        print(f"Similitud normalizada promedio entre semilla y arco{i}: {similitud_promedio}")
    else:
        print(f"No se pudo calcular la similitud promedio para arco{i}: No hay campos comparables")


'''
for i, arco in enumerate(arcos):
    similitud_total = 0
    campos_comparados = 0
    for campo in semilla:
        valor_semilla = str(semilla[campo]).lower()
        valor_arco = str(arco.get(campo, '')).lower()
        distancia = Levenshtein.distance(valor_semilla, valor_arco)
        longitud_maxima = max(len(valor_semilla), len(valor_arco))
        if longitud_maxima != 0:  # Verificar si la longitud máxima es cero para evitar la división por cero
            similitud_normalizada = (longitud_maxima - distancia) / longitud_maxima
            similitud_total += similitud_normalizada
            campos_comparados += 1
    if campos_comparados != 0:  # Verificar si se compararon campos para evitar la división por cero
        similitud_promedio = similitud_total / campos_comparados
        print(f"Similitud normalizada promedio entre semilla y arco{i}: {similitud_promedio}")
    else:
        print(f"No se pudo calcular la similitud promedio para arco{i}: No hay campos comparables")

'''


''' 
{"id": "123ABC", "prefix": "", "firstName": "STANFORD", "middleName": "", "lastName": "SMITH", "suffix": "MD", "nameAlias1": "SMITH,STANFORD", "nameAlias2": "S,F,SMOTH", "nameAlias3": "", "dob": "1965-01-09", "ssn": "987654321", "addres1Line1": "123 MAIN ST", "addres1Line2": "", "addres1City": "MOSCOW", "addres1State": "ID", "addres1Zip": "83844", "address1Zip4": "", "addres2Line1": "456 ELM RD", "addres2Line2": "", "addres2City": "MOSCOW", "addres2State": "ID", "addres2Zip": "83844", "address2Zip4": "", "phone1AreaCode": "208", "phone1BaseNumber": "3450998", "phone2AreaCode": "208", "phone2BaseNumber": "4569845", "gender": "M", "similarityScore": "0.5", "caseType": "SEED"},

{"id": "123ABC", "prefix": "", "firstName": "STANFORD", "middleName": "", "lastName": "SMITH", "suffix": "MD", "nameAlias1": "SMITH,STANFORD", "nameAlias2": "S,F,SMOTH", "nameAlias3": "", "dob": "1965-01-09", "ssn": "123456789", "addres1Line1": "123 MAIN ST", "addres1Line2": "", "addres1City": "MOSCOW", "addres1State": "ID", "addres1Zip": "83844", "address1Zip4": "", "addres2Line1": "456 ELM RD", "addres2Line2": "", "addres2City": "MOSCOW", "addres2State": "ID", "addres2Zip": "83844", "address2Zip4": "", "phone1AreaCode": "310", "phone1BaseNumber": "3450998", "phone2AreaCode": "208", "phone2BaseNumber": "4569845", "gender": "M", "similarityScore": "0.5", "caseType": "SEED"},

{"id": "123ABC", "prefix": "", "firstName": "STANFORD", "middleName": "", "lastName": "SMITH", "suffix": "MD", "nameAlias1": "SMITH,STANFORD", "nameAlias2": "S,F,SMOTH", "nameAlias3": "", "dob": "1965-01-09", "ssn": "987654321", "addres1Line1": "123 MAIN ST", "addres1Line2": "", "addres1City": "MOSCOW", "addres1State": "WA", "addres1Zip": "83844", "address1Zip4": "", "addres2Line1": "456 ELM RD", "addres2Line2": "", "addres2City": "MOSCOW", "addres2State": "ID", "addres2Zip": "83844", "address2Zip4": "", "phone1AreaCode": "310", "phone1BaseNumber": "6789012", "phone2AreaCode": "208", "phone2BaseNumber": "4569845", "gender": "M", "similarityScore": "0.5", "caseType": "SEED"},

{"id": "123ABC", "prefix": "", "firstName": "STANFORD", "middleName": "", "lastName": "SMITH", "suffix": "MD", "nameAlias1": "SMITH,STANFORD", "nameAlias2": "S,F,SMOTH", "nameAlias3": "", "dob": "1965-01-09", "ssn": "987654320", "addres1Line1": "123 MAIN ST", "addres1Line2": "", "addres1City": "MOSCOW", "addres1State": "WA", "addres1Zip": "83845", "address1Zip4": "", "addres2Line1": "456 ELM RD", "addres2Line2": "", "addres2City": "MOSCOW", "addres2State": "ID", "addres2Zip": "83844", "address2Zip4": "", "phone1AreaCode": "310", "phone1BaseNumber": "6789013", "phone2AreaCode": "208", "phone2BaseNumber": "4569845", "gender": "M", "similarityScore": "0.5", "caseType": "SEED"},

{"id": "123XYZ", "prefix": "Dr.", "firstName": "JOHN", "middleName": "ANDREW", "lastName": "DOE", "suffix": "PhD", "nameAlias1": "DOE, JOHN", "nameAlias2": "J,A,DOOH", "nameAlias3": "", "dob": "1970-05-15", "ssn": "123456789", "addres1Line1": "789 Maple Avenue", "addres1Line2": "Apt. 3B", "addres1City": "NEW YORK", "addres1State": "NY", "addres1Zip": "10001", "address1Zip4": "6789", "addres2Line1": "101 Oak Street", "addres2Line2": "Suite 200", "addres2City": "LOS ANGELES", "addres2State": "CA", "addres2Zip": "90001", "address2Zip4": "5432", "phone1AreaCode": "310", "phone1BaseNumber": "9876543", "phone2AreaCode": "213", "phone2BaseNumber": "1234567", "gender": "M", "similarityScore": "0.9", "caseType": "TEST"},

{"id": "123ABC", "prefix": "", "firstName": "STANFJRD", "middleName": "", "lastName": "SMITH", "suffix": "MD", "nameAlias1": "SMITH,STANFORD", "nameAlias2": "S,F,SMOTH", "nameAlias3": "", "dob": "1965-01-09", "ssn": "343679845", "addres1Line1": "123 MAIN ST", "addres1Line2": "", "addres1City": "MOSCOW", "addres1State": "ID", "addres1Zip": "83844", "address1Zip4": "", "addres2Line1": "456 ELM RD", "addres2Line2": "", "addres2City": "MOSCOW", "addres2State": "ID", "addres2Zip": "83844", "address2Zip4": "", "phone1AreaCode": "208", "phone1BaseNumber": "3450998", "phone2AreaCode": "208", "phone2BaseNumber": "4569845", "gender": "M", "similarityScore": "0.5", "caseType": "SEED"},

{"id": "123ABC", "prefix": "", "firstName": "STANFJRD", "middleName": "", "lastName": "SMITH", "suffix": "MD", "nameAlias1": "SMITH,STANFORD", "nameAlias2": "S,F,SMOTH", "nameAlias3": "", "dob": "1965-01-09", "ssn": "343679845", "addres1Line1": "123 MAIN ST", "addres1Line2": "", "addres1City": "MOSCOW", "addres1State": "ID", "addres1Zip": "83844", "address1Zip4": "", "addres2Line1": "456 ELM RD", "addres2Line2": "", "addres2City": "MOSCOW", "addres2State": "ID", "addres2Zip": "83844", "address2Zip4": "", "phone1AreaCode": "208", "phone1BaseNumber": "3450998", "phone2AreaCode": "208", "phone2BaseNumber": "4569845", "gender": "M", "similarityScore": "0.5", "caseType": "SEED"},

{"id": "123ABC", "prefix": "", "firstName": "STANFORZ", "middleName": "", "lastName": "SMITH", "suffix": "MD", "nameAlias1": "SMITH,STANFORD", "nameAlias2": "S,F,SMOTH", "nameAlias3": "", "dob": "1965-01-09", "ssn": "343679845", "addres1Line1": "123 MAIN ST", "addres1Line2": "", "addres1City": "MOSCOW", "addres1State": "ID", "addres1Zip": "83844", "address1Zip4": "", "addres2Line1": "456 ELM RD", "addres2Line2": "", "addres2City": "MOSCOW", "addres2State": "ID", "addres2Zip": "83844", "address2Zip4": "", "phone1AreaCode": "208", "phone1BaseNumber": "3450998", "phone2AreaCode": "208", "phone2BaseNumber": "4569845", "gender": "M", "similarityScore": "0.5", "caseType": "SEED"},

{"id": "123ABC", "prefix": "", "firstName": "STANFQRD", "middleName": "", "lastName": "SMITH", "suffix": "MD", "nameAlias1": "SMITH,STANFORD", "nameAlias2": "S,F,SMOTH", "nameAlias3": "", "dob": "1965-01-09", "ssn": "343679845", "addres1Line1": "123 MAIN ST", "addres1Line2": "", "addres1City": "MOSCOW", "addres1State": "ID", "addres1Zip": "83844", "address1Zip4": "", "addres2Line1": "456 ELM RD", "addres2Line2": "", "addres2City": "MOSCOW", "addres2State": "ID", "addres2Zip": "83844", "address2Zip4": "", "phone1AreaCode": "208", "phone1BaseNumber": "3450998", "phone2AreaCode": "208", "phone2BaseNumber": "4569845", "gender": "M", "similarityScore": "0.5", "caseType": "SEED"},

{"id": "123ABC", "prefix": "", "firstName": "STqNFORl", "middleName": "", "lastName": "SMITH", "suffix": "MD", "nameAlias1": "SMITH,STANFORD", "nameAlias2": "S,F,SMOTH", "nameAlias3": "", "dob": "1965-01-09", "ssn": "343679845", "addres1Line1": "123 MAIN ST", "addres1Line2": "", "addres1City": "MOSCOW", "addres1State": "ID", "addres1Zip": "83844", "address1Zip4": "", "addres2Line1": "456 ELM RD", "addres2Line2": "", "addres2City": "MOSCOW", "addres2State": "ID", "addres2Zip": "83844", "address2Zip4": "", "phone1AreaCode": "208", "phone1BaseNumber": "3450998", "phone2AreaCode": "208", "phone2BaseNumber": "4569845", "gender": "M", "similarityScore": "0.5", "caseType": "SEED"}

'''

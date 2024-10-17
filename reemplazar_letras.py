from collections import Counter

def contar_frecuencias(mensaje):
    # Eliminar espacios y contar las frecuencias de las letras
    mensaje_sin_espacios = mensaje.replace(" ", "")
    frecuencias = Counter(mensaje_sin_espacios)
    
    # Ordenar las frecuencias de mayor a menor
    frecuencias_ordenadas = frecuencias.most_common()
    
    return frecuencias_ordenadas

def reemplazar_caracteres(mensaje, sustituciones):
    # Crear una copia del mensaje con los caracteres reemplazados según el diccionario de sustituciones
    mensaje_descifrado = ""
    for caracter in mensaje:
        if caracter in sustituciones:
            mensaje_descifrado += sustituciones[caracter]
        else:
            mensaje_descifrado += caracter
    return mensaje_descifrado

# Mensaje cifrado
mensaje_cifrado = '''
RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE
AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.
AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ
TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX
DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936,
PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN
TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,
HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK
HKCZJOI OKEJSZCNHE.
'''

# Contar las frecuencias de aparición de cada carácter
frecuencias = contar_frecuencias(mensaje_cifrado)
print("Frecuencias de caracteres:")
for caracter, frecuencia in frecuencias:
    print(f"'{caracter}': {frecuencia}")

# Diccionario para almacenar las sustituciones manuales (ejemplo inicial)
sustituciones = {'A': 'd', 'X': 'e', 'K': 'r', 'C': 'i', 'Z': 'u', 'E': 'a', 'R': 'c', 'I': 'o', 'J': 'n', 'H': 't', 'N': 's', 'O': 'f', 'P': 'm', 'T': 'l', 'D': 'p', 'Q': 'b', 'U': 'g', 'Y': 'l', 'G': 'j', 'F': 'x', 'V': 'y', 'S': 'q', 'M': 'h'}
 }


# Reemplazar los caracteres según las sustituciones
mensaje_descifrado = reemplazar_caracteres(mensaje_cifrado, sustituciones)
print("\nMensaje parcialmente descifrado:")
print(mensaje_descifrado)

# Ciclo para permitir al usuario cambiar manualmente las sustituciones
while True:
    print("\nSustituciones actuales:")
    print(sustituciones)

    opcion = input("\n¿Deseas hacer una nueva sustitución? (s/n): ").lower()
    if opcion != 's':
        break

    caracter_cifrado = input("Introduce el carácter cifrado que deseas sustituir: ").upper()
    caracter_descifrado = input("Introduce el carácter descifrado: ").lower()

    # Actualizar el diccionario de sustituciones
    sustituciones[caracter_cifrado] = caracter_descifrado

    # Mostrar el mensaje con las nuevas sustituciones
    mensaje_descifrado = reemplazar_caracteres(mensaje_cifrado, sustituciones)
    print("\nMensaje descifrado con las nuevas sustituciones:")
    print(mensaje_descifrado)


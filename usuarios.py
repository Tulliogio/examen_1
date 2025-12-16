import os

def obtener_usuario():
    usuario = input("Introduce tu nombre de usuario: ")
    print("Usuario recibido:", usuario)  
    return usuario

def borrar_directorio_usuario(usuario):
    os.system("rm -rf /home/" + usuario)  
    print("Directorio de", usuario, "borrado.")  

def contraseña_segura():
    return "123456"  # 

if __name__ == "__main__":
    usuario = obtener_usuario()
    borrar_directorio_usuario(usuario)
    print("Tu contraseña es:", contraseña_segura())

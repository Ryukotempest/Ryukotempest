- 👋 Hi, I’m @Ryukotempest
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...

<!---
Ryukotempest/Ryukotempest is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->[Dis-Liekov.txt](https://github.com/Ryukotempest/Ryukotempest/files/15254100/Dis-Liekov.txt)
import os
import getpass

usuarios={"josed":{"ctr":"holakase","ROL":"ADMIN"}, "katrinam":{"ctr":"554422","ROL":"MASTER"},"dalithd":{"ctr":"12345","ROL":"FARMAC"},"hanielc":{"ctr":"test123xd","ROL":"FARMAC"}}
rol=None     
Medic={}
user=[]

def ext_men():
    print("Hasta la vista {usr}")



def ing_usr():
    print("╔"+"═"*31+"╗")
    print("║"+"▓"*12+" Login "+"▓"*12+"║")
    print("╠"+"═"*31+"╣")
    print("║"+"Usuario:"+" "*23+"║")
    print("║"+"Contraseña:"+" "*20+"║")
    print("╚"+"═"*31+"╝")
    usr=input("Usuario: ")
    cnt=getpass.getpass("Constraseña: ")
    
    if usr in usuarios and cnt == usuarios[usr]["ctr"]:
        global user
        user=usr
        return usuarios[usr]["ROL"]        
    else:
        print("Contraseña o Usuario incorrecto")
        input("Pulse enter para reintentar\n\n\n")
        
def adm_fn(): 
    a=1
    while a == 1:
        os.system ("cls" if os.name == "nt" else "clear") 
        adm=int(input(f"Bienvenido {user} que funcion desea realizar?\n1. Para administrar usuarios\n2. Para administrar los medicamentos\n3.Para salir\n\n-"))
        if adm==1:
            os.system ("cls" if os.name == "nt" else "clear")
            print("┌"+"─"*43+"┐")
            print("├"+"─"*8+"┤ MENU DEL ADMINISTRADOR ├"+"─"*9+"┤") 
            print("├"+"─"*43+"┤")
            print("├ 1. CREAR USUARIO Y ASIGNAR ROL"+" "*12+"┤")
            print("│"+" "*43+"│")
            print("├ 2. CONSULTAR USUARIO Y ASIGNAR ROL"+" "*8+"┤")
            print("│"+" "*43+"│")
            print("├ 3. ACTUALIZAR USUARIOS"+" "*20+"┤")
            print("│"+" "*43+"│")
            print("├ 4. BORRAR USUARIO"+" "*25+"┤")
            print("│"+" "*43+"│")
            print("├ 5. CREAR COPIA DE SEGURIDAD"+" "*15+"┤")
            print("│"+" "*43+"│")
            print("├ 6. REGRESAR"+" "*31+"┤")
            print("└"+"─"*43+"┘")
            h=int(input("Que desea hacer?: "))
            while h != 6:
                h=int(input("Opcion en desarrollo xd\nQue desea hacer?: "))                 
                if h==6:
                    a=1
                    os.system ("cls" if os.name == "nt" else "clear")
         
                    
        elif adm==2:
            os.system ("cls" if os.name == "nt" else "clear")
            print("┌"+"─"*43+"┐")
            print("├"+"─"*9+"┤ MENU DEL ADMINISTRADOR ├"+"─"*8+"┤")
            print("├"+"─"*43+"┤")
            print("├ 1. INGRESAR NUEVO MEDICAMENTO"+" "*13+"┤")
            print("│"+" "*43+"│")
            print("├ 2. CONSULTAR MEDICAMENTOS"+" "*17+"┤")
            print("│ a. CONSULTAR TODOS LOS MEDICAMENTOS"+" "*7+"│")
            print("│ b. CONSULTAR UN MEDICAMENTO"+" "*15+"│")
            print("│ c. CONSULTAR VARIOS MEDICAMENTOS"+" "*10+"│")
            print("│"+" "*43+"│")
            print("├ 3. ACTUALIZAR MEDICAMENTOS"+" "*16+"┤")
            print("│ a. ACTUALIZAR SOLO UN MEDICAMENTO"+" "*9+"│")
            print("│ b. ACTUALIZAR VARIOS MEDICAMENTOS"+" "*9+"│")
            print("│ c. ACTUALIZAR TODOS LOS MEDICAMENTOS"+" "*6+"│")
            print("│"+" "*43+"│")
            print("├ 4. BORRAR MEDICAMENTO"+" "*21+"┤")
            print("│"+" "*43+"│")
            print("├ 5. REGRESAR"+" "*31+"┤")
            print("└"+"─"*43+"┘")
            t=int(input("Que desea hacer?: "))
            while t != 5:
                t=int(input("Opcion en desarrollo xd\nQue desea hacer?: "))
                if t==5:
                    a=1
                    os.system ("cls" if os.name == "nt" else "clear")
                
                
        elif adm==3:
            os.system ("cls" if os.name == "nt" else "clear")
            a=0
            global rol
            rol=None

           
def mstr_fn():
    os.system ("cls" if os.name == "nt" else "clear")
    print(f"BIENVENIDO {user}")
    print("┌"+"─"*43+"┐")
    print("├"+"─"*12+"┤ MENU DEL MASTER ├"+"─"*12+"┤") #22
    print("├"+"─"*43+"┤")
    print("├ 1. INGRESAR NUEVO MEDICAMENTO"+" "*13+"┤")
    print("│"+" "*43+"│")
    print("├ 2. CONSULTAR MEDICAMENTOS"+" "*17+"┤")
    print("│ a. CONSULTAR TODOS LOS MEDICAMENTOS"+" "*7+"│")
    print("│ b. CONSULTAR UN MEDICAMENTO"+" "*15+"│")
    print("│ c. CONSULTAR VARIOS MEDICAMENTOS"+" "*10+"│")
    print("│"+" "*43+"│")
    print("├ 3. ACTUALIZAR MEDICAMENTOS"+" "*16+"┤")
    print("│ a. ACTUALIZAR SOLO UN MEDICAMENTO"+" "*9+"│")
    print("│ b. ACTUALIZAR VARIOS MEDICAMENTOS"+" "*9+"│")
    print("│ c. ACTUALIZAR TODOS LOS MEDICAMENTOS"+" "*6+"│")
    print("│"+" "*43+"│")
    print("├ 4. BORRAR MEDICAMENTO"+" "*21+"┤")
    print("│"+" "*43+"│")
    print("├ 5. SALIR DEL SISTEMA"+" "*22+"┤")
    print("└"+"─"*43+"┘")
    o=int(input("Que desea hacer?: "))
    while o != 5:
        o=int(input("Opcion en desarrollo xd\nQue desea hacer?: "))
    if o==5:
        global rol
        rol=None    
        
def frm_fn():
    os.system ("cls" if os.name == "nt" else "clear")
    print(f"BIENVENIDO {user}")
    print("┌"+"─"*43+"┐")
    print("├"+"─"*9+"┤ MENU DEL FARMACEUTICO ├"+"─"*9+"┤") #22
    print("├"+"─"*43+"┤")
    print("├ 1. INGRESAR NUEVO MEDICAMENTO"+" "*13+"┤")
    print("│"+" "*43+"│")
    print("├ 2. CONSULTAR MEDICAMENTOS"+" "*17+"┤")
    print("│ a. CONSULTAR TODOS LOS MEDICAMENTOS"+" "*7+"│")
    print("│ b. CONSULTAR UN MEDICAMENTO"+" "*15+"│")
    print("│ c. CONSULTAR VARIOS MEDICAMENTOS"+" "*10+"│")
    print("│"+" "*43+"│")
    print("├ 3. ACTUALIZAR MEDICAMENTOS"+" "*16+"┤")
    print("│ a. ACTUALIZAR SOLO UN MEDICAMENTO"+" "*9+"│")
    print("│ b. ACTUALIZAR VARIOS MEDICAMENTOS"+" "*9+"│")
    print("│ c. ACTUALIZAR TODOS LOS MEDICAMENTOS"+" "*6+"│")
    print("│"+" "*43+"│")
    print("├ 4. SALIR DEL SISTEMA"+" "*22+"┤")
    print("└"+"─"*43+"┘") 
    y=int(input("Que desea hacer?: "))
    while y != 4:
        y=int(input("Opcion en desarrollo xd\nQue desea hacer?: "))
    if y==4:
        global rol
        rol=None    





while rol==None:
    os.system ("cls" if os.name == "nt" else "clear")
    rol=ing_usr()
    if rol == "ADMIN":
        os.system ("cls" if os.name == "nt" else "clear")
        adm_fn()
    elif rol == "MASTER":
        os.system ("cls" if os.name == "nt" else "clear")
        mstr_fn()
    elif rol == "FARMAC":
        os.system ("cls" if os.name == "nt" else "clear")
        frm_fn()



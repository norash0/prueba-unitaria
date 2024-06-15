def sum(x,y):
    return x+y
def rest(x,y):
    return x - y
def mult(x,y):
    return x*y
def div(x,y):
    if y == 0:
        return None  
    return x/y

def login(usuario, contrasena):
    if((usuario=="sharon bejarano") and (contrasena=="2372085")):
      return True
    else:
     return False
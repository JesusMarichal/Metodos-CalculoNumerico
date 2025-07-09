def bi(ni,a,b,r,func):
        i=0
        x=0
        res=100
        while res>r and i<ni:
            def getFor(a,b):return (a+b)/2
            def getErr (a,b):return (a-b)/a
            print("\niteracion N.: ",i+1)
            #se queda con el dato anterior para la formula del error
            ant=x
            #realiza las formulas para decidir que direccion tomar
            x=getFor(a,b)
            print("\nm:",a,"+",b,"/2= ",x)
            #en los "if" analiza si es negativo o positivo para saber que lado tomar
            if func(x)*func(b)<0:
                a=x
            else :
                b=x
            #realiza la formula del error
            if i>0 :
                res=abs(getErr(x,ant))
                print("err:",x,"-",ant,"/",x,"=",res,"\n")
                print(" ")
                print(f"Resultado aproximado: x = {x}, Error final = {res}")
            #Si la condicion de parada se cumple se detiene
            i=i+1
        return x,res
if __name__ == "__main__":
    def getFun(n):return n**2 - 4
    
    ##INGRESE LOS VALORES AQUI EN LAS VARIABLES RES,NI,a,b
    res=0.01
    Ni=100
    a=1
    b=3 
    result=bi(Ni,a,b,res,getFun)
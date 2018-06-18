
class Heap:
        
    def __init__(self, datos):
        self.datos = datos
        self.heapify()
        
    def downheap(self,indice):
        hayHijoIzquierdo = len(self.datos) - 1 >= (2*indice + 1)
        hayHijoDerecho = len(self.datos) - 1 >= (2*indice + 2)
        if hayHijoIzquierdo:
            hijoIzquierdo = self.datos[2*indice + 1]
        if hayHijoDerecho:
            hijoDerecho = self.datos[2*indice + 2]
        padre = self.datos[indice]
        while (hayHijoIzquierdo and padre > hijoIzquierdo) or (hayHijoDerecho and padre > hijoDerecho):
            if hayHijoDerecho and hijoDerecho < hijoIzquierdo:
                self.datos[2*indice + 2],self.datos[indice] = self.datos[indice],self.datos[2*indice + 2]
                indice = 2*indice + 2
            else:
                self.datos[2*indice + 1],self.datos[indice] = self.datos[indice],self.datos[2*indice + 1]
                indice = 2*indice + 1
            hayHijoIzquierdo = len(self.datos) - 1 >= (2*indice + 1)
            hayHijoDerecho = len(self.datos) - 1 >= (2*indice + 2)
            if hayHijoIzquierdo:
                hijoIzquierdo = self.datos[2*indice + 1]
            if hayHijoDerecho:
                hijoDerecho = self.datos[2*indice + 2]
            padre = self.datos[indice]
    
    def upheap(self,indice):
        while indice > 0:
            padre = self.datos[int((indice-1)/2)]
            if padre > self.datos[indice]:
                self.datos[indice],self.datos[int((indice-1)/2)] = self.datos[int((indice-1)/2)],self.datos[indice]
                indice = int((indice-1)/2)
            else:
                return
            
    def heapify(self):
        for i in range(int(len(self.datos)/2)-1,-1,-1):
            self.downheap(i)
            
    def push(self, elemento):
        self.datos.append(elemento)
        self.upheap(len(self.datos) - 1)
    
    def pop(self):
        raiz = self.datos[0]
        self.datos[len(self.datos) - 1],self.datos[0] = self.datos[0],self.datos[len(self.datos) - 1]
        minimo = self.datos.pop()
        if len(self) > 0:
            self.downheap(0)
        return minimo
    
    def __len__(self):
        return len(self.datos)
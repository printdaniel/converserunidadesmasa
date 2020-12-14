from tkinter import*
from PIL import Image, ImageChops, ImageEnhance, ImageOps

class conversor_app:
    def __init__(self,window):
        self.root=window
        self.root.title("Conversor kilos a otras unidades de masa")
        self.root.config(bg="#B22222")
        
        self.kilos = DoubleVar()
        self.gramos = StringVar()
        self.onzas = StringVar()  
        self.ton = StringVar()  
        self.libras = StringVar()  
        self.decagra = StringVar()  
        self.miligra = StringVar()  
        self.tonM = StringVar()    
        
        #FRAME PARA DATOS
        
        frame = LabelFrame(self.root, text = 'Panel de datos',bg='#578D2F', padx=20, pady=20)
        frame.grid(row=0,column=0,padx=10,pady=10)
        
        frame1 = LabelFrame(self.root, text='Controles', bg='#578D2F', padx=20, pady=20)
        frame1.grid(row=1, column=0, pady=10, padx=10)
        
        # LABELS para ingreso y salida de datos.
        
        l_kilos = Label(frame, text='Kilogramos:',font=('arial', 12, 'bold'),bg="#578D2F")
        l_gramos = Label(frame, text='Gramos:',font=('arial', 12, 'bold'),bg="#578D2F")
        l_onzas = Label(frame, text='Onzas:',font=('arial', 12, 'bold'),bg="#578D2F")
        l_ton = Label(frame, text='Toneladas:',font=('arial', 12, 'bold'),bg="#578D2F")
        l_libras = Label(frame, text='Libras:',font=('arial', 12, 'bold'),bg="#578D2F")
        l_decagra = Label(frame, text='Decagramos:',font=('arial', 12, 'bold'),bg="#578D2F")
        l_miligra = Label(frame, text='Miligramos:',font=('arial', 12, 'bold'),bg="#578D2F")
        l_tonM = Label(frame, text='Toneladas Métricas:',font=('arial', 12, 'bold'),bg="#578D2F")
        
        # GRIDS
        
        l_kilos.grid(row=0,column=0) 
        l_gramos.grid(row=1,column=0) 
        l_onzas.grid(row=2,column=0) 
        l_ton.grid(row=3,column=0) 
        l_libras.grid(row=0,column=2)  
        l_decagra.grid(row=1,column=2) 
        l_miligra.grid(row=2,column=2) 
        l_tonM.grid(row=3,column=2)  
        
        #ENTRY
        e_kilos = Entry(frame,width=20,textvariable=self.kilos)
        e_kilos.grid(row=0, column=1)
        e_kilos.focus()
        
        e_gramos = Entry(frame,width=20,textvariable=self.gramos)
        e_gramos.grid(row=1, column=1)
        
        e_onzas = Entry(frame,width=20,textvariable=self.onzas)
        e_onzas.grid(row=2, column=1)
        
        e_ton = Entry(frame,width=20,textvariable=self.ton)
        e_ton.grid(row=3, column=1)
        
        e_libras = Entry(frame,width=20,textvariable=self.libras)
        e_libras.grid(row=0, column=3)
        
        e_decagra = Entry(frame,width=20,textvariable=self.decagra)
        e_decagra.grid(row=1, column=3)
        
        e_miligra = Entry(frame,width=20,textvariable=self.miligra)
        e_miligra.grid(row=2, column=3)
        
        e_tonM = Entry(frame,width=20,textvariable=self.tonM)
        e_tonM.grid(row=3, column=3)
        
        #BOTONES
        
        btn_conv = Button(frame1, text='Convertir',padx=5, pady=5,bg='#836F41',width=9,command=self.f_conv)
        btn_conv.grid(row=0,column=0)
        
        btn_limpiar = Button(frame1, text='Limpiar',padx=5, pady=5,bg='#836F41',width=9,command=self.limpiarCampos)
        btn_limpiar.grid(row=0,column=1)
        
        btn_salir = Button(frame1, text='Salir',padx=5, pady=5,bg='#836F41',width=9,command=lambda:self.root.destroy())
        btn_salir.grid(row=0,column=2)
        
    def limpiarCampos(self):
        self.kilos.set("0")
        self.gramos.set("0")
        self.onzas.set("0")
        self.ton.set("0")
        self.libras.set("0")
        self.decagra.set("0")
        self.miligra.set("0")
        self.tonM.set("0")
       
        
    def f_conv(self):
        gramos_conv = self.kilos.get()*1000
        self.gramos.set(gramos_conv)
        
        onzas_conv = self.kilos.get()*35.27
        self.onzas.set(onzas_conv)
        
        ton_conv = self.kilos.get()/1000
        self.ton.set(ton_conv)
        
        libras_conv = self.kilos.get() *2.2046
        self.libras.set(libras_conv)
        
        deca_conv = self.kilos.get()*100
        self.decagra.set(deca_conv)
        
        miligra_conv = self.kilos.get()*1000000
        self.miligra.set(miligra_conv)
         
        tonM_conv = self.kilos.get() * 0.98
        self.tonM.set(tonM_conv)
    
    
           
        
    

if __name__=='__main__':
    window=Tk()
    app=conversor_app(window)
    window.mainloop()
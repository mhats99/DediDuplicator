from processes import Info


class InfoWindows:
    
    def __init__(self,base):
        
        self.__base = base

    def open(self):
        
        def close_window():

            self.__base._open_info.close()  
            self.__base._open_info = None 
            
        if self.__base._open_info is None:
            
            self.__base._open_info = Info()
            self.__base._open_info.show()
            self.__base._open_info.close_window.connect(close_window)
            
        else:

            close_window()


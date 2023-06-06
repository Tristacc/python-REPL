class Load_data():
    def __init__(self):
        pass

    #print out the commands we have
    def usage(self):
        print('''usage:
                tracker add [item#] [amount] [category] [date] [description]
                tracker show 
                tracker delete [item#]
                tracker date
                '''
                )

    #'item#','amount','category','date','description'
    def showTable(self, items):
        if len(items)==0:
            print('no tasks to print')
            return
        print('\n')
        
        # header 設定寬度
        print("%-10s %-10s %-10s %-6s %-5s"%('item#','amount','category','date','description'))
        print('-'*70)
        for item in items:
            values = tuple(item.values()) 
            #python string formating 
            print("%-10d %-10d %-10s %04d %10s"% ( values[1], values[2], values[3], values[4],"  "+values[5]))

    #'id','item#','amount','category','date','description'
    def dateTable(self, items):
        if len(items)==0:
            print('no tasks to print')
            return
        print('\n')
        
        
        print("%-6s %-10s %-10s %-10s %-5s"%('date','item#','amount','category','description'))
        print('-'*70)
        for item in items:
            values = tuple(item.values()) 
            #python string formating 
            print(" %04d %-10d %-10d %-10s %10s"% (values[4], values[1], values[2], values[3],"  "+values[5]))
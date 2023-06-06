# this file is more like a building CLI platform page
from transaction import Transaction
from load_data import Load_data
import sys
load = Load_data()

#get the input from the terminal 
def process_args(arglist):
    ''' examine args and make appropriate calls to TodoList'''
    tracker = Transaction()
    if arglist==[] or arglist==["menu"]:
        load.usage()

    elif arglist[0]=="show":
        load.showTable(tracker.showTransactions())

    elif arglist[0]=='add':
        if len(arglist)!=6:
            print(len(arglist))
            print("more information needed")
            load.usage()
        else:
            userInput = {'item_num':arglist[1],'amount':arglist[2],'category':arglist[3], 'date':arglist[4],'description':arglist[5]}
            tracker.add(userInput)

    elif arglist[0] =='delete':
        if len(arglist)!=2:
            print("please enter the item#")
            load.usage()
        else:
            userInput = {'item_num':arglist[1]}
            tracker.delete(userInput)

    elif arglist[0] =='date':
       load.dateTable(tracker.sumByDate())
    else:
        print(arglist,"do it again!")
        load.usage()

def toplevel():
    if len(sys.argv)==1:
        load.usage()
        '''#initilized the list'''
        args = []
        while args!=['']:
            args = input("tracker> ").split(' ')
            # when user try to add something
            if args[0]=='add':
                args = ['add',args[1],args[2],args[3],args[4]," ".join(args[5:])]
            # process_args(args)
            # print('-'*70+'\n')
            #when user try to delet somthing 
            if args[0]=='delete':
                args = ['delete',args[1]]
            process_args(args)
            print('-'*70+'\n')
    else:
        args = sys.argv[1:]
        process_args(args)
        print('-'*70+'\n')
    
toplevel()
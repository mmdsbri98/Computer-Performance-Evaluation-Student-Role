from heapq import heapify , heappush , heappop;

import math

import random  

def Q_Calculate( N , Service_Rate , Live_Time):

    Factorial = math.factorial(N)

    Divide = Factorial / (Service_Rate ** (N + 1))

    Sum = 0;

    for i in range( 0 , N ): 

        Sum = Sum + (((Service_Rate * Live_Time) ** i) /  math.factorial(i));  

    E =  2.71828 ** -(Service_Rate * Live_Time)

    Interal = 1 - ( E * Sum);    
        
    Q = Divide * Interal

    return Q         

def Formola_X( N ,Entry_Rate , Service_Rate , Live_Time ):

    X = []

    for i in range(0 , N + 1 ):

        if i == 0:

            X.append(1);

        elif i == 1:

            Initial = Entry_Rate / Service_Rate ;

            X.append(Initial);

        else:

            Initial = (Entry_Rate ** i ) * (Q_Calculate(i - 1 , Service_Rate , Live_Time) / math.factorial( i - 1 ))

            X.append(Initial)  

    Sum = 0

    for i in range( 0 , len(X)):

        Sum = Sum + X[i];

    P_0 = 1 / Sum; 

    P_b = P_0 * X[ len(X) - 1];

    P_d = 1 - (( Service_Rate / Entry_Rate) * ( 1 - P_0)) - P_b

    N_c = 0;
    
    for u in range(0,len(X)):

        X[u] = X[u] * P_0
             
    for h in range(0 , len(X)):

        N_c = N_c + ( h * X[h]);

    return [ P_b , P_d , N_c]

class Customer:

    def __init__(self, Name, Live_Time, Arrival_Time, Service_Time, Eviction_Time) :

        self.Name = Name;

        self.Live_Time = Live_Time;

        self.Arrival_Time = Arrival_Time;

        self.Service_Time = Service_Time;

        self.Eviction_Time = Eviction_Time;

        self.Priority = None;

        self.State = False;

        self.Get_Time = None;

Queque = ['Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty'  ];

Entry_Rate = 0.1;

Service_Rate = 1;

Number_of_Customers = 10000;

while Entry_Rate < 20.1:

    Min_Heap_Arrival_Time =[];

    heapify(Min_Heap_Arrival_Time); 

    Customers = [];
    
    Index = 0;

    for i in range( 0 , Number_of_Customers):

        if len(Customers) == 0 :

            Arrival_Time = 0;

        else:

            Arrival_Time = Customers[len(Customers)-1].Arrival_Time + (-(math.log(1-random.random())/Entry_Rate)) 

        Service_Time = -(math.log(1-random.random())/ Service_Rate)     

        Live_Time = 3;

        Eviction_Time = Live_Time + Arrival_Time

        Custom = Customer('C'+str(Index) , Live_Time , Arrival_Time , Service_Time , Eviction_Time);

        Customers.append(Custom);

        Index = len(Customers) - 1;

        heappush( Min_Heap_Arrival_Time , [Arrival_Time , Index]);

    Loop_Number = len(Min_Heap_Arrival_Time) + len(Queque)

    Formol = Formola_X( len(Queque) , Entry_Rate , Service_Rate , 3 );

    P_b = Formol[0];
    
    P_d = Formol[1];

    N_c = Formol[2];

    Free_Time = 0;

    Time = 0;

    Drop = 0;

    Service = 0;

    Block = 0;

    Customers_In_Queque = 0;
 
    while Loop_Number > 0: 

        Check = False;

        try:

            Arrival_Element = heappop(Min_Heap_Arrival_Time);
            
            Time = Arrival_Element[0]

        except:

            Arrival_Element = 'Empty';

            Min = 1000000000000;

            Minimum = 1000000000000;

            #if Queque[0] != 'Empty': 

                #Free_Time = Customers[Queque[0][1]].Service_Time + Free_Time

            #for o in range( 1 , len(Queque)):
                
                #if Queque[o] != 'Empty' and Customers[Queque[o][1]].Service_Time + Time < Minimum:
                
                   #Mininum = Customers[Queque[o][1]].Service_Time + Time

            for o in range( 1 , len(Queque)):
                
                if Queque[o] != 'Empty' and Customers[Queque[o][1]].Eviction_Time < Min:
                
                    Min = Customers[Queque[o][1]].Eviction_Time

            if Min < Minimum:

                Time = Min;

            else:

                Time = Minimum;    

        Loop_Number = Loop_Number - 1;

        Tik_Man = 1
        
        while Tik_Man <= len(Queque) - 1 :
            
            if Queque[Tik_Man] != 'Empty' and Customers[Queque[Tik_Man][1]].Eviction_Time <= Time:
                
                Drop = Drop + 1;
                
                Queque[Tik_Man] = 'Empty';
                
                for j in  range ( Tik_Man , len(Queque)):

                    if j != len(Queque)-1:

                        Queque[j] = Queque[j+1];

                    else:

                        Queque[j] = 'Empty'        

                try:

                    if Check == False:

                        Number_Empty = Queque.index('Empty')

                        Customers_In_Queque = Customers_In_Queque + Number_Empty;

                        Check = True;

                except:

                    if Check == False:

                        Number_Empty = 0

                        for y in range( 0 , len(Queque)):

                            if Queque[y] != 'Empty':

                                Number_Empty = Number_Empty + 1

                        Customers_In_Queque = Customers_In_Queque + Number_Empty;

                        Check = True
                
            else:

                Tik_Man = Tik_Man + 1;                                              

        try:

            Cell = Queque.index('Empty');   

            if Cell == 0 :

                Queque[Cell] = Arrival_Element

                Is_Process = Queque[Cell];
            
                Free_Time =  Customers[Queque[0][1]].Service_Time + Free_Time;

                try:

                    if Check == False:

                        Number_Empty = Queque.index('Empty')

                        Customers_In_Queque = Customers_In_Queque + Number_Empty;

                        Check = True;

                except:

                    if Check == False:

                        Number_Empty = 0

                        for y in range( 0 , len(Queque)):

                            if Queque[y] != 'Empty':

                                Number_Empty = Number_Empty + 1

                        Customers_In_Queque = Customers_In_Queque + Number_Empty;

                        Check = True 

            elif Cell != 0:

                if Free_Time <= Time  :     
                    
                    Service = Service + 1;
                
                    for i in  range ( 0 , len(Queque)):

                        if i != len(Queque)-1:

                            Queque[i] = Queque[i+1];

                        else:

                            Queque[i] = 'Empty' 
                    
                    Empty_Index = Queque.index('Empty')

                    if Customers[Arrival_Element[1]].State == False:

                        Queque[Empty_Index] = Arrival_Element;

                        Free_Time = Customers[Queque[0][1]].Service_Time + Free_Time;  
                    
                        Is_Process = Queque[0];  

                        Customers[Arrival_Element[1]].State = True;

                    try:

                        if Check == False:

                            Number_Empty = Queque.index('Empty')

                            Customers_In_Queque = Customers_In_Queque + Number_Empty;

                            Check = True;

                    except:

                        if Check == False:

                            Number_Empty = 0

                            for y in range( 0 , len(Queque)):

                                if Queque[y] != 'Empty':

                                    Number_Empty = Number_Empty + 1

                            Customers_In_Queque = Customers_In_Queque + Number_Empty;

                            Check = True     

                else:

                    if Customers[Arrival_Element[1]].State == False:

                        Empty_Index = Queque.index('Empty');

                        Queque[Empty_Index] = Arrival_Element;

                        Customers[Arrival_Element[1]].State = True;

                    try:

                        if Check == False:

                            Number_Empty = Queque.index('Empty')

                            Customers_In_Queque = Customers_In_Queque + Number_Empty;

                            Check = True;

                    except:

                        if Check == False:

                            Number_Empty = 0

                            for y in range( 0 , len(Queque)):

                                if Queque[y] != 'Empty':

                                    Number_Empty = Number_Empty + 1

                            Customers_In_Queque = Customers_In_Queque + Number_Empty;

                            Check = True 

        except:

            Emp = 0 ;

            for i in range( 0 , len(Queque)):

                if Queque[i] != 'Empty':

                    Emp = Emp + 1;

            if Emp == len(Queque):

                Block = Block + 1;

                if Check == False: 

                    Customers_In_Queque = Customers_In_Queque + 14

                    Check = True;      
                               
    Entry_Rate = Entry_Rate + 0.1 ;

    with open('Drops-Simulate(Fixed).txt','a') as Output:

            Out = Output.writelines( str(Drop / Number_of_Customers) + '\n');

    with open('Drops-Analytic(Fixed).txt','a') as Output:

            Out = Output.writelines(  str(P_d) + '\n');        

    with open('Blocks-Simulate(Fixed).txt','a') as Output:

            Out = Output.writelines( str(Block / Number_of_Customers)+ '\n');        

    with open('Blocks-Analytic(Fixed).txt','a') as Output:

            Out = Output.writelines( str(P_b) + '\n');   

    with open('Customers_In_Queque-Simulate(Fixed).txt','a') as Output:

            Out = Output.writelines( str(Customers_In_Queque / Number_of_Customers) + '\n');   

    with open('Customers_In_Queque-Analytic(Fixed).txt','a') as Output:

            Out = Output.writelines( str(N_c) + '\n');               
        
        
    
    print('DROP:' + str(Drop/Number_of_Customers) + '     ' + str(P_d))

    print('BLOCK:' + str(Block/Number_of_Customers) + '     ' + str(P_b))

    print('Customers_In_Queque:' + str(Customers_In_Queque / Number_of_Customers) + '     ' + str(N_c) )

    print('---------------------------------------------------')
    
    




            
    




from heapq import heapify , heappush , heappop;

import math

import random  

def Q_Calculate( N , Live_Time):

    if N == 0:

        Q = 0;

    elif N > 0 :

        Q = N / Live_Time;    

    return Q         

def Formola_X( N ,Entry_Rate , Service_Rate , Live_Time ):

    Total_Sum = 0;

    X = [];

    for i in range( 1 , N + 1 ):

        Up_Frac = Entry_Rate ** i;

        Mult = 1

        for j in range ( 1 , i + 1):

            Mult = Mult * ( Service_Rate + Q_Calculate( j , Live_Time) )

        Total_Sum = Total_Sum + (Up_Frac / Mult)      

    X.append( ( 1 + Total_Sum) ** (-1) ); 

    for i in range( 1 , N + 1):

        Up = Entry_Rate ** i;

        Down = 1

        for j in range ( 1 , i + 1):

            Down = Down * ( Service_Rate + Q_Calculate( j , Live_Time ) )

        P = X[0] * ( Up / Down);

        X.append(P);

    P_b = X[14]

    P_d = 1 - (( Service_Rate / Entry_Rate) * ( 1 - X[0])) - P_b

    N_c = 0;
         
    for i in range(0 , len(X)):

        N_c = N_c + ( i * X[i]);

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

Queque = ['Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty'];

Entry_Rate = 0.1;

Service_Rate = 1;

Number_of_Customers = 1000000;

while Entry_Rate < 20.1:

    Min_Heap_Arrival_Time =[];

    Min_Heap_Eviction_Time = [];

    heapify(Min_Heap_Eviction_Time);

    heapify(Min_Heap_Arrival_Time); 

    Customers = [];
    
    Index = 0;

    for i in range( 0 , Number_of_Customers):

        if len(Customers) == 0 :

            Arrival_Time = 0;

        else:

            Arrival_Time = Customers[len(Customers)-1].Arrival_Time + (-(math.log(1-random.random())/Entry_Rate)) 

        Service_Time = -(math.log(1-random.random())/ Service_Rate)     

        Rate_Live_Time = 1 / 3;    

        Live_Time = -(math.log(1-random.random()) / Rate_Live_Time )

        Eviction_Time = Live_Time + Arrival_Time

        Custom = Customer('C'+str(Index) , Live_Time , Arrival_Time , Service_Time , Eviction_Time);

        Customers.append(Custom);

        Index = len(Customers) - 1;

        heappush( Min_Heap_Arrival_Time , [Arrival_Time , Index]);

        heappush( Min_Heap_Eviction_Time , [Eviction_Time , Index]);

    Loop_Number = len(Min_Heap_Arrival_Time) + len(Queque)   

    Formol = Formola_X( len(Queque), Entry_Rate , Service_Rate , 3 );

    P_b = Formol[0];
    
    P_d = Formol[1];

    N_c = Formol[2];

    Free_Time = 0;

    Time = 0;

    Drop = 0;

    Service = 0;

    Block = 0;

    Customers_In_Queque = 0;

    Number_of_Customer_in_Queque = 1;

    Prev_Time = 0;

    Free_Time = ['Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty' ,'Empty'  ];
 
    while Loop_Number != 0:

        Loop_Number = len(Min_Heap_Arrival_Time) + len(Min_Heap_Eviction_Time)

        Input_Element = False;

        Eviction_Alow  = False;
        
        Check = False; 
        
        try:

            Arrival_Element = heappop(Min_Heap_Arrival_Time);

            Time_2 = Arrival_Element[0];

        except:

            Time_2 = Customers[len(Customers)-1].Eviction_Time + 100;

            Arrival_Element = 'Empty';

        try:

            Eviction_Element = heappop(Min_Heap_Eviction_Time);

            Time_1 = Eviction_Element[0];

        except:

            Time_1 = Customers[len(Customers)-1].Arrival_Time + 100;    
        
        if Time_1 <= Time_2 :

            Time = Time_1;
                
            Eviction_Alow = True;

            if Arrival_Element != 'Empty':

                heappush(Min_Heap_Arrival_Time , Arrival_Element);
            
        elif Time_2 < Time_1:

            Time = Time_2;
                
            Input_Element = True;

            heappush(Min_Heap_Eviction_Time , Eviction_Element); 

        for k in range( 0 , len(Free_Time)):
            
            if Free_Time[k] != 'Empty':

                Free_Time[k] = Free_Time[k] - (( 1 / Number_of_Customer_in_Queque) * (Time - Prev_Time))           

        Number_of_Customer_in_Queque = 1;

        Loop = 0
        
        while Loop <= len(Queque) - 1:
            
            if Free_Time[Loop] != 'Empty' and Free_Time[Loop] <= 0 :
                
                Service = Service + 1;
                
                for j in  range ( Loop , len(Free_Time)):

                    if j != len(Free_Time) - 1:

                        Free_Time[j] = Free_Time[j+1];

                    else:

                        Free_Time[j] = 'Empty';
                
                Queque[Loop] = 'Empty';

                for j in  range ( Loop , len(Queque)):

                    if j != len(Queque)-1:

                        Queque[j] = Queque[j+1];

                    else:

                        Queque[j] = 'Empty'

            else:

                Loop = Loop + 1;

        Tik_Man = 0
       
        while Tik_Man <= len(Queque) - 1 :
            
            if Queque[Tik_Man] != 'Empty' and Customers[Queque[Tik_Man][1]].Eviction_Time <= Time and Free_Time[Tik_Man] > 0:
                
                Drop = Drop + 1;
                
                Queque[Tik_Man] = 'Empty';
                
                for j in  range ( Tik_Man , len(Queque)):

                    if j != len(Queque)-1:

                        Queque[j] = Queque[j+1];

                    else:

                        Queque[j] = 'Empty' 

                Free_Time[Tik_Man] = 'Empty'

                for j in  range ( Tik_Man , len(Free_Time)):

                    if j != len(Free_Time)-1:

                        Free_Time[j] = Free_Time[j+1];

                    else:

                        Free_Time[j] = 'Empty';        
                
            else:

                Tik_Man = Tik_Man + 1;  

        if Input_Element == False and Eviction_Alow == True:

            try:

                if Check == False:

                    Number_Empty = Queque.index('Empty')

                    Customers_In_Queque = Customers_In_Queque + Number_Empty - 1;

                    Check = True;

            except:

                if Check == False:

                    Number_Empty = 0

                    for y in range( 0 , len(Queque)):

                        if Queque[y] != 'Empty':

                            Number_Empty = Number_Empty + 1

                    Customers_In_Queque = Customers_In_Queque + Number_Empty - 1;

                    Check = True                                                          

        if Input_Element == True:
        
            try:

                Cell = Queque.index('Empty');   
                
                if Cell == 0 :
                    
                    Queque[Cell] = Arrival_Element;

                    Free_Time[Cell] = Customers[Arrival_Element[1]].Service_Time;

                    try:

                        if Check == False:

                            Number_Empty = Queque.index('Empty') 

                            Customers_In_Queque = Customers_In_Queque + Number_Empty - 1 ;

                            Check = True;

                    except:

                        if Check == False:

                            Customers_In_Queque = Customers_In_Queque - 1 ;

                            Check = True;

                elif Cell != 0 :

                        if Customers[Arrival_Element[1]].State == False:
                        
                            Empty_Index = Queque.index('Empty')

                            Queque[Empty_Index] = Arrival_Element;
                        
                            Free_Time[Empty_Index] = Customers[Arrival_Element[1]].Service_Time

                            Customers[Arrival_Element[1]].State = True;

                            try:

                                if Check == False:

                                    Number_Empty = Queque.index('Empty') 

                                    Customers_In_Queque = Customers_In_Queque + Number_Empty  ;

                                    Check = True;

                            except:

                                if Check == False:

                                    Number_Empty = 0

                                    for y in range( 0 , len(Queque)):

                                        if Queque[y] != 'Empty':

                                            Number_Empty = Number_Empty + 1

                                    Customers_In_Queque = Customers_In_Queque + Number_Empty ;

                                    Check = True;    

                else:

                        if Customers[Arrival_Element[1]].State == False:

                            Empty_Index = Queque.index('Empty');

                            Queque[Empty_Index] = Arrival_Element;

                            Free_Time[Empty_Index] = Customers[Arrival_Element[1]].Service_Time;

                            Customers[Arrival_Element[1]].State = True;

                            try:

                                if Check == False:

                                    Number_Empty = Queque.index('Empty') 

                                    Customers_In_Queque = Customers_In_Queque + Number_Empty ;

                                    Check = True;

                            except:

                                if Check == False:

                                    Number_Empty = 0

                                    for y in range( 0 , len(Queque)):

                                        if Queque[y] != 'Empty':

                                            Number_Empty = Number_Empty + 1

                                    Customers_In_Queque = Customers_In_Queque + Number_Empty ;

                                    Check = True;
            
            except:

                Emp = 0 ;

                for i in range( 0 , len(Queque)):

                    if Queque[i] != 'Empty':

                        Emp = Emp + 1;

                if Emp == len(Queque):

                    Block = Block + 1; 

                    if Check == False:

                        Customers_In_Queque = Customers_In_Queque + 14 ;

                        Check = True  
            
        Prev_Time = Time;               

        for i in range( 0 , len(Queque)):

            if Queque[i] != 'Empty':

                Number_of_Customer_in_Queque = Number_of_Customer_in_Queque + 1;
        
    Entry_Rate = Entry_Rate + 0.1 ;

    with open('Drops-Simulate(Exp).txt','a') as Output:

            Out = Output.writelines( str(Drop / Number_of_Customers) +  '\n');

    with open('Drops-Analytic(Exp).txt','a') as Output:

            Out = Output.writelines( str(P_d) +  '\n');

    with open('Blocks-Simulate(Exp).txt','a') as Output:

            Out = Output.writelines( str(Block / Number_of_Customers) + '\n');

    with open('Blocks(Exp)-Analytic.txt','a') as Output:

            Out = Output.writelines( str(P_b) + '\n');   

    with open('Customers_In_Queque-Simulate(Exp).txt','a') as Output:

            Out = Output.writelines( str(Customers_In_Queque / (Number_of_Customers * 2) ) +  '\n');    

    with open('Customers_In_Queque-Analytic(Exp).txt','a') as Output:

            Out = Output.writelines(str(N_c) + '\n'); 
    
    print('DROP:' + str(Drop/Number_of_Customers) + '    ' + str(P_d))

    print('BLOCK:' + str(Block/Number_of_Customers)+ '    ' + str(P_b))

    print('Customers_In_Queque:' + str(Customers_In_Queque / (Number_of_Customers * 2))+ '    ' + str(N_c))

    print('---------------------------------------------------')
    




            
    




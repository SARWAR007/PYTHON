import pandas as pd

purchase_order1 = pd.Series({'Item_Purchased' : 'Pen',
                             'Name' : 'Farhan',
                             'Cost' : '20.50'})

purchase_order2 = pd.Series({'Item_Purchased' : 'Notebook',
                             'Name' : 'Rohit',
                             'Cost' : '25.50'})

purchase_order3 = pd.series({'Item_Purchased' : 'Sheets',
                             'Name' : 'Vinod',
                             'Cost' : '33.50'})


df = pd.DataFrame([purchase_order1,purchase_order2,purchase_order3],index =['Rupashree Store','Bhawani Store','Vartika Store'])

df.head()


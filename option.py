def switch(i):
        print("IN switch")
        def environment():
                      print("WELCOME")
        def exe():
                      exit()
        switcher={
                
                1: environment ,
                2: exe ,
             }
        switcher.get(i)()

y= int(input("\t\t\tPRESS 1 TO SET UP ENVIRONMENT AND 2 TO Exit"))        
switch(y)

class bank:
    class employ:
        def __init__(self,name,sal,pos):
            self.name=name
            self.sal=sal
            self.pos=pos
            print(f"i'm {pos} my name is {name} and my salary is :{sal}")
    class customer:
        def __init__(self,name,sal,loan):
            self.name=name
            self.sal=sal
            self.loan=loan   
            print(f"my name is {name} and my salary is : {sal} and loan : {loan}")

c1=bank.employ("ahmed",10000,"developer")
a1=bank.customer("saeed",12000,134567890)
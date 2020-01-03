class Math:
    def add(self):
        no1=10
        no2=20
        print(no1+no2)
    def add(self,no1,no2):
        self.no1=no1
        self.no2=no2
        print(self.no1+self.no2)

    def add(self, no1):
        self.no1 = no1
        print(self.no1 + 10)

m=Math()
#m.add(10,20)
m.add(20)
# m.add()
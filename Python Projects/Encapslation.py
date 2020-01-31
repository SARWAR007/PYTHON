class SeeMee:
    
    __car = "Ferrari"
    __house = "Villa"
    __bank_balance = "40 billion USD"
  def youcanseeme(self):
      
      return 'you can see me'
    
  def __youcannotseeme(self):
      
    
     return 'you cannot see me'+self.car
    
#Outside class    
Check = SeeMee()
print(Check.youcanseeme())
print(Check._SeeMee__youcannotseeme()) 

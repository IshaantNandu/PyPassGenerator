from secrets import token_urlsafe as passwordx
from random import randrange as ranBit
class PasswordGenerator():
    def __init__(self,*args,**kwargs):
        self.NumOfBytes,self.BruteForceBytes=ranBit(4,10),ranBit(64,256)
        self.MaxIter=2
        self.IterCount=0
    @property
    def BruteForcePassword(self,*args,**kwargs):
        """
        Gives a password which *Maybe* is Brute-Force safe
        """
        return passwordx(self.BruteForceBytes)
    @property
    def NormalPassword(self,*args,**kwargs):
        return passwordx(self.NumOfBytes)
    def SetupDaemon(self,*args,**kwargs):
        print("Welcome to Password Generator By Ishaant Nandu")
        BruteForceAsker=input("Do you want a Brute-Force safe password? (Y/n)")
        BruteForceAsker=BruteForceAsker.upper()
        if BruteForceAsker=="Y" or BruteForceAsker=="'Y'":
            print(f"Password: {self.BruteForcePassword} ")
            return None
        elif BruteForceAsker=="N" or BruteForceAsker=="'N'":
            print(f"Password: {str(self.NormalPassword)}")
            return None
        else:
            if self.IterCount<=self.MaxIter:
                print("Sorry, Didn't understand, please input 'n' for no or 'y' for yes")
                self.SetupDaemon()
                self.IterCount +=1
            else:
                raise(NameError(f"You didn't follow the instructions to input 'y' or 'n' {self.IterCount} times, so your code DESERVES to have an error 😭 "))
            
            

            
if __name__=="__main__":
    x=PasswordGenerator(2)
    x.SetupDaemon()

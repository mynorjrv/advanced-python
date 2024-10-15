class AccountException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
class BankAccount:
    def __init__(self, *, accountNumber=0, apertureBalance=0):
        self.__accoutNumber = accountNumber
        self.__balance = apertureBalance
        
    @property
    def accountNumber(self):
        return self.__accoutNumber
    
    @accountNumber.setter
    def accountNumber(self, newAccountNumber):
        raise AccountException('Account number cannot change.')
    
    @accountNumber.deleter
    def accountNumber(self):
        if self.__balance>0:
            raise AccountException(
                'Account number cannot be deleted with positive balance.'
                )
        else:
            self.__accoutNumber = None

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, newBalance):
        if newBalance<0:
            raise AccountException('Not enough funds.')
        if abs(newBalance-self.balance)>100_000:
            print('Voluminous transaction')
            self.__balance = newBalance
        self.__balance = newBalance


A = BankAccount(
    accountNumber=102424554,
    apertureBalance=10
)

print('balance: ', A.balance)
A.balance = 1000
print('balance: ', A.balance)
print()

try:
    A.balance = -200
except AccountException:
    print('Negative value vas not accepted')
    print(A.balance)
print()

print('Account number: ', A.accountNumber)
try:
    A.accountNumber = 2
except AccountException:
    print('Not possible to change account number')
print('Account number: ', A.accountNumber)
print()

print('balance: ', A.balance)
A.balance += 1_000_000
print('balance: ', A.balance)
print()

try:
    del A.accountNumber
except AccountException:
    print('Account number cannot be deleted with balance not zero.')
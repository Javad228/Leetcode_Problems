class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.hashy_accounts = {}
        for b in range(len(balance)):
            self.hashy_accounts[b+1] = balance[b]
        

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if account1 not in self.hashy_accounts or account2 not in self.hashy_accounts or self.hashy_accounts[account1] - money < 0:
            return False
        self.hashy_accounts[account1] = self.hashy_accounts[account1] - money
        self.hashy_accounts[account2] = self.hashy_accounts[account2] + money
        return True

        

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account not in self.hashy_accounts:
            return False
        self.hashy_accounts[account] = self.hashy_accounts[account] + money
        return True

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account not in self.hashy_accounts or self.hashy_accounts[account] - money < 0:
            return False
        self.hashy_accounts[account] = self.hashy_accounts[account] - money
        return True



# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
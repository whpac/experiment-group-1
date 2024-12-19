class BankAccount:
    def __init__(self, accountNumber, initialBalance):
        self.__accountNumber = accountNumber
        self.__balance = initialBalance
        print(f'Account {accountNumber} created successfully with balance of {initialBalance}')

    def deposit(self, amount):
        assert amount > 0
        self.__balance += amount
        print(f'Deposited {amount} to account {self.__accountNumber}. Current balance: {self.__balance}')

    def withdraw(self, amount):
        assert amount > 0
        assert amount <= self.__balance
        self.__balance -= amount
        print(f'Withdrawn {amount} from account {self.__accountNumber}. Current balance: {self.__balance}')

    def transferTo(self, target, amount):
        assert amount > 0
        assert amount <= self.__balance

        self.__balance -= amount
        target.__balance += amount
        print(f'Transferred {amount} from {self.__accountNumber} to {target.__accountNumber}')

    def displaySummary(self):
        print(f'Account {self.__accountNumber} with balance {self.__balance}')

class AccountManager:
    __accounts = []
    
    def createAccount(accountNumber, initialBalance):
        acc = BankAccount(accountNumber, initialBalance)
        AccountManager.__accounts.append(acc)
        return acc
    
    def viewAccounts():
        for acc in AccountManager.__accounts:
            acc.displaySummary()


#
# -----------------------------------------------------------------------------
#

class ToDoList:

    def __init__(self):
        self.tasks = []
    
    def add_task(self, title: str, description: str, priority: int) -> None:
        self.tasks.append(Task(title, description, priority, False))

    def remove_taks(self, title: str) -> None:
        for i, task in enumerate(self.tasks):
            if task.title == title:
                del self.tasks[i]
    
    def view_sorted_tasks(self) -> None:
        for task in self.tasks:
            print(task.title, f'(priority: {task.priority})')
            print('Completed' if task.is_completed else 'Not completed')
            print(task.description)

    def mark_as_completed(self, title) -> None:
        for task in self.tasks:
            if task.title == title:
                task.is_completed = True

class Task:
    
    def __init__(self, title: str, description: str, priority: int, is_completed: bool):
        self.title = title
        self.description = description
        self.priority = priority
        self.is_completed = is_completed
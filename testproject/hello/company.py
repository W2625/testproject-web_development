class Worker:
    def __init__(self, workerCode, workerName, fixedSalary, ndaatgal, emdaatgal):
        self.workerCode = workerCode
        self.workerName = workerName
        self.fixedSalary = fixedSalary
        self.ndaatgal = ndaatgal    # 社会保险税率
        self.emdaatgal = emdaatgal  # 医疗保险税率

    def calculateTax(self, salary=None):
        if salary is None:
            salary = self.fixedSalary
        tax = salary * (self.ndaatgal + self.emdaatgal)
        return tax
        
    def calculateSalary(self):
        after_tax_wages = self.fixedSalary - self.calculateTax()
        return after_tax_wages
    
    def __str__(self):
        return (f"workerCode: {self.workerCode}, " 
                f"workerName: {self.workerName}, " 
                f"fixedSalary: {self.fixedSalary}, "
                f"salary(after_tax): {self.calculateSalary():.2f}")
        
class BasicWorker(Worker):
    def __init__(self, workerCode, workerName, fixedSalary, ndaatgal, emdaatgal, bonusSalary=100000):
        super().__init__(workerCode, workerName, fixedSalary, ndaatgal, emdaatgal)
        self.bonusSalary = bonusSalary
        
    def calculateTax(self):
        total_revenue = self.fixedSalary + self.bonusSalary
        tax = total_revenue * (self.ndaatgal + self.emdaatgal)
        return tax
        
    def calculateSalary(self):
        after_tax_wages = self.fixedSalary + self.bonusSalary - self.calculateTax()
        return after_tax_wages
    
    def __str__(self):
        return (f"workerCode: {self.workerCode}, " 
                f"workerName: {self.workerName}, " 
                f"fixedSalary: {self.fixedSalary}, "
                f"salary_after_tax(fixed salary + bonus): {self.calculateSalary():.2f}")
        
class Company:
    def __init__(self):
        self.workers = []
        
    def addNewWorker(self, worker):
        if isinstance(worker, Worker):      # 检查 worker 是否 属于 Worker 类或 Worker 的子类
            self.workers.append(worker)
        else:
            raise TypeError("You can only add objects of the Worker class or its subclasses.")
        
    def countWorker(self):
        return len(self.workers)
    
    def calculateTotalTax(self):
        total_tax  = 0
        for w in self.workers:
            total_tax += w.calculateTax()
        return total_tax
    
    def __str__(self):
        info = ""
        for w in self.workers:
            info += str(w) + "\n"
        info += (f"The company has {self.countWorker()} employees.\n"
                f"Total tax amount for all employees: {self.calculateTotalTax():.2f}")
        return info

if __name__ == '__main__':
    # 创建公司
    company = Company()
    
    # 创建 Worker 对象
    w1 = Worker("W001", "Anna", 500000, 0.1, 0.05)
    w2 = Worker("W002", "Bob", 600000, 0.1, 0.05)
    
    # 创建 BasicWorker 对象
    b1 = BasicWorker("B001", "Candy", 400000, 0.1, 0.05)
    b2 = BasicWorker("B002", "James", 450000, 0.1, 0.05)
    b3 = BasicWorker("B003", "Linda", 420000, 0.1, 0.05)
    b4 = BasicWorker("B004", "Mary", 470000, 0.1, 0.05)
    b5 = BasicWorker("B005", "John", 430000, 0.1, 0.05)
    
    # 添加员工
    company.addNewWorker(w1)
    company.addNewWorker(w2)
    company.addNewWorker(b1)
    company.addNewWorker(b2)
    company.addNewWorker(b3)
    company.addNewWorker(b4)
    company.addNewWorker(b5)
    
    print(company)
    
    
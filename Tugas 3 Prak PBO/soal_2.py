class Employee:
    def __init__(self, name, role, hours_worked, task_completed):
        self.name = name
        self.role = role
        self.hours_worked = hours_worked
        self.task_completed = task_completed
    
    def work(self):
        # Method untuk menunjukkan karyawan sedang bekerja
        return f"{self.name} ({self.role}) is working."
    
    def evaluate_performance(self):
        # Metode dasar, akan di-override oleh kelas turunan
        productivity = self.task_completed / self.hours_worked if self.hours_worked > 0 else 0
        if productivity > 0.8:
            return "High Performance"
        elif productivity > 0.4:
            return "Medium Performance"
        else:
            return "Low Performance"

class SoftwareEngineer(Employee):
    def __init__(self, name, hours_worked, task_completed):
        super().__init__(name, "Software Engineer", hours_worked, task_completed)
    
    def work(self):
        return f"{self.name} (Software Engineer) is coding."
    
    def evaluate_performance(self):
        productivity = self.task_completed / self.hours_worked if self.hours_worked > 0 else 0
        if productivity > 1.0:  # Lebih dari 1 tugas per jam
            return "High Performance"
        elif productivity > 0.5:
            return "Medium Performance"
        else:
            return "Low Performance"

class DataScientist(Employee):
    def __init__(self, name, hours_worked, task_completed):
        super().__init__(name, "Data Scientist", hours_worked, task_completed)
    
    def work(self):
        return f"{self.name} (Data Scientist) is analyzing data."
    
    def evaluate_performance(self):
        productivity = self.task_completed / self.hours_worked if self.hours_worked > 0 else 0
        if productivity > 0.6:
            return "High Performance"
        elif productivity > 0.3:
            return "Medium Performance"
        else:
            return "Low Performance"

class ProductManager(Employee):
    def __init__(self, name, hours_worked, task_completed):
        super().__init__(name, "Product Manager", hours_worked, task_completed)
    
    def work(self):
        return f"{self.name} (Product Manager) is managing the product roadmap."
    
    def evaluate_performance(self):
        productivity = self.task_completed / self.hours_worked if self.hours_worked > 0 else 0
        if productivity > 0.5:
            return "High Performance"
        elif productivity > 0.2:
            return "Medium Performance"
        else:
            return "Low Performance"

def main():
    employees = [
        SoftwareEngineer("Agus Subekti", 8, 10),
        DataScientist("Cecep", 8, 3),
        ProductManager("Ucup", 8, 2),
        SoftwareEngineer("Bambhank", 8, 2),
    ]
    
    # Menampilkan hasil
    for emp in employees:
        print(emp.work())
        print(f"Performance Rating: {emp.evaluate_performance()}")
        print()

if __name__ == "__main__":
    main()
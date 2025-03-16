from abc import ABC, abstractmethod
import random

# Kelas abstrak Plant
class Plant(ABC):
    def __init__(self, name, water_needs, fertilizer_needs):
        self.name = name
        self.water_needs = water_needs  # Kebutuhan air standar (liter)
        self.fertilizer_needs = fertilizer_needs  # Kebutuhan pupuk standar (kg)
        self.adjusted_water = water_needs
        self.adjusted_fertilizer = fertilizer_needs
    
    @abstractmethod
    def grow(self):
        # Method abstrak yang di override kelas turunan
        pass
    
    def calculate_needs(self, rainfall, soil_moisture):
        # Pengurangan kebutuhan air berdasarkan curah hujan dan kelembapan tanah
        water_reduction = rainfall * 0.5  # 1 mm hujan = 0.5 liter pengurangan air
        if soil_moisture > 60:  # Jika tanah sangat lembap
            water_reduction += (soil_moisture - 60) * 0.1
        
        self.adjusted_water = max(0, self.water_needs - water_reduction)
        self.adjusted_fertilizer = self.fertilizer_needs  # Pupuk tidak berubah dalam contoh ini
    
    def show_needs(self):
        # Menampilkan kebutuhan air dan pupuk yang telah di adjusted
        return (f"{self.name} - Adjusted Water Needs: {self.adjusted_water:.1f} liters, "
                f"Adjusted Fertilizer Needs: {self.adjusted_fertilizer:.1f} kg")

# Kelas turunan RicePlant
class RicePlant(Plant):
    def __init__(self):
        super().__init__("Rice", 20, 4)  # Standar: 20L air, 4kg pupuk
    
    def grow(self):
        return "Rice is growing in the paddy field"

# Kelas turunan CornPlant
class CornPlant(Plant):
    def __init__(self):
        super().__init__("Corn", 18, 7)  # Standar: 18L air, 7kg pupuk
    
    def grow(self):
        return "Corn is growing in the farm"

# Fungsi untuk simulasi kondisi cuaca
def simulate_weather():
    rainfall = random.uniform(0, 15)  # Curah hujan acak antara 0-15 mm
    soil_moisture = random.uniform(20, 90)  # Kelembapan tanah acak antara 20-90%
    return rainfall, soil_moisture

def main():
    # Membuat objek tanaman
    rice = RicePlant()
    corn = CornPlant()
    
    # Cuaca acak
    rainfall, soil_moisture = simulate_weather()
    
    # Menghitung kebutuhan untuk setiap tanaman
    rice.calculate_needs(rainfall, soil_moisture)
    corn.calculate_needs(rainfall, soil_moisture)
    
    # Menampilkan hasil
    print(rice.grow())
    print(f"Weather Report: Rainfall = {rainfall:.1f} mm, Soil Moisture = {soil_moisture:.1f}%")
    print(rice.show_needs())
    print()
    print(corn.grow())
    print(f"Weather Report: Rainfall = {rainfall:.1f} mm, Soil Moisture = {soil_moisture:.1f}%")
    print(corn.show_needs())

if __name__ == "__main__":
    main()
class BankAccount:
    # Kurs konversi tetap sebagai contoh (dalam sistem nyata, ini bisa diambil dari API real-time)
    EXCHANGE_RATES = {
        "USD": {"EUR": 0.91, "IDR": 15500},  # 1 USD = 0.91 EUR, 15500 IDR
        "EUR": {"USD": 1.10, "IDR": 17000},  # 1 EUR = 1.10 USD, 17000 IDR
        "IDR": {"USD": 0.000064, "EUR": 0.000059}  # 1 IDR = 0.000064 USD, 0.000059 EUR
    }
    
    def __init__(self, account_holder, balance, currency):
        # Inisialisasi
        self.account_holder = account_holder
        self.balance = balance
        self.currency = currency.upper()  # Mata uang dalam huruf besar (USD, EUR, IDR)
    
    def __add__(self, other):
        # Operator + untuk menambah saldo dari akun lain, mendukung konversi mata uang
        if isinstance(other, BankAccount):
            # Konversi saldo dari akun 'other' ke mata uang akun ini
            converted_amount = self._convert_currency(other.balance, other.currency, self.currency)
            self.balance += converted_amount
            return self  # Kembalikan objek akun yang telah diperbarui
        return NotImplemented  # Jika operand bukan BankAccount, kembalikan NotImplemented
    
    def __sub__(self, amount):
        # Operator - untuk menarik uang, mendukung penarikan dalam mata uang lain
        if isinstance(amount, (int, float)):
            # Penarikan dalam mata uang akun ini
            if self.balance >= amount:
                self.balance -= amount  # Kurangi saldo jika cukup
            else:
                print("Insufficient balance for withdrawal!")  # Peringatan jika saldo tidak cukup
            return self  # Kembalikan objek akun yang telah diperbarui
        elif isinstance(amount, tuple):  # Jika penarikan dalam mata uang lain (jumlah, mata uang)
            target_amount, target_currency = amount  # Ambil jumlah dan mata uang target
            converted_amount = self._convert_currency(target_amount, target_currency, self.currency)
            if self.balance >= converted_amount:
                self.balance -= converted_amount  # Kurangi saldo jika cukup setelah konversi
            else:
                print("Insufficient balance for withdrawal!")  # Peringatan jika tidak cukup
            return self  # Kembalikan objek akun yang telah diperbarui
        return NotImplemented  # Jika operand tidak valid, kembalikan NotImplemented
    
    def _convert_currency(self, amount, from_currency, to_currency):
        # Fungsi internal untuk mengkonversi jumlah dari satu mata uang ke mata uang lain
        if from_currency == to_currency:
            return amount  # Jika mata uang sama, kembalikan jumlah asli
        rate = self.EXCHANGE_RATES[from_currency][to_currency]  # Ambil kurs dari dictionary
        return amount * rate  # Kembalikan jumlah yang sudah dikonversi
    
    def apply_interest(self):
        # Menambahkan bunga tahunan berdasarkan saldo (khusus USD dalam contoh ini)
        if self.currency == "USD":  # Hanya terapkan bunga untuk USD sebagai contoh
            if self.balance > 5000:
                interest_rate = 0.02  # Bunga 2% untuk saldo > $5000
            else:
                interest_rate = 0.01  # Bunga 1% untuk saldo ≤ $5000
            interest = self.balance * interest_rate  # Hitung jumlah bunga
            self.balance += interest  # Tambahkan bunga ke saldo
        # Cek apakah saldo rendah setelah dikonversi ke USD
        if self._convert_currency(self.balance, self.currency, "USD") < 100:
            print("Low Balance Warning!")  # Peringatan jika saldo < $100
    
    def show_balance(self):
        # Menampilkan informasi saldo dalam format yang rapi
        return f"{self.account_holder}'s Account: Balance = {self.currency}{self.balance:.2f}"

# Fungsi utama
def main():
    john_account = BankAccount("John", 5000, "USD")
    print(f"{john_account.account_holder}'s Account: Initial Balance = ${john_account.balance}")
    print("Applying interest...", end=" ")  # Menunjukkan proses penerapan bunga
    john_account.apply_interest()  # Terapkan bunga ke akun John
    print(f"New Balance = ${john_account.balance}")  # Tampilkan saldo baru
    print()
    
    # Membuat akun Emily dengan saldo awal €1000 dalam EUR
    emily_account = BankAccount("Emily", 1000, "EUR")
    print(f"{emily_account.account_holder}'s Account: Initial Balance = €{emily_account.balance}")
    
    # Konversi saldo Emily ke USD untuk informasi tambahan
    usd_balance = emily_account._convert_currency(emily_account.balance, "EUR", "USD")
    print(f"Converted to USD: ${usd_balance:.2f}")  # Tampilkan nilai dalam USD
    
    # Mencoba menarik $1200 dari akun Emily (dikonversi ke EUR)
    emily_account - (1200, "USD")  # Penarikan dalam USD
    print(f"{emily_account.show_balance()}")  # Tampilkan saldo akhir Emily

# Memastikan program hanya berjalan jika dijalankan langsung (bukan diimpor)
if __name__ == "__main__":
    main()
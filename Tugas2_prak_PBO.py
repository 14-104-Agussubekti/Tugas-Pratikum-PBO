import random

class Robot:
    def __init__(self, name, hp, attack, accuracy):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.accuracy = accuracy
        self.defense_mode = False  # Status bertahan
        self.stunned = False  # Status stun
        self.special_cooldown = 0  # Cooldown untuk skill khusus

    def attack_enemy(self, enemy):
        if self.stunned:
            print(f"{self.name} terkena stun dan tidak bisa menyerang!")
            return
        if random.random() < self.accuracy:
            damage = self.attack
            if enemy.defense_mode:
                damage = damage // 2  # Damage berkurang 50% saat musuh bertahan
                print(f"{enemy.name} bertahan, damage berkurang menjadi {damage}!")
            enemy.hp = max(0, enemy.hp - damage)
            print(f"{self.name} menyerang {enemy.name} dan memberikan {damage} damage!")
        else:
            print(f"------------ {self.name} gagal menyerang ----------------")

    def use_special(self, enemy):
        if self.special_cooldown > 0:
            print(f"Skill khusus {self.name} sedang cooldown ({self.special_cooldown} ronde lagi)!")
            return
        if self.name == "Atreus":
            enemy.stunned = True
            print(f"{self.name} menggunakan Stun! {enemy.name} tidak bisa menyerang di ronde berikutnya!")
            self.special_cooldown = 3  # Cooldown 3 ronde
        elif self.name == "Daedalus":
            heal = 10
            self.hp = min(self.max_hp, self.hp + heal)
            print(f"{self.name} menggunakan Regen dan memulihkan {heal} HP!")
            self.special_cooldown = 2  # Cooldown 2 ronde

    def defend(self):
        self.defense_mode = True
        print(f"{self.name} bertahan! Damage yang diterima akan berkurang 50% di ronde ini.")

    def reset_status(self):
        self.defense_mode = False  # Reset setelah ronde selesai
        self.stunned = False  # Reset stun setelah satu ronde
        if self.special_cooldown > 0:
            self.special_cooldown -= 1

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        status = ""
        if self.stunned:
            status += " [Stunned]"
        if self.defense_mode:
            status += " [Defending]"
        return f"{self.name} [{self.hp}|{self.attack}]{status}"

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1

    def display_status(self):
        print(f"Round-{self.round} ==========================================================")
        print(self.robot1)
        print(self.robot2)
        print()

    def get_action(self, robot):
        while True:
            print("1. Attack     2. Defense     3. Giveup     4. Special")
            choice = input(f"{robot.name}, pilih aksi: ")
            if choice in ['1', '2', '3', '4']:
                return choice
            print("Pilihan tidak valid, coba lagi.")

    def play_round(self):
        self.display_status()

        # Aksi robot pertama
        action1 = self.get_action(self.robot1)
        if action1 == '3':
            print(f"{self.robot1.name} surend gakuat bg!")
            return self.robot2

        # Aksi robot kedua
        action2 = self.get_action(self.robot2)
        if action2 == '3':
            print(f"{self.robot2.name} surend gakuat bg!")
            return self.robot1

        # Eksekusi aksi
        if action1 == '1':
            self.robot1.attack_enemy(self.robot2)
        elif action1 == '2':
            self.robot1.defend()
        elif action1 == '4':
            self.robot1.use_special(self.robot2)

        if action2 == '1' and self.robot2.is_alive():
            self.robot2.attack_enemy(self.robot1)
        elif action2 == '2' and self.robot2.is_alive():
            self.robot2.defend()
        elif action2 == '4' and self.robot2.is_alive():
            self.robot2.use_special(self.robot1)

        # Cek pemenang
        if not self.robot1.is_alive():
            return self.robot2
        elif not self.robot2.is_alive():
            return self.robot1

        # Reset status dan tambah ronde
        self.robot1.reset_status()
        self.robot2.reset_status()
        self.round += 1
        return None

    def start(self):
        print("Pertarungan Robot Dimulai!")
        while True:
            winner = self.play_round()
            if winner:
                print(f"\n{winner.name} ez game!")
                break
            print()

# Inisialisasi Gundaammmm dan game
if __name__ == "__main__":
    atreus = Robot("atreus", 500, 10, 0.9)  # Skill: Stun
    daedalus = Robot("daedalus", 500, 8, 0.7)  # Skill: Regen
    game = Game(atreus, daedalus)
    game.start()
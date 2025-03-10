class Computer:
    def __init__(self, cpu: float, memory: int):
        self.__cpu = cpu
        self.__memory = memory

    def get_cpu(self):
        return self.__cpu
    def set_cpu(self, cpu: float):
        self.__cpu = cpu
    def get_memory(self):
        return self.__memory
    def set_memory(self, memory: int):
        self.__memory = memory

    def make_computations(self):
        return {
            "плюс": self.__cpu + self.__memory,
            "минус": self.__cpu - self.__memory,
            "умножение": self.__cpu * self.__memory,
            "деление": self.__cpu / self.__memory
        }

    def __str__(self):
        return f"cpu={self.__cpu}, memory={self.__memory}"
    def __eq__(self, other):
        return self.__memory == other.__memory
    def __ne__(self, other):
        return self.__memory != other.__memory
    def __lt__(self, other):
        return self.__memory < other.__memory
    def __le__(self, other):
        return self.__memory <= other.__memory
    def __gt__(self, other):
        return self.__memory > other.__memory
    def __ge__(self, other):
        return self.__memory >= other.__memory

computer = Computer(3.5, 16)
print(computer)
print(computer.make_computations())

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list
    def get_sim_cards_list(self):
        return self.__sim_cards_list
    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list
    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            print(f"идет звонок на номер {call_to_number} с сим-карты - {self.__sim_cards_list[sim_card_number - 1]}")
    def __str__(self):
        return f"Phone(sim_cards_list={self.__sim_cards_list})"

phone = Phone(["Beeline", "Megacom"])
print(phone)
phone.call(1, "+996 999 99 99 99")

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)
    def __str__(self):
        return f"SmartPhone(cpu={self.get_cpu()}, memory={self.get_memory()}, sim_cards_list={self.get_sim_cards_list()})"

smartphone1 = SmartPhone(2.8, 8, ["O!", "Tel2"])
print(smartphone1)

print(computer > smartphone1)
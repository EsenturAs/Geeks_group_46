class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def __str__(self):
        return f"CPU: {self.__cpu}, Memory: {self.__memory}"

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    @property
    def cpu(self):
        return self.__cpu
    
    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        print(f"Computations complete, result: {self.__cpu * self.__memory}")


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def __str__(self):
        return f"List of sim cards: {self.__sim_cards_list}"

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {self.__sim_cards_list[sim_card_number - 1]}")


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def __str__(self):
        return f"CPU: {self.cpu}, Memory: {self.memory}, list of sim cards: {self.sim_cards_list}"

    def use_gps(self, location):
        print(f"Построен маршрут до {location}")


some_computer = Computer(3.4, 16000)
some_phone = Phone(["Beeline", "Mega", "O!"])
some_smartphone_1 = SmartPhone(1.2, 8000, ["Beeline", "Mega", "O!"])
some_smartphone_2 = SmartPhone(1.5, 12000, ["Mega", "Beeline"])

print(some_computer)
print(some_phone)
print(some_smartphone_1)
print(some_smartphone_2)

some_phone.call(1, "+996 773 503 402")
some_computer.make_computations()
some_smartphone_1.use_gps("BishkekPark")
print(f"SmartPhone_1 has equal memory as Smartphone_2: {some_smartphone_1 == some_smartphone_2}")
print(f"SmartPhone_1 hasn't equal memory as Smartphone_2: {some_smartphone_1 != some_smartphone_2}")
print(f"SmartPhone_1 has less memory than Smartphone_2: {some_smartphone_1 < some_smartphone_2}")
print(f"SmartPhone_1 has more memory than Smartphone_2: {some_smartphone_1 > some_smartphone_2}")
print(f"SmartPhone_1 has less or equal memory comparing to Smartphone_2: {some_smartphone_1 <= some_smartphone_2}")
print(f"SmartPhone_1 has more or equal memory comparing to Smartphone_2: {some_smartphone_1 >= some_smartphone_2}")

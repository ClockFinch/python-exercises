# 5. Napisac obiektowo program, ktory realizuje automat stanow (np. Mealy'ego albo Moore'a),
# czyli nalezy stworzyc odpowiednie klasy z funkcjami, a nastepnie z nich utworzyc konkretna przykladowe instancje

class Moore:
    def __init__(self):
        self.states = {}
        self.current_state = None
        self.start_state = None

    def add_state(self, state, output=None, t0=None, t1=None):
        if not bool(self.states):
            self.start_state = state
            self.current_state = self.start_state
        self.states[state] = {
            "output": output,
            0: t0,
            1: t1,
        }

    def set_output(self, state, value):
        self.states[state]["output"] = value

    def set_transition(self, state1, state2, value):
        self.states[state1][value] = state2

    def set_transitions(self, state, t0, t1):
        self.states[state][0] = t0
        self.states[state][1] = t1

    def set_start(self, state):
        if state in self.states:
            self.start_state = state
            self.current_state = self.start_state

    def show(self):
        for i in self.states.keys():
            print(i, "|", self.states[i]["output"], f":\t0->{self.states[i][0]}\t1->{self.states[i][1]}", end="", sep="")
            if i == self.start_state:
                print("\t<-START", end="")
            print()
        print("Current state: ", self.current_state)

    def process_bit(self, bit_input):
        self.current_state = self.states[self.current_state][bit_input]
        return self.states[self.current_state]["output"]

    def process_str(self, str_input):
        str_output = ""
        for i in str_input:
            str_output += chr(self.process_bit(ord(i)-48)+48)
        return str_output

    def reset_state(self):
        self.current_state = self.start_state


if __name__ == "__main__":
    test = Moore()
    test.add_state("S0", 1, 'S0', 'S1')
    test.add_state("S1", 0, 'S1', 'S0')
    test.show()
    tester = "111111111111111111100000000000000000"
    print(tester)
    print(test.process_str(tester))

class Automaton:

    def __init__(self, filename):
        self.filename = filename
        self.states = {}
        self.initialState = None
        self.finalStates = {}
        self.__read_from_file()

    def is_accepted(self, token):
        state = self.initialState
        for char in token:
            found = False
            for transition in state.next_states:
                if transition[1] == char:
                    found = True
                    state = transition[0]
                    break
            if not found:
                return False
        return state.final

    def __read_from_file(self):
        with open(self.filename) as file:
            inital_state_data = file.readline().strip()
            inital_state = State(inital_state_data)
            self.initialState = inital_state
            self.states[inital_state_data] = inital_state
            other_states = file.readline().split()
            for state in other_states:
                self.states[state] = State(state)
            final_states = file.readline().split()
            for state in final_states:
                final_st = State(state, True)
                self.states[state] = final_st
                self.finalStates[state] = final_st
            transition = file.readline()
            while transition:
                split = transition.split()
                source = split[0]
                target = split[1]
                action = split[2]
                self.states[source].add_next_state((self.states[target], action))
                transition = file.readline().strip()


class State:

    def __init__(self, data, final=False):
        self.data = data
        self.next_states = []  # tuple(state, transition)
        self.final = final

    def add_next_state(self, stateWithTransition):
        self.next_states.append(stateWithTransition)

    def __hash__(self):
        return self.data.__hash__()


a = Automaton('automaton1')
print(a.is_accepted('230000000001'))

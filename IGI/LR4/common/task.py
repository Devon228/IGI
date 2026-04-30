from common.action import Action
from common.ui import read_int


class Task:
    name = "Task"

    def __repr__(self):
        return f"Task({self.name})"

    def menu_text(self):
        return """Lab 4"""

    def actions(self):
        return []

    def run(self):
        should_exit = False
        while not should_exit:
            print()
            print(self.menu_text())
            print()
            print("Menu: ")
            print("0) Exit")

            actions = self.actions()
            for i, action in enumerate(actions):
                print(f"{i + 1}) {action.name}")

            choice = read_int("Choice: ", min=0, max=len(actions))
            if choice == 0:
                should_exit = True
            elif choice > 0 and choice <= len(actions):
                actions[choice - 1]()

    @classmethod
    def as_action(cls):
        def run():
            inst = cls()
            inst.run()

        return Action(cls.name, run)

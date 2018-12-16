import parse

class Step(object):
    step_instruction_format = "Step {} must be finished before step {} can begin."

    def __init__(self, step_id):
        self._id = step_id
        self._requirements = set()

    def add_requirements(self, step_required):
        self._requirements.add(step_required)

    def __str__(self):
        output_str = "Steps needed for " + self._id + ": "
        for req in self._requirements:
            output_str += req + " "
        return output_str.strip()

    def has_requirements(self):
        return len(self._requirements) > 0

    def remove_requirement(self, requirement_step_id):
        try:
            self._requirements.remove(requirement_step_id)
        except KeyError:
            pass

def part1(steps):
    step_order = []
    while True:
        no_requirements_steps = []
        for s_id in sorted(steps.keys()):
            if not steps[s_id].has_requirements():
                no_requirements_steps.append(s_id)

        if not no_requirements_steps:
            break

        no_requirements_steps.sort()
        selected_step = no_requirements_steps[0]
        del steps[selected_step]
        step_order.append(selected_step)
        for s_id in steps:
            steps[s_id].remove_requirement(selected_step)

    print("".join(step_order))

def parse_steps(steps_str):
    steps_ids = set()
    steps = {}

    for step_str in steps_str:
        r = parse.parse(Step.step_instruction_format, step_str)
        steps_ids.add(r[0])
        steps_ids.add(r[1])

    for step_id in steps_ids:
        steps[step_id] = Step(step_id)

    for step_str in steps_str:
        r = parse.parse(Step.step_instruction_format, step_str)
        steps[r[1]].add_requirements(r[0])

    return steps

def main():
    with open("input", "r") as f:
        steps_str = f.read().split("\n")
    steps = parse_steps(steps_str)
    part1(steps)

if __name__ == "__main__":
    main()
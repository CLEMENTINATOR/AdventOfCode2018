import parse

class Step(object):
    step_instruction_format = "Step {} must be finished before step {} can begin."

    def __init__(self, step_id):
        self._id = step_id
        self._requirements = set()
        self._seconds_to_run = (ord(step_id) - ord("A") + 1) + 60
        self._running = False

    def add_requirements(self, step_required):
        self._requirements.add(step_required)

    def to_str(self, verbose=False):
        if not verbose:
            output_str = "Steps needed for " + self._id + ": "
            for req in self._requirements:
                output_str += req + " "
            output_str += "({} seconds to run)".format(self._seconds_to_run)
        else:
            output_str = "Steps needed for " + self._id + ": "
            for req in self._requirements:
                output_str += req + " "
            if self._running and self._seconds_to_run:
                output_str += "-> Running ({} seconds left)".format(self._seconds_to_run)
        return output_str.strip()

    def __str__(self):
        return self.to_str(True)

    def has_requirements(self):
        return len(self._requirements) > 0

    def remove_requirement(self, requirement_step_id):
        try:
            self._requirements.remove(requirement_step_id)
        except KeyError:
            pass

    def run(self):
        self._running = True

    def update_time(self):
        if self._running:
            self._seconds_to_run-=1

    def is_running(self):
        return self._running and self._seconds_to_run > 0

    def is_done(self):
        if self._running and self._seconds_to_run == 0:
            return True
        else:
            return False

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

def part2(steps):
    cur_second = 0
    worker_count = 5
    while True:
        worked_on_tasks = 0
        no_requirements_steps = []
        done_steps = []

        # free done steps
        for s_id in steps.keys():
            if steps[s_id].is_done():
                done_steps.append(s_id)

        for done in done_steps:
            del steps[done]
            for s_id in steps:
                steps[s_id].remove_requirement(done)

        # find jobs without requirements and count jobs being worked on
        for s_id in sorted(steps.keys()):
            if not steps[s_id].has_requirements() and not steps[s_id].is_running():
                no_requirements_steps.append(s_id)
            if steps[s_id].is_running():
                worked_on_tasks+=1

        # if they are no jobs
        if not no_requirements_steps and not worked_on_tasks:
            break

        # if we have an available worker
        while worked_on_tasks < worker_count and no_requirements_steps:
            # sort
            no_requirements_steps.sort()
            steps[no_requirements_steps[0]].run()
            del no_requirements_steps[0]
            worked_on_tasks+=1

        cur_second+=1
        for s_id in sorted(steps.keys()):
            steps[s_id].update_time()

    print("Seconds to run : {}".format(cur_second))

def main():
    with open("input", "r") as f:
        steps_str = f.read().split("\n")
    steps = parse_steps(steps_str)
    part1(steps)
    steps = parse_steps(steps_str)
    part2(steps)

if __name__ == "__main__":
    main()
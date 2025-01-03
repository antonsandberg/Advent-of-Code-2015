import re
from collections import defaultdict


def process_data():
    with open("Day 19/input.txt") as f:
        data = f.read().splitlines()
    subst_match = re.compile(r"^(\w+) => (\w+)")

    # each src group can make many target groups
    src_groups = defaultdict(list)

    # each target group can be made from only one src group
    target_groups = {}

    for line in data:
        if "=>" in line:
            group, target_group = subst_match.findall(line)[0]
            src_groups[group] += [target_group]
            target_groups[target_group] = group

    return src_groups, target_groups, data[-1]


def substitute_groups(groups: dict, molecule: str) -> set:
    new_molecules = []

    for group, targets in groups.items():
        group_matches = re.finditer(group, molecule)

        for group_match in group_matches:
            start, end = group_match.span()
            prefix = molecule[:start]
            suffix = molecule[end:]
            for target in targets:
                new_molecules.append(prefix + target + suffix)
    return set(new_molecules)


def retrosynthesis(target_groups: dict, target_molecule: str) -> list:
    synthesis_stack = []
    current_molecule = target_molecule

    molecule_modified = True
    while molecule_modified:
        molecule_modified = False

        for tgt_grp, src_grp in target_groups.items():
            if src_grp == "e":
                continue

            substitutions = current_molecule.count(tgt_grp)

            if substitutions > 0:
                current_molecule = current_molecule.replace(tgt_grp, src_grp)
                molecule_modified = True
                synthesis_stack.append([substitutions, current_molecule])

    for tgt_grp, src_grp in target_groups.items():
        if src_grp != "e":
            continue

        substitutions = current_molecule.count(tgt_grp)

        if substitutions > 0:
            current_molecule = current_molecule.replace(tgt_grp, src_grp)
            synthesis_stack.append([substitutions, current_molecule])
    return synthesis_stack


if __name__ == "__main__":
    maps, targets, start = process_data()
    # part 1
    print(len(substitute_groups(maps, start)))
    # part 2
    synthesis_stack = retrosynthesis(targets, start)
    print(sum(subs for subs, molecule in synthesis_stack))

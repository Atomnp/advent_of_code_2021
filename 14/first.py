from collections import Counter

if __name__ == "__main__":
    with open("./14/input.txt", "r") as f:
        lines = f.read().splitlines()
        template = lines[0]
        formula = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in lines[2:]}

        for i in range(20):
            new_template = template[0]
            for j in range(1, len(template)):
                if template[j - 1 : j + 1] in formula:
                    new_template += formula[template[j - 1 : j + 1]] + template[j]
                else:
                    new_template += template[j]
            template = new_template
        print(
            template.count(max(template, key=template.count))
            - template.count(min(template, key=template.count))
        )

from collections import defaultdict

if __name__ == "__main__":
    with open("./14/input.txt", "r") as f:
        lines = f.read().splitlines()
        template = lines[0]
        formula = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in lines[2:]}

        formula_count, ans = defaultdict(int), defaultdict(int)

        """
        formula_count in the format {'NN': 1, 'NC': 1, 'CB': 1}
        ans in the format {'N': 2, 'C': 1, 'B': 1}
          
        """
        ans[template[0]] += 1
        for j in range(1, len(template)):
            ans[template[j]] += 1
            formula_count[template[j - 1 : j + 1]] += 1

        for i in range(40):

            new_count = formula_count.copy()
            for j in formula_count:
                if j in formula:
                    """
                    prev count, count[NN]=1
                    by applying NN->C
                    gives count[NC]=1, count[CN]=1 and count[NN]=0

                    generated new count in the format : {'NN': 0, 'NC': 1, 'CB': 0, 'CN': 1, 'NB': 1, 'BC': 1, 'CH': 1, 'HB': 1}
                    generated  new ans in the format : {'N': 2, 'C': 2, 'B': 2, 'H': 1}
                    """
                    new_count[j[0] + formula[j]] += formula_count[j]
                    new_count[formula[j] + j[1]] += formula_count[j]
                    new_count[j] -= formula_count[j]
                    ans[formula[j]] += formula_count[j]

            formula_count = new_count

        print(max(ans.values()) - min(ans.values()))

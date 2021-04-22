class Christmas_tree_forest:
    def __init__(self):
        while True:
            print(self)

            # ask to user number_floor and number_tree
            self.number_floor: int = self.get_number("Veuillez entrer le nombre d'étage que vous voulez : ")
            self.number_tree: int = self.get_number("Veuillez entrer le nombre de sapin que vous voulez : ")

            # all information
            self.width: int = 7
            self.size_without_trunk: int = self.number_floor * 4
            self.SPACE: str = " "
            self.STAR: str = "*"
            self.GARLAND: str = "|"
            self.BALL: str = "0"

            # initialisation of christmas tree
            self.tree_star()
            self.tree_content()
            self.tree_bottom()

            # ask the user if he want to start over
            while True:
                prompt: str = input("Voulez-vous recommencer ? (y/n): ")
                if prompt == "y" or prompt == "n":
                    break
                else:
                    print("Votre réponse est invalide")
            if prompt == "n":
                break

    def __str__(self):
        return "\nGénérateur de sapin de noel\n"

    @staticmethod
    def get_number(text: str):
        while True:
            try:
                result: int = int(input(text))
            except ValueError:
                print("Veuillez écrire un nombre valide!")
            else:
                return result

    def have_spaces(self, nb_spaces: int):
        for i in range(nb_spaces):
            print(self.SPACE, end="")

    def have_stars(self, nb_stars: int):
        for i in range(nb_stars):
            print(self.STAR, end="")

    def tree_star(self):
        if self.size_without_trunk > 4:
            middle_space_number: int = (self.size_without_trunk - 1)

            space_before_after: int = middle_space_number - 5
            space_between: int = 4
            for i in range(2):
                for tree in range(self.number_tree):
                    self.have_spaces(space_before_after)
                    for j in range(3):
                        print(self.STAR, end='')
                        if j != 2:
                            self.have_spaces(space_between)
                    self.have_spaces(space_before_after + 1)
                print()
                space_before_after += 2
                space_between -= 2

            for tree in range(self.number_tree):
                self.have_spaces(middle_space_number)
                print(self.STAR + self.SPACE, end='')
                self.have_spaces(middle_space_number)
            print()

            space_before_after: int = middle_space_number - 5
            for tree in range(self.number_tree):
                self.have_spaces(space_before_after)
                for i in range(6):
                    print(self.STAR + self.SPACE, end='')
                self.have_spaces(space_before_after)
            print()

            for tree in range(self.number_tree):
                self.have_spaces(middle_space_number)
                print(self.STAR + self.SPACE, end='')
                self.have_spaces(middle_space_number)
            print()

            space_before_after: int = middle_space_number - 3
            space_between: int = 2
            for i in range(2):
                for tree in range(self.number_tree):
                    self.have_spaces(space_before_after)
                    print(self.STAR, end='')
                    self.have_spaces(space_between)
                    print(self.GARLAND, end='')
                    self.have_spaces(space_between)
                    print(self.STAR, end='')
                    self.have_spaces(space_before_after + 1)
                print()
                space_between += 2
                space_before_after -= 2

    def tree_content(self):

        numberSpace: int = (self.size_without_trunk - 1)
        for floor in range(self.number_floor):
            numberStar: int = 1
            for i in range(4):
                for tree in range(self.number_tree):
                    self.have_spaces(numberSpace)
                    self.have_stars(numberStar + (floor * 2))
                    self.have_spaces(numberSpace)
                    self.width = numberStar + (floor * 2)
                    print(" ", end="")
                print()
                numberStar += 2 + (floor * 2)
                numberSpace -= 1 + floor
            numberSpace = (self.size_without_trunk - 2) - floor

    def tree_bottom(self):

        empty_space: int = int((self.width - 6) / 4)
        garlands: list = []
        balls: list = []
        trunk: list = []
        empty: list = []

        # add garlands, balls and empty for one side in list
        for i in range(empty_space * 2):
            if i % 2 == 0:
                garlands.extend([" " + self.GARLAND])
            else:
                balls.extend([" " + self.BALL])
            empty.extend([self.SPACE])

        # add trunk for one floor in list
        trunk.extend([" "])
        for i in range(5):
            trunk.extend([self.STAR])

        # create all floor in a dict
        treeBottom: dict = {
            'thirdFloor': garlands + trunk + garlands,
            'secondFloor': balls + trunk + balls,
            'firstFloor': empty + trunk + empty
        }

        # convert treeBottom dict in a string and print it
        strTreeBottom: str = ""
        for i in treeBottom:
            length: int = len(treeBottom[i])
            for tree in range(self.number_tree):
                strTreeBottom += "".join(treeBottom[i][y] for y in range(length))
                strTreeBottom += "  "
            strTreeBottom += "\n"
        print(strTreeBottom)

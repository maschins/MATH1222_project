# Code et données pour le projet du cours MATH1222

# Classe simple pour représenter un arbre phylogénétique (noeud)

# Pour visualiser un arbre de racine root, vous pouvez utiliser
# root.toNewick() pour générer une représenter newick de l'arbre que
# vous pouvez visualiser par exemple sur le site https://beta.phylo.io/


class PTNode:
    def __init__(self, name, length, treeleft=None, treeright=None):
        self.length = length
        self.name = name
        self.parent = None
        self.left = None
        self.right = None
        if treeleft != None:
            self.left = treeleft
            self.left.parent = self
        if treeright != None:
            self.right = treeright
            self.right.parent = self

    def toNewick(self):
        """output a newick representation of the tree"""
        namestr = ""
        if self.name != None:
            namestr += self.name
        if self.length != None:
            namestr += ":" + str(self.length)
        if self.left == None:
            return namestr
        if self.parent is None:
            namestr += ";"
        return "(" + self.left.toNewick() + "," + self.right.toNewick() + ")" + namestr


# Données pour les différentes sous-questions

# Partie 1
# ========

# 2) Matrice de transition d'une chaîne réversible

Prev = [
    [0.8860516969572614, 0.04737184130589218, 0.03104758075742727, 0.03552888097941914],
    [0.011842960326473046, 0.91799183092612, 0.023685920652946092, 0.04647928809446081],
    [0.01552379037871363, 0.04737184130589217, 0.901575487335975, 0.035528880979419135],
    [0.011842960326473044, 0.061972384125947765, 0.02368592065294609, 0.9024987348946332]
]

# Partie 2
# ========

# Question 1

tree_P2Q1a = PTNode("ROOT", None, PTNode("S1", 1), PTNode("S2", 4))
print("tree_P2Q1a: ", tree_P2Q1a.toNewick())
tree_P2Q1b = PTNode("ROOT", None, PTNode("S1", 3), PTNode("S2", 2))
print("tree_P2Q1b: ", tree_P2Q1b.toNewick())

sequences_P2Q1 = {"S1": "ccat", "S2": "ccgt"}

# Question 2

tree_P2Q2 = PTNode(
    "ROOT",
    None,
    PTNode(
        "N3",
        2,
        PTNode(
            "N2", 6, PTNode("N1", 2, PTNode("S1", 1), PTNode("S2", 4)), PTNode("S3", 1)
        ),
        PTNode("S4", 9),
    ),
    PTNode("S5", 9),
)
print("tree_P2Q2: ", tree_P2Q2.toNewick())

sequences_P2Q2 = {
    "S1": "aatta",
    "S2": "aatca",
    "S3": "aacca",
    "S4": "aaaca",
    "S5": "aacca",
}

# Question 3

d = 4

tree_P2Q3a = PTNode(
    None,
    None,
    PTNode("Chimp", 25),
    PTNode(None, d, PTNode("Human", 25 - d), PTNode("Gorilla", 25 - d)),
)
print("tree_P2Q3a: ", tree_P2Q3a.toNewick())

tree_P2Q3b = PTNode(
    None,
    None,
    PTNode("Gorilla", 25),
    PTNode(None, d, PTNode("Human", 25 - d), PTNode("Chimp", 25 - d)),
)
print("tree_P2Q3b: ", tree_P2Q3b.toNewick())

sequences_P2Q3 = {
    "Gorilla": "tttttttaggtcttcctgacacaaaaaccgcgccacctggtattgtgcgttaactcgctgggtagttaactgacgcactacgctcacatggttttgtaaa",
    "Human": "ctggatgatgccacacctaaattaaagatgagttgttgagtaaactggttcagttccccacgcggttatctagtgcccaactttcgagagggacgattgg",
    "Chimp": "gagttttagggcctagctaggctaggtccgaattgacgagcgaactggctcacttaatcagggaataatccagtgcccaaccctcgagaggtagggtgag",
}

# Partie 3
# ========

# L'outgroup est la séquence "Virus0". Le nom de la séquence est la ville
# dans laquelle le variant du virus a été trouvé.

sequences_P3 = {
    "Virus0": "cattgagattgccttataccgctgcccccacttgttttgctcccttttgagtcaacgtagttgacgagggtggtatacgatgtacgagccgagtgcgaccgtcctttctgtccctagccacaatggttgaagcatcagcatactggaggtcaatagaaccatccaacgcaatcgctagttcttgtatacgtcgacgataa",
    "Alger": "aatccgaagagctctactgcaccactgctacttatattgcgccagtctggatggactttaattccggagtacctatgctgcgtaccagacgagtccggcggtacctttgatcaccgggcgcgatggtcgaagcattactggagcgaaggactacgggattaccttatgctcttgttggagaccggagggtcagccgacta",
    "Amsterdam": "cattgggatggcatgataccggttccttcacttattctgcgccaatgtggatcgacgaagaattcggcatcagtctgtgccgtgccagccgtgtgcggcagttcttcccgtccctagacacatcgcttgaagcatctccgtaacgaacgaccatagaatcaacctgagcccgcgctagttcctagagatttcgacgataa",
    "Belfast": "cattcctattgcttgagggcggatcccccccttcgggcccgcccgcgcaaaccgacttaggtgtaggaggtaggaagtgacgcgccatacgtgtgaggcagatctttcggggcttacgccaaatggctggttcctcccagcatcgaaggggaatagtctcaccgagaactcgcgctactttccagatatatcggcgatta",
    "Bologne": "cacgagaatggctttttatgggctctgctacttattttgcgcaagtgcagatggattcggatgccggagtcagtatgcagcgcactagcggagtgcggcggcccatgcgagcaccgaacgcaatggtcgaagcactagcgaaaagaaggaatccacgataatctattccccgcgctaatctctagagattgcgtcgataa",
    "Bruxelles": "cattgggatgactttataccggttccgccacttattttgcgccaatgtgggtctacgtagatgtcggcgtcagtctgtgacgtgccagccgtctgcggcgctcctttccgtccctaggcgcaatgattgaagcatcaccgtaacgaaggaccatagaatcatgcagagcccgcgctagttcctggatatttcgacgataa",
    "Casablanca": "aatgctagaacctctatagcacctctgctagtgataatgcgtctctctcgatggactttaatgcgggagaattgatgcgacggacccgacgagtgccagggtccctagcagaaccgaacgcgatggtcgagacattaccacgaggaagtagaatccggtaatccagtgctttcggtcgcgagtgggaagtcagccgatga",
    "Cork": "cattcaaattgcctgagggagggtcccccccttcgggcccgtcagcgcaacccgagttgggtgtcagaggtgggaagtgatgcgccatacgtgtggggcggatctttagggccttacgccaaatggtaggatcaggccagtatcggaaggggaccgtcccaccgagaactcgcgctactttccagatatttcgctgatta",
    "Dublin": "cattcaaattgcttgagaccggatcccctccttcgggcccgctagcgcaactcgacttgggtgtcggaggtgggaagtgacgcgccatacgtgtgaggcggggctttcgggccttacgccaaatgattggatcagcccagtatcggagggggatagactcaccgagaactcgtgctactttccagatatatcggcgatta",
    "Edimbourg": "cattcagattgttttatatcgaatcccctccctcggtcccgctcgggatggtcgacttgggtgtctgggcgagtccgtgacgcgccatacgtgtgatgctgtgctttcgggtcccatgtgaaatgcgttaatcattacagtacctgggagcgatagacccgtcgagaacctgcgctagttcccaggtatattggcgataa",
    "Glasgow": "cattgagagtgctttgtatcggatcccctccttaggtcccgctcatgaaggtcaacttgggtttctgggcgagtccgtgacgtgccatacgtgtggtgctgtgcgttcgagtcctatgtaaaatgagtgaatcatcacagtaactgggagcgatagaatcgttgagaacctgcacttgttcttaggtatatcggcgatag",
    "Lilles": "cattgggatggttgtctgtgggtttctccatttgttttgcgctcgtatgggtccacgtagaggccgcaatcagcctgtgacgtgccagccgtgcgtggtggtcgaggacgtccatggacgcaaaggccgaagcgccaccgaaacgaaggaccatagcaccatccagtacccgcgctagttcccagatatttaggggacaa",
    "Ljubljana": "catgcaaatggctttatcccggctctgcagcttattgtgcgcaaatgcagatggactaggatgcccgagtctgtatgtcgagtactagcgaagtgcggcggaccttgcgagccccaaacacaatggtcgaagcataagcggaacgctggaacacaggatcatccgctccccgcgctaatctctagagattgcgtcgatta",
    "Londres": "cactaagatcactttaccttggttccttcacttagaaacaccgcatgtatgtcgacttagttgtcgggggaggtcagcgatccgccagtactgcgcggccagtctttcagttcccaggggcaatgattgtagcgtgactgtaacggaggtccacggaatcctccagagcccgcgctctttccttgatatagcggcgataa",
    "Manchester": "tattgagattactttacatcggttccctcacttaagaaccacccatgcagacaaacttagttggcgggggtggtctgcgataggccagtcgtgtgcggccgttatctcagttctgaggagcaaagagtggagcgataccatactgtagcgtcacagaatcatccaccgcccgcgctaactccttgatatagcggcgaaaa",
    "Marrakech": "aatactagaacctctatcgcacctctgctagtggtaatgcgtctctctcgatggtctttaatgcgggagaattgatgcgtcggacccgacgcgtgccagggtccctaggagaaccgaactcgatggtcgagacatcaccaggaggaagtagaatccggtactccagagctttccgttgcgagtggggagtctgccgatga",
    "Marseille": "cattggaacggctttatatcacctcggctactcattttgcgcccttggggatggacgtggatgccggtgtcactatgtgacgtgcgagccgagtgcggcggtcgttgccgtctccggacgcaatggtggaagcatcaccgaaacgaaggaatataggactatccagtccccgcgcaagtttccagagatttcgccgatta",
    "Milan": "catgggaatggctttatatcggctctaccacttattttgcgtcagtgcagatggacttggatgccggagtcagtatgcggcgtactagccgagcgcgccggtccctgcgatcaccggacgctatggtcggagcattaccgaaacgaaggaatataggatcatctactccctgcgctagcctctatacattacgccgatta",
    "Paris": "catcggaatggctttctattacctcggctacttattttgcgcccgtgcggatagacgtggatgccggagtcagtatgtgacgtgccagccgagttcggcagtccttagcgtcaccgaacgcaatggtcgaagcatcaccgaaacgaagggatataggatgatccagtcaccgcgttagttcctagagatttcgccgatta",
    "Tunis": "aatgcgagaacctttatagcatctctgttagtgataacgcgtcactctggatgggctctaatgcgcgagaattgatagggcggaccagacgagtgcaagggtcccttcgagagcggaacgcaatggtccagacgttaccgaaacgaaggaaaattggggaattcaatgctttcggtgtttagcggagagtccgccgatga",
    "Venise": "cacgagaatggcttgatatgggctctgctacttattttgcgccagtgcagatggactaggctgccggagtcagtatgcagcgtactagcggagtgcggcggcccgtgcgcgcactgaacgcaatgttcgaagcactagcgaaaccaaggaataaaggataatctattccccgcgctaatctctagagattgcgtcgatta",
}

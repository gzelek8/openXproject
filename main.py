from tree import Tree


def main():
    tree = Tree(5)
    n1 = tree.insert(3, tree.root, "left")
    n2 = tree.insert(2, n1, "left")
    n3 = tree.insert(5, n1, "right")
    n4 = tree.insert(7, tree.root, "right")
    n5 = tree.insert(1, n4, "left")
    n6 = tree.insert(0, n4, "right")
    n7 = tree.insert(2, n6, "left")
    n8 = tree.insert(8, n6, "right")
    n9 = tree.insert(5, n8, "right")

    print("Sum is {}".format(tree.calculate_sum(n1)))
    print("Average is {}".format(tree.calculate_average(n4)))
    print("Medium is: {}".format(tree.calculate_median(n6)))


main()

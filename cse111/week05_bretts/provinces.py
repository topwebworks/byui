def main():

    provinces = read_list("provinces.txt")

    print(provinces)

    provinces.pop(0)
    provinces.pop()

    for i in range(len(provinces)):
        if provinces[i] == "AB":
            provinces[i] = "Alberta"

    alberta_num = provinces.count("Alberta")

    print()
    print(f"Alberta occurs {alberta_num} times in the modified list.")


def read_list(filename):

    file_list = []

    with open(filename, "rt") as file:

        for line in file:
            file_line = line.strip()
            file_list.append(file_line)

    return file_list


if __name__ == "__main__":
    main()

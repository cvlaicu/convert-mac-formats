import csv


def colon_to_x(macs, choice2):
    # This function converts from colon format to both hyphen and dot format.
    def colon_to_hyphen(mac_addresses1):
        # Here I am converting from colon notation to hyphen notation
        macs1_list = []
        for mac1 in mac_addresses1:
            mac1 = "-".join(mac1)
            macs1_list.append(mac1)
        return macs1_list

    def colon_to_dot(mac_addresses2):
        macs2_list = []
        for mac2 in mac_addresses2:
            mac2 = mac2[0] + mac2[1][::2] + "." + mac2[1][1::] + mac2[2] + "." + mac2[3] + mac2[4][::2] + "." + mac2[4][1::] + mac2[5]
            macs2_list.append(mac2)
        return macs2_list

    mac_list = []
    # Here I am separating the MAC elements by " : "
    for mac_address in macs:
        mac_address = mac_address.split(":")
        mac_list.append(mac_address)

    if choice2 == "hypen":
        hypen_list = colon_to_hyphen(mac_list)
        return hypen_list
    elif choice2 == "dot":
        dot_list = colon_to_dot(mac_list)
        return dot_list


def hypen_to_x(macs, choice2):
    # This function converts from colon format to both hyphen and dot format.
    def hypen_to_colon(mac_addresses1):
        # Here I am converting from colon notation to hyphen notation
        macs1_list = []
        for mac1 in mac_addresses1:
            mac1 = ":".join(mac1)
            macs1_list.append(mac1)

        return macs1_list

    def hypen_to_dot(mac_addresses2):
        macs2_list = []
        for mac2 in mac_addresses2:
            mac2 = mac2[0] + mac2[1][::2] + "." + mac2[1][1::] + mac2[2] + "." + mac2[3] + mac2[4][::2] + "." + mac2[4][1::] + mac2[5]
            macs2_list.append(mac2)

        return macs2_list

    mac_list = []
    # Here I am separating the MAC elements by " - "
    for mac_address in macs:
        mac_address = mac_address.split("-")
        mac_list.append(mac_address)

    if choice2 == "colon":
        colon_list = hypen_to_colon(mac_list)
        return colon_list
    elif choice2 == "dot":
        dot_list = hypen_to_dot(mac_list)
        return dot_list


def dot_to_x(macs, choice2):

    def dot_to_colon(mac_addresses1):
        mac_list3 = []
        for mac in mac_addresses1:
            mac = mac[0][:2] + ":" + mac[0][-1] + mac[1][:1] + ":" + mac[1][1:2] + mac[1][-1] + ":" + mac[2][:2] + ":" + mac[2][-1] + mac[3][:1] + ":" + mac[3][-2:]
            mac_list3.append(mac)
        return mac_list3

    def dot_to_hypen(mac_addresses1):
        mac_list4 = []
        for mac in mac_addresses1:
            mac = mac[0][:2] + "-" + mac[0][-1] + mac[1][:1] + "-" + mac[1][1:2] + mac[1][-1] + "-" + mac[2][:2] + "-" + \
                  mac[2][-1] + mac[3][:1] + "-" + mac[3][-2:]
            mac_list4.append(mac)
        return mac_list4

    mac_list = []
    # Here I am separating the MAC elements by " - "
    for mac_address in macs:
        mac_address = mac_address.split(".")
        mac_list.append(mac_address)

    if choice2 == "colon":
        colon_list = dot_to_colon(mac_list)
        return colon_list
    elif choice2 == "hypen":
        hypen_list = dot_to_hypen(mac_list)
        return hypen_list


def user_input():
    print("\n[+] Hello!")

    possible_choices = ["hypen", "colon", "dot"]

    while True:
        user_input1 = input("\n[+] Please tell me in what format the MACs currently are (hypen/colon/dot): ")
        if user_input1 not in possible_choices:
            print("\n[-] Please enter either /hypen/, /colon/ or /dot/...")
        else:
            break

    while True:
        user_input2 = input("\n[+] Please tell me to what format you want to convert the MAC addresses (hypen/colon/dot): ")
        if user_input2 not in possible_choices:
            print("\n[-] Please enter either /hypen/, /colon/ or /dot/...")
        else:
            break

    return user_input1, user_input2


def mac_parsing(macs):
    with open("mac_output.csv", "w", newline="") as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        for mac in macs:
            filewriter.writerow([mac])


if __name__ == "__main__":

    mac_lists = []
    with open("macs.csv") as unread_file:
        read_file = csv.reader(unread_file)
        for row in read_file:
            mac_lists.append(row[0])

    user_choice = user_input()

    if user_choice[0] == "colon":
        colon_macs = colon_to_x(mac_lists, user_choice[1])
        mac_parsing(colon_macs)

    elif user_choice[0] == "hypen":
        hypen_macs = hypen_to_x(mac_lists, user_choice[1])
        mac_parsing(hypen_macs)

    elif user_choice[0] == "dot":
        dot_macs = dot_to_x(mac_lists, user_choice[1])
        mac_parsing(dot_macs)

    print("\n[+] DONE!\n[+] Please check the mac_output.csv file."
          "\n[+] If the output is not right, then please check whether you entered the correct parameters.")



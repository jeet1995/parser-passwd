import argparse
import json

# Instantiate a parser to parse command line arguments
# from file_setup import get_file_to_read
from constants import *
from file_setup import get_file_to_read

runner_parser = argparse.ArgumentParser(
    description='This parser parses command line arguments for the runner.py script')

# Add command line arguments to be parsed
runner_parser.add_argument('--path_etc_passwd', type=str, default=30, required=False)
runner_parser.add_argument('--path_etc_group', type=str, default=20, required=False)

dictionary = {}
all_usr_names = []
all_usr_ids = []

if __name__ == "__main__":

    parsed_arguments = runner_parser.parse_args()

    passwd_file_path = get_file_to_read(parsed_arguments.path_etc_passwd, 1)

    group_file_path = get_file_to_read(parsed_arguments.path_etc_group, 2)

    passwd_lines = passwd_file_path.readlines()

    group_lines = group_file_path.readlines()

    # Process all lines in the /etc/passwd file
    for line in passwd_lines:
        if not line.startswith("#"):
            splits = line.split(":")
            dictionary[splits[USR_NAME_IDX]] = {}
            dictionary[splits[USR_NAME_IDX]]["uid"] = splits[UID_IDX]
            dictionary[splits[USR_NAME_IDX]]["full_name"] = splits[GECOS_IDX]
            dictionary[splits[USR_NAME_IDX]]["groups"] = []

    # Process all lines in the /etc/group file
    for line in group_lines:
        if not line.startswith("#"):
            splits = line.split(":")
            group_members = "".join(splits[GRP_MEMBERS_IDX].splitlines()).split(",")
            if len(group_members) > 1:
                for member in group_members:
                    dictionary[member]["groups"].append(splits[0])

    with open("results.json", "w") as output:
        json.dump(dictionary, output)

    print('Data has been dumped as a json file')

import argparse, random

def parse_args():
    parser = argparse.ArgumentParser(description='Simple password generator that generates safe, but easy to remember passwords.')
    parser.add_argument('--length', type=int, help='Number of words to be generated', default=4, required=False)
    parser.add_argument('--randomorg', help='Use random.org for entropy', action='store_true')
    return parser.parse_args()

def load_word_list():
    with open('res/words.txt') as word_list_file:
        return [line.strip() for line in word_list_file]

def get_random_number_list(num_of_words, pass_len, use_random_org):
    if use_random_org:
        print("Random.org API not yet supported, please do not use this option now. Exiting...")
        exit()
    else:
        return random.sample(range(num_of_words), pass_len)


def run(pass_len, use_random_org):
    word_list = load_word_list()
    num_of_words = len(word_list)
    word_id_list = get_random_number_list(num_of_words, pass_len, use_random_org)
    pass_words = [word_list[idx] for idx in word_id_list]
    password = " ".join(pass_words)
    print (f"Your generated password: {password}")

def warn_usr(str):
    while (True):
        decision = input(f"{str} Type yes or no... ")
        if decision == "yes":
            return True
        elif decision == "no":
            return False
        else:
            print(f"Unknown decision: {decision}. Please repeat...")

if __name__ == "__main__":
    # Parse arguments
    args = parse_args()

    # Print version and exit
    if args.length < 4:
        if not warn_usr("Warning: Selected password length is too short and is unsafe. Do you really want to continue?"):
            exit()

    run(args.length, args.randomorg)

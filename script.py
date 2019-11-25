import argparse
import subprocess
import os
import sys


def get_command_line_arguments():
    """Get arguments from command line"""
    parser = argparse.ArgumentParser(prog="Pygit")

    parser.add_argument('-t', '--create_tag', help='Tag formats: janus/v1.2.3 for production,'
                                                   'janus/v1.2.3suffix for development.')
    parser.add_argument('-p', '--push', help='push janus/1.2.3[something] - put a tag on HEAD'
                                             'Example: push janus/v1.2.3dev')
    parser.add_argument('-g', '--get_tag', action='store_true', help='get - give a version (without janus / v) if HEAD'
                                                                     'is on the tag, otherwise version + abracadabra.')
    parser.add_argument('-b', '--get_build', action='store_true', help='get-build-type - write production if HEAD is on'
                                                                       'a tag without a suffix, development if HEAD is'
                                                                       'on a tag with a suffix,fall off with an error'
                                                                       'if HEAD is not on the version tag')
    return parser.parse_args()


def git_tag(tag):
    """Create tag from command line"""
    subprocess.check_output(['git', 'tag', tag])
    return "Tag created"


def git_push(tag):
    """Push data with tag from command line"""
    try:
        sub = subprocess.check_output(['git', 'push', 'origin', tag])
    except subprocess.CalledProcessError:
        print("Error: Create tag and then push it!")
        sys.exit(1)
    return "Push completed.{}".format(sub.decode("utf-8"))


def git_get():
    """Get All Tag and clean them"""
    sub = subprocess.check_output(['git', 'tag'])
    output = sub.decode('utf-8').split("\n")
    clean_result = [p[p.find("/") + 2:] for p in output]
    return "All tag: {}".format(clean_result[:len(clean_result)-1])


def git_build():
    """Get arguments from command line"""
    sub = subprocess.check_output(['git', 'log', '--decorate=full']).decode("utf-8")
    parse_output = sub[sub.find("tag"):sub.rfind(",")].split('/')[-1]
    result = ''
    if parse_output[-3:] == 'dev':
        result = 'development'
    elif parse_output == result:
        result = "You don't have tag"
    elif parse_output[-3:] != 'dev':
        result = 'production'
    return result


def main():
    """Get the values and call the methods"""
    args = get_command_line_arguments()

    if args.create_tag:
        print(git_tag(args.create_tag))
    elif args.push:
        print(git_push(args.push))
    elif args.get_tag:
        print(git_get())
    elif args.get_build:
        print(git_build())


if __name__ == "__main__":
    """Determine if a folder is a git repo"""
    if os.path.exists('.git'):
        main()
        sys.exit(0)
    else:
        print("You don'n have .git in current folder")
        sys.exit(1)

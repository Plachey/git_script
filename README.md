Simple Test Script for work with git.
===================================================

Write a script for putting tags with the version in the git-repository:
1. Tag formats: janus / v1.2.3 for production, janus / v1.2.3suffix for development.
2. push 1.2.3[something] - put a tag on HEAD
3. get - give a version (without janus / v) if HEAD is on the tag, otherwise version + abracadabra. 
4. get-build-type - write production if HEAD is on a tag without a suffix, development if HEAD is on a tag with a
suffix, fall off with an error if HEAD is not on the version tag.
#####Warning!!! To run the script must be located in the folder with the initialized git (with the contents of .git) 

Example
---------------------

### 1. create_tag formats: janus/v1.2.3 for production, janus/v1.2.3suffix for development.

    >>> script.py --create_tag janus/v1.2.3

### 2. push janus/1.2.3[something] - put a tag on HEAD. Example: push janus/v1.2.3dev or push janus/v1.2.3'

    >>> script.py --push janus/v1.2.3 

### 3. get_tag - give a version (without janus / v) if HEAD is on the tag, otherwise version + abracadabra. 

    >>> script.py --get_tag
    
### 3. get_build - write production if HEAD is on a tag without a suffix, development if HEAD is on a tag with a suffix, fall off with an error if HEAD is not on the version tag. 

    >>> script.py --get_build

'''
Simple Operational Transformer Example takes in an old string and a 
new string (used in version control) along with a simple set of operations 
to verify if the changes match.

Operations: Skip, Insert, Delete
Operational Parameters: count, chars
'''

import json

# Create an Operational Transformer that compares strings and validates if the latest version is correct after applying a series of operations


def isValid(stale, latest, otjson):
    '''isValid function starts with the stale string, applies the operations, and then compares to the latest to see if they match.'''
    # Parse the json operations sting input so that we can use python dictionary syntax
    otjson = json.loads(otjson)

    # create a variable that store the cursor postion
    cur_position = 0
    # Iterate through each operation in the otjson
    for ops in otjson:
        # Check the skip oeration and move the cursor postion
        if ops['op'] == 'skip':
            cur_position = min(cur_position + ops['count'], len(stale))
        # Perform the insert operation and update cussor
        if ops['op'] == 'insert':
            # Insert the text
            stale = stale[:cur_position] + ops['chars'] + stale[cur_position:]
            # Move cursor to new location
            cur_position = min(cur_position + len(ops['chars']), len(stale))
        # Perform the delete operation and update cussor
        if ops['op'] == 'delete':
            # Delete the text at current cusor location and the number of characters
            stale = stale[:cur_position] + stale[cur_position + ops['count']:]
            # Move cursor to new location
            cur_position = max(cur_position - ops['count'], 0)

    return stale == latest


'''Uncomment below print statment to test sample functions provided on the instructions'''
# print(
#     isValid(
#         'This is an example sentence that shows how deleting works.',
#         'This is an example sentence.',
#         '[{"op": "skip", "count": 27}, {"op": "delete", "count": 30}]'
#     )  # // true
# )

# print(
#     isValid(
#         'This is an example sentence that shows how deleting works, but also catches the input error.',
#         'This is an example sentence.',
#         '[{"op": "skip", "count": 45}, {"op": "delete", "count": 100}]'
#     )  # // false, delete past end
# )

# print(
#     isValid(
#         'This is an example sentence that shows how deleting, and skipping past string lenght.',
#         'This is an example sentence.',
#         '[{"op": "skip", "count": 45}, {"op": "delete", "count": 40}, {"op": "skip", "count": 100}]'
#     )  # // false, delete past end
# )

# print(
#     isValid(
#         'Shows all operations working in one function and retuning the correct output.',
#         'Now all operations are working in one function and retuning the correct output.',
#         '[{"op": "delete", "count": 9}, {"op": "insert", "chars": "Now all"}, {"op": "skip", "count": 12}, {"op": "insert", "chars": "are "}]'
#     )  # // true
# )

# print(
#     isValid(
#         'Example where no changes are made.',
#         'Example where no changes are made.',
#         '[]'
#     )
#     #// true
# )

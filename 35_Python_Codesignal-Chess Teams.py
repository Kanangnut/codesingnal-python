Chess Teams:
A grand Team Chess Tournament will be held at your University. Two teams, smarties and cleveries, will clash to determine whose chess skills are better. The teams have the same number of members, and the ith member of smarties will play against the ith member of cleveries in the ith game for each valid i

Given the names of the players of both smarties and cleveries, return the games in the order they will be played.

Example

For smarties = ["Jane", "Bob", "Peter"] and
cleveries = ["Oscar", "Lidia", "Ann"], the output should be

solution(smarties, cleveries) = [["Jane",  "Oscar"],
                                 ["Bob",   "Lidia"],
                                 ["Peter", "Ann"]]
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.string smarties

Array of strings, where each string is the name of the member of smarties.

Guaranteed constraints:
0 ≤ smarties.length ≤ 10,
2 ≤ smarties[i].length ≤ 10.

[input] array.string cleveries

Members of cleveries in the same format as smarties.

Guaranteed constraints:
cleveries.length = smarties.length,
2 ≤ cleveries[i].length ≤ 10.

[output] array.array.string

The games in the following format: [game0, game1, ..., gamesmarties.length - 1] where gamei = [smartyi, cleveryi].


Solution:
def solution(smarties, cleveries):
    return [[smarties[i], cleveries[i]] for i in range(len(smarties))]

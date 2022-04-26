<h1>0x02. Minimum Operations</h1>

In a text file, there is a single character <strong>H</strong>. Your text editor can execute only two operations in this file: <m>Copy All</m> and <m>Paste</m>. Given a number <strong>n</strong>, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

<strong>Prototype:</strong> def minOperations(n)
Returns an integer
If <strong>n</strong> is impossible to achieve, return 0
<hr>
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

<strong>Number of operations:</strong> 6

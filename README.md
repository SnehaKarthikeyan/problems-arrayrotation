# problems-arrayrotation

Question:

Write a program to rotate the given input array for the given k number of times.

Input Description:

The first contains a positive integer n denoting the length of the array, 1<=n<=20. The second line contains an array of n positive integers, 1<=arr[i]<=10^4. The third line contains an integer k, the number of times the array should be rotated.

Output Description:

Print the resultant array after rotation of the given input array for the given k number of times.

Hints:

Traverse the elements of the array to rotate the array for k number of times.

Sample Input:

8\n
5 6 3 4 2 6 1 7\n
3

Sample Output:

4 2 6 1 7 5 6 3

Explanation:

After rotating the array 5 6 3 4 2 6 1 7, 3 times, the output is 4 2 6 1 7 5 6 3

Testcase 1:

Input:

22\n
3 33 56 78 3 12 45 98 3 22 56 3 78 90 43 11 25 4 51 6 12 34\n
8

Output:

3 22 56 3 78 90 43 11 25 4 51 6 12 34 3 33 56 78 3 12 45 98

Testcase 2:

Input:

42\n 
78 67 22 43 54 66 87 67 23 45 78 67 22 43 54 66 87 67 23 45 68 11 25 45 55 67 11 73 67 34 56 68 11 25 45 55 67 11 73 67 34 56\n
19

Output:

45 68 11 25 45 55 67 11 73 67 34 56 68 11 25 45 55 67 11 73 67 34 56 78 67 22 43 54 66 87 67 23 45 78 67 22 43 54 66 87 67 23

Testcase 3:

Input:

30\n 
3 33 56 78 3 12 45 98 3 22 56 3 78 90 43 11 25 4 51 6 3 22 56 3 78 90 43 11 12 34\n
28

Ouput:

12 34 3 33 56 78 3 12 45 98 3 22 56 3 78 90 43 11 25 4 51 6 3 22 56 3 78 90 43 11

Testcase 4:

Input:

24\n 
93 22 6 45 23 56 79 99 54 2 4 51 6 12 34 3 43 2 5 34 78 66 45 78\n
11

Output:

51 6 12 34 3 43 2 5 34 78 66 45 78 93 22 6 45 23 56 79 99 54 2 4

Testcase 5:

40\n
2112 5126 3378 5651 6722 1903 1125 1173 1251 1334 4456 5111 2112 4445 1227 2112 5126 3378 5651 6722 1903 1125 1173 1251 1334 4456 5111 2112 4445 1227 7457 2112 5144 3443 9722 7457 2112 5144 3443 9722\n
21

Output:

1125 1173 1251 1334 4456 5111 2112 4445 1227 7457 2112 5144 3443 9722 7457 2112 5144 3443 9722 2112 5126 3378 5651 6722 1903 1125 1173 1251 1334 4456 5111 2112 4445 1227 2112 5126 3378 5651 6722 1903


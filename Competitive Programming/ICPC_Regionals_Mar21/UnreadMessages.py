
'''
There is a group of people in an internet email message group. Messages 
are sent to all members of the group, and no two messages are sent at the 
same time.

Immediately before a person sends a message, they read all their unread 
messages up to that point. Each sender also reads their own message the 
moment it is sent. Therefore, a person’s unread messages are exactly the 
set of messages sent after that person’s last message.

Each time a message is sent, compute the total number of unread messages 
over all group members.

Input:
The first line of input contains two integers n (1≤n≤109) and m 
(1≤m≤1000), where n is the number of people in the group, and m is the 
number of messages sent. The group members are identified by number, 1 
through n.

Each of the next m lines contains a single integer s (1≤s≤n), which is 
the sender of that message. These lines are in chronological order.

Output:
Output m lines, each with a single integer, indicating the total number 
of unread messages over all group members, immediately after each message 
is sent.


To solve:
Every time a person sends a message, all messages sent before then are read
Goal: subtract out number of read messages from total possible unread
Ideas:
    - make list of who sent messages
    - go through messages in reverse order, for each *new* person (must
      create a check to see if that person sent a message "later"),
      subtract (index+1) from total
      Note - index+1 is the number of messages sent before the current 
      message was sent
(numOfMessages*numOfPeople)-
'''
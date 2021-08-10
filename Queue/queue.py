from collections import deque;

# Python’s library offers a deque object, which stands for the double-ended queue.

# Let’s see various Operations on deque : 

# append() :- This function is used to insert the value in its argument to the right end of deque.
# appendleft() :- This function is used to insert the value in its argument to the left end of deque.
# pop() :- This function is used to delete an argument from the right end of deque.
# popleft() :- This function is used to delete an argument from the left end of deque. 
def Queue():

    q = deque()

    q.append(1)
    q.append(2)
    q.append(3)

    print(q)

    q.popleft()
    print(q)
    
    q.pop()
    print(q)

    if len(q) == 0:
        print("queue is empty")
    else:
        print('Queue is not empty')

    print(q)

Queue()
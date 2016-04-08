### Name: Pavan Kumar Duppala 
### M20227948
### 08 Apr 2016

## Explain the differences between Threads1 and Threads2 using lines from the code and a precise explanation.

Threads1.py has local variable 'k' ,which works only within the loops of threadA and threadB,whereas threads2.py has global variable 'sharedcounter' which shares the value
in both the threads during the execution process.

##After running Thread3.py does it fix the problems that occured in Threads2.py? What's the down-side?

Yes,the problem that occured in Threads2.py(simultaneous access of sharedcounter by both the threads called as race condition) is fixed in threads3.py since it is 
locked so that when one thread is accessing sharecounter the other thread cant.The downside is that running time is more when compared to the threads2.py since it has 
to wait for the other thread to unlock the sharedcounter

##Comment out the join statements at the bottom of the program and describe what happens.

Join command waits until both the threads complete their execution.So,by commenting it main thread prints 'Goodbye from the main program' before the completion of threadA and
threadB

##What happens if you try to Ctrl-C out of the program before it terminates?

ctrl-c doesnt effect the termination process of this program.

##Read and run Threads4.py. This generates a different and more ridiculous race condition. Write concise explanation of what's happening to cause this bizarre behavior using lines from the code and precise explanation.

Racing condition is far more when compared to the other programs .One of the cause is that there is no locking concept used .The other is that when the value of sharedcounter is initalized
to a 1 or 2,the other thread may run at the same and changes it to a 2 or 1 respectively,thus IF condition may become true and prints "A :that wa weird" and B:that was
weird respectively,which leads to unusual behaviour.

##Does uncommenting the lock operations clear up the problem in question 5?

Yes,uncommenting solves the unusual behaviour of race condition

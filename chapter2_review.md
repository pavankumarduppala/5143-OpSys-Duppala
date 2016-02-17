#Chapter 2 Review Questions

Name:Pavan Kumar Duppala

Course:5143 Operating Systems

Date:17 Feb 2016

## 1.What are three objectives of an OS design?
System (OS) that manages both hardware and software resources and provides common services for computer programs is called as operating system.
It is a component of the system software.
In that we are going to have three objectives.They are

Convenience:
This was the first main objective in operating system design by which it makes a computer more comfortable or more convenience to use.

Efficiency:
By this objective we can make a computer resource much more efficienct.

Ability to evolve: 
The operating system should be built with a good objective by keeping about the future development.If there is an update in a single service,it should not be disturbed the other service.It should permit the effective development, testing, and introduction of new system functions without any interrupts.


##2.What is the kernel of an OS?
A kernel is a part of the operating system which includes the most repeatedly used portions in a particular software.The kernel is permanently stored in  the main memory. 
The main function of kernel is it runs in a privileged mode.It is also responded to calls from processes and it stops interrupts from  other devices.


##3.What is multiprogramming?
Multiprogramming is a concept of operation in which a multiple number of programs are running on just single processor.
It is also called as multi-tasking too.The main operation used in the modern computers is multiprogramming.

There must be enough memory to hold the OperatingSystem for one user program.When one job needs to wait for
I/O, the processor can switch to the other job,we might expand memory to hold three, four, or more
programs and switch among all of them.The approach is known as multiprogramming or multitasking . It is applied in modern operating
systems


##4.What is a process?
An entity which represents the basic unit of work to be implemented in the system is called as Process.
It is also called a program in execution.process is controlled and scheduled by the operating system.
A process can initiate a subprocess, which is a called a child process (and the initiating process is sometimes referred to as its parent ).
child process is a replicable of the parent process.Child process shares some of its resources.But Child process cannot exsist if its parent has been terminated. 



##5.How is the execution context of a process used by the OS?
The execution context,is the internal data through which the operating system can be able to look after the process.It s also used to control the process. 
The internal information is not accessible to the process.so this internal information is separated from the process.The internal infromation includes each and every information about the operating system.
It just needs to manage the process and that processor needs to execute the process properly.
It also includes the contents of the various processor registers.Some of them program counter and data registers. 
It checks about the priority of the process and about the process is waiting for the completion of a particular I/O event.


##6.List and briefly explain five storage management responsibilities of a typical OS.
Modular programming and the flexible use of data is the best environment for every user.System managers need efficient
and orderly control of storage allocation.To satisfy these requirements,the OS has five principal storage management responsibilities:

Process isolation:  Process isolation is a set of different hardware and software technologies[1] 
designed to protect each process from other processes on the operating system.

Automatic allocation and management:  Dynamic memory allocation will be used according to the memory hierarchy.The memory management function keeps track of the status of each memory location, either allocated or free.
It determines how memory is allocated among competing processes, deciding which gets memory, when they receive it, and how much they are allowed.
When memory is allocated it determines which memory locations will be assigned. 
Allocation should be transparent to the programmer.
Thus programmer is relieved of concerns relating to memory limitations, and the OS can achieve efficiency by assigning
memory to jobs only as needed.

Support of modular programming:   Modular programming is a software design technique that emphasizes separating the functionality of a program into independent, 
interchangeable modules, such that each contains everything necessary to execute only one aspect of the desired functionality.
Programmers should be able to define program modules, and to create, destroy, and alter the size of modules dynamically.Modularity should be the programmer main view.

Protection and access control:   It creates the potential for one program to address the memory spaceof the another.Memory is shared at any level of the memory hierarchy,but this was desirable by particular applications.
Some point it threatens the integrity of programs and even of the OS itself.
The OS allow portions of memory to access in various ways from diffrent users.

Long-term storage:   Lot of applications requires memory to store their information for a period of time.
If the inormation is not saved due to sudden power down of the system then we use Long-term storage by which we can store the applications for a long period even the computer has been powered down.


##7.Explain the distinction between a real address and a virtual address.
The major differences between real adress and virtual adress are as follows: 
              Virtual adress:                                                                                          
1.)Complete adress generated by the CPU is a Virtual address.                                               

2.)Logical address is also known a Virtual address.                                                         

3.)Virtual and physical addresses are the same in compile-time and load-time address-binding schem           

4.)The set of all Virtual addresses generated by a program is referred to as a logical address space.
 
              Real adress:
1.)Complete address actually available on memory unit is a Real address. 

2.)real adress is also known as physical adress.

3.)Virtual and physical addresses are the same in compile-time and load-time address-binding scheme.

4.)The set of all Real addresses corresponding to these logical addresses is referred to as a physical address space.


##8.Describe the round-robin scheduling technique.
Round Robin Scheduling Algorithm:
To process each process there will be a fixed time to execute called quantum.
Once a process is executed for given time period,the process is automatically preempted and other process executes for given time period.
In this we use a method to save states of preempted process called as Context switching.
There will be,Procss Wait time,Service Time,Arrival Time and Average time in this Round Robin Algorithm.



##9.Explain the difference between a monolithic kernel and a microkernel.
             Monolithic kernel:

1.)By the definition Monolithic kernel means Large kernel.

2.)Monolithic kernel means a single large process running entirely in a single address space. 

3.)It is a single static binary file. 

4.)Monolithic kernel services exist and execute in the Monolithic kernel address space. 

5.)It can invoke functions directly.

6.) Unix, Linux are the best examples of Monolithic kernel.

              Micro Kernels:
1.)By the definition Micro Kernel means small kernel.

2.)In microkernels,the kernel is broken down into separate processes and these are known as servers. 

3.)servers can run in kernel space and in user-space also.

4.)All servers are kept separate and run in different address spaces. 

5.)Servers invoke services from each other by sending messages through Interprocess Communication commonly known as IPC.

6.)This separation has the advantage that if one server fails, other servers can still work efficiently.

7.)Mac OS X and Windows NT are the best examples for Micro kernels.


##10.What is multithreading?
A flow of execution of program through the process code with its own program counter is called a thread. 
A thread is also called a light weight process.
The ability of operating system process to manage its use by more than one or multiple requests by the same user without any multiple copies of the programming running in the computer is called as Multi-threading. 
There will be a separate track of as a thread with a separate identity. 
As programs work on behalf of the initial request for that thread and are interrupted by other requests,the status of work on behalf of that thread is kept track of until the work is completed.

there will be three models in this concept:

1.)Many to many relationship model.

2.)Many to one relationship model.

3.)one to one relationship model.


##11.List the key design issues for an SMP operating system.
The main issues for a key Design in an SMP operating system:

In the Key Design issues for an SMP operating system there are five main issues which stated as the

1.)Simultaneous concurrent process or threads.

2.)Scheduling.

3.)Synchronization.

4.)Memory management.

5.)Reliability and fault tolerancce.


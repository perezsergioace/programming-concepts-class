# Chapter 1 Introduction to Computers and Programming

### Topics

* 1.1 Introduction
* 1.2 Hardware and Software
* 1.3 How Computers Store Data
* 1.4 How a Program Works
* 1.5 Using Python

## **1.1 Introduction**
<details>
<summary>Click to see notes</summary>

<br>

Computers can perform variety of tasks because they can be programmed. Computers are not designed to do just one job, but to do any job that their programs tell them to do.

A *program* is a set of instructions that a computer follows to perform a task.

Programs are commonly referred to as *software*. Software is essential to a computer because it controls everything the computer does. All of the software that we use are created by individuals working as programmers or software developers.

A *programmer*, or *software developer*, is a person with the training and skills necessary to design, create, and test computer programs.
</details>

## **1.2 Hardware and Software**
<details>
<summary>Click to see notes</summary>

<br>

### **Concept:**
The physical devices of which a computer is made are referred to as the computer's hardware. The programs that run on a computer are referred to as software.

### **Hardware**
The term *hardware* refers to all of the physical devices, or *components*, of which a computer is made. A computer is not one single device, but a system of devices that all work together. Like the different instruments in a symphony orchestra, each device in a computer plays its own part.

### **The CPU**
When a computer is performing the tasks that a program tells it to do, we say that the computer is *running* or *executing* the program. The *central processing unit*, or **CPU**, is the part of a computer that actually runs programs. The **CPU** is the most important component in a computer because without it, the computer could not run software.

### **Main Memory**
This is where the computer stores a program while the program is running, as well as the data that the program is working with. Kind of like the work area of the computer.
> * Main memory is commonly know as *random-access memory*, or **RAM**.
> 
> * It is called this because the **CPU** is able to quickly access data stored at any random location in **RAM**
> * **RAM** is usually a *volatile* type of memory that is used only for temporary storage while a program is running.
> 
> * When the computer is turned off, the contents of **RAM** are erased.

### **Secondary Storage Devices**
*Secondary storage* is a type of memory that can hold data for long periods of time, even when there is no power to the computer. Programs are normally stored in secondary memory and loaded into main memory as needed.
> * Data can be stored on a traditional disk drive or a *Solid-state drives*, which store data in solid-state memory.
> 
> * External Storage devices can be used to create backup copies of important data or to move data to another computer.

### **Input Devices**
Input is any data the computer collects from people and from other devices. The component that collects the data and sends it to the computer is called an *input device*.
> * Common input devices are the keyboard, mouse, touchscreen, scanner, microphone, and digital camera.
>
> * Disk drives and optical drives can also be considered input devices, because programs and data are retrieved from them and loaded into the computer's memory.

### **Output Devices**
*Output* is any data the computer produces for people or for other devices. It might be a sales report, a list of names, or a graphic image.
> * The data is sent to an output device, which formats and presents it.
> 
> * Common output devices are video display and printers.
> 
> * Disk drives can also be considered output devices because the system sends data to them in order to be saved.

### **Software**
If a computer is to function, software is not optional. Everything a computer does, from the time you turn the power switch on until you shut the system down, is under the control of software. There are two general categories of software: **system software** and **application software**. Most computer programs clearly fit into one of these two categories.

### **System Software**
The programs that control and manage the basic operations of a computer are generally referred to as *system software*. System software typically includes the following types of programs:

* #### **Operating Systems**: 
    An *operating system* is the most fundamental set of programs on a computer. The operating system controls the internal operations of the computer's hardware, manages all of the devices connected to the computer, allows data to be saved to and retrieved from storage devices, and allows other program to run on the computer. 

* #### **Utility Programs**:
   A *utility program* performs a specialized task that enhances the computer's operation or safeguards data. Example of utility programs are virus scanners, file compressions program, and data backup programs. 

* #### **Software Development Tools**:
    *Software development tools* are the programs that programmers use to create, modify, and test software. Assemblers, compilers, and interpreters are examples of programs that fall into this category.

### **Application Software**
Programmers that make a computer useful for everyday tasks are know as application software. These are the programs that people normally spend most of their time running on their computers.
</details>

## **1.3 How Computers Store Data**
<details>
<summary>Click to see notes</summary>

<br>

### **Concept:**
All data that is stored in a computer is converted to sequences of 0s and 1s.

A computer's memory is divided into tiny storage locations known as *bytes*. One byte is only enough memory to store a letter of the alphabet or a small number. In order to do anything meaningful, a computer has to have lots of bytes. Most computers today have millions, or even billions, of bytes of memory.

Computer scientists usually think of bits as tiny switches that can be either on or off.

In most computer systems, bits are tiny electrical components that can hold either a positive or a negative charge.

Computer scientists think of a positive charge as a switch in the *on* position, and a negative charge as a switch in the *off* position.

### **Storing Numbers**
In computer systems, a bit that is turned off represents the number **0**, and a bit that is turned on represents the number **1**. This corresponds perfectly to the *binary numbering system*. In the binary numbering system, all numeric values are written as sequences of 0s and 1s.

The position of each digit in a binary number has a value assigned to it. Starting with the rightmost digit and moving left. Starting with the rightmost digit and moving left, the position values are 1, 2, 4, 8, and so forth.

[Article on Binary](https://www.japanistry.com/binary/)

![](https://japanistry-yvxqriqk.netdna-ssl.com/wp-content/uploads/2017/09/Binary-v01.jpg?raw=true)

To determine the value of a binary number, you simply add up the position values of all the 1s. For example, in the binary number 01011101, the position values of the 1s are 1, 4, 8, 16, 64. The sum of all of these position values is 93. So, the value of the binary number 01011101 is 93.

When all of the bits in a byte are set to 0 (turned off), then the value of the byte is 0. When all of the bits in a byte are set to 1 (turned on), then they byte holds the largest value that can be stored in it.

The largest value that can be stored in a byte is 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 = 255. This limit exists because there are only eight bits in a byte.

**What if you need to store a number larger than 255?** The answer is simple: use more than one byte. The maximum value that can be stored in two bytes is 65,535. Example below.

| 32768 | 16384 | 8192 | 4096 | 2048 | 1024 | 512 | 128 | 642 |  32   |  16   | 8 | 4 | 2 | 1 |
| :---: | :---: | :--: | :--: | :--: | :--: | :-: | :-: | :-: | :---: | :---: | - | - | - | - |
|   1   |   1   |   1  |  1   |  1   |  1   |  1  |  1  |  1  |   1   |   1   | 1 | 1 | 1 | 1 |

### **Storing Characters**
Any piece of data that is stored in a computer's memory must be stored as a binary number. That includes characters, such as letters and punctuation marks. When a character is stored in memory, it is first converted to a numeric code. The numeric code is then stored in memory as a binary number.

### **Advanced Number Storage**
Negative numbers and real numbers (such as 3.14159) cannot be represented using the simple binary numbering technique. 

Computers are able to store negative numbers and real numbers in memory, but to do so they use encoding schemes along with the binary numbering system. Negative numbers are encoded using a technique know as *two's complement*, and real real numbers are encoded in *floating-point notation*.

### **Other Types of Data**
Computers are often referred to as digital devices. The term *digital* can be used to describe anything that uses binary numbers. *Digital data* is data that is stored in binary format, and a *digital device* is any device that works with binary data.
</details>

## **How a Program Works**

### **Concept:**
A computer's CPU can only understand instructions that are written in machine language. Because people find it very difficult to write entire programs in machine language, other programming languages have been invented.

Sometimes the CPU is called the "computer's brain" and is described as being "smart". Although these are common metaphors, you should understand that the CPU is not a brain, and its is not smart. The CPU is an electronic device that is designed to do specific things. In particular, the CPU is designed to perform operations such as the following:

> * Reading a piece of data from main memory
> * Adding two numbers
> * Subtracting one number from another number
> * Multiplying two numbers
> * Dividing one number by another number
> * Moving a piece of data from one memory location to another
> * Determining whether one value is equal to another value

As seen from the list above, the CPU performs simple operations on pieces of data. The CPU does nothing on its own, however. It has to be told what to do, and that's the purpose of a program. A program is nothing more than a list of instructions that cause the CPU to perform operations. Each instruction in a program is a command that tells the CPU to perform a specific operation.

Programs are usually stored on a secondary storage device such a disk drive. When you install a program on your computer, the program is typically copied to your computer's disk drive from a CD-ROM, or downloaded from a website.

Although a program can be stored on a secondary storage device such as a disk drive, it has to be copied into main memory, or RAM, each time the CPU executes it.

For example, suppose you have a word processing program on your computer's disk. To execute the program, you use the mouse to double-click the program's icon. This causes the program to be copied from the disk into main memory. Then, the computer's CPU executes the copy of the program that is in main memory.

When a CPU executes the instructions in program, it is engaged in a process that is know as the *fetch-decode-execute cycle*. This cycle, which consists of three steps, is repeated for each instruction in the program. The steps are:

> 1. **Fetch**. A program is a long sequence of machine language instructions. The first step of the cycle is to fetch, or read, the next instruction from memory into the CPU.
> 2. **Decode**. A machine language instruction is a binary number that represents a command that tells the CPU to perform an operation. In this step, the CPU decodes the instruction that was just fetched from memory, to determine which operation should perform.
> 3. **Execute**. The last step in the cycle is to execute, or perform, the operation.

### **From Machine Language to Assembly Language**
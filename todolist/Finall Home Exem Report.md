`<824>, <Shibru> <David>`
# Final Exam Report

## Part 1: Malware Types, Brief Descriptions, Notable Representatives

* Adware

  this virus that shows advertising to the user without breaking it, thereby receiving money from advertising

* Attack kit

  This is a toolkit for creating your own virus using special tools from the set.

* Auto-rooter

  this tool with the help of which you can control a computer that was taken by an autorooter

* Downloaders

tThis is a short code that after downloading to a computer can download larger programs or viruses.

* Drive-by-Download

  it is a virus that attacks web site visitors who use unprotected browsers

* Exploits

  it is a type of virus program or a piece of code that is looking for vulnerabilities and who can use them

* Flooders (DoS client)

  this is a huge amount of generated data that is sent to any server in order to cause an error in it

* Keyloggers

  it is a program that is able to track user keystrokes and send this data to the creator of the program

* Logic bomb

  this is a code that will not act until a specific action is taken by the user.

* Macro virus

this is a type of virus that, when opening an infected document, runs and infects other documents similar to the infected one.

* Mobile code

this is a program that sends itself to different platforms and performs the same actions independently of it.

* Rootkit

  this is a set of software tools that allows hackers to obtain user data or control the victim's computer.

* Spammer programs

  this is a program that sends a predetermined text to everyone else through e-mail.

* Spyware

  this is a software that, when come on a computer, begins to collect screen, network, keyboard data, etc.

* Trojan horse

  this is a program that keeps the virus and because it is hard to see in the program for antiviruses

* Virus

  it is a program that tries to infect other computers or programs

* Worm

  it is a program that exploits system vulnerabilities and also distributes itself by creating its own copy and does it all automatically.

* Zombie, Bot

  this is a program that makes of native machines a army with the help of which you can attack various services and servers.

## Part 2: Malware Analyses

* What is the name of the malware?

  Stuxnet

* What is the type of the malware?

  Worm

* What was the language used to create the malware?

  Assembler, С and С++.

* What Windows-specific APIs were used to allow the malware to function (at least 7)?

  1)Stuxnet extracts the MrxNet.sys resource from the flash drive via export  
    2)MrxNet.sys driver is registered as a service, creating an entry in the registry  
    3)Driver scans filesystem driver objects  
    4)intercept IRP requests (write, read, to NTFS, FAT devices, or CD-ROM devices)  
    5)The driver is registered in the file system callback registration routine  
    6)Driver cling to newly created file system objects  
   7)Driver hides files used by Stuxnet for distribution via removable disk  

* What Windows-specific vulnerabilities were used to allow the malware to function?

  The stuxnet virus exploits 4 windows vulnerabilities: zero day, CVE 2010-2658, BID 41732 and BID 31874

* Were any other software APIs or vulnerabilities exploited by the tool?

  -

* How can one protect the system against this particular malware (describe multiple approaches)?

  To remove the stuxnet virus, you can use specially created programs to remove this SpyHunter virus or BitDefender Stuxnet Removal Tool.

* What general conclusions can we make after studying the malware?

  To protect against the virus, you cannot use flash drives that were in unknown places and if you do regular computer checks with an antivirus

Outline the functionality of the malware and the basic steps the tool was doing to abuse the system.

  1)Driver Entry  
  2)Hooking File Systems  
  3)Driver Notification Routine  
  4)Attaching Device  
  5)File System Control  
  6)Directory Control  
  7)File Checking  

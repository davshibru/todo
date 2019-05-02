`<825>, <Kasymov> <Nurali>`
# Final Exam Report

## Part 1: Malware Types, Brief Descriptions, Notable Representatives

* Adware
program is designed to display ads on your computer.

* Attack kit
a set of tools for creating viruses

* Auto-rooter
tools that allow you to attack the machine remotely

* Downloaders
 this is a small piece of code that gets on the computer downloads the software against the user's wishes

* Drive-by-Download
Drive-by downloads malware is presented in the form of a Trojan, the virus makes itself felt when the user enters the site infected by hackers

* Exploits
an exploit is a type of viral program that allows you to take advantage of the vulnerability in for example your browser and the remote to make viral code

* Flooders (DoS client)
Flooders is a stream of meaningless messages that is found on chat rooms, forums and social networks.

* Keyloggers
 tool allows you to record all the actions performed on the keyboard

* Logic bomb
this is the code that will not be valid until a certain action occurs

* Macro virus
the type of embedded virus that runs when you view or edit a document

* Mobile code
 malicious code that when it enters the computer downloads unnecessary

* Rootkit
is a program that allows an attacker to gain access to your device without your knowledge

* Spammer programs
 Used to send large volumes of unwanted e-mail. 

* Spyware
Spyware is a spyware program to collect information about your computer without your knowledge

* Trojan horse
 a useful program in which is hidden a virus that bypasses antivirus

* Virus
 the program that is activated when you run the infected file and begins to infect other files for further distribution

* Worm
a program that creates its own kind and works no matter what it does

* Zombie, Bot
a program that infects a computer and then uses that computer to attack other computers

## Part 2: Malware Analyses

* What is the name of the malware?
Mydoom
* What is the type of the malware?
Multi-vector worm
* What was the language used to create the malware?
С++

* What Windows-specific APIs were used to allow the malware to function (at least 7)?
basically mydoom spread to computers in which there was OC Windows

* What Windows-specific vulnerabilities were used to allow the malware to function?
-
* Were any other software APIs or vulnerabilities exploited by the tool?
-
* How can one protect the system against this particular malware (describe multiple approaches)?
download Security Stronghold utility that is designed to remove Mydoom. In manual it is possible to remove: to delete files WNSPOO~1.EXE
shimgapi.dll, after delete the folder no information, then delete the keys Key: CLSID\{E6FB5E20-DE35-11CF-9C87-00AA005127ED}\InProcServer32
Value: (Default)
Data: %system%\shimgapi.dll and finally to Reset browsers

* What general conclusions can we make after studying the malware?
in the course of viewing this worm, we learned that it was transmitted through e-mails and in General caused damage in the amount of $ 38.5 billion
Outline the functionality of the malware and the basic steps the tool was doing to abuse the system.
Mydoom was distributed via Bounce Message. These are the "Non Delivery Notification" notifications that the mail server generates if the message cannot be delivered. As soon as the user opened this notification, the computer was infected. After the worm sent itself to all contacts found.

# RDT Data Transfer Simulation
### This project sets up and simulates the transfer of packets between a server (A) and a client (B), allowing users to compare the performance of the go_back_n and stop_and_wait transfer protocols
Thomas Knickerbocker,03/20/2023  
==================================================================

  

## Compilation

1.  Change into the desired directory (go\_back\_n or stop\_and\_wait)
2.  If you would like to alter simulation parameters prior to running, change into the "pj2" subfolder and edit the variables at the top of simulator.py, such as the corruptionprob (the probability a message is corrupted as it passes through layer three) and nsmax (the maximum number of messages the simulation can generate)

  

## Running

1.  Change into the desired directory (go\_back\_n or stop\_and\_wait)
2.  Enter "python3 main.py"
3.  The terminal should print out the data recieved from each packet. See evaluation section for expected outputs given certain simulator parameters

  

## Description

#### This program:

*   Simulates RDT 3.0 data transfer between two systems, A.py and B.py, where A is the sender and B is the receiver
*   Has two different implementations of the transfer protocol, one being stop\_and\_wait and the other being go\_back\_n
*   Allows the user to tune parameters for the simulation and run it to their liking
*   Supports a reliable unidirectional transfer of data across a simulated lossy and noisy channel

## Evaluation

### Test Cases:

#### stop\_and\_wait1:
1.  **Simulation parameters:** nsimmax=30, lossprob=0, corruptprob=0, lambda = 1000  
    **Expected Output:** data recieved：aaaaaaaaaaaaaaaaaaaa data recieved：bbbbbbbbbbbbbbbbbbbb data recieved：cccccccccccccccccccc data recieved：dddddddddddddddddddd data recieved：eeeeeeeeeeeeeeeeeeee data recieved：ffffffffffffffffffff data recieved：gggggggggggggggggggg data recieved：hhhhhhhhhhhhhhhhhhhh data recieved：iiiiiiiiiiiiiiiiiiii data recieved：jjjjjjjjjjjjjjjjjjjj data recieved：kkkkkkkkkkkkkkkkkkkk data recieved：llllllllllllllllllll data recieved：mmmmmmmmmmmmmmmmmmmm data recieved：nnnnnnnnnnnnnnnnnnnn data recieved：oooooooooooooooooooo data recieved：pppppppppppppppppppp data recieved：qqqqqqqqqqqqqqqqqqqq data recieved：rrrrrrrrrrrrrrrrrrrr data recieved：ssssssssssssssssssss data recieved：tttttttttttttttttttt data recieved：uuuuuuuuuuuuuuuuuuuu data recieved：vvvvvvvvvvvvvvvvvvvv data recieved：wwwwwwwwwwwwwwwwwwww data recieved：xxxxxxxxxxxxxxxxxxxx data recieved：yyyyyyyyyyyyyyyyyyyy data recieved：zzzzzzzzzzzzzzzzzzzz data recieved：aaaaaaaaaaaaaaaaaaaa data recieved：bbbbbbbbbbbbbbbbbbbb data recieved：cccccccccccccccccccc simulation end  
    **Analysis:** In this test, we set the max messages to 30, and have no simulated loss or corruption. We limit the simulation's arrival rate to 1000, which is more than enough when loss doesn't occur and the stop\_and\_wait protocol is being used (since lambda is high and there is more time for our sender to process individual packets). Thus, we are able to get all of our messages successfully (the simulation loops back to the front of the alphabet once it has gone through every letter)
2.  **Simulation parameters:** nsimmax=30, lossprob=0.2, corruptprob=0, lambda = 1000  
    **Expected Output:** same as above test, as we are maxing out at the same number of messages and our lossprob is quite low, so we should get all of them delivered with a lambda this high.  
    **Analysis:** This test is the exact same as the prior, except we introduce a 20% chance of loss accross the channel. This should result in more retransmissions, but not so many that we cross the lambda threshold and stop our simulation prior to every data packet being received at layer five.
3.  **Simulation parameters:** nsimmax=30, lossprob=0, corruptprob=0.3, lambda = 1000  
    **Expected Output:** same as above test, as we are maxing out at the same number of messages and our corrupt is relatively low, so we would expect to get all of them delivered.  
    **Analysis:** This test is the exact same as the prior, except we introduce a 30% chance of corruption accross the channel, and set the probability of loss to 0. This should result in more retransmissions, but not so many that our sender gets overwhelmed, due to the higher lambda. Since, in this scenario, corruption is handled in the same way loss is, we do not expect any significant differences between the prior test case and this one.
4.  **Simulation parameters:** nsimmax=20, lossprob=0.8, corruptprob=0.8, lambda = 100  
    **Expected Output:** Since nsimmax is now = 20, in a perfect run, we would expect our terminal to print out data received: \_\_\_\_\_ for all letters from a-s. However, due to the high noise and loss coupled with a low lambda, we should actually expect far fewer packets to be successfully delivered.  
    **Analysis:** When I run my simulation with these parameters, I rarely get past aaaaaaa. This is because the probability of loss and corruption are so high that getting a "perfect" run with these parameters is nearly impossible. There are multiple data transfers involved in a single packet being ultimately received in layer five, and it is so likely to fail that we rarely get even two.
5.  **Simulation parameters:** nsimmax=20, lossprob=0.8, corruptprob=0.8, lambda = 100000  
    **Expected Output:** Since nsimmax is now = 20, in a perfect run, we would expect our terminal to print out data received: \_\_\_\_\_ for all letters from a-s.  
    **Analysis:** When I run my simulation. I typically do get all data received in layer five from aaaa-ssss. This is due to our (now very large) lambda value, because although the probabilities of corruption and loss are very high accross channels, the simulation is given many more events. The sheer amount of time given to the receiver in this simulation allows us to frequently receive all of our packets, despite having a ludicrously lossy and noisy channel.

#### go\_back\_n1:
1.  **Simulation parameters:** nsimmax=30, lossprob=0, corruptprob=0, lambda = 1000  
    **Expected Output:** data recieved：aaaaaaaaaaaaaaaaaaaa data recieved：bbbbbbbbbbbbbbbbbbbb data recieved：cccccccccccccccccccc data recieved：dddddddddddddddddddd data recieved：eeeeeeeeeeeeeeeeeeee data recieved：ffffffffffffffffffff data recieved：gggggggggggggggggggg data recieved：hhhhhhhhhhhhhhhhhhhh data recieved：iiiiiiiiiiiiiiiiiiii data recieved：jjjjjjjjjjjjjjjjjjjj data recieved：kkkkkkkkkkkkkkkkkkkk data recieved：llllllllllllllllllll data recieved：mmmmmmmmmmmmmmmmmmmm data recieved：nnnnnnnnnnnnnnnnnnnn data recieved：oooooooooooooooooooo data recieved：pppppppppppppppppppp data recieved：qqqqqqqqqqqqqqqqqqqq data recieved：rrrrrrrrrrrrrrrrrrrr data recieved：ssssssssssssssssssss simulation end  
    **Analysis:** Just as was the case in our first test case for the stop\_and\_wait protocol, we would expect all packets to be successfully delivered in our simulated perfectly secure channel. This is because there is no probability of a packet not being delivered, and so we should always get the output above, given the input parameters for this test case.
2.  **Simulation parameters:** nsimmax=20, lossprob=0.2, corruptprob=0, lambda = 1000  
    **Expected Output:** Same as previous test case  
    **Analysis:** Even though go\_back\_n involves redundant retransmissions, leading us to use more of our lamda on average in simulations over channels with noise and/or loss, our lambda is high enough, and our lossprob low enough, where we expect to get every packet (a-s) successfully delivered to layer five without any outward-facing issues.
3.  **Simulation parameters:** nsimmax=20, lossprob=0, corruptprob=0.3, lambda = 1000  
    **Expected Output:** Same as previous test case  
    **Analysis:** Even though go\_back\_n involves redundant retransmissions, leading us to use more of our lamda on average in simulations over channels with noise and/or loss, our lambda is high enough, and our corruptionprob low enough, where we expect to get every packet (a-s) successfully delivered to layer five without any outward-facing issues. This test case is virtually identical to the one before it.
4.  **Simulation parameters:** nsimmax=20, lossprob=0.8, corruptprob=0.8, lambda = 100  
    **Expected Output:** We would expect to get a few packets delivered, because the loss and prob are quite high, however go\_back\_n sends packets in quick succession, which can help speed up the overall sim. When I run this, I frequently get between 0 and 3 packets delivered, so a common output is: data recieved：aaaaaaaaaaaaaaaaaaaa data recieved：bbbbbbbbbbbbbbbbbbbb simulation end  
    **Analysis:** Because our noise and loss are both very high and lambda is low, our sender will quickly get overwhelmed and the simulation will end, almost never even recieving packet e. Go back n with our window size of 8 allows for many transmissions, but an approach like this can get messy and result in redundant retransmission when the probability of corruption and loss are high, wasting computing resources, and in this case, giving us unsatisfying delivery results.
5.  **Simulation parameters:** nsimmax=20, lossprob=0.8, corruptprob=0.8, lambda = 100000  
    **Expected Output:** Even with a lambda value this high, we should still expect a low number of packets to be delivered, not only due to the high noise & loss, but, primarily, the nature of go back n. Here is a frequent output I received when running with these parameters: data recieved：aaaaaaaaaaaaaaaaaaaa data recieved：bbbbbbbbbbbbbbbbbbbb data recieved：cccccccccccccccccccc data recieved：dddddddddddddddddddd simulation end  
    **Analysis:** Packets are being resent in blocks of windowSize (8) all of the time, which requires many events and transfers. All 8 virtually never all make it, and timeouts become extremely frequent. The computing resources used ramps up very very quickly, and things are being thrown at our sender quite often, leading to this implementation actually performing worse than stop\_and\_wait, which would seem counterintuitive at first. Assuming my implementations are correct, what we may conclude from this is that stop\_and\_wait is actually preferable in terms of computational resources used and reliability by a server when the channel is significantly noisy, lossy, and/or the window size for go\_back\_n is relatively large.


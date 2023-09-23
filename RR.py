
def findWaitingTime(processes, n, bt,
						wt, quantum):
	rem_bt = [0] * n

	# Copy the burst time into rt[]
	for i in range(n):
		rem_bt[i] = bt[i]
	t = 0 

	while(1):
		done = True


		for i in range(n):
			
			# If burst time of a process is greater
			# than 0 then only need to process further
			if (rem_bt[i] > 0) :
				done = False 
				
				if (rem_bt[i] > quantum) :
				

					t += quantum


					rem_bt[i] -= quantum
				

				else:
				
					t = t + rem_bt[i]

					wt[i] = t - bt[i]

					rem_bt[i] = 0
				
		# If all processes are done
		if (done == True):
			break
			
# Function to calculate turn around time
def findTurnAroundTime(processes, n, bt, wt, tat):
	
	# Calculating turnaround time
	for i in range(n):
		tat[i] = bt[i] + wt[i]


# Function to calculate average waiting
# and turn-around times.
def findavgTime(processes, n, bt, quantum):
	wt = [0] * n
	tat = [0] * n

	# Function to find waiting time
	# of all processes
	findWaitingTime(processes, n, bt,
						wt, quantum)

	# Function to find turn around time
	# for all processes
	findTurnAroundTime(processes, n, bt,
								wt, tat)

	# Display processes along with all details
	print("Processes Burst Time	 Waiting",
					"Time Turn-Around Time")
	total_wt = 0
	total_tat = 0
	for i in range(n):

		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" ", i + 1, "\t\t", bt[i],
			"\t\t", wt[i], "\t\t", tat[i])

	print("\nAverage waiting time = %.5f "%(total_wt /n) )
	print("Average turn around time = %.5f "% (total_tat / n))
	
# Driver code
if __name__ =="__main__":
	
	# Process ids
	proc = [1, 2, 3]
	n = 3

	# Burst time of all processes
	burst_time = [10, 5, 8]

	# Time quantum
	quantum = 2;
	findavgTime(proc, n, burst_time, quantum)

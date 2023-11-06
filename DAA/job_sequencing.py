def job_sequencing_with_deadlines(jobs):
    # Sort the jobs in decreasing order of their profits
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(jobs, key=lambda x: x[1])[1]
    schedule = [-1] * (max_deadline + 1)
    total_profit = 0
    # Iterate through each job
    for job in jobs:
        job_id, deadline, profit = job
        # Find the latest available slot before the deadline
        for slot in range(deadline, 0, -1):
            if schedule[slot] == -1:
                schedule[slot] = job_id
                total_profit += profit
                break
    return schedule[1:], total_profit

# Example usage:
jobs = [(1, 4, 70), (2, 2, 60), (3, 4, 50), (4, 3, 40), (5, 1, 30)]
schedule, profit = job_sequencing_with_deadlines(jobs)
print("Job Sequence:", schedule)
print("Total Profit:", profit)


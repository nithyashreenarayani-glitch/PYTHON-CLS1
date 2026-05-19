def maxProfitAssignment(difficulty, profit, worker):
    total_profit = 0

    for w in worker:
        best = 0
        for i in range(len(difficulty)):
            if w >= difficulty[i]:   # if worker can do this job
                best = max(best, profit[i])  # choose higher paying job
        total_profit += best  # add that worker’s profit

    return total_profit

# Example
difficulty = [2, 4, 6, 8, 10]
profit = [10, 20, 30, 40, 50]
worker = [4, 5, 6, 7]

print(maxProfitAssignment(difficulty, profit, worker))

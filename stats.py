import math

def calculateStats(numbers):
    if not numbers:
        return {"avg": math.nan, "min": math.nan, "max": math.nan}

    avg = sum(numbers) / len(numbers)
    return {
        "avg": avg,
        "min": min(numbers),
        "max": max(numbers)
        
    }

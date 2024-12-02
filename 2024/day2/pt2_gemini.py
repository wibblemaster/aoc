def is_safe_with_dampener(report):
    """Checks if a report is safe, considering the Problem Dampener."""

    def is_monotonic(report):
        """Checks if a report is monotonically increasing or decreasing."""
        return all(report[i] <= report[i+1] for i in range(len(report)-1)) or \
               all(report[i] >= report[i+1] for i in range(len(report)-1))

    def is_adjacent_diff_valid(report):
        """Checks if adjacent levels differ by at most 3."""
        return all(abs(report[i] - report[i+1]) <= 3 for i in range(len(report)-1))

    if is_monotonic(report) and is_adjacent_diff_valid(report):
        return True

    # Check if removing a single level makes the report safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_monotonic(modified_report) and is_adjacent_diff_valid(modified_report):
            return True

    return False

def count_safe_reports_with_dampener(reports):
    """Counts the number of safe reports, considering the Problem Dampener."""

    count = 0
    for report in reports:
        if is_safe_with_dampener(report):
            count += 1
    return count

# Example usage:
#reports = [
#    [7, 6, 4, 2, 1],
#    [1, 2, 7, 8, 9],
#    [9, 7, 6, 2, 1],
#    [1, 3, 2, 4, 5],
#    [8, 6, 4, 4, 1],
#    [1, 3, 6, 7, 9]
#]

with open("data.txt", "r") as f:
    lines = f.readlines()

preproc = [x.strip() for x in lines]
reports = []
for i in preproc:
    element = [int(x) for x in i.split()]
    reports.append(element)
safe_count = count_safe_reports_with_dampener(reports)
print("Number of safe reports with Problem Dampener:", safe_count)

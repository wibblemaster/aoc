def is_safe_report(report):
    """Checks if a given report is safe."""

    is_increasing = report[1] - report[0] > 0
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if diff == 0 or (diff < 0 and is_increasing) or (diff > 0 and not is_increasing) or abs(diff) > 3:
            return False
    return True

def count_safe_reports(reports):
    """Counts the number of safe reports in a list of reports."""

    count = 0
    for report in reports:
        if is_safe_report(report):
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

print(reports)

safe_count = count_safe_reports(reports)
print("Number of safe reports:", safe_count)

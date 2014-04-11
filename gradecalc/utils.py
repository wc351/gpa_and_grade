

def GetGrade(c):
    hw = (c.homework_total / float(c.homework_possible)) * c.homework_percent
    tests = (c.tests_total / float(c.tests_possible)) * c.tests_percent
    final = (c.final_total / float(c.final_possible)) * c.final_percent
    tot = hw + tests + final
    return round(tot, 2)
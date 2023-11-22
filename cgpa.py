import math
class GPA:
    def __init__(self,subjects):
        self.subjects = subjects

    def calculate_c(self):
        total_credit_points = 0
        total_credits = 0

        for credit, grade in self.subjects:
            credit_points = credit * grade
            total_credit_points += credit_points
            total_credits += credit

        g = total_credit_points / total_credits
        return g

class Mathematics:
    #variables is a list, strictly
    def add(self,variables):
        return sum(variables)
    
    def subtract(self,variables):
        sub1=0
        enolisti=[]
        for j in variables:
            if j == variables[0]:
                enolisti.append(j)
            else:
                j = j*-1
                enolisti.append(j)
        sub1=sum(enolisti)

        return sub1
    
    def multiplier(self,variables):
        result = math.prod(variables)
        return result
    
    def divider_method(self,variables):
        return variables[0]/variables[1]

#logic
subjects_data = [
    (4, 3.5),
    (3, 4.0),
    (3, 3.0),
    (4, 4.0),
]

GPA_calculator = GPA(subjects_data)
gpa = GPA_calculator.calculate_c()

file_name = 'reports.txt'
file = open(file_name,'w')
file.write(f"Calculated : {gpa:.2f}")
file.close()

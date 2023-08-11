from statistics import mean
import numpy as np


numA = int(input())
A_info = []
for _ in range(3):
    classA_info = input()
    A_info.append(classA_info.split())
A_info = np.float_(A_info)

numB = int(input())
B_info = []
for _ in range(3):
    classB_info = input()
    B_info.append(classB_info.split())
B_info = np.float_(B_info)

class ClassAInfo:
    def __init__(self, A_info: list, B_info: list):
        """
        get needed input
        """
        self.classA = A_info
        self.classB = B_info
    def calculate_mean_A(self) -> int:
        """
        calculate means of class A list ---> (age, height, weight)
        """
        self.means = []
        for i in self.classA:
            self.means.append(float(mean(i)))
        for j in self.means:
            print(j)
    def calculate_mean_B(self) -> int:
        """
        calculate means of class B list ---> (age, height, weight)
        """
        self.means1 = []
        for i in self.classB:
            self.means1.append(float(mean(i)))
        for j in self.means1:
            print(j) 
    def comparing_A_B(self) -> str:
        """
        Comparing class A nad B  means of height and weight.
        (larger height mean and smaller weight mean. None of them print(Same))
        """
        if self.means[1] > self.means1[1]:
            print('A')
        elif self.means[1] < self.means1[1]:
            print('B')
        elif self.means[1] == self.means1[1]:
            if self.means[2] < self.means1[2]:
                print('A')
            elif self.means[2] > self.means1[2]:
                print('B')
            elif self.means[2] == self.means1[2]:
                print('Same')
    
    
    
class_A_B = ClassAInfo(A_info, B_info)
class_A_B.calculate_mean_A()
class_A_B.calculate_mean_B()
class_A_B.comparing_A_B()
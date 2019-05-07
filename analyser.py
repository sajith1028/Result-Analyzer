#########################################################################################
##to run, download all the exam results .pdf file open them and select all (crtl+a) them#
##and place them into individually numbered files from 1 to n                           #
##then change the range in line 8 from 1 to n+1                                         #
#########################################################################################
import re
import PyPDF2
import os
from pathlib import Path

grade = ['A+\n','A\n','A-\n','B+\n','B\n','B-\n','C+\n','C\n','C-\n','D+\n','D\n','D-\n','E\n','F\n']
out = open("analysis.txt","w")
out.write("Analysis of the 3rd Year CS Exams of 2018")
directory = Path("C:/Users/Sajith/Documents/3rd Year UCSC/3rd Year Results 2018")

for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        pdfFile = open(filename,"rb")
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        numPages = pdfReader.numPages
        count = 0
        text = ""
        while count<numPages:
            pageObj = pdfReader.getPage(count)
            count += 1
            text += pageObj.extractText()
        out.write("\n-----------------------------------------------------------------");
        gradeCount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i in text:
            if i == "Paper Name\n":
                paperName = f.readline()
            if i in grade:
                gradeCount[grade.index(i)]+=1
        out.write("\n"+paperName)
        out.write("\nGrade\t|  Count")
        out.write("\n--------+--------")
        for i in range(0,14):
            out.write("\n  "+re.sub('\\n$','',grade[i])+"\t|    "+str(gradeCount[i])+"")
            
        noOfCandidates = sum(gradeCount)
        noOfFails = sum(gradeCount[8:])
        passRate = ((noOfCandidates-noOfFails)/noOfCandidates)*100
        out.write("\nNo. of Candidates = "+str(noOfCandidates))
        out.write("\nNo. of Fails      = "+str(noOfFails))
        out.write("\nPass Rate         = "+str(passRate))
        out.write("\n-----------------------------------------------------------------\n\n");
        continue
    else:
        continue
out.close()


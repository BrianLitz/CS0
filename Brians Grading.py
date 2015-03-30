HW= [100,100,100,85,65,100,100,100,0,105,105]
HWGrade=.2
HWAverage= float(sum(HW)/11*HWGrade)
print "Average Homework Score=" ,HWAverage

Quiz= [93,87,100,100,100,72]
QuizGrade=.25
QuizAverage= float(sum(Quiz)/6*QuizGrade)
print "Average Quiz Score=" ,QuizAverage

Test= [98,92,75,80]
TestGrade=.3
TestAverage= float(sum(Test)/4*TestGrade)
print "Average Score For Tests=" ,TestAverage

Midterm= (85)
MidtermGrade=.10
MidtermAverage= float((Midterm)*MidtermGrade)
print "Average For Midterm=" ,MidtermAverage

Averagelist= [HWAverage,QuizAverage,TestAverage,MidtermAverage]
AllAverage= sum(Averagelist)
print"Average Without Final Exam =" + str(AllAverage)

ScoreForA= 90
AverageScoreNeededForFinal= ScoreForA- (AllAverage)
ScoreNeededOnFinalExam= AverageScoreNeededForFinal / .15
print "The Score You Need On Final Exam To Pass Is"+ str(ScoreNeededOnFinalExam)


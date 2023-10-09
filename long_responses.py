import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_COURSE = "Available many of the course in the college"
R_HOD = "name of hod cse department Dr.Velmurugan"
R_DEPARTMENT = "CSE,EEE,ECE,IT,CIVIL,MECHANICAL,CHEMICAL"
R_PLACEMENTOFFICER = "placement officer of this college is Dr.G.Nandhakumar"
R_STAFFNAME = "Dr.T.Vigneswari ASP/CSE,Mr.N.Vijayakrishanan AP/Maths,Mr.P.Dinesh AP/CSE,MR.P.Manikandaprabu AP/CSE,Mr.K.Pazhanivel AP/CSE,Dr.R.Karthikeyan ASP/English"
R_STUDENTCOUNT = "there are 360 students in cse department"
R_LAB = "3 Labs that are i)data science ii)Artificial intelligence iii)Open Source Lab"
R_SYSTEM = "There are 152 system in cse department"
R_PLACEMENTCOMPANY = "that are sysarc,wipro,vuram,boson labs"
R_COLLEGELOCATION="located at kovilvenni-614403,thiruvarur DT"
R_FEESSTRUCTURE="For management quota = 98000,For Government quota = 59000"
R_STUDENTPLACEMENT="There are totally 590 students are placed in various companies"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
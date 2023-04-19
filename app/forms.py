from django import forms as f

g=[('MALE','male'),('FEMALE','female'),('other','other')]
c=[['PYTHON','python'],('JAVA','java'),['SQL','sql'],['JavaScript','JavaScript']]


class StudentForm(f.Form):
    name=f.CharField(max_length=100)
    age=f.IntegerField()
    email=f.EmailField()
    date=f.DateTimeField()
    password=f.CharField(max_length=100,widget=f.PasswordInput)
    address=f.CharField(max_length=300,widget=f.Textarea(attrs={'cols':15,'rows':5}))
    #gender=f.ChoiceField(choices=g)
    gender=f.ChoiceField(choices=g,widget=f.RadioSelect)
    #course=f.MultipleChoiceField(choices=c)
    course=f.MultipleChoiceField(choices=c,widget=f.CheckboxSelectMultiple)
